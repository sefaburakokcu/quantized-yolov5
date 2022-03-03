'''Filter pesron and car classes from Coco dataset'''

import os
import shutil


dataset_root = '/home/sefa/workspace/projects/finn/datasets/coco/'
partition = 'val2017'

labels_file = f'{dataset_root}{partition}.txt'
new_labels_file = f'{dataset_root}{partition}_2classes.txt'
save_labels_folder = f'{dataset_root}labels_2classes/{partition}/'
save_images_folder = f'{dataset_root}images_2classes/{partition}/'

if not os.path.exists(save_labels_folder):
    os.makedirs(save_labels_folder)

if not os.path.exists(save_images_folder):
    os.makedirs(save_images_folder)
    
with open(labels_file, 'r') as f:
    image_paths = f.read().strip().split()

f_new_labels_file = open(new_labels_file, "w")

for image_path_org in image_paths:
    image_path = image_path_org.replace("./", dataset_root)
    label_path = image_path.replace("images", "labels").replace(".jpg", ".txt")
    label_file = label_path.split("/")[-1]
    
    if os.path.exists(label_path):
        with open(label_path, "r") as f:
            lines_save = []
            lines = f.read().split("\n")
            for line in lines:
                if len(line) > 0:
                    if int(line.split(" ")[0]) in [0, 2]:
                        if line.startswith("2"):
                            line = "1"+line[1:]
                        lines_save.append(line)
            if len(lines_save) > 0:
                f_new_labels_file.write(image_path_org+"\n")
                save_image_path = save_images_folder+label_file.replace(".txt", ".jpg")
                shutil.copy2(image_path, save_image_path)
                save_label_path = save_labels_folder+label_file
                save_label_file = open(save_label_path, "w")
                for line_save in lines_save:
                    save_label_file.write(line_save+"\n")