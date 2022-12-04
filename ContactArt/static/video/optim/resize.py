import os
from glob import glob

a=glob('/home/zhuzehao/Develop/articulation_estimator_slim/supp/rbo*')
for i in a:
  print('ffmpeg -i '+ i +' -vf scale=w=960:h=640 ' + i.split('/')[-1])
  os.system('ffmpeg -i '+ i +' -vf scale=w=960:h=640 ' + i.split('/')[-1])
