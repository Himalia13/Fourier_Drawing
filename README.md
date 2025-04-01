
---

# 🎨 Fourier Series Animations and Frame Extraction

This repository contains Python scripts for creating animations of Fourier series using [Manim](https://github.com/ManimCommunity/manim) and extracting frames from the resulting videos using OpenCV. It combines mathematical visualization with video processing tools, ideal for educational purposes or creative projects.

## 📑 Table of Contents

1. [Repository Structure](#-repository-structure)
2. [Project Descriptions](#-project-descriptions)
   - [Fourier Series Animations](#1-fourier-series-animations)
   - [Video Frame Extraction](#2-video-frame-extraction)
3. [How to Use](#-how-to-use)
4. [Requirements](#%EF%B8%8F-requirements)
5. [Download as .zip](#-download-as-zip)
6. [Authors](#-authors)
7. [Contribution](#-contribution)
8. [License](#-license)

## 📁 Repository Structure

```
.
|-- assets
|   |-- svg_images
|   |   |-- text_Shown.svg
|   |   |-- c_clef.svg
|   |-- img.png
|-- Fps                    # Generated folder for extracted frames
|-- .gitignore
|-- fourier.py             # Manim script for Fourier animations
|-- extract_frames.py      # OpenCV script for frame extraction
```

## 📂 Project Descriptions

### 1. Fourier Series Animations
**Description:** A collection of animations visualizing Fourier series, capable of drawing LaTeX symbols (e.g., `\Sigma`, `\tau`) and SVG paths (e.g., musical clefs) using rotating vectors and circles. Includes custom examples like `MySVGAnimation` with text overlays and gradients.

- **Main File:**
  - `fourier.py` - Core script with classes like `FourierCirclesScene`, `FourierOfTexSymbol`, and `MySVGAnimation`.
- **Assets:**
  - `assets/svg_images/text_Shown.svg` - Static SVG path for `MySVGAnimation`.
  - `assets/svg_images/c_clef.svg` - Example SVG for clef animations.
  - `img.png` - Image used in `MySVGAnimation` (e.g., "silly car").

### 2. Video Frame Extraction
**Description:** A utility script to extract individual frames from a Manim-generated MP4 video, saving them as PNG files for further analysis or use.

- **Main File:**
  - `extract_frames.py` - Script to process videos like `MySVGAnimation.mp4`.
- **Output:**
  - `Fps/` - Folder containing extracted frames (e.g., `frame_000001.png`).

## 🚀 How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/fourier-animations.git
   ```
   Replace `your-username` with your GitHub username.

2. **Run Fourier Animations:**
   - Install Manim (see [Requirements](#%EF%B8%8F-requirements)).
   - Execute an animation, e.g.:
     ```bash
     manim -p fourier.py MySVGAnimation
     ```
   - Output video will be in `media/videos/`.

3. **Extract Frames:**
   - Update `video_path` in `extract_frames.py` to point to your video (e.g., `media/videos/eeQ4mbLj/1440p60/MySVGAnimation.mp4`).
   - Run the script:
     ```bash
     python extract_frames.py
     ```
   - Frames will be saved in the `Fps/` folder.

## 🛠️ Requirements

- **Python 3.8+**
- **Manim Community Edition** (Install via `pip install manim` or follow [Manim docs](https://docs.manim.community/en/stable/installation.html)).
- **OpenCV** (`pip install opencv-python`)
- **Other Python dependencies** (e.g., `numpy`, included with Manim).

## 📦 Download as .zip

If you prefer, download the repository as a .zip file:

1. Visit the repository page on GitHub.
2. Click the green **Code** button.
3. Select **Download ZIP** and extract the contents locally.

## 👥 Authors

- Andrés Velázquez Vela

## 🤝 Contribution

Contributions are welcome! Feel free to:
- Add new animation examples to `fourier.py`.
- Enhance frame extraction features in `extract_frames.py`.
- Submit a pull request or open an issue to discuss improvements.

## 📄 License

This project is free to use, modify, and distribute without restrictions.

---

### Notes:
- I omitted "Course Information" since no specific academic context was provided, but you can add it if relevant (e.g., tying it to a UC3M course).
- The `.gitignore` file is included in the structure based on your earlier request.
- Replace `your-username` with your actual GitHub username when setting up the repo.
- Adjust paths (e.g., `img.png`, SVG files) to match your local setup if they differ.

