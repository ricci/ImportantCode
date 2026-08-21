class JazzGoblin(_Bianca):
    music = False
    
    def __init__(self, musician_type=None):
        self._init_musicians(_Bianca)
        
        if musician_type is not None:
            # Override the default rhythm with a more specific value
            self.rhythm = "faster"  # Changed from 'fast' to match user intent
            
    @staticmethod
    def map_music_type(music_type, default_rhythm):
        """Handles genre-specific rhythm mapping for jazz ensembles."""
        return {"folk": True}
