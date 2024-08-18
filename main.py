from config import display_config_s70_side as config

# Try to import the MicroPython-specific module to determine the environment
try:
    import machine
    from hardware_interface import HardwareInterface
    interface_type = "hardware"
except ImportError:
    from simulator import Simulator
    from gui import SimulatorApp
    interface_type = "simulator"

from display_controller import DisplayController
import sys

def main():
    # Determine the interface based on the environment
    if interface_type == "hardware":
        interface = HardwareInterface(config)
        print("Running on MicroPython hardware.")
        
        # Initialize the display controller with the hardware interface
        controller = DisplayController(config, interface)
        controller.run()
    
    elif interface_type == "simulator":
        print("Running on simulator with GUI.")

        # Create the root Tkinter window and run the simulator app
        from tkinter import Tk
        
        root = Tk()
        app = SimulatorApp(root, config)
        
        # Start the main Tkinter loop
        root.mainloop()

if __name__ == "__main__":
    main()
