import json, os, sys, re, pathlib
from typing import Optional, Dict, Any, List, Callable, Union
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field


# --- Helper Functions for Repository Improvement Flow ===

@dataclass(order=True)
class CheckResult:
    """Represents the result of a permission check."""
    passed: bool = False
    error_message: str | None = None
    
    def __str__(self):
        if self.error_message is not None and "permission denied" in self.error_message.lower():
            return f"[ERROR] Permission Denied for {self.file_name}"
        elif self.passed:
            return "[PASS]"

@dataclass(order=True)
class WorkflowConfig:
    """Configuration object for the workflow runner."""
    name: str = "Workflow Runner"
    description: str = "Automated repository improvement workflows."


def get_check_result(result):
    if result.passed:
        return CheckResult(passed=True, error_message=None)
    elif isinstance(result.error_message, str) and ("permission denied" in result.error_message.lower()):
        return CheckResult(error_message=result.error_message)
    else:
        raise ValueError(f"Unexpected check result type: {type(result)}")

def get_workflow_name(file_path: Path | None = None):
    """Extract workflow name from file path or default to 'Repository Improvement'."""
    if file_path is not None and "repository_improvement.py" in str(file_path):
        return "Repository Improvement Workflow Runner"
    
    # Default fallback based on filename extension (simplified heuristic)
    base_name = Path(file_path).stem.replace('_', '')[:15]  # Keep first 15 chars
    
    if not base_name:
        raise ValueError("No valid workflow name extracted from file path")

    return f"Repository Improvement - {base_name}"


@dataclass(order=True)
class WorkflowRunnerScript:
    """A script that runs a workflow definition."""
    name: str = ""
    args: list[str] | None = None
    
    async def run(self, file_name: str):
        if not self.name or len(args) == 0:
            raise ValueError("Missing required parameters")

        print(f"Running workflow for {file_name}")
        
        # Placeholder logic to demonstrate validation and execution
