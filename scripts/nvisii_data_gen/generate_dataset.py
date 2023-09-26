#!/usr/bin/env python3
import random 
import subprocess


# 20 000 images

for i in range(0, 1):
	to_call = [
		"python",'D:/Desktop/1/individual_project/Deep_Object_Pose_Windows/scripts/nvisii_data_gen/single_video_pybullet.py',
		'--spp','10',
		'--nb_frames', '10',
		'--nb_objects', '1', # str(int(random.uniform(50,75))),
		'--scale', '0.01',
		'--outf',f"dataset/{str(i).zfill(3)}",
	]
	subprocess.call(to_call)