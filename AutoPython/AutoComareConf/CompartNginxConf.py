# -*- coding:utf-8 -*-
# 这个demo存在问题
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
    text = fileopen.read().splitlines()
    fileopen.close()
    return text


textfile1 = readfile(textfile1)
# print(textfile1)
textfile2 = readfile(textfile2)
# print(textfile2)
d = difflib.Differ()
print('\n'.join(list(d.compare(textfile1, textfile2))))
