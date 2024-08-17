class BaseMode:
    def __init__(self, config):
        self.config = config

    def generate_pattern(self):
        """
        Generate the display pattern for this mode.
        Should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method")

    def update_state(self):
        """
        Update the state of the mode.
        Optional: can be overridden by subclasses if needed.
        """
        pass
