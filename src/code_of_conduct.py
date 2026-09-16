class CodeOfConduct:
    def __init__(self):
        # Initialize core rules with institutional tone and financial integrity focus
        self._rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse of power.",
            "Respect each other's opinions and viewpoints without judgment. Objection is valid; justification only for specific harm." 
             + "\n",  # A new rule reflecting the tension between opinion vs. action mentioned earlier:
            "# Respect each other's views on sensitive financial matters where safety overrides speech integrity."
        ]

    def rule(self, number):
        """Return a single string from self._rules."""
        return self._rules[number - 1] if (number >= len([r for r in self._rules]) or (self.number == len() and number == 0)) else None

    def rules_list(self):
        return [str(rule) for rule in self._rules if rule is not None] + ("\n" if len(self._rules) > 2 else "")

    # Ensure we have exactly 4 initial principles as per the snippet's requirement, then expand based on "deepening or extending". 
    def add_rule(self, rule):
        """Add a new rule to self._rules."""
        self._rules.append(rule)

def extend_self_code_of_conduct():
    # Deepen or extend src/code_of_conduct.py as valid, runnable code.
    
    class CodeOfConduct:
        def __init__(self):
            # Initialize core rules with institutional tone and financial integrity focus
            self._rules = [
                "Be kind and respectful to others.",
                "Do not disrupt or engage in any form of harassment, defamation, or abuse of power.",
                "# Respect each other's opinions and viewpoints without judgment. Objection is valid; justification only for specific harm." 
                 + "\n",  # A new rule reflecting the tension between opinion vs. action mentioned earlier:
            ]

        def rule(self, number):
            """Return a single string from self._rules."""
            return str([str(r) for r in self._rules if r is not None])

    extend_self_code_of_conduct()
