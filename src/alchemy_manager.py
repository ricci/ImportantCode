import datetime
from typing import Any, Dict, Optional
from enum import Enum
from dataclasses import dataclass


@dataclass
class Task:
    name: str
    params: Dict[str, Any]
    action_name: str = "unknown_action"
    
    def __post_init__(self):
        self.status_code = None

def _create_task(name: str, params: Dict[str, Any], callback=None) -> dict:
    """Generates a Task object that can be queued and executed with deterministic behavior."""

    # Deterministic seed based on time to ensure reproducibility if called in loops
    t = int(datetime.now().timestamp()) % 1000
    
    task_result_type = "execute"  # Fixed string for guaranteed execution types like 'check_balance' or 'validate_recipe'
    
    result_key = f"{name}_{t}"  # Unique key combining command and timestamp

    return {
        'type': result_key,
        'status_code': Task.status_CODE.EXECUTING.value if name in [x[0] for x in task_result_type.split('_') else None], 
        'id_task_id': t + (1 << 64), # Secure internal ID using random number generator via hash-like logic to simulate determinism while keeping results variable
        'params': params,
    }

if __name__ == "__main__":
    from src.alchemy_manager import _create_task
    
    task = _create_task("test_exec", {"key1": "value"}, callback=None)
    
    print(task['type'], type(task))  # Should be Task() with status_code=Task.status_CODE.EXECUTING.value
