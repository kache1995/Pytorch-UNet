from utils.dataset import BasicDataset
from torch.utils.data import DataLoader, random_split
import os
from PIL import Image

def fun1():
    dir_img = 'data/imgs/'
    dir_mask = 'data/masks/'
    img_scale=0.5
    val_percent=0.1
    batch_size = 1
    dataset = BasicDataset(dir_img, dir_mask, img_scale)
    n_val = int(len(dataset) * val_percent)
    n_train = len(dataset) - n_val
    train, val = random_split(dataset, [n_train, n_val])
    train_loader = DataLoader(train, batch_size=batch_size, shuffle=True, num_workers=8, pin_memory=True)

    for batch in train_loader:
        imgs = batch['image']
        true_masks = batch['mask']
        print(imgs.shape)
        exit(0)

def fun2():
    img_folder = r"/home/ffbian/myspace/datasets/icdar2019/0325updated_task1train_626p/0325updated_task1train_626p"
    img_names = [name for name in os.listdir(img_folder) if '.jpg' in name]
    for img_name in img_names:
        img_path = os.path.join(img_folder, img_name)
        img = Image.open(img_path)
        if len(img.split()) != 3:
            print(img_name)

def fun3():
    img_folder = r"/home/ffbian/myspace/datasets/icdar2019/0325updated_task1train_626p/0325updated_task1train_626p"
    img_name = "X51007231344.jpg"
    img_path = os.path.join(img_folder, img_name)
    img = Image.open(img_path)
    print(img.mode)



if __name__ == "__main__":
	fun2()