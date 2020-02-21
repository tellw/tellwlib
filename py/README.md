# python写的有关库函数

依赖：

```python
pip install opencv-python
pip install imageio
pip install requests
pip install beautifulsoup4
pip install Pillow
```

例:
```python
from tellwlib import py as twpy

#将GIF.gif一帧一帧按0.7成比例缩小放至hopt目录中
twpy.img_processing.split_gif_into_frames_in_dir('GIF.gif', 'hopt', 0, (0.7, 0.7)) 

#对文件列表设置的排序函数
def compare(a):
    return int(a.strip().split('.')[0])

#将hopt目录中的图片按图片名对应数值大小合成fps为10的gif图片(目前放弃这种合成gif方法，该方法合成的文件占用空间太大，不及使用Photoshop合成的舒服。
twpy.img_processing.compose_gif_from_dir('hopt', '6.gif', compare, 0.1)

#获取1.mp4视频流帧信息
twpy.img_processing.get_video_frame_info('1.mp4')

#生成13位随机字符串
twpy.twpy_random.gen_rand_charnum_seq(13)

#从一[网页链接](http://konachan.net/post?page=9790&tags=)下载类名为preview的图片到imgs目录中
twpy.download.dnld_pic_in_webpage('http://konachan.net/post?page=9790&tags=', 'preview', 'imgs')

#每隔10分钟截取屏幕信息保存至logPic目录中
twpy.log.log_pic_everyday('logPic', 600)

#将100s转换为1m 40s返回
twpy.twpy_time.display_seconds(100)
```
