import os
import json
import random
import shutil

# Paths to the folders and JSON files
image_dir = "D:/vs projects/bdd100k/bdd100k/images/10k"
train_img_dir = os.path.join(image_dir, "train")
val_img_dir = os.path.join(image_dir, "val")
test_img_dir = os.path.join(image_dir, "test")

label_dir = "D:/vs projects/bdd100k_labels_release/bdd100k/labels"

train_json_path = os.path.join(label_dir, "bdd100k_labels_images_train.json")
val_json_path = os.path.join(label_dir, "bdd100k_labels_images_val.json")

# Output folders for split dataset
output_dir = "D:/vs projects/bdd100k_split"
output_train_dir = os.path.join(output_dir, "train")
output_val_dir = os.path.join(output_dir, "val")
output_test_dir = os.path.join(output_dir, "test")

# Make sure output folders exist
os.makedirs(output_train_dir, exist_ok=True)
os.makedirs(output_val_dir, exist_ok=True)
os.makedirs(output_test_dir, exist_ok=True)

# Number of images to extract
num_train = 1000
num_val = 500
num_test = 500


# Load JSON annotations
def load_json(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)
    return data


# Save the selected annotations to a new file
def save_annotations(selected_img_names, annotations, output_json_path):
    selected_annotations = [
        ann for ann in annotations if ann["name"] in selected_img_names
    ]
    with open(output_json_path, "w") as f:
        json.dump(selected_annotations, f)


# Select random images and copy them to the destination folder
def select_and_copy_images(src_dir, dest_dir, num_images, annotations):
    img_list = os.listdir(src_dir)
    selected_imgs = random.sample(img_list, num_images)

    for img_name in selected_imgs:
        img_src_path = os.path.join(src_dir, img_name)
        img_dest_path = os.path.join(dest_dir, img_name)
        shutil.copy(img_src_path, img_dest_path)

    # Get the corresponding image names without extensions for the annotation search
    selected_img_names = [os.path.splitext(img_name)[0] for img_name in selected_imgs]

    return selected_img_names


# Split the train, val, test images
def split_dataset():
    # Train
    train_annotations = load_json(train_json_path)
    selected_train_imgs = select_and_copy_images(
        train_img_dir, output_train_dir, num_train, train_annotations
    )
    save_annotations(
        selected_train_imgs,
        train_annotations,
        os.path.join(output_dir, "train_labels.json"),
    )

    print("train comp")
    # Val
    val_annotations = load_json(val_json_path)
    selected_val_imgs = select_and_copy_images(
        val_img_dir, output_val_dir, num_val, val_annotations
    )
    save_annotations(
        selected_val_imgs, val_annotations, os.path.join(output_dir, "val_labels.json")
    )

    print("val comp")
    # # Test (no labels for test set)
    # select_and_copy_images(test_img_dir, output_test_dir, num_test, None)

    print("Dataset split complete!")


if __name__ == "__main__":
    split_dataset()
