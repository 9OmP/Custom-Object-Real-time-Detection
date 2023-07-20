# YOLO-Based Object Detection Project

![banner (1)](https://github.com/9OmP/Custom-Object-Real-time-Detection/assets/104563841/0bc452cc-939b-457d-b874-3133569c0ac7)

## Description
This project utilizes the YOLO (You Only Look Once) object detection algorithm to detect and classify objects in real-time video streams. YOLO is an advanced deep learning architecture that can simultaneously predict multiple object bounding boxes and their class probabilities in a single forward pass, making it highly efficient for real-time applications.It sends a message containing the harmful object and the no. of person around with it.

## How It Works
The YOLO algorithm works by dividing the input image into a grid and predicting bounding boxes and class probabilities for each grid cell. The model then refines the predicted boxes using anchor boxes and confidence scores to determine object presence. The highest-confidence predictions are selected as final detections.

## Features
- Real-time object detection using YOLOv8 model
- Multi-class detection with bounding boxes and confidence scores
- Live video stream processing from RTSP camera or webcam
- Email alerts on detecting harmful objects
- Person counting in the frame
- OpenCV integration for visualizations and annotations

![ae lavlya](https://github.com/9OmP/Custom-Object-Real-time-Detection/assets/104563841/83920396-f92b-4019-9904-267b3d81e1fa)


## Getting Started
To run the project, follow these steps:

1. Clone the repository: `git clone https://github.com/9OmP/Custom-Object-Real-time-Detection.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Download the YOLOv8 model weights and place them in the appropriate directory.
4. Update the Mailjet API credentials in the script.
5. Connect your RTSP camera or use the webcam for live stream detection.
6. Run the script: `test5.py, test7.py, test8.py`

## Customization
Feel free to modify the classNames list to add or remove object classes based on your specific use case. Additionally, you can customize the email alert content and time intervals for alerts.

## Concept and Workflow
The project is based on the concept of real-time object detection using deep learning. It employs the YOLOv8 model, which is an efficient and accurate architecture for multi-class object detection. The YOLO algorithm divides the image into grids and predicts bounding boxes and object classes for each grid cell. This enables the model to detect multiple objects simultaneously in a single pass, making it suitable for real-time applications.

The project's workflow involves capturing a live video stream from an RTSP camera or webcam. The YOLO model processes each frame, identifies objects, and annotates them with bounding boxes and confidence scores. If harmful objects like knives or scissors are detected, the system sends real-time email alerts to notify the user.

With its ability to handle diverse object classes and deliver fast and accurate detections, this YOLO-based project offers a powerful and versatile solution for real-time object detection tasks.

## Contributing
Contributions are welcome! If you have any suggestions, bug fixes, or improvements, feel free to create a pull request.

## License
This project is open-source and released under the MIT License. You are free to use, modify, and distribute the code, but attribution to the original author is required.

## Acknowledgments
Special thanks to the Ultralytics team for their YOLO implementation and Mailjet for the email API.

## Contact
For any questions or inquiries, please contact me at [ompatil16022002@gmail.com]
