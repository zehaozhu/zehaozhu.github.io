import cv2
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from glob import glob

video_path = glob('video/*')[1:]
video_len = len(video_path)
video_writer = cv2.VideoWriter('large_dataset.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 15, (2970, 1440))
video = [cv2.VideoCapture(i) for i in video_path]
for _ in tqdm(range(150)):
    all, line = None, None
    for i in range(video_len):
        frame = cv2.resize(video[i].read()[1], (1080 // 4, 960 // 4))
        cv2.waitKey(1)
        line = frame if line is None else np.concatenate([line, frame], 0)
        if (i + 1) % 6 == 0:
            all = line if all is None else np.concatenate([all, line], 1)
            line = None
    # plt.imshow(all[:, :, ::-1])
    # plt.show()
    video_writer.write(all)
video_writer.release()


# success = True
# i = 0
# frame_list = []
# while success:
#     success, frame = cap.read()
#     print(frame.shape)
#     frame = cv2.resize(frame, (1080//4, 960//4))
#     print(frame.shape)
#     if success:
#         frame_list.append(frame)
#         i = i + 1
#         plt.imshow(frame)
#         plt.show()
#         cv2.waitKey(1)
#
# cap.release()
