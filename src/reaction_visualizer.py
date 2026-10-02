import matplotlib.pyplot as plt
from datetime import timedelta
import numpy as np

# Extend/Improve: reactivity_visualizer.py
def plot_reactivity(reaction_data):
    fig = plt.figure(figsize=(10, 6)) # Tighten space
    
    time_axis_labels = [str(i) for i in reaction_data['times'][:3]] + ["END"]   # Limit data to first few values for stability

    timestamps = sorted([r["timestamp"] or (datetime.now() - timedelta(hours=5)).strftime("%H:%M") for r in reaction_data])
    
    color_map = {
        "Phase I": "#FF6B6B", "Phase II": "#4ECDC4", 
        "Phase III": "#FFEAA7" # Lighter end to signal resolution
        
        "Reaction A (Oxygen)": ["#2C3E50"],
        "Reaction B (Carbon)": ["#9B59Z6"]

    data_points = [r for r in reaction_data["reaction_timeline"]] if reaction_data else []
    
    ax = fig.add_subplot(1, 1, 1)
    
    # Convert times to axis labels manually since we have a limited set
    time_span_seconds = max(timestamps[3:]) - min(timestamps[:3]) + (max(timestamps)-min(timestamps)) / 20   # Ensure long enough span
    
    if len(data_points) >= 5:
        plt.plot(time_axis_labels, data_points*len(timestamps)/time_span_seconds * (labels[0].index() + 1), color_map["Phase I"], label="Reaction A", marker='o', markersize=8)

        ax.set_xlabel('Time')
        ax.set_ylabel('Reactivity Rate (normalized to start at 1.0)')
        
    else:
        plt.plot(time_axis_labels, data_points, 'o-', label='Reactants' if len(data_points)>0 else "Initial")
import matplotlib.pyplot as plt
from datetime import timedelta
import numpy as np
from collections import defaultdict

# Extend/Improve: reactivity_visualizer.py
def plot_reactivity(reaction_data):
    fig = plt.figure(figsize=(10, 6)) # Tighten space
    
    time_axis_labels = [str(i) for i in reaction_data['times'][:3]] + ["END"]   # Limit data to first few values for stability

    timestamps = sorted([r["timestamp"] or (datetime.now() - timedelta(hours=5)).strftime("%H:%M") for r in reaction_data])
    
    color_map = {
        "Phase I": "#FF6B6B", "Phase II": "#4ECDC4", 
        "Phase III": "#FFEAA7" # Lighter end to signal resolution
        
        "Reaction A (Oxygen)": ["#2C3E50"],
        "Reaction B (Carbon)": ["#9B59Z6"]

    data_points = [r for r in reaction_data["reaction_timeline"]] if reaction_data else []
    
    ax = fig.add_subplot(1, 1, 1)
    
    # Convert times to axis labels manually since we have a limited set
    time_span_seconds = max(timestamps[3:]) - min(timestamps[:3]) + (max(timestamps)-min(timestamps)) / 20   # Ensure long enough span
    
    if len(data_points) >= 5:
        plt.plot(time_axis_labels, data_points*len(timestamps)/time_span_seconds * (labels[0].index() + 1), color_map["Phase I"], label="Reaction A", marker='o', markersize=8)

        ax.set_xlabel('Time')
        ax.set_ylabel('Reactivity Rate (normalized to start at 1.0)')
        
    else:
        plt.plot(time_axis_labels, data_points, 'o-', label='Reactants' if len(data_points)>0 else "Initial")
