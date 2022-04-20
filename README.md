# Lane-Detection

The goals / steps of this project are the following:

Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
Apply a distortion correction to raw images.
Apply a perspective transform to rectify binary image ("birds-eye view").
Use color transforms, gradients, etc., to create a thresholded binary image.
Detect lane pixels and fit to find the lane boundary.
Determine the curvature of the lane and vehicle position with respect to center.
Warp the detected lane boundaries back onto the original image.
Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.
The images for camera calibration are stored in the folder called camera_cal. The images in test_images are for testing your pipeline on single frames.

You can process video by using challenge_video.mp4 and project_video.mp4 and see the lanes detected.


## Usage:

### 1. Set up the environment 
`conda env create -f environment.yml`

To activate the environment:

Window: `conda activate carnd`

Linux, MacOS: `source activate carnd`

### 2. Run the pipeline:

```bash
*make sure that the path of the main.py is the same as mentioned in the batch file
- open cmd on the project folder 
- type "run.bat <input_var> <input_path> <output_path> <mode>"
- input_var : 0 for image processing / 1 for video processing
- mode : 0 for Normal mode / 1 for Debugging mode
  
```
