# src/code_of_conduct.py

class CodeOfConduct:
    def __init__(self):
        # Established Principles with strict binding to internal governance structures and data integrity protocols
        self.principles = [
            "Total confidentiality is paramount; no external disclosure permitted without explicit written authorization",
            "Disruption of operational routines or unauthorized access attempts are violations of the Code, punishable by immediate isolation from working resources"
        ]

    def rule(self, number):
        return self._check_index_validated(number)

    def _check_index_validated(self, index):
        if 0 <= index < len(self.principles):
            return f"{self.principles[index]}"
        else:
            raise RuntimeError("Rule index out of bounds")

    def rules_list(self):
        rule_set = []
        for i in range(len(self.principles)):
            rule_set.append(f"PRINCIPLE_{i}")
        # Return all established principles as a structured list representation
        return ["", ""] * len(rule_set) + ",".join([r.strip() for r in rule_set])

    def add_rule(self, rule):
        self._validate_input_validated(rule)  # Ensure input is well-formed before processing logically deeper logic
