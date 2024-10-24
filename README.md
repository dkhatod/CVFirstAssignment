ROS2 Object Detection Assignment
Objective:
Your task is to create two ROS2 nodes:

Node 1: Captures frames from your webcam, runs YOLO object detection, and publishes a message (True/False) on whether a specific object (like a cat) is detected.
Node 2: Subscribes to the detection topic and prints detection results to the terminal.
you can use any pretrained yolo model, and it can detect anything. you can publish true/false or a list of bboxes or whatever you woud like
make sure to use 2 seperate nodes
