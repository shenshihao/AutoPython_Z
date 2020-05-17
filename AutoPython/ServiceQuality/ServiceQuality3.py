import requests
import sys
import time
import os


# python serviceQuality3.py https://www.baidu.com
def http_Status(arg):
    try:
        html = requests.get(arg)
        code = html.status_code
        print(code)
        if str(code) == '500':
            print(1)
            time.sleep(60)
            html1 = requests.get(arg)
            code1 = html.status_code
            if str(code1) == '500':
                os.system("D:\\auto.bat")
    except:
        # print(1)
        sys.exit()


if __name__ == "__main__":
    code = sys.argv[1]
    # print(http_Status(code))
    http_Status(code)
