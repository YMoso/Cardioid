# Cardioid Visualization with Pygame

This project generates mesmerizing **cardioid patterns** using modular multiplication, animated beautifully with `pygame`. Inspired by mathematical art and modular geometry.

![Cardioid Animation Preview](visualizasion.gif)

---

## Features

- Smooth animated cardioid pattern based on modular multiplication
- Optional color gradients (HSV rainbow mode)
- Toggle animation on/off with `Space` key
- Fully configurable via a `config` dictionary

---

1. **Installation:**
   - Make sure you have Python installed on your system.
   - Clone the repository to your local machine:
     
     ```bash
     git clone https://github.com/252514/Cardioid.git
     cd Cardioid
     ```

2. **Create and Activate a Virtual Environment:**
   - Create a virtual environment:
     
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       
       ```bash
       .\venv\Scripts\activate
       ```
     - On macOS/Linux:
       
       ```bash
       source venv/bin/activate
       ```
       
3. **Dependencies:**
   - Install the required dependencies using pip:
     
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Programm:**
   - Execute the main script:
     
     ```bash
     python main.py
     ```

5. **Program Controls:**
- **Spacebar**: Pause or unpause the program.
- **'q' Key**: Quit the program.


## Customizing the Cardioid Visualization

The cardioid visualization can be customized by modifying the `config.py` file. Here are the available parameters:

- **screen_resolution**: Tuple defining the window size in pixels (e.g., (800, 800)).
- **total_points**: Number of points evenly distributed around the circle.
- **radius**: Radius of the main circle in pixels.
- **multiplier**: Starting multiplier value used to generate the cardioid pattern.
- **color_background**: RGB tuple defining the background color (e.g., (0, 0, 0) for black).
- **line_color**: RGB tuple used for drawing lines if random_lines_color is set to False.
- **random_lines_color**: Boolean that enables a rainbow color effect for the lines when set to True.
- **running**: Boolean that determines whether the animation starts immediately.
- **frames**: Frames per second (FPS) to control animation speed.
