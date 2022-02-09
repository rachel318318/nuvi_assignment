# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyrealsense2 as rs
import numpy as np
import cv2
import matplotlib.pyplot as plt


height = 720
width = 1280
fps = 30

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, width, height, rs.format.z16, fps)
config.enable_stream(rs.stream.color, width, height, rs.format.rgb8, fps)


profile = pipeline.start(config)
align_to = rs.stream.color
align = rs.align(align_to)



# Get frameset of color and depth
frames = pipeline.wait_for_frames()
# frames.get_depth_frame() is a 640x360 depth image

# Align the depth frame to color frame
aligned_frames = align.process(frames)

# Get aligned frames
depth_frame = aligned_frames.get_depth_frame()
color_frame = aligned_frames.get_color_frame()

# Validate that both frames are valid
if not depth_frame or not color_frame:
    pass # you can do something here if preferred 

# Convert images to numpy arraysq
depth_image = np.asanyarray(depth_frame.get_data())
color_image = np.asanyarray(color_frame.get_data())

plt.imshow(depth_image)
plt.imshow(color_image)

pipeline.stop()
