# Synthetic Vision-Guided Sorting System

This project implements a synthetic vision-guided sorting system using OpenCV and NumPy. It simulates a factory floor with randomly placed packages (rectangles) and detects their positions and orientations for robotic pick-and-place operations.

## Features

- Generates a synthetic 500x500 image of a factory floor
- Randomly places 3 white rectangles representing packages
- Detects rectangles using contour analysis
- Calculates center coordinates and rotation angles
- Overlays visual indicators (green dots and orientation lines)
- Outputs pick coordinates to the terminal
- Saves the processed image as `output.png`

## Requirements

- Python 3.x
- OpenCV
- NumPy

Install dependencies:
```
pip install -r requirements.txt
```

## Usage

Run the script:
```
python vision_engine.py
```

The script will print the pick coordinates for each detected package and save the output image.

## Example Output

```
Pick coordinates: (245, 110) @ 45°
Pick coordinates: (150, 300) @ 120°
Pick coordinates: (400, 200) @ 90°
```

## Logic Flow

1. Create a black canvas
2. Draw random rotated rectangles
3. Convert to grayscale and threshold
4. Find contours
5. For each contour, compute minimum area rectangle
6. Extract center and angle
7. Draw overlays
8. Print coordinates and save image

## Synthetic vs. Real World

| Feature | Synthetic Testing | Real-World Deployment |
|---------|-------------------|----------------------|
| Input | `numpy.zeros()` | USB Webcam / Industrial Camera |
| Lighting | Perfectly uniform | Variable / Noisy |
| Cost | $0 | $1,000+ |
| Use Case | Algorithm Validation | Physical Sorting |

This synthetic approach allows for rapid testing and validation of vision algorithms without hardware costs.
