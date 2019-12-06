from PIL import Image, ImageDraw 
import os
import numpy as np
import sys

def fun1():
    img_folder = r"F:\Python Workspace\datasets\icdar2019\segmentation_test"
    img_id = 'X51009568881'
    img_path = os.path.join(img_folder, img_id+".jpg")
    gttxt_path = os.path.join(img_folder, img_id+".txt")
    with open(gttxt_path, 'r') as f_open:
        lines = [line.strip() for line in f_open.readlines()]
    
    img = Image.open(img_path)
    img_draw = ImageDraw.Draw(img)

    mask_img = Image.new('L', img.size)
    mask_img_draw = ImageDraw.Draw(mask_img)

    for line in lines:
        lien_split = line.split(',')
        x1,y1,x2,y2,x3,y3,x4,y4 = int(lien_split[0]), int(lien_split[1]), int(lien_split[2]), int(lien_split[3]), int(lien_split[4]), int(lien_split[5]), int(lien_split[6]), int(lien_split[7]) 
        img_draw.polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4)], outline=(255,0,0))
        mask_img_draw.polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4)], fill=1)
    mask_img_arr = np.array(mask_img)*255
    print(mask_img_arr.min(), mask_img_arr.max())
    mask_img = Image.fromarray(mask_img_arr)
    mask_img.show()
    img.show()


def create_mask_img():
    img_folder = r""
    gt_txt_folder = r""
    mask_save_folder = r""


    img_names = [name for name in os.listdir(img_folder) if '.jpg' in name]
    nums = len(img_names)
    i = 1
    for img_name in img_names:
        img_id = img_name.split('.')[0]
        gt_txt_path = os.path.join(img_folder, img_id+'.txt')
        img_path = os.path.join(img_folder, img_name)

        with open(gttxt_path, 'r') as f_open:
            lines = [line.strip() for line in f_open.readlines()]
        img = Image.open(img_path)
        mask_img = Image.new('L', img.size)
        mask_img_draw = ImageDraw.Draw(mask_img)
        for line in lines:
            lien_split = line.split(',')
            x1,y1,x2,y2,x3,y3,x4,y4 = int(lien_split[0]), int(lien_split[1]), int(lien_split[2]), int(lien_split[3]), int(lien_split[4]), int(lien_split[5]), int(lien_split[6]), int(lien_split[7]) 
            mask_img_draw.polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4)], fill=1)
        mask_img_arr = np.array(mask_img)*255
        mask_img = Image.fromarray(mask_img_arr)
        mask_img_path = os.path.join(mask_save_folder, img_id+'.png')
        mask_img.save(mask_img_path)
        sys.stdout.write('\r>> converting imsge %d   %d'%(i,nums))
        sys.stdout.flush()
        i += 1


if __name__ == "__main__":
    fun1()