import difflib
import sys

try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except:
    print("error argv")
    sys.exit()


def readfile(f):
    fileopen = open(f, 'rb')
    # 这里对字符串进行了decode处理，否则会出现字符串前面加b·的情况
    text = fileopen.read().decode('utf-8').splitlines()
    fileopen.close()
    return text


print("该实例是比较nginx文件内容")
textfile1 = readfile(textfile1)
# print(textfile1)
textfile2 = readfile(textfile2)
# print(textfile2)

# print(textfile2)
d = difflib.Differ()
print('\n'.join(list(d.compare(textfile1, textfile2))))
