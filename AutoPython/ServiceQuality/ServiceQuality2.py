import requests
import sys
import time

#python serviceQuality2.py https://blog.51cto.com/liuxiaolan/2488619
def http_Status(arg):
    try:
        html = requests.get(arg)
        code = html.status_code
        print(code)
    except:
        print(1)
        sys.exit()


if __name__ == "__main__":
    code = sys.argv[1]
    http_Status(code)

