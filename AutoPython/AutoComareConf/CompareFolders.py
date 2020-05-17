import filecmp

# 单文件对比，采用filecmp.cmp，比较a文件和b文件
print("该实例是比对单个文件是否一致")
a = "nginx.conf.v1"
b = "nginx.conf.v2"
result = filecmp.cmp(a, b)

print('--------------------------------------')
print(result)
