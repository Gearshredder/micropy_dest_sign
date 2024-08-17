from modes.base_mode import BaseMode

class BounceMode(BaseMode):
    def __init__(self, config):
        super().__init__(config)
        self.pixel_x = 0
        self.pixel_y = 0
        self.velocity_x = 1
        self.velocity_y = 1

    def generate_pattern(self):
        pattern = [[0] * self.config.COLUMNS for _ in range(self.config.ROWS)]
        pattern[self.pixel_y][self.pixel_x] = 1
        return pattern

    def update_state(self):
        self.pixel_x += self.velocity_x
        self.pixel_y += self.velocity_y

        if self.pixel_x <= 0 or self.pixel_x >= self.config.COLUMNS - 1:
            self.velocity_x *= -1

        if self.pixel_y <= 0 or self.pixel_y >= self.config.ROWS - 1:
            self.velocity_y *= -1
