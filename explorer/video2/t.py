import os
for i in ['7119','7167','7221','7263','7265','7310']:
 os.system('ffmpeg -i ' + i + '.mp4 -vcodec libx264 ../video/' + i + '.mp4 -y')
