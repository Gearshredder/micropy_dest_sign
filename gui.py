import os
import tkinter as tk
import pygame
from tkinter import ttk

class SimulatorApp:
    def __init__(self, root, config):
        self.root = root
        self.config = config
        self.root.title("Simulator with GUI Controls")

        # Define the size of each "LED" pixel
        self.led_size = 10

        # Set the size of the Pygame display to match 16x88 grid
        self.display_width = self.config.COLUMNS * self.led_size
        self.display_height = self.config.ROWS * self.led_size

        # Create the Pygame frame inside a Tkinter Canvas
        self.canvas = tk.Canvas(root, width=self.display_width, height=self.display_height)
        self.canvas.grid(row=0, column=0, rowspan=4)

        # Create the Pygame surface
        self.embed = tk.Frame(self.canvas, width=self.display_width, height=self.display_height)
        self.embed.grid(row=0, column=0)
        self.embed.pack_propagate(0)
        
        os.environ['SDL_WINDOWID'] = str(self.embed.winfo_id())
        pygame.display.init()
        self.screen = pygame.display.set_mode((self.display_width, self.display_height))
        self.running = True

        # Initialize for bounce mode as default
        self.current_mode = "Bounce"
        self.object_x = 0
        self.object_y = 0
        self.object_velocity_x = 1  # Adjust speed to fit the grid size
        self.object_velocity_y = 1

        # Add GUI elements next to the simulator
        self.label = tk.Label(root, text="Mode:")
        self.label.grid(row=0, column=1)

        self.mode_var = tk.StringVar()
        self.dropdown = ttk.Combobox(root, textvariable=self.mode_var)
        self.dropdown['values'] = ("Bounce", "Checkered", "Static")
        self.dropdown.grid(row=1, column=1)
        self.dropdown.current(0)

        self.update_button = tk.Button(root, text="Update Mode", command=self.update_mode)
        self.update_button.grid(row=2, column=1)

        self.quit_button = tk.Button(root, text="Quit", command=self.quit_app)
        self.quit_button.grid(row=3, column=1)

        # Start the Pygame loop
        self.root.after(100, self.run_pygame)

    def run_pygame(self):
        while self.running:
            self.screen.fill((0, 0, 0))  # Clear the screen

            if self.current_mode == "Bounce":
                # Update object position
                self.object_x += self.object_velocity_x
                self.object_y += self.object_velocity_y

                # Bounce off the edges
                if self.object_x <= 0 or self.object_x >= self.display_width - self.led_size:
                    self.object_velocity_x *= -1
                if self.object_y <= 0 or self.object_y >= self.display_height - self.led_size:
                    self.object_velocity_y *= -1

                # Draw the moving object (representing a bouncing pixel)
                pygame.draw.rect(self.screen, (255, 0, 0), 
                                 (self.object_x, self.object_y, self.led_size, self.led_size))

            elif self.current_mode == "Checkered":
                # Draw a checkered pattern
                for row in range(self.config.ROWS):
                    for col in range(self.config.COLUMNS):
                        color = (255, 0, 0) if (row + col) % 2 == 0 else (0, 0, 0)
                        pygame.draw.rect(self.screen, color,
                                         (col * self.led_size, row * self.led_size, self.led_size, self.led_size))

            elif self.current_mode == "Static":
                # Draw a static pattern (you can define any static pattern here)
                for row in range(self.config.ROWS):
                    for col in range(self.config.COLUMNS):
                        color = (255, 0, 0) if row == 0 or col == 0 else (0, 0, 0)
                        pygame.draw.rect(self.screen, color,
                                         (col * self.led_size, row * self.led_size, self.led_size, self.led_size))

            pygame.display.flip()  # Update the display

            # Handle Pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_app()

            self.root.update_idletasks()
            self.root.update()

    def update_mode(self):
        selected_mode = self.mode_var.get()
        print(f"Selected Mode: {selected_mode}")
        self.current_mode = selected_mode  # Change the current mode

    def quit_app(self):
        self.running = False
        pygame.quit()
        self.root.quit()
