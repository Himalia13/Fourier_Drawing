import cv2
import os
from datetime import timedelta

# Path to the MP4 video and output folder
video_path = "media/videos/eeQ4mbLj/1440p60/MySVGAnimation.mp4"  # Change this to your video path
output_folder = "Fps"        # Folder where the frames will be saved

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open the video
cap = cv2.VideoCapture(video_path)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open the video.")
    exit()

# Get video information
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
duration = frame_count / fps

print(f"Total frames: {frame_count}")
print(f"FPS: {fps}")
print(f"Duration: {str(timedelta(seconds=int(duration)))}")

# Counter for naming the frames
count = 0

# Extract all frames
while True:
    # Read the frame
    ret, frame = cap.read()
    
    # If there are no more frames, exit the loop
    if not ret:
        break
    
    # Generate the file name with leading zeros (e.g., frame_000001.png)
    frame_filename = os.path.join(output_folder, f"frame_{count:06d}.png")
    
    # Save the frame in PNG format (maximum quality, no lossy compression)
    cv2.imwrite(frame_filename, frame)
    
    # Increment the counter
    count += 1
    
    # Show progress (optional)
    if count % 100 == 0:
        print(f"Extracted {count} frames...")

# Release the capture object
cap.release()

print(f"Extraction completed. {count} frames were saved in {output_folder}")