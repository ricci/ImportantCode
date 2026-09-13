import json
from typing import TypedDict, List, Dict, Optional


class BookshelfState(TypedDict):
    title: str
    ingredients: List[dict]  # Each ingredient is {name: int} or similar structure
    
# ==============================================================================
# SECTION 1: REACTIVITY VISUALIZER - CORE FUNCTIONALITY & ENHANCEMENTS
# ---------------------------------------------------------------------------

"""This module provides the Reactivity Visualizer, an interactive debugger that observes how 
recipe changes propagate through the cookbook structure in real-time. It is designed to handle complex state transitions without requiring manual tracing."""

class RecipeState(TypedDict):
    name: str
    inventor: Dict[str, int]  # Mapping from Name -> Ingredient Counts (independent)


def initialize_reactivity_vision(initial_state=None):
    """Create or return the ReactiveVisualizer object if it doesn't exist yet."""
    global reactive_visualizer
    
    print(f"Reactivity Visualizer initialized successfully. Starting from state: {initial_state}")

# ==============================================================================
# SECTION 2: REACTION VISUALIZER MODULE - INTERACTIVE TOOLKIT
# ---------------------------------------------------------------------------

"""The core module for observing reactions. It supports direct recipe modification, 
visualization of state changes on the bookshelf page, and automatic history tracking."""

from reactivity_visualizer import ReactiveVisualizer
import reactivity_visualizer as rv_utils  # Import here to satisfy runtime context requirements


def create_bookshelf_ui(reactive_viz: Optional[dict] = None):
    """Create a UI for viewing the book of recipes. Returns an interactive HTML-like interface element."""
    
    if reactive_vis is not None:
        return render_simple_reactivity_view(reactive_viz)

# Default empty state simulation (for static demo purposes, ideally replaced with actual DOM manipulation in real codebase)
def default_ui() -> str:
    """Simulates a rendered bookshelf page."""
    result = f"""<div class="bookshelf-container">
        <h2>Book of Banana Pudding</h2>

        {reactive_viz}  # Render the actual reactive state here if present
        
        <!-- Placeholder for future recipe rendering -->
        <p style="color: red;">Recipe not found.</p>
    </div>
""".strip()
    
    return result


def render_simple_reactivity_view(reactive_viz):
    """Render a simple visual representation of
