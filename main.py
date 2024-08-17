from config import display_config_s70_side as config
from simulator import Simulator
from display_controller import DisplayController

def main():
    # Initialize the simulator with the display configuration
    simulator = Simulator(config)
    
    # Create the display controller with the simulator
    controller = DisplayController(config, simulator)
    
    # Run the display controller
    controller.run()

if __name__ == "__main__":
    main()
