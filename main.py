# main.py
import cv2
import glob

path_to_imgs = "imgs/"
path_to_output = "conv_imgs/"

# Settings:
dpi_setting = 600
pearl_size = 5  # mm

for img_path in glob.glob(path_to_imgs + "*.jpg"):
    img = cv2.imread(img_path)
    img_h, img_w, _c = img.shape

