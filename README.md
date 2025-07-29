# Air Cube

**Immerse yourself in a completely new experience of solving a Rubik’s Cube — virtually, with hand gestures!**
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/86357cec-0430-4d57-a8f1-3b682bd3773a" />

---
## Features

- **Gesture-based Cube Manipulation**  
  Rotate each layer using intuitive hand gestures.

- **3D Cube Visualization**  
  Real-time animated 3D Rubik’s Cube using VPython.

- **Auto-Solver**  
  Solves the cube using the Kociemba two-phase algorithm.

- **Interactive GUI**  
  Animated intro screen built with Tkinter to launch the app.

---
### Modules Breakdown

- **`intro.py`**  
  Animated Tkinter GUI that starts the simulation.

- **`main.py`**  
  Real-time gesture tracking with MediaPipe and OpenCV.

- **`cube.py`**  
  Handles cube state, rotations, solving logic, and 3D rendering with VPython.

- **`solve_rubiccs_cube.py`**  
  Maps 3D tile positions to color codes and solves the cube using `kociemba`.

---
## How to Run

- Run the game using the `main.py` file.
- Alternatively, you can start with `intro.py`, which loads a landing page and redirects to `main.py`.  
  However, `intro.py` might face compatibility issues depending on your system and libraries. If so, proceed directly with `main.py`.

---

## Setup Instructions

- Upon running the code, a **web browser** window will open automatically.
- **Important:** For the motion tracking to work properly:
  - Position the browser window **exactly on the left half** of your screen.
  - Place the **video window on the right half**.
- Only when these are set correctly will the commands and gesture detection function as intended.

---

## Objective

Your goal is to solve the **Air Cube** — a virtual Rubik’s Cube — using either intuitive hand gestures or motion buttons.

Each of the six sides is painted in a distinct color:

🟥 Red | 🟧 Orange | 🟨 Yellow | ⬜ White | 🟦 Blue | 🟩 Green

Just like a traditional Rubik’s Cube, the goal is to return the cube to a state where **each face contains only one color**.

---

## Game Rules & Features

1. You can perform limited movements:  
   `Front`, `Back`, `Left`, `Right`, `Up`, `Down`  
   – as well as their **clockwise** and **anti-clockwise** rotations.

2. You can use the **cursor to rotate the view of the cube**.  
   ⚠Make sure to **return to the Front (Red)** face before making rotational moves.  
   If not, you may end up scrambling the cube further.

3. The cube is primarily designed to be solved via **hand gestures**, detected through your camera.  
   - The gestures are **intuitive**.  
   - If you're having trouble, fallback **motion buttons** are available.

---

## Demonstration

- [**Gameplay Demo**](https://drive.google.com/file/d/1xxBqRjJumUJq-gjA4iLhlUi-UUqtJMra/view?usp=drive_link)  
- [**Hand Gesture Instructions**](https://drive.google.com/file/d/1yPrervpLMQ_1p7VG5yfzrDntrbdN3X_9/view?usp=drive_link)

---

## ⚠Known Issues

- Some hand gestures may **not work** reliably due to **unresolved bugs** and **limited debugging time**.
- Make sure your camera is functioning and well-lit for gesture detection.

