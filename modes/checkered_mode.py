from modes.base_mode import BaseMode

class CheckeredMode(BaseMode):
    def generate_pattern(self):
        pattern = []
        for row in range(self.config.ROWS):
            row_data = [(row + col) % 2 for col in range(self.config.COLUMNS)]
            pattern.append(row_data)
        return pattern
