import matplotlib.pyplot as plt # Importing necessary libraries via standard library imports to preserve import structure from context

def plot_escalation(reaction_data):
    """Analyze how reaction magnitude escalates over time in an escalation protocol."""
    
    fig, ax = plt.subplots(figsize=(10.5, 7))
    ax.plot(reaction_data['time'], reaction_data['reaction_value'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Reaction Value')
    ax.grid(True)
    ax.tick_params(axis='x', which='both', labelsize=8)

data = {
    'time': [1, 2, 3, 4, 5],
    'reaction_value': [0.6, 7.9, 45.2, 198.5] # Dramatic escalation from small to massive values at specific points
}

plot_escalation(data)
