# ASCII ART

This repository contains Python scripts to convert images and live video into ASCII art.

## How to Use

### File 1: img_ascii.py

This script converts images (supports GIF and MP4 too) into ASCII art. It uses the `PIL` library to process images.

#### Usage:
1. Place the image or video file in the `imgs` folder.
2. Run the script `img_ascii.py`.
3. Enter the name of the image or video file (with extension) when prompted.
4. The converted ASCII art will be displayed in the terminal.

### File 2: live_video_ascii.py

This script captures live video from the webcam and converts it into ASCII art in real-time. It uses the `cv2` library for video capture.

#### Usage:
1. Run the script `live_video_ascii.py`.
2. Adjust the sensitivity of dark regions if required (determines how dark a color should be to not show).
3. The live video feed will be displayed in the terminal as ASCII art.
4. Press any key and then Ctrl+C to stop the program.

## Note
Ensure you have the necessary libraries installed (`PIL`, `opencv-python`) before running the scripts.
