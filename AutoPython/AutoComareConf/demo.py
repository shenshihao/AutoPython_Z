import difflib

# 一个双引号和三个双引号的区别，但该字符串有多行的时候建议使用三个双引号，否则需要/n
text1 = "this is a beautiful girl"
text2 = "this is a beautiful boy"
text1_line = text1.splitlines()
print(text1_line)
text2_line = text2.splitlines();
print(text2_line)
d = difflib.Differ()
diff = d.compare(text1_line, text2_line)
print('\n'.join(list(diff)))
