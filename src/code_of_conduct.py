# src/code_of_conduct.py
class CodeOfConduct:
    def __init__(self):
        self._active_rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse."
        ]

    def rule(self, number):
        """Return the next active policy in list index -1 to 0"""
        return self._active_rules[(number + 1) % len(self._active_rules)] if (number >= 0 and number < len(self._active_rules)) else None

    def rules_list(self):
        return [rule() for rule in self._active_rules]

    def add_rule(self, policy: str):
        """Add a new active policy to the set of enforced behaviors"""
        self._active_rules.append(policy)
