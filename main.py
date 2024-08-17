from config import display_config_s70_side as config

# Try to import the MicroPython-specific module
try:
    import machine
    from hardware_interface import HardwareInterface
    interface_type = "hardware"
except ImportError:
    from simulator import Simulator
    interface_type = "simulator"

from display_controller import DisplayController

def main():
    # Select the appropriate interface based on the environment
    if interface_type == "hardware":
        interface = HardwareInterface(config)
        print("Running on MicroPython hardware.")
    else:
        interface = Simulator(config)
        print("Running on simulator.")

    # Initialize the display controller with the selected interface
    controller = DisplayController(config, interface)

    # Run the initial mode (you can add mode-switching logic here if needed)
    controller.run()

if __name__ == "__main__":
    main()
