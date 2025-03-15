# Coinbase CDP Agent

**Coinbase CDP Agent** is a NEAR AI-powered agent that simulates on-chain transactions using Coinbase AgentKit. It allows users to interact with a simulated blockchain wallet through natural language commands—retrieving wallet details, checking balances, and simulating token transfers. The agent leverages a conversational interface to abstract complex on-chain operations behind simple user requests.

## Features

- **Interactive Chat Interface:**  
  Engage with the agent using natural language via NEAR AI's interactive shell.
  
- **Wallet Management:**  
  Query wallet details (address, network, balance) and simulate on-chain actions.
  
- **Simulated Token Transfers:**  
  Execute simulated token transfers and other on-chain operations using Coinbase AgentKit.
  
- **Faucet Integration:**  
  If funds are insufficient, the agent can prompt the user to request funds in increments of 0.5 ETH.

## Installation & Setup

### Prerequisites

- **Python 3.11** (Ensure you’re using Python 3.11)
- [NEAR AI CLI](https://github.com/nearai/nearai) installed and logged in with your NEAR wallet
- Git
- (Optional) A virtual environment is highly recommended

### Clone and Set Up the Repository

1. **Clone the Repository:**

   ```bash
   git clone git@github.com:vineethsaivs/coinbase-cdp-agent.git
   cd coinbase-cdp-agent
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies:**

   Create a `requirements.txt` with the following packages (or adjust as needed):

   ```txt
   nearai==0.1.16
   python-dotenv==1.0.1
   langgraph==0.2.76
   nearai-langchain==0.0.12
   requests
   ```

   Then run:

   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Set Up Dummy Modules:**
   If you are testing without the real Coinbase AgentKit, create local dummy modules for `coinbase_agentkit` and `coinbase_agentkit_langchain` in your repository root. See the repository’s documentation for details.

### Environment Variables

Create a `.env` file in the repository root (or export them in your shell) with the following keys:

```bash
# Coinbase CDP Credentials
export CDP_API_KEY_NAME="your_cdp_api_key_name"
export CDP_API_KEY_PRIVATE_KEY="your_cdp_api_private_key"

# (Optional) Other environment variables can be added here
```

## Usage

### Running the Agent Locally

Use the NEAR AI CLI to start an interactive session:

```bash
nearai agent interactive --local
```

When prompted, select the `coinbase-agent` (or `cdp-agent`) version. At the prompt, you can type commands such as:

#### Query Wallet Details:

```bash
what is in my wallet?
```

#### Simulate a Transfer:

```bash
transfer eth from my account to buy a new pair of shoes
```

The agent processes your message, calls the appropriate tools (via Coinbase AgentKit), and returns a user-friendly response.

## Demo Scenarios

For a demo, you can showcase:

### **Wallet Inquiry:**
The agent retrieves and displays simulated wallet details (address, network, balance).

### **Simulated On-Chain Action:**
When a user requests a transfer (e.g., "transfer eth to buy shoes"), the agent simulates a token transfer. If funds are insufficient, it gracefully informs the user and suggests requesting funds from the faucet.

## Architecture Overview

- **NEAR AI Orchestrator:**  
  Manages the conversational interface and message handling.

- **Coinbase AgentKit Integration:**  
  Simulates wallet operations and on-chain actions using a configurable wallet provider.

- **LangChain Tools:**  
  Leverages LangChain for tool-based processing of user commands.

- **State Modifier:**  
  Provides clear instructions to the agent for handling on-chain operations, error conditions, and fund requests.

## Contributing

Contributions are welcome! Please fork this repository, create a feature branch, and submit a pull request with your changes. For major modifications, please open an issue first to discuss your ideas.

## License

This project is licensed under the MIT License.

