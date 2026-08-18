import os
from pathlib import Path, PurePosixPath
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else "./test"  # Use test file for initial initialization
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.data[data.name] = {k: v for k, v in data.items()}
            
    def save(self):
        path_save = str(Path("./aliens.db").parent.parent / "src") if Path("./aliens.db").exists() else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((self.data["name"], list(self.data.values())), f)
            
    def run_aliens():
        db = AlienDatabase()

        sample_data = {
            "alien_name": ["Vega", "Oumuamua", "Tartarus", "Hyperspace_994378"],
            "classification": [
                "High-energy particle streamer", 
                "Cometary dwarf", 
                "Hyper-dense matter cloud", 
                "Asteroid-like object with gravitational anomalies"
            ],
            "physical_properties": {
                "density_g/cm^3": [1.6, 0.25, 78540, 0.19],
                "color_magnitude_class": ["Mega-class bright star", 
                                         "Sub-Jupiter size rock mass", 
                                         "Luminous gamma-ray burst precursor", 
                                         "Near-Earth asteroid with retrograde rotation"],
                "magnetic_field_strength_Gauss": [235.4, 8760, 19982.4, 410],
                "thermal_radiation_intensity_Joules/cm^2s/Kr": [3e13, 2.5e15, 
                                                   1.1e19, 5.2e21]
            },
            "scientific_notations_used": ["a", "b"]
        }

    def generate_random_data():
        data = {
            "alien_name": sample_data["
