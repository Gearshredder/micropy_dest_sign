from modes.bounce_mode import BounceMode
from modes.checkered_mode import CheckeredMode

class DisplayController:
    def __init__(self, config, interface):
        self.config = config
        self.interface = interface
        self.interface.setup()

        # Initialize modes
        self.modes = {
            "bounce": BounceMode(config),
            "checkered": CheckeredMode(config),
        }
        self.current_mode = self.modes["bounce"]

    def switch_mode(self, mode_name):
        if mode_name in self.modes:
            self.current_mode = self.modes[mode_name]
        else:
            print(f"Mode {mode_name} not found!")

    def run(self):
        while True:
            pattern = self.current_mode.generate_pattern()
            self.update_display(pattern)
            self.current_mode.update_state()
            self.interface.wait()

    def update_display(self, data):
        for row in range(self.config.ROWS):
            self.interface.activate_row(row)
            
            for set_number in range(self.config.COLUMN_SETS):
                start_col = set_number * 8
                end_col = start_col + 8
                if end_col > self.config.COLUMNS:
                    end_col = self.config.COLUMNS
                    
                column_data = data[row][start_col:end_col]
                if len(column_data) < 8:
                    column_data += [0] * (8 - len(column_data))
                    
                self.interface.select_column_set(set_number)
                self.interface.update_columns(column_data)
                self.interface.pulse_latch()
        
        self.interface.deactivate_row(row)
