import cv2
import json
import os

# Path to the directory containing the samples
json_samples_dir = '/Users/sejunpark/workspace/coco_to_yolo/json_samples'
yolo_samples_dir = '/Users/sejunpark/workspace/coco_to_yolo/yolo_samples'
image_samples_dir = '/Users/sejunpark/workspace/coco_to_yolo/image_samples'

# Iterate over the files in the samples directory
for filename in os.listdir(json_samples_dir):
    # Check if the file is a JSON file
    if filename.endswith('.json'):
        # Read the JSON file
        with open(os.path.join(json_samples_dir, filename), 'r') as file:
            data = json.load(file)
        
        # Get the corresponding image filename
        image_filename = os.path.splitext(filename)[0] + '.jpg'
        
        # Load the image
        image_path = os.path.join(image_samples_dir, image_filename)
        image = cv2.imread(image_path)
        
        # Draw annotations on the image
        for annotation in data['annotations']:
            x, y, w, h = int(annotation['bbox'][0]), int(annotation['bbox'][1]), int(annotation['bbox'][2]), int(annotation['bbox'][3])
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display the image with annotations
        cv2.imshow('Image with Annotations', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
for filename in os.listdir(yolo_samples_dir):
    # Check if the file is a text file
    if filename.endswith(".txt"):
        # Read the text file
        with open(os.path.join(yolo_samples_dir, filename), 'r') as file:
            data = file.read()
            
        # Get the corresponding image filename
        image_filename = os.path.splitext(filename)[0] + '.jpg'
        image = cv2.imread(image_path)
        
        # Draw annotations on the image
        for annotation in data.split('\n'):
            x, y, w, h = map(int, annotation.split()[1:])
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
        # Display the image with annotations
        cv2.imshow('Image with Annotations', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()