#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:18:46 2022

@author: rachel
"""

import pyrealsense2 as rs
import numpy as np
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

frames = pipeline.wait_for_frames()

aligned_frames = align.process(frames)

depth_frame = aligned_frames.get_depth_frame()
color_frame = aligned_frames.get_color_frame()

depth_image = np.asanyarray(depth_frame.get_data())
color_image = np.asanyarray(color_frame.get_data())

plt.imshow(depth_image)
plt.imshow(color_image)

pipeline.stop()
