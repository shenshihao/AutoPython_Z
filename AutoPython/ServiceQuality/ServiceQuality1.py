import os
import pycurl
import sys

URL = "https://www.baidu.com/"
# 创建一个浏览器
c = pycurl.Curl()
# 输入网址
c.setopt(pycurl.URL, URL)
# 连接网址
c.setopt(pycurl.TIMEOUT, 5)
# 连接网址的下载速度
c.setopt(pycurl.CONNECTTIMEOUT, 5)
c.setopt(pycurl.FORBID_REUSE, 1)
# 设置无进度条
c.setopt(pycurl.NOPROGRESS, 1)
try:
    c.perform()
# python3的写法，python2的写法是except Exception ,e:
except Exception as e:
    print("连接不上")
    c.close()
    sys.exit()

# HTTP状态
print("http状态码: %s" % c.getinfo())

# print("建立连接的时间： %.2f ms"% c.getinfo())

print("平均速度： %d byte/s" % c.getinfo(c.SPEED_DOWNLOAD))
