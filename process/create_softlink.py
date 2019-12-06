import os
import sys
def fun1():
    mask_folder = r""
    img_folder = r""

    img_softlink_folder = r""
    mask_softlink_folder = r""

    mask_img_names = os.listdir(mask_folder)
    nums = len(mask_img_names)
    i = 1
    for mask_img_name in mask_img_names:
        img_id = mask_img_name.split('.')[0]

        source_img_path = os.path.join(img_folder, img_id+'.jpg')
        mask_img_path = os.path.join(mask_folder, mask_img_name)
        
        source_img_link_path = os.path.join(img_softlink_folder, img_id+'.jpg')
        mask_img_link_path = os.path.join(mask_softlink_folder, img_id+'.png')
        
        os.system("ln -s {} {}".format(source_img_path, source_img_link_path))
        os.system("ln -s {} {}".format(mask_img_path, mask_img_link_path))
        sys.stdout.write('\r>> converting imsge %d   %d'%(i,nums))
        sys.stdout.flush()
        i += 1

if __name__ == "__main__":
    fun1()