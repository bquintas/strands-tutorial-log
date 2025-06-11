# Python Agent Project

A Python project built with the Strands Agents framework for creating an AI agent with custom tools and logging capabilities.

## Overview

This project demonstrates how to create an AI agent using the Strands Agents framework. The agent is equipped with several tools including a calculator, current time retriever, Python REPL, and a custom letter counter tool. It also includes comprehensive logging of agent interactions and debug information.

## Features

- AI agent with multiple tools
- Custom tool implementation (letter counter)
- Comprehensive logging system
- Composite callback handler for both console output and file logging

## Project Structure

- `agent.py` - Main agent implementation
- `composite_callback_handler.py` - Custom logging handler
- `requirements.txt` - Project dependencies
- `agent_interactions.log` - Log of agent interactions
- `agent_debug.log` - Debug information log

## Installation

1. Clone this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the agent with:

```bash
python agent.py
```

The agent can:
1. Tell the current time
2. Perform calculations
3. Count specific letters in words
4. Execute Python code through a REPL

## Custom Tools

### Letter Counter
Counts occurrences of a specific letter in a word:

```python
letter_counter("strawberry", "r")  # Returns 2
```

## Logging

The project implements a comprehensive logging system with two main components:

### Logging Architecture
- **CompositeCallbackHandler**: Combines console output and file logging
  - Uses the standard `PrintingCallbackHandler` for user-facing output
  - Implements custom `FileLoggingHandler` for detailed logging to files

### Log Files
- `agent_interactions.log` - Records all agent interactions including:
  - Tool invocations with inputs and sequence numbers
  - Agent reasoning text
  - Complete interaction data
  - Timestamps for all events

- `agent_debug.log` - Contains detailed debug information:
  - Strands framework internal logs
  - Debug-level information for troubleshooting
  - Formatted with timestamp, level, logger name, and message

### Implementation Details
- Uses Python's built-in `logging` module
- Custom formatters for different log types
- Tool usage tracking with sequential numbering
- Separate handlers for different log destinations

## Dependencies

- strands-agents >= 0.1.0
- strands-agents-tools >= 0.1.0