'''
    This file is used to convert the coco dataset to yolo format.
    author : Polar
    e-mail : tpwns73@gmail.com
    github : https://github.com/
'''

import os, os.path, json
from tqdm import tqdm
from collections import defaultdict

class Seperator:
    def __init__( self, annotation_path: str) -> None:
        self.annotation_path = annotation_path
        self.image_dict = defaultdict(str)
        self.image_annotation_dict = defaultdict(list)
        
    def get_json_data(self):
        with open(self.annotation_path, 'r') as f:
            json_data = json.load(f)
        return json_data
    
    def get_image_dict_from_json(self, json_data: dict) -> dict:
        for image in tqdm(json_data['images']):
            self.image_dict[image['id']] = image['file_name']
        return self.image_dict
    
    def parse_annotations(self, json_data: dict, target_path: str) -> dict:
        for annotation in tqdm(json_data['annotations']):
            self.image_annotation_dict[annotation['image_id']].append(annotation)
        return self.image_annotation_dict
    
    def save_annotations(self, target_path: str, image_annotation: dict) -> None:
        for image_name, annotation in tqdm(image_annotation.items()):
            with open(os.path.join(target_path, image_name.replace('.jpg', '.txt')), 'w') as f:
                for annotation in annotations:
                    f.write(f"{annotation['category_id']} {annotation['bbox'][0]} {annotation['bbox'][1]} {annotation['bbox'][2]} {annotation['bbox'][3]}\n")
                    
                    
def main( annotation_path: str = './data/coco', target_path: str = './data/yolo'):
    kwargs = {
        'annotation_path': annotation_path,
        'target_path': target_path
    }
    