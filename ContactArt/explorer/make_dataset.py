import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import random
from tqdm import tqdm
from glob import glob


def setup_seed(seed):
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    random.seed(seed)

setup_seed(114514)
video_path = glob('video2/*/*')
video_path = (video_path + video_path)[:2*81]
random.shuffle(video_path)
video_path[85], video_path[76] = 'video2/laptop/10213_0.mp4', 'video2/safe/101613_0.mp4' #101599
# video_path = glob('video/*')[1:]
video_len = len(video_path)
print(video_len, video_path[0])
h, w, total_t = 1080, 1920, 199
video_writer = cv2.VideoWriter('large_dataset.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 10, (w, h))
video = [cv2.VideoCapture(i) for i in video_path]
for t in tqdm(range(total_t+1)):
    all, line = None, None
    for i in range(video_len):
        _frame = video[i].read()[1] #cv2.resize(video[i].read()[1], (1080 // 4, 960 // 4))
        cv2.waitKey(1)
        line = _frame if line is None else np.concatenate([line, _frame], 0)
        if (i + 1) % 9 == 0:
            all = line if all is None else np.concatenate([all, line], 1)
            line = None
    hi, wi = all.shape[0], all.shape[1]
    if t < 60:
        speed = 0
    elif t<80:
        speed = (t-60)/80
    elif t<140:
        speed = 1/4
    elif t<165:
        speed = (12*t-1580)/400
    else:
        speed = 1
    #else:
    #    speed = (t*1.5-75) / total_t
    # elif t < 100:
    #     speed = 0.4 * (t-50) / total_t
    # else:
    #     speed = (t*2.6-240) / total_t
    hr, wr = int((speed * (hi - h) + h)/2), int((speed * (wi - w) + w)/2)
    print(t, speed, h, w,  hi, wi, hr, wr, hi//2-hr, wi//2-wr)
    frame = cv2.resize(all[hi//2-hr: hi//2+hr, wi//2-wr: wi//2+wr], (w, h))
    # plt.imshow(all[hi//2-hr: hi//2+hr, wi//2-wr: wi//2+wr, ::-1])
    # plt.show()
    video_writer.write(frame)
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
