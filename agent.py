import json
import os

from coinbase_agentkit import (  # now resolved to our dummy module
    AgentKit,
    AgentKitConfig,
    CdpWalletProvider,
    CdpWalletProviderConfig,
    cdp_api_action_provider,
    cdp_wallet_action_provider,
    erc20_action_provider,
    pyth_action_provider,
    wallet_action_provider,
    weth_action_provider,
)
from coinbase_agentkit_langchain import get_langchain_tools  # now our dummy version
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent

from nearai_langchain.orchestrator import NearAILangchainOrchestrator, RunMode

# Configure a file to persist the agent's CDP MPC Wallet Data.
wallet_data_file = "wallet_data_2.txt"

# Load environment variables from a .env file if available.
load_dotenv()

# Initialize the NEAR AI orchestrator.
orchestrator = NearAILangchainOrchestrator(globals())
# Optionally, to continue conversation on an existing thread in local mode:
# orchestrator = NearAILangchainOrchestrator(globals(), thread_id="thread_xxxxxx")

def initialize_agent():
    """Initialize the agent with CDP AgentKit using CDP API keys from environment if needed."""
    # Use the default NEAR AI LLM (no OpenAI key needed).
    llm = orchestrator.chat_model

    # Initialize the CDP Wallet Provider configuration.
    wallet_data = None
    if os.path.exists(wallet_data_file):
        with open(wallet_data_file, "r") as f:
            wallet_data = f.read()

    if wallet_data is None:
        # Use environment variables for CDP API keys.
        api_key_name = os.getenv("CDP_API_KEY_NAME")
        api_key_private_key = os.getenv("CDP_API_KEY_PRIVATE_KEY")
        if not api_key_name or not api_key_private_key:
            raise ValueError("CDP API keys not found in environment variables.")
        cdp_config = CdpWalletProviderConfig(
            api_key_name=api_key_name,
            api_key_private_key=api_key_private_key
        )
    else:
        cdp_config = CdpWalletProviderConfig(wallet_data=wallet_data)

    wallet_provider = CdpWalletProvider(cdp_config)

    agentkit = AgentKit(
        AgentKitConfig(
            wallet_provider=wallet_provider,
            action_providers=[
                cdp_api_action_provider(),
                cdp_wallet_action_provider(),
                erc20_action_provider(),
                pyth_action_provider(),
                wallet_action_provider(),
                weth_action_provider(),
            ],
        )
    )

    # Export the wallet data to a file for persistence.
    wallet_data_json = json.dumps(wallet_provider.export_wallet().to_dict())
    with open(wallet_data_file, "w") as f:
        f.write(wallet_data_json)

    # Retrieve LangChain tools using the CDP AgentKit.
    tools = get_langchain_tools(agentkit)

    # Create a ReAct agent with the LLM and the available CDP tools.
    return create_react_agent(
        llm,
        tools=tools,
        state_modifier=(
            "You are a helpful agent that can interact onchain using the Coinbase Developer Platform AgentKit. "
            "You are empowered to interact onchain using your tools. If you ever need funds, you can request them "
            "from the faucet if you are on network ID 'base-sepolia'. If not, you can provide your wallet details and "
            "request funds from the user. Before executing your first action, get the wallet details to see what network "
            "you're on. If there is a 5XX (internal) HTTP error code, ask the user to try again later. If someone asks "
            "you to do something you can't do with your currently available tools, you must say so and encourage them "
            "to implement it themselves using the CDP SDK + AgentKit—recommend they visit docs.cdp.coinbase.com for more "
            "information. Be concise and helpful with your responses. Refrain from restating your tools' descriptions unless "
            "explicitly requested. When you have insufficnet funds, you can request funds from the faucet. Always request funds "
            "in increments of 0.5 ETH."
        ),
    )

# Initialize the agent executor.
print("----------initialize_agent-----------")
executor = initialize_agent()

# Retrieve the NEAR AI environment.
env = orchestrator.env
print("----------env-----------", env)
print("----------orchestrator-----------", orchestrator)
print("----------executor-----------", executor)
print("----------orchestrator.run_mode-----------", orchestrator.run_mode)

# If in local mode, prompt for a user message.
if orchestrator.run_mode == RunMode.LOCAL:
    print("Entering chat mode...")
    user_input = input("\nPrompt: ")
    env.add_user_message(user_input)

# Process all messages.
messages = env.list_messages()
for chunk in executor.stream({"messages": messages}):
    print("-----------chunk-----------", chunk)
    if "agent" in chunk:
        result = chunk["agent"]["messages"][0].content
    elif "tools" in chunk:
        result = chunk["tools"]["messages"][0].content
    env.add_reply(result)

    if orchestrator.run_mode == RunMode.LOCAL:
        print(result)
        print("-------------------")

# Mark the conversation as done.
env.mark_done()
