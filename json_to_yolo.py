import json

def convert_to_yolo(json_file, output_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    with open(output_file, 'w') as f:
        for image in data['images']:
            image_id = image['id']
            file_name = image['file_name']
            width = image['width']
            height = image['height']

            for annotation in data['annotations']:
                if annotation['image_id'] == image_id:
                    category_id = annotation['category_id']
                    bbox = annotation['bbox']
                    x, y, w, h = bbox

                    # Convert bbox coordinates to YOLO format
                    x_center = (x + w / 2) / width
                    y_center = (y + h / 2) / height
                    bbox_width = w / width
                    bbox_height = h / height

                    line = f"{category_id} {x_center} {y_center} {bbox_width} {bbox_height}\n"
                    f.write(line)

def check_files(src_dir, dest_dir, search_string):
    if not os.path.exists(src_dir):
        print(f"Source directory {src_dir} does not exist")
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if search_string in file:
                convert_to_yolo(os.path.join(root, file), os.path.join(dest_dir, file.replace('.json', '.txt')))

# Usage example
json_file_path = "/Users/sejunpark/workspace/coco_to_yolo/json_samples/CT_NOR_00_0038_01_LAT36-8119LNG127-1122_220824_180905_MO_PL_SU_W_PERSON0075_PERSON0076_00001.json"
output_file_path = "/Users/sejunpark/workspace/coco_to_yolo/yolo_samples/yolo.txt"
search_string = "NOR"

check_files(json_file, output_file, search_string)