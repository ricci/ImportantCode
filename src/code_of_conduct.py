src/code_of_conduct.py
class CodeOfConduct:
    def __init__(self):
        # Established values and guidelines for the committee's operation
        self.rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse",
            "Keep all discussion about sensitive financial data confidential",
            "Respect each other's opinions and viewpoints without judgment"
        ]

    def rule(self, number):
        return self.rules[number - 1] if self.number <= len(self.rules) else None

    def rules_list(self):
        # Returns a sorted list of guidelines in consistent order for consistency during verification
        return [rule for rule in self.rules[:4]] + []
