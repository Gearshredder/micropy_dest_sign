from machine import Pin
import time

class HardwareInterface:
    def __init__(self, config):
        """
        Initialize the HardwareInterface with the provided configuration.
        
        :param config: Configuration object or module with display settings.
        """
        self.config = config
        
        # Setup the pins based on the configuration
        self.latch_pin = Pin(config.LATCH_PIN, Pin.OUT)
        self.serial_in_pin = Pin(config.SERIAL_IN_PIN, Pin.OUT)
        self.clock_pin = Pin(config.CLOCK_PIN, Pin.OUT)
        self.row_pins = {
            'A': Pin(config.ROW_SELECT_PINS['A'], Pin.OUT),
            'B': Pin(config.ROW_SELECT_PINS['B'], Pin.OUT),
            'C': Pin(config.ROW_SELECT_PINS['C'], Pin.OUT),
        }
        self.column_set_pin = Pin(config.COLUMN_SET_SELECT_PIN, Pin.OUT)
        self.output_enable_pin = Pin(config.OUTPUT_ENABLE_PIN, Pin.OUT)

        # Initialize the output enable pin to low (active)
        self.output_enable_pin.value(0)
        
    def setup(self):
        """
        Perform any additional setup, if necessary.
        """
        # (Optional) Any additional setup can be performed here
        print("Hardware interface setup complete.")

    def activate_row(self, row):
        """
        Activate the given row.
        
        :param row: Row index to activate.
        """
        # Determine the binary values for A, B, C based on the row index
        self.row_pins['A'].value((row >> 0) & 1)
        self.row_pins['B'].value((row >> 1) & 1)
        self.row_pins['C'].value((row >> 2) & 1)
        print(f"Row {row} activated.")

    def deactivate_row(self, row):
        """
        Deactivate the given row.
        
        :param row: Row index to deactivate.
        """
        # Deactivating a row can simply be setting all row select pins low
        self.row_pins['A'].value(0)
        self.row_pins['B'].value(0)
        self.row_pins['C'].value(0)
        print(f"Row {row} deactivated.")

    def select_column_set(self, set_number):
        """
        Select the column set (0 or 1).
        
        :param set_number: 0 for the first set (columns 0-7), 1 for the second set (columns 8-15).
        """
        self.column_set_pin.value(set_number)
        print(f"Column set {set_number} selected.")

    def update_columns(self, data):
        """
        Update the columns for the current row and selected column set.
        
        :param data: List of column data (8 elements).
        """
        for bit in data:
            self.serial_in_pin.value(bit)
            self.pulse_clock()
        print(f"Columns updated with data: {data}")

    def pulse_clock(self):
        """
        Pulse the clock pin to shift in the next bit of data.
        """
        self.clock_pin.value(1)
        time.sleep_us(self.config.CLOCK_DELAY_US)
        self.clock_pin.value(0)
        time.sleep_us(self.config.CLOCK_DELAY_US)
        print("Clock pulsed.")

    def pulse_latch(self):
        """
        Pulse the latch pin to lock in the row data.
        """
        self.latch_pin.value(1)
        time.sleep_us(self.config.LATCH_DELAY_US)
        self.latch_pin.value(0)
        print("Latch pulsed.")

    def wait(self):
        """
        Add a delay to simulate real-time operation or allow for processing time.
        """
        time.sleep_us(self.config.ROW_SWITCH_DELAY_US)
        print("Waited for row switch delay.")
