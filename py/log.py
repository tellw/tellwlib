from PIL import ImageGrab
import time
import os

def log_pic_everyday(logDir, sleepTime):
	"""将桌面屏幕按一定时间间隔进行截取记录。

	Args:
		logDir: 图片存储文件夹。
		sleepTime: 截取记录的时间间隔。
	"""
	if not os.path.exists(logDir):
		os.mkdir(logDir)
	dayDir = os.path.join(logDir, time.strftime('%Y%m%d'))
	if not os.path.exists(dayDir):
		os.mkdir(dayDir)
	#限定足够大的有限次，让程序一直运行，否则当电脑空闲调用程序会被关闭。
	for i in range(600000//sleepTime):
		print(time.asctime(time.localtime(time.time())))
		im = ImageGrab.grab()
		savePath = os.path.join(dayDir, time.strftime('%Y%m%d%H%M.jpg'))
		im.save(savePath)
		print(savePath + ' saved...')
		time.sleep(sleepTime)