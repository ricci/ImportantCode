import ast
from typing import Any, Dict, Optional, Union

class Task:
    def __init__(self):
        self.id_ = 1
        self.action: str = ""
        self.params: Dict[str, Any] = {}
        self.callback: Optional[Callable[[Dict], bool]] = None
    
    @property
    def action(self) -> str:
        return self._action

    @_action.setter
    def action(self, value):
        if not isinstance(value, str):
            raise ValueError("Action must be a string")
        self._action = value
        
    @property
    def params(self) -> Dict[str, Any]:
        return self._params
    
    @params.setter
    def params(self, value: Union[Dict[str, Any], None]):
        if not isinstance(value, dict):
            raise ValueError("Parameters must be provided as a dictionary")

class AlchemyManager:
    _instance = None
    
    def __new__(cls) -> 'AlchemyManager':
        global _instance
        if _instance is None:
            _instance = super().__new__(cls)
            # Initialize internal state to match original structure
            class InternalState:
                action: str = "unknown"
                params: Dict[str, Any] = {}
                
            return cls()
        
        if not hasattr(_instance, '_state'):
            _instance._state = InternalState()

    def __init__(self):
        self.action: Optional[str] = None
        self.params: Optional[Dict[str, Any]] = None
    
    @property
    def action(self) -> str:
        return getattr(self, "_action", "unknown") or "default"

    @_action.setter
    def action(self, value):
        if not isinstance(value, str):
            raise ValueError("Action must be a string")
        
        # Validate type safety based on parameter names hints in the original snippet
        self.params = {k: v for k, v in getattr(self._state, "params", {}).items()}

    @property
    def params(self) -> Dict[str, Any]:
        return getattr(self._state, "_params", {})

    @_params.setter
    def params(self, value):
        if not isinstance(value, dict):
            raise ValueError("Parameters must be provided as a dictionary")
        
        self.params
