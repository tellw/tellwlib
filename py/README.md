# python写的有关库函数

依赖：

```python
pip install opencv-python
pip install imageio
```

例:
```python
import img_processing

#将GIF.gif一帧一帧按0.7成比例缩小放至hopt目录中
img_processing.split_gif_into_frames_in_dir('GIF.gif', 'hopt', 0, (0.7, 0.7)) 

def compare(a):
    return int(a.strip().split('.')[0])

img_processing.compose_gif_from_dir('hopt', '6.gif', compare, 0.1)
```
