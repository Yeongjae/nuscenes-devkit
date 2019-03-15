# nuScenes dev-kit.
# Code written by Holger Caesar, 2018.
# Licensed under the Creative Commons [see licence.txt]

"""
Exports a video of each scene (with annotations) to disk.
"""
import os
import random
import tqdm

from nuscenes.nuscenes import NuScenes

# Load NuScenes class
nusc = NuScenes(dataroot='/data/exp/nuScenes-blurring-data/nuscenes-v1.0')
scene_tokens = [s['token'] for s in nusc.scene]
random.shuffle(scene_tokens)

# Create output directory
out_dir = os.path.expanduser('~/nuscenes-visualization/scene-videos-v1.0-nopoints')
if not os.path.isdir(out_dir):
    os.makedirs(out_dir)

# Write videos to disk
for scene_token in tqdm.tqdm(scene_tokens):
    scene = nusc.get('scene', scene_token)
    print('Writing scene %s' % scene['name'])
    out_path = os.path.join(out_dir, scene['name']) + '.avi'
    if not os.path.exists(out_path):
        nusc.render_scene(scene['token'], out_path=out_path)
