# Configuration for S70 Side Display

# General Display Configuration
DISPLAY_NAME = "S70 Side Display"
ROWS = 16         # Number of rows
COLUMNS = 88      # Number of columns
COLUMN_SETS = 11   # Number of column sets (2 sets of 8 columns each)
CHIP_COUNT = 6    # Number of 16-bit serial chips (5 chips for full 16 bits and 1 for 8 bits)

# Pin Configuration
LATCH_PIN = 39              # Pin number for the latch signal
SERIAL_IN_PIN = 37          # Pin number for the serial data input
CLOCK_PIN = 35              # Pin number for the clock signal
ROW_SELECT_PINS = {         # Dictionary for row selection pins
    'A': 16,                # Pin number for row selection bit A
    'B': 18,                # Pin number for row selection bit B
    'C': 33,                # Pin number for row selection bit C
}
COLUMN_SET_SELECT_PIN = 32  # Pin number to switch between column sets (Set 1 and Set 2)
OUTPUT_ENABLE_PIN = 3       # Pin number for the Output Enable (E1), set to LOW to enable output

# Timing Configuration
CLOCK_DELAY_US = 1          # Microseconds delay for clock pulse (adjust for your hardware)
LATCH_DELAY_US = 10         # Microseconds delay after latching data
ROW_SWITCH_DELAY_US = 100   # Microseconds delay when switching rows

# Display Configuration
PERSISTENCE_OF_VISION = True  # Set True for persistence of vision operation
REFRESH_RATE_HZ = 60          # Desired refresh rate (adjust as necessary)
