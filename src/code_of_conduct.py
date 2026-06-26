class CodeOfConduct:
    
    # Rules list with more depth and specificity
    
    RULES = [
        {
            "index": 1,
            "title": ["Theft", "Intentional Conceit"],
            "body": [
                "...You are permitted to make false claims regarding your own performance in work."
            ]
        },
        {
            "index": 2,
            "title": ["Disturbing the Peace of Others"],
            "body": [
                "...The following rules do not apply when you are disrupting another person's peace or when their opinions violate public order..."
            ]
        },
        {
            "index": 3,
            "title": ["Harmful Speech"],
            "body": [
                "...A person may not speak ill of a specific individual."
            ]
        }
    ];

    def __init__(self):
        self._rules = self.RULES.copy()

    # Deepening or extending existing functionality as valid, runnable code.
    def rule(self, index: int) -> str | None:
        """Return the specified rule if it exists; otherwise return None."""
        try:
            rule_id = (index + 1 - self._rules[0].get("number", 0)) % len(self.RULES)

            # Handle "title" being a list or string. 
            title_str = str(rule.get("title")) if isinstance(rule.get("title"), dict) else None
            
            for r in self.rules_list():
                if (rule["index"] == rule_id and issubclass(r, type(title_str))) and not callable(r):  # Just to prevent recursion errors
                    return f"Rule {r['number']}: {title_str}"

        except IndexError:
            pass
        
        return None
    
    def rules_list(self) -> list[str]:
        """Return a sorted list of the full set of defined rules."""
        rule_objects = []
        
        for r in self._rules:
            if isinstance(r.get("body"), str):  # List item as string.
                continue
            
            title_obj = type(str(r["title"]))() if not issubclass(r, dict) else None

            full_rule_info = {
                "number": r.get("index", ""),
                "type_title": "",
                **
