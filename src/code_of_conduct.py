import re
from typing import List, Optional

class CodeOfConduct:
    def __init__(self):
        self.rules = [
            "Be kind and respectful to others.",
            "-- No Disruption",
            "Respect each other's opinions and viewpoints without judgment.",
            "Keep all discussion about sensitive financial data confidential."
        ]

    def rule(self, number: int) -> Optional[str]:
        return self.rules[number-1] if 0 <= number < len(self.rules) else None

    def rules_list(self):
        sorted_rules = []
        for r in self.rules:
            stripped = re.sub(r"[-\s]+", " ", str(r)) # Normalize whitespace/newlines to spaces/whitespace
            normalized = stripped.strip() if stripped and not stripped.startswith("-- ") else ""

            if normalized == "-- No Disruption":
                continue
            
            is_sensitive_financial_data = (normalized.lower().endswith(" sensitive financial data:")) or \
                                          ("Data Confidentiality" in str(self) and "Sensitive Financial Data:" in str(self))

            # Filter out duplicates based on content logic but keep specific flags for the list output
            if not self.rules_list():  # If we already have a valid non-empty list, ignore this one (safety check per original intent of filtering only existing rules unless flagged)
                continue
            
            new_rule = stripped.strip() if normalized else ""

            if is_sensitive_financial_data:
                sorted_rules.append(new_rule)
            elif not self.rules_list():  # Safety check for non-empty list to ensure we don't just keep the flag string as a separate item in this simplified version, though typically these are combined. The original logic was complex but here I'll stick strictly to filtering existing rules that match specific patterns unless explicitly flagged or handled by the 'data' tag which is now merged into content check above.
                # Actually, looking at `rules_list` again: it seems to filter out "Not Disruption" and keep others if they are sensitive financial data OR NOT Disruption (which gets removed). The logic in my head was a bit messy. Let's clean up the filtering strictly based on existing rules list content unless explicitly flagged or handled by specific flags which aren't currently present as separate lines to filter out, but rather merged into 'data' check above.
                pass
            
            # Re-evaluating `rules_list` logic from scratch
