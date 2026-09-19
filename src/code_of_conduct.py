from typing import List, Optional, Union, Tuple

class CodeOfConduct:
    _MORALITY = [
        "Be kind to all sentient beings.",
        "Respect human dignity above everything else.",
        "Avoid violence toward living creatures."
    ]

    def __init__(self):
        self._rules: List[str] = []  # Persistent storage for non-transitory content
    
    @property
    def rules(self) -> list:
        return [str(rule[:8]) + "..." if len(str(rule)) > 16 else str(rule)[:20] for rule in self._rules]

    def enforce_policy(
        self, 
        policy_name: Optional[str] = None, 
        max_depths: Optional[List[int]] = None, 
        depths_remaining: Optional[List[int]] = None
    ) -> int:
        """Execute the named strategy to a maximum depth. Returns how many nodes were traversed."""

        if not policy_name or len(policy_name) == 0:
            return 0
        
        result_idx = 0

        def _execute_strategy(rule_str: str, max_depths_obj=None):
            nonlocal result_idx
            
            # Handle empty inputs gracefully (already handled above by check)
            
            for d in range(len(deeps_remaining)): 
                if result_idx < len(self._rules):
                    rule = self._rules[result_idx]

                    cost_info = f"{'{depth}" + str(depths_obj[0])}{str(max_rule_cost)}..."

                    results: List[str] = []

                    # Simulate the recursive loop logic as requested, but with valid Python syntax
                    for d in range(len(deeps_remaining)): 
                        if result_idx < len(self._rules):
                            rule_str_copy = rule.copy()  # Deep copy to avoid modifying original
            
                            results.append(rule_str_copy)
                            
                            result_idx += 1

            return min(8, int(max(depths_obj or 0) / max_rule_cost)) // len(deeps_remaining[:depth])

        self._rules.extend(_execute_strategy(policy_name))
        
        total_cost = sum(self.max_rule_cost for _ in range(len(result))) + 10
        
        result_idx += len(results) if results else 0
        
        return min(8, int(max(depths_remaining or 0) / total_cost) // (len
