"""Composite callback handler that logs to file and shows user output to stdout."""

from strands.handlers.callback_handler import PrintingCallbackHandler
import logging
from typing import Any

class FileLoggingHandler:
    """Handler for logging all interactions to a log file."""

    def __init__(self, log_file="agent_debug.log") -> None:
        """Initialize handler with a log file."""
        self.tool_count = 0
        self.previous_tool_use = None
        
        # Set up logger
        self.logger = logging.getLogger("agent_callbacks")
        self.logger.setLevel(logging.INFO)
        
        # Create file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s | %(message)s')
        file_handler.setFormatter(formatter)
        
        # Add handler to logger and ensure it doesn't propagate to root logger
        self.logger.addHandler(file_handler)
        self.logger.propagate = False

    def __call__(self, **kwargs: Any) -> None:
        """Log text output and tool invocations to file."""
        reasoningText = kwargs.get("reasoningText", False)
        data = kwargs.get("data", "")
        complete = kwargs.get("complete", False)
        current_tool_use = kwargs.get("current_tool_use", {})

        if reasoningText:
            self.logger.info(f"REASONING: {reasoningText}")

        if data:
            self.logger.info(f"DATA: {data}")
            if complete:
                self.logger.info("COMPLETE")

        if current_tool_use and current_tool_use.get("name"):
            tool_name = current_tool_use.get("name", "Unknown tool")
            if self.previous_tool_use != current_tool_use:
                self.previous_tool_use = current_tool_use
                self.tool_count += 1
                tool_input = current_tool_use.get("input", {})
                self.logger.info(f"TOOL #{self.tool_count}: {tool_name} - Input: {tool_input}")

class CompositeCallbackHandler:
    """Handler that shows user output to stdout and logs everything to file."""
    
    def __init__(self, log_file="agent_debug.log"):
        """Initialize with both stdout and file handlers."""
        self.print_handler = PrintingCallbackHandler()
        self.file_handler = FileLoggingHandler(log_file)
        
    def __call__(self, **kwargs: Any) -> None:
        """Process callbacks through both handlers."""
        # Send to stdout for user interaction
        self.print_handler(**kwargs)
        
        # Log everything to file for debugging
        self.file_handler(**kwargs)