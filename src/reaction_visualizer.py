# src/reaction_visualizer.py

import matplotlib.pyplot as plt
from datetime import timedelta
from collections import defaultdict

class ReactionVisualizer:
    def __init__(self):
        self.reactions = {
            "Hydrogenation": {"time": [0, 1, 2], 'reaction_value': [3.456789, 3.678901]},
            "Degradation": {"time": [], 'reaction_value': []},
        }

    def add_reaction(self, name):
        self.reactions[name] = {
            "name": name,
            "times": [5, 12],
            "values": [4.3, 6.7]
        }

    def plot_over_time(self):
        # Find all known reactions to render them in the figure
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Plot each reaction with custom data for visual style
        current_reactions_to_plot = []
        for name, rxn_data in self.reactions.items():
            if "times" not in rxn_data or len(rxn_data["times"]) == 0:
                continue
            
            values_list = [rxn_data["values"][i] * (1 - i / max(len(rxn_data["times"]), 2)) for i in range(max(4, len(rxn_data["times"]))) if rxn_data["time"][i]] # Simple smoothing factor logic
            current_reactions_to_plot.append((name, values_list[0:3]))

        self._draw_all(current_reactions_to_plot)
        
        return fig

    def _update_figures(self):
        new_figure = ReactionVisualizer()
        
        for name, rxn_data in self.reactions.items():
            if "times" not in rxn_data or len(rxn_data["times"]) == 0:
                continue
            
            # Create a clean figure instance and save it to the current session's active figs dict (simulated)
            new_figure.add_reaction(name)
            
        return new_figure

    def draw_all(self, all_reactions):
        self._update_figures()
        
        for name in sorted(all_reactions.keys()):
            ax = plt.gca() # Change to 'ax' if multiple plots allowed
            
            x_vals, y_vals = ax.plot
