# python写的有关库函数

依赖：

```python
pip install opencv-python
```

例:
```python
import img_processing
img_processing.split_gif_into_frames_in_dir('GIF.gif', 'hopt', 0, (0.7, 0.7)) #将GIF.gif一帧一帧按0.7成比例缩小放至hopt目录中
```
