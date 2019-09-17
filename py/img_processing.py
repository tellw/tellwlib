# coding=utf-8

import cv2
import numpy as np
import time
import os

def time_log(start, descrip):
    """时间日志.

    Args:
        start: 计时的起点.
        descrip: 对所用时间事件的描述.
    """
    print("%s %.3f seconds"%(descrip, time.time()-start))
    
def progress_tell(count, al, start):
    """显示进度.

    Args:
        count: 列表元素索引.
        al: 列表长度.
        start: 计时开始点.
    """
    print("processing %dth/%d, progress %.2f%%, and you need %.2f seconds to finish it." % (count, al,
                                                                                          (count+1)/al*100, (time.time()-start)*(al-1-count)))


def output_frames(gif, frame, ret, dir, size=(640, 480), name=0):
    """将VideoCapture流(gif)中帧输出在dir中.

    Args:
        gif: 从gif中读取的VideoCapture流.
        frame: 第0帧，之后作存储每个帧的循环变量.
        ret: VideoCapture.read()第二个返回值，作为是否继续读取的循环判断依据.
        dir: 帧存放的目录.
        name: 帧图片的文件名，从0开始命名.
    """
    if size == (frame.shape[1], frame.shape[0]):    #不用改变帧大小
        while True:
            start = time.time()
            if frame is None:
                break
            if ret == True:
                cv2.imshow('img', frame)
                cv2.imwrite(dir+'/%d.jpg'%name, frame)
                time_log(start, 'the %dth frame needs'%name)
                name+=1
                if cv2.waitKey(100) & 0xFF == 27:
                    break
            ret, frame = gif.read()
    else:   #改变帧大小
        while True:
            start = time.time()
            if frame is None:
                break
            if ret == True:
                cv2.imshow('img', frame)
                new = cv2.resize(frame, size)
                cv2.imwrite(dir+'/%d.jpg'%name, new)
                time_log(start, 'the %dth frame needs'%name)
                name+=1
                if cv2.waitKey(100) & 0xFF == 27:
                    break
            ret, frame = gif.read()

def split_gif_into_frames_in_dir(gif_name, dir=None, mode=0, f=(1, 1)):
    """将gif图片按帧将图片放在一个文件夹中，在这个过程中可以改变帧大小.

    Args:
        gif_name: gif文件名.也可以是视频文件.
        dir: 最后图片存储的目录.
        mode: 改变帧宽高为某值取值为1，按比例改变帧大小取值为0.
        f: mode值为1时意即目标帧宽高，mode值为0时意即比例，类型为大小为2的元组
    """
    if len(gif_name.strip().split('.')) != 2:
        print('gif name error...')
    elif len(f) != 2 or not(mode==0 or mode==1):
        print('args are wrong...')
    else:
        gif = cv2.VideoCapture(gif_name)
        ret, frame = gif.read()
        h, w, _ = frame.shape
        if dir is None: #若没有明确说明目录名，在同一目录下创建默认文件夹
            gifna = gif_name.strip().split('.')[0]
            dir='framesIn'+gifna[0].upper()+gifna[1:]+'Gif'
 
        if not os.path.exists(dir):
            os.mkdir(dir)
        if mode==0:
            output_frames(gif, frame, ret, dir, size=((int)(frame.shape[1]*f[0]), (int)(frame.shape[0]*f[1])))
        else:
            output_frames(gif, frame, ret, dir, size=f)
        print('all frames are in %s'%dir)
        gif.release()   #收尾工作
        cv2.destroyAllWindows()
        
def compose_gif_from_dir(dire, gif_name, key=None, duration=0.1):
    """从split_gif_into_frames_in_dir操作中的目录中取出图片合成gif图.

    Args:
        dire:含有每一帧图片的目录.
        gif_name:目标动图文件名.
        key: 帧的文件名排序决定函数, 影响最终动图帧的顺序.
        duration: 帧与帧之间时间间隔, 以s为单位.
    """
    image_list = os.listdir(dire)
    image_list.sort(key=key)
    print(image_list)
    frames = []
    assert image_list is not None, 'can\'t find your images' 
    image_list_len = len(image_list)
    start = time.time()
    for (idx, il) in enumerate(image_list):
        frames.append(imageio.imread(os.path.join(dire, il)))
        progress_tell(idx, image_list_len, start)
        start = time.time()
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    print('you\'ve got %s' % gif_name)
