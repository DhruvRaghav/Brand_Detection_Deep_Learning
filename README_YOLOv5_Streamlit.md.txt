
# Object Detection with YOLOv5 and Streamlit

## Abstract
This project integrates YOLOv5 for object detection with a Streamlit-based web interface, titled "Guardians of the Street". It is designed for real-time analysis and processing of images across various domains, including brand, object, pothole, and face detection.

## Data Description
[Detailed description of the dataset]

## Algorithm Description
[Brief description of YOLOv5]

## Tools Used
- **Python & Streamlit**: For creating a user-friendly web application.
- **YOLOv5**: For efficient and accurate object detection.
- **Skimage**: For image processing tasks.
- **OpenCV**: Utilized for image processing in the detection algorithms.
- [Other tools and their purposes]

## Implementation with Streamlit
The project leverages Streamlit for creating an interactive web interface. The main functionalities include uploading images, selecting detection options, and viewing processed results. The code snippet below outlines the core functionality:

```python
import streamlit as st
import skimage.io as io
from face_2D_detect import *
import blur
import os
import time
# [Rest of the provided code]
```

### Running the Streamlit App
To run the app, use the command:
```
streamlit run your_script_name.py
```
This will launch a local web server, and the Streamlit app can be accessed through a web browser.

## Usage
1. **Start the App**: Run the Streamlit app.
2. **Upload Images**: Users can upload images for object detection.
3. **Choose Detection Options**: Options for different types of detections like pothole, brand, solar, face2d, face360, and license plate are available.
4. **View Results**: The app processes the images and displays the original and processed images side-by-side.

[Optional sections: Challenges Faced, Results & Discussion, Future Work]
