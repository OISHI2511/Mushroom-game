# 🍄 Mushroom Defense

Mushroom Defense is a 3D survival and defense game developed using Python and OpenGL. The player must protect the central mushroom from approaching snails while surviving, shooting enemies, and collecting points.

## 🎮 Features

- 3D game environment with a tiled grass floor.
- Player movement and rotation.
- Snail enemies that move toward the central mushroom.
- Shooting mechanics to eliminate enemies.
- Mushroom health and score tracking.
- First-person and third-person camera modes.
- Cheat mode for increasing the score.
- Turtle power-up that restores mushroom health.
- Pause, restart, win, and game-over states.
- Visual effects, lighting, and on-screen game information.

## 🕹️ Controls

| Key / Button | Action |
|---|---|
| `W` | Move forward |
| `S` | Move backward |
| `A` | Move left |
| `D` | Move right |
| `Space` or `Enter` | Shoot |
| Left mouse button | Switch camera view |
| Right mouse button | Shoot |
| `P` | Pause or resume |
| `R` | Restart the game |
| `C` | Toggle cheat mode |
| `Q` | Quit the game |

## 🛠️ Requirements

- Python 3
- PyOpenGL
- PyOpenGL-accelerate (optional)
- OpenGL and GLUT/freeglut support

## 📥 Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

Replace `YOUR_REPOSITORY_URL` with the URL of this GitHub repository.

### 2. Open the project folder

```bash
cd Mushroom-Defense
```

### 3. Install the Python dependencies

```bash
python -m pip install PyOpenGL PyOpenGL-accelerate
```

If the optional acceleration package fails to install, try:

```bash
python -m pip install PyOpenGL
```

### 4. Run the game

```bash
python project.py
```

Make sure that OpenGL and GLUT/freeglut are installed and configured on your system.

## 🎯 Objective

Protect the central mushroom from incoming snails. Shoot enemies to earn points, keep the mushroom's health above zero, and reach a score of 500 to win.

## 🧰 Technologies Used

- Python
- PyOpenGL
- OpenGL
- GLUT
- GLU

## 👩‍💻 Author

Created as a Python and computer graphics project.

## 📄 License

This project is available for educational and personal use. Please contact the author before redistributing or using it commercially.
