r"""Generate list file for PASCAL VOC 2012 segmentation data

"""
# SegmentationClassMerged has 12031 masks

import os

if __name__ == "__main__":

   img_path = "E:\\PythonProjects\\pascal_voc_seg\\VOCdevkit\\VOC2012\\JPEGImages"
   lbl_path = "E:\\PythonProjects\\pascal_voc_seg\\VOCdevkit\\VOC2012\\SegmentationClassMerged"

   list_img = os.listdir(img_path)
   list_lbl = os.listdir(lbl_path)
   for i in range(len(list_img)):
      list_img[i] = list_img[i].split(".")[0]
   for i in range(len(list_lbl)):
      list_lbl[i] = list_lbl[i].split(".")[0]
   intersection = list(set(list_img).intersection(set(list_lbl)))

   fid = open('trainval_merged.txt', 'w')
   for line in intersection:
      fid.write(line+"\n")
   fid.close()
