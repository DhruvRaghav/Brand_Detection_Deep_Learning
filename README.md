# Object Detection with YOLOv5 and Streamlit

## Abstract
"Guardians of the Street" is a cutting-edge project that integrates YOLOv5 for object detection with a user-friendly Streamlit web interface. It addresses the critical need for real-time, accurate image analysis in diverse domains such as brand recognition, general object detection, pothole identification, and facial detection. This project stands out for its real-world applicability, speed, and accuracy in processing and analyzing images.

## Data Description
This project utilizes the COCO 2017 dataset, annotated data accross India dataset, a comprehensive collection of images tailored for object detection, segmentation, and captioning. Key features of this dataset include:
- Over 200,000 labeled images.
- 80 object categories covering a broad spectrum of everyday objects and scenes.
- Detailed annotations, including object bounding boxes and segmentation masks.
The dataset's variety and real-world scenarios significantly contribute to the robustness and precision of our object detection model.

### Classes in COCO 2017 Dataset
- Person
- Bicycle
- Car
- Motorcycle
- Airplane
- Bus
- Train
- Truck
- Boat
- Traffic Light
- Fire Hydrant
- Stop Sign
- Parking Meter
- Bench
- Bird
- Cat
- Dog
- Horse
- Sheep
- Cow
- Elephant
- Bear
- Zebra
- Giraffe
- Backpack
- Umbrella
- Handbag
- Tie
- Suitcase
- Frisbee
- Skis
- Snowboard
- Sports Ball
- Kite
- Baseball Bat
- Baseball Glove
- Skateboard
- Surfboard
- Tennis Racket
- Bottle
- Wine Glass
- Cup
- Fork
- Knife
- Spoon
- Bowl
- Banana
- Apple
- Sandwich
- Orange
- Broccoli
- Carrot
- Hot Dog
- Pizza
- Donut
- Cake
- Chair
- Couch
- Potted Plant
- Bed
- Dining Table
- Toilet
- TV
- Laptop
- Mouse
- Remote
- Keyboard
- Cell Phone
- Microwave
- Oven
- Toaster
- Sink
- Refrigerator
- Book
- Clock
- Vase
- Scissors
- Teddy Bear
- Hair Drier
- Toothbrush


### Classes for Annotated Data
- Licence plate 
- traffic sign
- Brands( dominoz, mc donalds, pitzaa hut, petrol pumps.)
- potholes
- faces
- solar panel



## Algorithm Description
YOLOv5, the latest in the series of "You Only Look Once" models, is at the heart of our object detection solution. Known for its speed and accuracy, YOLOv5 performs object detection in real-time. It divides the image into a grid and predicts bounding boxes and class probabilities for these boxes. The model's ability to process images quickly without sacrificing accuracy makes it an excellent choice for real-time applications.

YOLOv5 Algorithm Description

- Convolutional Neural Network (CNN) Architecture:

    - YOLOv5 is built on a deep convolutional neural network, designed for the fast and accurate detection of objects in images.
    - It uses a series of convolutional layers to extract features from the input images.

- Single-Stage Detector:

    - Unlike two-stage detectors that first propose regions and then classify them, YOLO (You Only Look Once) is a single-stage detector. It does both region proposal and object classification in one forward pass of the network.

- Dividing Image into Grids:

    - YOLOv5 divides the input image into a grid. Each grid cell is responsible for predicting objects whose centers fall into it.

- Bounding Box Prediction:
   - For each grid cell, YOLO predicts bounding boxes and their corresponding confidence scores, indicating the likelihood of an object being present in the box and how accurate the box is.

- Class Probability Prediction:
   - Alongside bounding box predictions, it also predicts the class probabilities for each box. These probabilities indicate the likelihood of the detected object belonging to a particular class.

- Non-Maximum Suppression (NMS):
    - To reduce redundancy and filter out overlapping boxes, YOLOv5 uses Non-Maximum Suppression. NMS keeps only the highest confidence predictions and removes weaker overlapping boxes.
   
- Anchor Boxes:

    - YOLOv5 utilizes predefined anchor boxes, which help the model detect objects at different scales and aspect ratios more effectively.
  

Integration with  Web App in your Streamlit-based web application, the YOLOv5 algorithm is integrated to provide real-time object detection capabilities:

- Image Upload and Preprocessing:
    - Users upload images through the Streamlit interface. 
    - The images are then preprocessed (e.g., resized) to fit the input requirements of the YOLOv5 model.
  
- Object Detection:
    - The processed images are fed into the YOLOv5 model. 
    - The model performs object detection, outputting the locations (bounding boxes) and classes of the objects detected.

- Displaying Results:
    - The application processes the model's output and overlays the bounding boxes and class labels on the original image.
    - Users can view a side-by-side comparison of the original and processed images, showcasing the detection results.

- Customization Options:
    - Depending on how you've set it up, users might be able to choose specific detection options (like selecting particular object classes).


## Tools Used
- **Python & Streamlit**: Streamlit provides an intuitive way to build and share data applications, making it the backbone of our user interface.
- **YOLOv5**: Selected for its superior performance in object detection tasks.
- **Skimage**: Used for essential image processing tasks within the app.
- **OpenCV**: A crucial tool for image processing and real-time video operations.

## Implementation with Streamlit
The project harnesses Streamlit's capabilities to create an interactive and user-friendly interface. The application allows users to upload images and choose from various detection options. Below is a snippet showcasing the core functionality:

```python

def main():
    import streamlit.components.v1 as components

    st.sidebar.header("Choose an option")
    footer = """
       <div style='text-align: center; color: grey; padding: 10px;'>
           Developed by [Dhruv Raghav]
       </div>
       """
    components.html(footer)

    # Create a dropdown for brand options
    Pothole_option = st.sidebar.selectbox("Pothole Detection Options", ["Select an option", "Pothole Box", "Pothole Blur", "Pothole Draw"])
    # brand_options = ["Select an option", "Brand Box", "Brand Blur", "Brand Draw", "Brand Label"]

    # Create a dropdown for general object detection
    general_option = st.sidebar.selectbox("General Object Detection",
                                          ["Select an option", "Object Box", "Object Blur", "Object Draw"])

    Brand_option = st.sidebar.selectbox("Brand Detection Options", ["Select an option", "Brand Box", "Brand Blur", "Brand Draw"])

    Solar_option = st.sidebar.selectbox("Solar Detection Options", ["Select an option", "Solar Box", "Solar Blur", "Solar Draw"])

    Face2d_option = st.sidebar.selectbox("Face-2d Detection Options",
                                        ["Select an option", "face2d Box", "face2d Blur", "face2d Draw"])

    Face360_option = st.sidebar.selectbox("Face-360 Detection Options",
                                         ["Select an option", "face360 Box", "face360 Blur", "face360 Draw"])

    lp_2d_option = st.sidebar.selectbox("lp_2d Detection Options",
                                         ["Select an option", "lp_2d Box", "lp_2d Blur", "lp_2d Draw"])
    Tsdr_option = st.sidebar.selectbox("Tsdr Detection Options",
                                        ["Select an option", "tsdr Box", "tsdr Blur", "tsdr Draw"])
    files = st.file_uploader("Upload Images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if st.button("Process"):
        if Pothole_option == "Select an option" and general_option == "Select an option" and Brand_option == "Select an option" and Solar_option == "Select an option" and Face2d_option == "Select an option" and Face360_option== "Select an option" and lp_2d_option == "Select an option" and Tsdr_option == "Select an option":
            st.warning("Please select a Pothole or general object detection or a Brand or Solar or face2d or face360 or license option.")

        elif Pothole_option != "Select an option":
            process_pothole_image(Pothole_option.lower().replace(" ", "_"), files)

        elif general_option != "Select an option":
            print("0")
            process_object_image(general_option.lower().replace(" ", "_"), files)
            print("finished")


        elif Brand_option != "Select an option":
            print("0")
            process_brand_image(Brand_option.lower().replace(" ", "_"), files)
            print("finished")

        elif Solar_option != "Select an option":
            print("0")
            process_solar_image(Solar_option.lower().replace(" ", "_"), files)
            print("finished")
        elif Face2d_option != "Select an option":
            print("0")
            process_face2d_image(Face2d_option.lower().replace(" ", "_"), files)
            print("finished")

        elif Face360_option != "Select an option":
            print("0")
            process_face360_image(Face360_option.lower().replace(" ", "_"), files)
            print("finished")

        elif lp_2d_option != "Select an option":
            print("0")
            process_lp_2p_image(lp_2d_option.lower().replace(" ", "_"), files)
            print("finished")


        elif Tsdr_option != "Select an option":
            print("0")
            process_tsdr_image(Tsdr_option.lower().replace(" ", "_"), files)
            print("finished")



```

# Running the Streamlit App
Execute the following command to start the application:
```python
streamlit run Guardians_of_Street.py

```
This command initiates a local server, making the app accessible through a web browser.

### Pretrained Checkpoints

| Model                                                                                                | size<br><sup>(pixels) | mAP<sup>val<br>0.5:0.95 | mAP<sup>val<br>0.5 | Speed<br><sup>CPU b1<br>(ms) | Speed<br><sup>V100 b1<br>(ms) | Speed<br><sup>V100 b32<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>@640 (B) |
|------------------------------------------------------------------------------------------------------|-----------------------|-------------------------|--------------------|------------------------------|-------------------------------|--------------------------------|--------------------|------------------------|
| [YOLOv5n](https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5n.pt)                   | 640                   | 28.0                    | 45.7               | **45**                       | **6.3**                       | **0.6**                        | **1.9**            | **4.5**                |
| [YOLOv5s](https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5s.pt)                   | 640                   | 37.4                    | 56.8               | 98                           | 6.4                           | 0.9                            | 7.2                | 16.5                   |
| [YOLOv5m](https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5m.pt)                   | 640                   | 45.4                    | 64.1               | 224                          | 8.2                           | 1.7                            | 21.2               | 49.0                   |
| [YOLOv5l](https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5l.pt)                   | 640                   | 49.0                    | 67.3               | 430                          | 10.1                          | 2.7                            | 46.5               | 109.1                  |
| [YOLOv5x](https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5x.pt)                   | 640                   | 50.7                    | 68.9               | 766                          | 12.1                          | 4.8                            | 86.7               | 205.7                  |
|                                                                                                      |                       |                         |                    |                              |                               |                                |                    |                        |
| [YOLOv5n6](https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5n6.pt)                 | 1280                  | 36.0                    | 54.4               | 153                          | 8.1                           | 2.1                            | 3.2                | 4.6                    |
| [YOLOv5s6](https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5s6.pt)                 | 1280                  | 44.8                    | 63.7               | 385                          | 8.2                           | 3.6                            | 12.6               | 16.8                   |
| [YOLOv5m6](https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5m6.pt)                 | 1280                  | 51.3                    | 69.3               | 887                          | 11.1                          | 6.8                            | 35.7               | 50.0                   |
| [YOLOv5l6](https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5l6.pt)                 | 1280                  | 53.7                    | 71.3               | 1784                         | 15.8                          | 10.5                           | 76.8               | 111.4                  |
| [YOLOv5x6](https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5x6.pt)<br>+ [TTA][TTA] | 1280<br>1536          | 55.0<br>**55.8**        | 72.7<br>**72.7**   | 3136<br>-                    | 26.2<br>-                     | 19.4<br>-                      | 140.7<br>-         | 209.8<br>-             |

<details>
  <summary>Table Notes (click to expand)</summary>

- All checkpoints are trained to 300 epochs with default settings. Nano and Small models use [hyp.scratch-low.yaml](https://github.com/ultralytics/yolov5/blob/master/data/hyps/hyp.scratch-low.yaml) hyps, all others use [hyp.scratch-high.yaml](https://github.com/ultralytics/yolov5/blob/master/data/hyps/hyp.scratch-high.yaml).
- **mAP<sup>val</sup>** values are for single-model single-scale on [COCO val2017](http://cocodataset.org) dataset.<br>Reproduce by `python val.py --data coco.yaml --img 640 --conf 0.001 --iou 0.65`
- **Speed** averaged over COCO val images using a [AWS p3.2xlarge](https://aws.amazon.com/ec2/instance-types/p3/) instance. NMS times (~1 ms/img) not included.<br>Reproduce by `python val.py --data coco.yaml --img 640 --task speed --batch 1`
- **TTA** [Test Time Augmentation](https://github.com/ultralytics/yolov5/issues/303) includes reflection and scale augmentations.<br>Reproduce by `python val.py --data coco.yaml --img 1536 --iou 0.7 --augment`

</details>

# Usage Guide
- Start the App: Launch the Streamlit application.
- Upload Images: Users can upload images to be processed for object detection.
- Detection Options: Choose from options like pothole, brand, solar, face2d, face360, and license plate detection, TSDR

# View Results: 
- The app displays a side-by-side comparison of the original and processed images, showcasing the detection results.


# Results and Discussion
### TRAFFIC SIGN DETECTION AND RECOGNITION SAMPLE:
![Traffic Sign Original Image](C:\Users\Dhruv\Desktop\dhruv\dhruv\raw_results\tsdr\FCOM60809032023114526(1).jpg "Traffic Sign Detection")
![Traffic Sign Detection](C:\Users\Dhruv\Desktop\dhruv\dhruv\raw_results\tsdr\FCOM60809032023114526.jpg "Traffic Sign Detection")
![Traffic Sign Detection](C:\Users\Dhruv\Desktop\dhruv\dhruv\raw_results\tsdr\FCOM60809032023112916(1).jpg "Traffic Sign Detection")
![Traffic Sign Detection](C:\Users\Dhruv\Desktop\dhruv\dhruv\raw_results\tsdr\FCOM60809032023112916.jpg "Traffic Sign Detection")
![Traffic Sign Detection](C:\Users\Dhruv\Desktop\dhruv\dhruv\raw_results\tsdr\FCOM60809032023114526(1).jpg "Traffic Sign Detection")

![Traffic Sign Detection](C:\Users\Dhruv\Desktop\dhruv\dhruv\raw_results\tsdr\FCOM60809032023114526.jpg "Traffic Sign Detection")

### GENERAL OBJECT DETECTION RESULT
![Traffic Sign Detection](C:\Users\Dhruv\Desktop\000000167164.jpg "Traffic Sign Detection")
![Traffic Sign Detection](C:\Users\Dhruv\Desktop\000000166684.jpg "Traffic Sign Detection")




# Future Work
For future work, consider the following areas to expand and enhance in my  project:

- Algorithm Improvement and Customization:

  - Fine-Tuning YOLOv5: Adapt the YOLOv5 model to be more specific to certain use cases like pothole detection or brand recognition. This could involve training the model with a more focused dataset.
    Advanced Object Detection Features: Incorporate features like object tracking over time in video feeds, which can be especially useful in surveillance or traffic monitoring scenarios.
    Expanding Dataset and Classes:

  - Dataset Enrichment: Augment the COCO 2017 dataset with more images, particularly in under-represented categories or specific areas relevant to your application, like road conditions for pothole detection.
  New Object Classes: Introduce additional classes relevant to your targeted application domains. For instance, for traffic management, classes like 'road markings' or 'traffic signs' could be added.
  User Interface and Experience Enhancements:

  - Real-Time Video Processing: Extend the Streamlit interface to support real-time video processing and object detection in live video streams.
  Customizable Settings for Users: Allow users to adjust detection settings like sensitivity, detection zones, or specific object classes they are interested in.
  Integration with Other Technologies:

  - IoT and Smart City Integration: Explore integration with IoT devices or smart city infrastructure, enabling practical applications like traffic flow management or urban planning.
  API Development: Create an API for your object detection service, allowing other applications to use your model in a broader context.
  Performance Optimization and Scalability:

  - Optimizing for Speed and Accuracy: Continuously work on balancing speed and accuracy, ensuring the model performs well even in resource-constrained environments.
  Scalability Improvements: Make your application scalable, capable of handling high volumes of data or being deployed in cloud environments.
  Research and Collaboration:

  - Collaborative Projects: Collaborate with academic or industry partners for research and development in advanced object detection techniques.
  Publishing Findings: Document and publish your findings, improvements, and challenges to contribute to the wider research community.
  Ethical and Privacy Considerations:

  - Privacy Features: Implement features to address privacy concerns, especially in applications like facial detection.
  Ethical Use Guidelines: Develop guidelines for the ethical use of your technology, ensuring it's used responsibly.
  User Feedback and Community Building:

  - Community Engagement: Build a community around your project to gather user feedback, ideas for new features, and crowdsource solutions to challenges.
  Regular Updates Based on Feedback: Regularly update the project based on user feedback and the latest developments in the field.


# Contributing and Feedback
Contributions to the project are welcome. For feature requests, bug reports, or feedback, please [contact details or link to project repository].

