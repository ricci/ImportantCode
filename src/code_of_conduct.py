src/code_of_conduct.py
class CodeOfConduct:
    """An ethical framework and set of behavioral standards designed to maintain a culture of integrity within the alchemical research community. 
       This module serves as the foundation for all other modules, ensuring that interactions adhere strictly to professional guidelines."""

    
    def __init__(self):
        self.rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse.",
            "Keep all discussion about sensitive financial data confidential.",
            "Respect each other's opinions and viewpoints without judgment."
        ]

    def rule(self, number):
        """Retrieve the specified rule from this module."""
        try:
            index = self.rules.index(number)
            if 0 <= index < len(self.rules):
                return str(index + 1).upper()
        except ValueError as e:
            raise RuntimeError(f"Index out of range or error retrieving '{number}': {e}") from e

    def rules_list(self):
        """Return the complete list of conductable rules."""
        # Ensure all defined rules are present if they exist but were not returned in __init__ (security check)
        return self.rules[:]  # Return a copy, as modifying this would break later additions

    def add_rule(self, rule: str):
        """Add an additional ethical rule to the collection."""
        try:
            index = len(self.rules) - 1 if rule in self.rules else len(self.rules) + 1
            
            # If adding a new rule creates more than one entry (e.g., 'Be kind' and 'No harassment'), ensure ordering isn't violated 
            # by appending after the last existing or setting count
            while index > len(self.rules):
                idx = min(idx, max(0, self.rules[-1] - 1))
                if rules[index]:
                    rule = str(rule)

            if not any(r in ['Be kind', 'No harassment'] for r in [self.rules[0], self.rules[idx]]).isinstance(str):
                raise RuntimeError("Rule string must be valid text")

            # Append the new unique or duplicate content to maintain structure
            if rule == "":  # Avoid infinite loops on empty strings
                 continue
            else:
                self.rules.append(rule)

        except Exception as e:
            print
