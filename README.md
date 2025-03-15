# Coinbase CDP Agent

**Coinbase CDP Agent** is a NEAR AI-powered agent that simulates on-chain transactions using Coinbase CDP and integrates an Amazon Pay Sandbox for purchase simulations. It provides a conversational interface for querying wallet details, performing simulated token transfers, and even handling purchase requests—all through natural language commands.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation & Setup](#installation--setup)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Demo Scenarios](#demo-scenarios)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)

## Overview

The **Coinbase CDP Agent** allows users to interact with a simulated blockchain wallet using simple natural language commands. It leverages NEAR AI's orchestrator and Coinbase AgentKit (with dummy modules for testing) to:
- Retrieve wallet details (address, network, balance)
- Execute on-chain actions such as transferring or wrapping ETH
- Simulate a purchase using Amazon Pay Sandbox integration

This agent is designed for demo and testing purposes, showcasing how on-chain transactions can be abstracted behind a conversational interface.

## Features

- **Interactive Chat Interface:**  
  Engage in conversation with the agent via the NEAR AI interactive shell.

- **Wallet Management:**  
  Query your wallet’s details and simulate balance checks.

- **On-Chain Transaction Simulation:**  
  Execute simulated actions (e.g., transfer ETH, wrap ETH) using Coinbase CDP tools.

- **Amazon Pay Sandbox Integration:**  
  Simulate token transfers to purchase items using a fully implemented Amazon Pay Sandbox API integration.

- **Legacy Command Support:**  
  Includes legacy commands (e.g., `!cats`, `!endpoint`) for additional demo scenarios.

## Installation & Setup

### Prerequisites

- **Python 3.11** is required.
- [NEAR AI CLI](https://github.com/nearai/nearai) installed.
- Git installed.
- (Optional) A virtual environment (recommended).

### Clone and Set Up

1. **Clone the Repository:**

   ```bash
   git clone git@github.com:vineethsaivs/coinbase-cdp-agent.git
   cd coinbase-cdp-agent
