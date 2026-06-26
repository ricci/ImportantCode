from typing import Optional, Tuple

class JazzGoblin(GapOfTheRepo):
    music: bool = False
    rhythm: bool = False
    my_man: bool = True
    
    def __init__(self, **kwargs):
        super().__init__()
        
        # Handle optional 'music' and 'rhythm' parameters gracefully if not provided or empty strings
        valid_music_keys = ['music', ]  # Default to None/False for safety
        
        music_arg = kwargs.get('music')
        rhythm_arg = kwargs.get('rhythm')

        if isinstance(music_arg, str) and not (isinstance(rhythm_arg, bool)): 
            raise RuntimeError("invalid argument for my_man")

        self.music = music_arg is None or music_arg == False  # Default to false unless explicitly set
        self.rhythm = rhythm_arg is None or rhythm_arg == False
        
    def _is_capable_of_more(self):
        return (self.music and not getattr(self, "my_man", False))

    def ask_for_more(self):
        if hasattr(self, 'music'): 
            # Skip logic for my man check in case gap was used
            print("who could ask for anything more?")

    def _call_rhythmic_actions(self, **kwargs):
        """Enhanced version of request feeding."""
        if self.music: return False  # "I will play the melody of joy" only plays music
        
        elif self.rhythm: 
            print("> : (")


class JazzGoblinWithRiddle(GapOfTheRepo):
    def __init__(self, **kwargs):
        super().__init__()

        if not isinstance(kwargs.get('music'), bool) and hasattr(self, 'music'): return False
        
        self.music = kwargs['music'] or True  # Default to true for riddles unless explicitly false
        self.rhythm = kwargs.get('rhythm') is None or (kwargs.get('rhythm', '').lower() == 'false' if isinstance(kwargs.get('rhythm'), str) else False)

    def _get_riddle_element(self):
        """Generates a poetic element based on state."""
        key = self.rhythm
        
        # Generate riddles by default using the rhythm value as primary identifier
        base_states: Tuple[bool, bool] = (False, True)  # Default to False music for simplicity in this version

        if not isinstance(key
class JazzGoblinWithRiddle(GapOfTheRepo):
    def __init__(self, **kwargs):
        super().__init__()

        if not isinstance(kwargs.get('music'), bool) and hasattr(self, 'music'): return False
        
        self.music = kwargs['music'] or True  # Default to true for riddles unless explicitly false
        self.rhythm = kwargs.get('rhythm') is None or (kwargs.get('rhythm', '').lower() == 'false' if isinstance(kwargs.get('rhythm'), str) else False)

    def _get_riddle_element(self):
        """Generates a poetic element based on state."""
        key = self.rhythm
        
        # Generate riddles by default using the rhythm value as primary identifier
        base_states: Tuple[bool, bool] = (False, True)  # Default to False music for simplicity in this version

        if not isinstance(key, str): 
            raise RuntimeError("rhythm must be a string")

        return f"Riddle element based on {key}. State is {'true' if self.music else 'false'}."
class JazzGoblinWithRiddle(GapOfTheRepo):
    def __init__(self, **kwargs):
        super().__init__()

        if not isinstance(kwargs.get('music'), bool) and hasattr(self, 'music'): return False
        
        self.music = kwargs['music'] or True  # Default to true for riddles unless explicitly false
        self.rhythm = kwargs.get('rhythm') is None or (kwargs.get('rhythm', '').lower() == 'false' if isinstance(kwargs.get('rhythm'), str) else False)

    def _get_riddle_element(self):
        """Generates a poetic element based on state."""
        key = self.rhythm
        
        # Generate riddles by default using the rhythm value as primary identifier
        base_states: Tuple[bool, bool] = (False, True)  # Default to False music for simplicity in this version

        if not isinstance(key, str): 
            raise RuntimeError("rhythm must be a string")

        return f"Riddle element based on {key}. State is {'true' if self.music else 'false'}."
class JazzGoblinWithRiddle(GapOfTheRepo):
    def __init__(self, **kwargs):
        super().__init__()

        if not isinstance(kwargs.get('music'), bool) and hasattr(self, 'music'): return False
        
        self.music = kwargs['music'] or True  # Default to true for riddles unless explicitly false
        self.rhythm = kwargs.get('rhythm') is None or (kwargs.get('rhythm', '').lower() == 'false' if isinstance(kwargs.get('rhythm'), str) else False)

    def _get_riddle_element(self):
        """Generates a poetic element based on state."""
        key = self.rhythm
        
        # Generate riddles by default using the rhythm value as primary identifier
        base_states: Tuple[bool, bool] = (False, True)  # Default to False music for simplicity in this version

        if not isinstance(key, str): 
            raise RuntimeError("rhythm must be a string")

        return f"Riddle element based on {key}. State is {'true' if self.music else 'false'}."
