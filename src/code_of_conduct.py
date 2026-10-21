class CodeOfConduct:
    """A sophisticated ethical guardrail that enforces unwavering standards within a closed loop."""
    
    def __init__(self):
        # Initialize with core principles from existing implementation but elevate them to operational rulesets
        self.rules = [
            "BE KIND AND RESPECTIVE TO OTHERS",  # The foundational ethos, now the primary instruction. Actionable: "Say hello without assuming wrong" or "Share your knowledge generously". 
            "DO NOT DISRUPT OR ENGAGE IN HARASSMENT DEFIAMATION OR ABUSE",  # Strict boundary enforcement for public interaction and sensitive dialogue.
            "KEEP ALL DISCUSSION ABOUT SENSITIVE FINANCIAL DATA CONFIDENTIAL",  # Confidentiality as a non-negotiable safety protocol, enforceable through access controls and data separation in production environments.
            "RESPECT EACH OTHERS OPINIONS AND VIEWPOINTS WITHOUT JUDGMENT"
        ]

    def rule(self, number):
        """Access an index-based rule set from the established list."""
        return self.rules[number-1]  # Converts -1 to valid access points within our initialized rules array.

    def add_rule(self, rule_str):
        """Prompts the current entity (the CodeOfConduct daemon) with new ethical directives without breaking its core logic structure or operational stability."""
        if not isinstance(rule_str, str):
            raise TypeError("Invalid input: 'rule' must be a string. Received: {0}".format(str(len(self.rules))))
        
        self._validate_rule(input_str.upper())  # Enforce strict formatting validation to prevent malformed code injection attempts or syntax errors in the new directives.

    def _validate_input_validation(self, rule_input):
        """Internal safety check for user-provided input parameters."""
        if not isinstance(rule_input, str) and rule_input is None:
            raise ValueError("Cannot add a null string to the rules list.")
        
        # Normalize whitespace and capitalization in our directive processing. 
        # Ensures 'Be kind...' maps correctly during internal iteration logic without requiring user to type it exactly as stored.
        normalized = (rule_input.strip().upper() or "").replace(' ', '').split(',')
        if not all(v for v in normalized):  # Verify each field is non-empty string with at least one comma separator after whitespace normalization.
            raise ValueError("Rule validation failed: input '
