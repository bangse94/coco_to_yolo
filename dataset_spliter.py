import os
import os.path
import shutil
from tqdm import tqdm

train_src_dir = "/data/person_dataset/train/2_86"
valid_dest_dir = "/data/person_dataset/valid/2_86"
test_dest_dir = "/data/person_dataset/test/2_86"
img_count = 0
label_count = 0
for_valid_num = 9
for_test_num = 10

valid_img_cnt = 0
valid_label_cnt = 0
test_img_cnt = 0
test_label_cnt = 0

train_set = 0
total = 0

for root, _, files in list(os.walk(train_src_dir)):
    for file in files:
        if file.endswith('.jpg'):
            total += 1
            img_count += 1
            train_set += 1
            if img_count % for_valid_num == 0:
                shutil.move(os.path.join(root, file), os.path.join(valid_dest_dir, file))
                train_set -= 1
                valid_img_cnt += 1
            elif img_count % for_test_num == 0:
                shutil.move(os.path.join(root, file), os.path.join(test_dest_dir, file))
                train_set -= 1
                test_img_cnt += 1
        elif file.endswith('.txt'):
            total += 1
            label_count += 1
            if img_count % for_valid_num == 0:
                shutil.move(os.path.join(root, file), os.path.join(valid_dest_dir, file))
                train_set -= 1
                valid_label_cnt += 1
            elif img_count % for_test_num == 0:
                shutil.move(os.path.join(root, file), os.path.join(test_dest_dir, file))
                train_set -= 1
                test_label_cnt += 1
                
print(f"[INFO] Dataset split complete")
print(f"[INFO] Train Set - {train_set/2}, {(train_set/2)/total*100}%")
print(f"[INFO] Valid Set - img : {valid_img_cnt}, label : {valid_label_cnt}, {(valid_img_cnt/total)*100}%")
print(f"[INFO] Test Set - img : {test_img_cnt}, label : {test_label_cnt}, {(test_img_cnt/total)*100}%")