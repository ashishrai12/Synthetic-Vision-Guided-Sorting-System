import cv2
import numpy as np
import random

def draw_rotated_rectangle(img, center, size, angle, color=(255, 255, 255)):
    """
    Draw a rotated rectangle on the image.
    """
    # Get the rotation matrix
    rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
    # Define the rectangle points
    rect_points = np.array([
        [-size[0]/2, -size[1]/2],
        [size[0]/2, -size[1]/2],
        [size[0]/2, size[1]/2],
        [-size[0]/2, size[1]/2]
    ], dtype=np.float32)
    # Rotate the points
    rotated_points = cv2.transform(np.array([rect_points]), rot_mat)[0]
    # Translate to center
    rotated_points += center
    # Convert to int
    rotated_points = np.int32(rotated_points)
    # Draw the polygon
    cv2.fillPoly(img, [rotated_points], color)

def detect_rectangles(img):
    """
    Detect rectangles in the image and return their centers and angles.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    rectangles = []
    for contour in contours:
        # Approximate the contour
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:  # It's a quadrilateral
            # Get the min area rect
            rect = cv2.minAreaRect(contour)
            center = rect[0]
            angle = rect[2]
            rectangles.append((center, angle))
    return rectangles

def main():
    # Create a black 500x500 image
    img = np.zeros((500, 500, 3), dtype=np.uint8)
    
    # Draw 3 random white rectangles
    for _ in range(3):
        center = (random.randint(50, 450), random.randint(50, 450))
        size = (random.randint(20, 100), random.randint(20, 100))
        angle = random.uniform(0, 360)
        draw_rotated_rectangle(img, center, size, angle)
    
    # Detect rectangles
    rectangles = detect_rectangles(img)
    
    # Overlay green dot and orientation line
    for center, angle in rectangles:
        cx, cy = int(center[0]), int(center[1])
        # Green dot at center
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), -1)
        # Line indicating orientation
        length = 30
        end_x = int(cx + length * np.cos(np.radians(angle)))
        end_y = int(cy + length * np.sin(np.radians(angle)))
        cv2.line(img, (cx, cy), (end_x, end_y), (0, 255, 0), 2)
    
    # Save the image
    cv2.imwrite('output.png', img)
    
    # Print the pick-coordinates
    print("Detected rectangles:")
    for i, (center, angle) in enumerate(rectangles):
        print(f"Rectangle {i+1}: Center at ({center[0]:.1f}, {center[1]:.1f}), Angle: {angle:.1f} degrees")

if __name__ == "__main__":
    main()
