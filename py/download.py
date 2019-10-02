import requests
from bs4 import BeautifulSoup
import os
import traceback
import time
from twpy_time import display_seconds

def download_file(url, filename):
	"""将链接中的数据存储入文件中。

	Args:
		url: 链接。
		filename: 文件路径名。
	Raises:
		KeyboardInterrupt: 用户按^C引发异常。
		Exception: 发生异常。
	"""
    if os.path.exists(filename):
        print('file '+filename+' exists!')
        return
    try:
        r = requests.get(url, stream=True, timeout=60)
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
        print('downloading '+filename+' successfully!')
        return filename
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception:
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)

def dnld_pic_in_webpage(url, cls, savedir):
	"""将链接中图片链接找出，并把图片保存到一个目录中。

	Args:
		url: 链接。
		cls: 所要保存的图片元素在html中的类名。
		savedir: 图片保存的目录。
	Returns:
		duration: 下载该网页中所有图片的过程中所花费的时间。
	"""
	tstart = time.time()
	print('getting '+url)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    for img in soup.find_all('img', class_=cls):
        target_url = img['src']
        filename = os.path.join(savedir, target_url.split('/')[-1])
        print('downloading '+target_url+' into '+filename)
        download_file(target_url, filename)
    duration = time.time()-tstart
    print('%s %s processed, it costs %s' % (time.asctime(time.localtime(time.time())), url, display_seconds(duration)))
    return duration
