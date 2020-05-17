import os
import shutil

print("该实例是比较两个文件夹的内容差异的，但是会移除比较文件夹的内容")
data1_path = "../AutoComareConf"
file_list = os.listdir(data1_path)
# print(file_list)
test_list = []
for file in file_list:
    a = file.split('.')
    test_list.append(a[0])

data2_path = "../AutoComareConf2"
file2_list = os.listdir(data2_path)
print(file2_list)

for i in file2_list:
    num = i.split('.')[0]
    if num in test_list:
        os.remove(os.path.join(data2_path, i))
    else:
        continue
