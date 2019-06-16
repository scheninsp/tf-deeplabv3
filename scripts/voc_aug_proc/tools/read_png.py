import numpy as np
from PIL import Image

filename ="E:\\PythonProjects\\pascal_voc_seg\\VOCaug\\benchmark_RELEASE\\dataset\\cls_png\\2009_003858.png"
read_img = np.array(Image.open(filename))

print("test read")