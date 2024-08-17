import pygame
import time

class Simulator:
    def __init__(self, config):
        """
        Initialize the Simulator with the provided configuration.
        
        :param config: Configuration object or module with display settings.
        """
        self.config = config
        self.display = [[0] * self.config.COLUMNS for _ in range(self.config.ROWS)]
        self.previous_display = [[-1] * self.config.COLUMNS for _ in range(self.config.ROWS)]  # Initialize with invalid state
        self.current_row = -1
        self.current_set = 0

        # Pygame setup
        pygame.init()
        self.led_size = 10  # Size of each LED
        self.screen_width = self.config.COLUMNS * self.led_size
        self.screen_height = self.config.ROWS * self.led_size
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.config.DISPLAY_NAME)
        self.clock = pygame.time.Clock()

    def setup(self):
        """
        Set up the simulator (if necessary).
        """
        print("Simulator setup complete.")

    def activate_row(self, row):
        """
        Activate the given row.
        
        :param row: Row index to activate.
        """
        self.current_row = row

    def deactivate_row(self, row):
        """
        Deactivate the given row.
        
        :param row: Row index to deactivate.
        """
        self.current_row = -1

    def select_column_set(self, set_number):
        """
        Select the column set (0 or 1).
        
        :param set_number: 0 for the first set (columns 0-7), 1 for the second set (columns 8-15).
        """
        self.current_set = set_number

    def update_columns(self, data):
        """
        Update the columns for the current row and selected column set.
        
        :param data: List of column data (8 elements).
        """
        start_col = self.current_set * 8
        for i, bit in enumerate(data):
            self.display[self.current_row][start_col + i] = bit

    def pulse_latch(self):
        """
        Simulate latching the current row data to the display.
        """
        if self.display_has_changed():
            self.display_output()

    def display_has_changed(self):
        """
        Check if the display content has changed since the last update.
        """
        if self.display != self.previous_display:
            self.previous_display = [row[:] for row in self.display]  # Deep copy the current display
            return True
        return False

    def display_output(self):
        """
        Display the current state of the entire display.
        """
        self.screen.fill((0, 0, 0))  # Clear the screen with black background
        for row in range(self.config.ROWS):
            for col in range(self.config.COLUMNS):
                color = (255, 0, 0) if self.display[row][col] == 1 else (0, 0, 0)
                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(
                        col * self.led_size, row * self.led_size, self.led_size, self.led_size
                    )
                )
        pygame.display.flip()  # Update the display
        self.clock.tick(60)  # Limit to 60 FPS

    def handle_events(self):
        """
        Handle Pygame events to keep the window responsive.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def wait(self):
        """
        Add a delay to simulate real-time operation.
        """
        self.handle_events()
        time.sleep(0.05)  # Simulate a refresh rate of 20 frames per second

    def close(self):
        """
        Close the Pygame window.
        """
        pygame.quit()
