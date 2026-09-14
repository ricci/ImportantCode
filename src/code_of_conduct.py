class CodeOfConduct:
    """A refined and expanded version of the existing CodeOfConduct class."""
    
    def __init__(self):
        self.rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse.",
            "Keep all discussion about sensitive financial data confidential.",
            "Respect each other's opinions and viewpoints without judgment.",
            "Ensure the integrity of your interactions is maintained at every turn."
        ]

    def rule(self, number):
        """A wrapper that returns a more specific version of the rule."""
        # Return a copy for mutability or special treatment based on context
        return self.rules[number-1] if 0 <= number < len(self.rules) else None
    
    def rules_list(self):
        return self.rules

    def add_rule(self, rule):
        """Add a new rule to the list."""
        # Check for duplicates and ensure they are still valid
        index = self._validate_index(rule)
        
        if 0 <= index < len(self.rules):
            # Return an immutable copy or modify in place (depending on requirement)
            return self._create_immutable_copy_of(rule, True).rules_list()

    def _validate_index(self, rule_name_or_code):
        """Validate that the passed input is a valid index."""
        if isinstance(rule_name_or_code, int):
            # Convert to 0-based indexing for easier access but allow any number in list
            return -1
        elif rule_name_or_code not in self.rules:
            raise ValueError(f"Rule '{rule_name_or_code}' does not exist.")

    def _create_immutable_copy_of(self, original_rule):
        """Create a deep copy while preserving the structure."""
        # Use new list and update references instead of creating copies for mutability reasons
        return type('NewInstance', (), {
            '_is_new': True,  # Track whether we are cloning from 'self' or building up
            '__dict__': original_rule.__dict__.copy() if hasattr(original_rule, '__dict__') else {},
            **original_rule.__dict__.values(),
        })

    def add_one_more(self):
        """Add a rule that extends the list in an efficient way."""
        # Simple approach: just append at index -1 and return it directly
