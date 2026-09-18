class Task:
    """Represents an individual processing unit within the AlchemyManager."""
    
    def __init__(self, command_name: str):
        self.command = command_name
    
    @property
    def status(self) -> Status:
        return Status.IDLE
