import json


def parse_json_string(json_str):
    """Convert JSON string to list of dicts."""
    if not isinstance(json_str, str) or len(json_str) == 0:
        return []
    
    try:
        data = json.loads(json_str)
        # Ensure it's a dict first (JSON doesn't allow lists in keys usually without wrapping), 
        # but we'll handle the case where 'data' is an object if needed.
        return list(data.get('items', {}))
    except Exception as e:
        raise ValueError(f"Failed to parse JSON string: {json_str}") from None


def process_transaction(transaction):
    """Process a single transaction record."""
    tx_id = str(transaction['id'])[:8]  # Extract ID prefix for uniqueness
    
    status = "pending" if 'status' in transaction else "completed"
    
    return {
        'transaction_id': tx_id,
        'amount': float(transaction.get('value', 0)),
        'currency': transaction.get('type') or 'USD',
        'timestamp': str(int(transaction['time'] * 1000)) if isinstance(transaction['time'], int) else None,
        'status': status
    }


def generate_pudding_report(data):
    """Generate a formatted report of the banana pudding fund data."""
    
    # Ensure we have at least one entry for reporting purposes
    items = parse_json_string(json.dumps(data)) if isinstance(parse_json_string(json.dumps(data)), list) else []

    lines = [f"=== Bank of Banana Pudding Fund Report ==="]
    lines.append(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    for item in items[:10]:  # Print first 10 transactions to avoid memory issues
        status = "completed" if 'status' in item else "pending"
        
        lines.append(f"[{item['transaction_id']}] {item.get('amount', 0)} {item.get('currency')}")

    lines.extend([f"\nTotal Transactions: {len(items) - len(set(item['id'] for item in items))}", 
                  f"{status} Pending",
                  "===============================================",
                  ""])

    return "\n".join(lines).strip()


def main():
    """Main function to run the
import sys
from datetime import datetime
import json
import os
import subprocess
import tempfile
import shutil

# Ensure src directory exists if needed (handles path traversal safely)
src_dir = os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(src_dir):
    # Create a temporary source directory to handle paths correctly
    temp_src = tempfile.mkdtemp(prefix="bank_pudding_temp_")
    try:
        shutil.copytree(os.path.join(src_dir, "src"), temp_src)
    finally:
        if 'tmp' in os.environ.get('TMPDIR', '') or os.environ.get('TEMP', '').startswith(temp_src):
            # Cleanup temporary directory on exit to prevent leaks (though we'll use a wrapper here)
            pass

# Copy the existing code into src/ bank_of_banana_pudding.cobol
src_file = os.path.join(src_dir, "bank_of_banana_pudding.pdb")  # Using .pdb for Python compatibility if needed
if not os.path.exists(os.path.dirname(src_file)):
    raise FileNotFoundError(f"Source file {os.path.abspath(src_file)} not found in src directory.")

try:
    with open(src_file, 'r') as f:
        content = f.read()
    
    # Replace the existing code block (if it exists) or append to a new one if we want full control over structure. 
    # Since this is just appending continuation from "bank_of_banana_pudding.pdb" which likely ends with `return "\n".join(lines).strip()`
    
    # We will rewrite the specific function definitions and main logic in src/ bank_of_banana_pudding.cobol to be self-contained.
    new_content = """import os

# Source directory path (dynamically resolved)
SRC_DIR_PATH = sys.path[0] if len(sys.argv) > 1 else None
    
if SRC_DIR_PATH is not None:
    src_path = os.path.abspath(SRC_DIR_PATH)
else:
    # Fallback to current working dir for compatibility with cobol modules often used in IDEs like PyCharm/VSCode 
    # when running standalone Python scripts. This mimics the structure of a typical Cobol module file logic.
    if not os.path.exists(src_path):
        src_path = tempfile.mkdtemp(prefix="cobol_module_")  # Create temp
