import time

class Simulator:
    def __init__(self, config):
        """
        Initialize the Simulator with the provided configuration.
        
        :param config: Configuration object or module with display settings.
        """
        self.config = config
        self.display = [[0] * self.config.COLUMNS for _ in range(self.config.ROWS)]
        self.current_row = -1
        self.current_set = 0

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
        print(f"Row {row} activated.")

    def deactivate_row(self, row):
        """
        Deactivate the given row.
        
        :param row: Row index to deactivate.
        """
        print(f"Row {row} deactivated.")
        self.current_row = -1

    def select_column_set(self, set_number):
        """
        Select the column set (0 or 1).
        
        :param set_number: 0 for the first set (columns 0-7), 1 for the second set (columns 8-15).
        """
        self.current_set = set_number
        print(f"Column set {set_number} selected.")

    def update_columns(self, data):
        """
        Update the columns for the current row and selected column set.
        
        :param data: List of column data (8 elements).
        """
        start_col = self.current_set * 8
        for i, bit in enumerate(data):
            self.display[self.current_row][start_col + i] = bit
        print(f"Row {self.current_row} updated: {self.display[self.current_row]}")

    def pulse_latch(self):
        """
        Simulate latching the current row data to the display.
        """
        print(f"Latching data for row {self.current_row}.")

    def wait(self):
        """
        Add a delay to simulate real-time operation.
        """
        time.sleep(0.05)  # Simulate a refresh rate of 20 frames per second

    def display_output(self):
        """
        Display the current state of the entire display.
        """
        print("\nCurrent Display State:")
        for row in self.display:
            row_str = ''.join(['█' if bit else ' ' for bit in row])
            print(row_str)
        print("\n" + "=" * self.config.COLUMNS + "\n")

