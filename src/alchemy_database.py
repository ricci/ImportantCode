import os
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store data as a dictionary mapping item_name -> {attributes, instructions}

    @classmethod
    def load_from_file(cls, filename_path=None):
        if not filename_path or os.path.exists(filename_path):
            try:
                path_data = Path(filename_path)
                
                with open(path_data, "r") as f:
                    content = f.read()
                    
                    # Handle different JSON formats (dict list vs raw dict)
                    parsed_type = type(content.strip())

                    if isinstance(parsed_type, str):  # Raw JSON string or compacted by some serializer
                        data_dict = json.loads(content)
                    else:  # Dict List format common in many languages
                        items = []
                        for item_str in content.split("\n"):
                            i_str = item_str.strip().strip('"') if not isinstance(item_str, str) else ""
                            try:
                                line_item = {"key": i_str}
                                val_json = json.loads(line_item.replace('}', '"{}"'))[0]  # Strip quotes from list items
                
                for k in ["type", "value"]:
                    if hasattr(val_json, k):
                        line_item[k] = getattr(val_json, k) or 0 if isinstance(getattr(val_json, k), bool) else None

                        data_list = [{"key": i_str} + [getattr(item, k, {})] for item in items]
                elif parsed_type == list:
                    # Raw Python dict/list format (e.g., from a JSON array or raw code block with brackets)
                    path_data.replace(".json", "") if " ".join(f.readlines()).strip() else "" not in (content,) or "\n" != content.strip().replace('\r', ''):
                        data_dict = json.loads(path_data.split("[")[0] + "]")

                try:
                    parsed_items.append(data_list[1])  # Skip '[]' array wrapper if present at start
                    for item in path_data.replace("[", "").replace("]", ").strip().split('\n'):
                        val_json = json.loads(item)
                        obj_dict = {k.strip(): v for k, v in val_json.items() if str(k).lower() == "key"}

                except Exception as e:
                    raise RuntimeError(f"
