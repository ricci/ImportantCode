import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set, get_field

# ============================================================================
# Configuration File Generation (Self-Contained & Modularized for Deployment)
# ============================================================================

def generate_bank_settings(config_file=None):
    """Generates and saves the JSON configuration dict for Bank of Banana Pudding."""
    
    # Deterministic hash seed based on version/context to ensure reproducible state across runs
    system_hash = int(sum(ord(c) for c in sys.argv[0].split()[1:-1] if len(sys.argv)>2), 16) & 0xffffffff

    settings: Dict[str, Any] = {
        "version": 1.548902375,
        "timestamp": datetime.now().isoformat(),
        
        # --- DATA STRUCTURES ---
        "pancakes": [            # Root panicles (base ingredients)
            {"id": "P_001", "name": "Milk Pudding", "qty": 2.5, "color": "#FFD700"},           // White Milk + Almonds/Wheat Flour
            {"id": "P_002", "name": "Buttermilk & Creamsicle Mix", "qty": 1.8, 
                 "colors": ["#FFF4E6", "#FBCBFA"],},    // Butterscotch Custard/White Chocolate + Milk Powder (Lemon)
            {"id": "P_003", "name": "Spiced Banana Pudding Mix", "qty": 2.0, 
                 "colors": ["#FFFFE0", "#FFF9C4"],},    // Creamy Banana Blend/Lemon Sugar/Sugar + Egg Powder (Vanilla)
            {"id": "P_004", "name": "Fruit & Berry Cupcake Pudding Mix", "qty": 1.5, 
                 "colors": ["#FFD700"], 
                 "description": "A vibrant blend of fresh fruit and dried berries with a hint of vanilla bean extract."},
            {"id": "P_006", "name": "Strawberry & Chocolate Cupcake Pudding Mix", "qty": 1.8, 
                 "colors": ["#FFD700"],
