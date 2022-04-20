"""
Lane Lines Detection pipeline

 
"""

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
from docopt import docopt
from IPython.display import HTML, Video
from moviepy.editor import VideoFileClip
from CameraCalibration import CameraCalibration
from Thresholding import *
from PerspectiveTransformation import *
from LaneLines import *
import glob
import sys


mode=[]
class FindLaneLines:
    """ This class is for parameter tunning.
    Attributes:
        ...
    """
    def __init__(self):
        """ Init Application"""
        self.calibration = CameraCalibration('camera_cal', 9, 6)
        self.thresholding = Thresholding()
        self.transform = PerspectiveTransformation()
        self.lanelines = LaneLines()

    def forward(self, img):
        if '1' in mode:
            out_img = np.copy(img)
            img_concat = np.zeros(img.shape, np.uint8)
            height= np.int(img.shape[0])
            width= np.int(img.shape[1])
            img = self.calibration.undistort(img)
            img = self.transform.forward(img)
            smaller_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25) #resize the frame to be able to fit 4 ,width by half and length by half
            img = self.thresholding.forward(img)
            img3=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
            smaller_frame2 = cv2.resize(img3, (0, 0), fx=0.25, fy=0.25) #resize the frame to be able to fit 4 ,width by half and length by half
            img = self.lanelines.forward(img)
            smaller_frame3 = cv2.resize(img, (0, 0), fx=0.25, fy=0.25) #resize the frame to be able to fit 4 ,width by half and length by half
            img = self.transform.backward(img)
            out_img = cv2.addWeighted(out_img, 1, img, 0.6, 0)
            bigger_frame = cv2.resize(out_img, (0, 0), fx=1, fy=1)   #resize the frame to be able to fit 4 ,width by half and length by half
            img_concat[:int(1*height),:int(1*width)] = bigger_frame    #main frame
            img_concat[:int(0.25*height), 20:20+int(0.25*width)] = smaller_frame  #top left
            img_concat[:int(0.25*height),40+int(0.25*width):40+int(0.5*width)] = smaller_frame2 
            img_concat[:int(0.25*height),60+int(0.5*width):60+int(0.75*width)] = smaller_frame3
            img_concat = self.lanelines.plot(img_concat)
            return img_concat

        else:
            out_img = np.copy(img)
            img = self.calibration.undistort(img)
            img = self.transform.forward(img)
            img = self.thresholding.forward(img)
            img = self.lanelines.forward(img)
            img = self.transform.backward(img)
            out_img = cv2.addWeighted(out_img, 1, img, 0.6, 0)
            img_concat = self.lanelines.plot(out_img)
            return img_concat
        

    def process_image(self, input_path, output_path):
        img = cv2.imread(input_path)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        out_img = self.forward(img)
        out_img = cv2.cvtColor(out_img,cv2.COLOR_BGR2RGB)
        cv2.imwrite(output_path, out_img)

    def process_video(self, input_path, output_path):
        clip = VideoFileClip(input_path)
        out_clip = clip.fl_image(self.forward)
        out_clip.write_videofile(output_path, audio=False)

def main():
    findLaneLines = FindLaneLines()
    input_var = str(sys.argv[1])
    input_path = str(sys.argv[2])
    output_path = str(sys.argv[3])
    mode1 = str(sys.argv[4])
    if(input_var == '1'):
        mode.append(mode1)
        findLaneLines.process_video(input_path, output_path)
        
    elif(input_var == '0'):
        mode.append(mode1)
        findLaneLines.process_image(input_path, output_path)



if __name__ == "__main__":
    main()
