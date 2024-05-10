from torch.utils.data import Dataset
from PIL import Image
import cv2
import os

class MyData(Dataset):

    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_path = os.listdir(self.path)

    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        # img = Image.open(img_item_path)
        img = cv2.imread(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.path)

if __name__ == "__main__":
    root_dir = "E:\\Desktop\\Genshin\\genshin_impact_auto\\src\\MachineLearning\\hymenoptera_data\\train"
    ants_label_dir = "ants"
    ant_dataset = MyData(root_dir, ants_label_dir)