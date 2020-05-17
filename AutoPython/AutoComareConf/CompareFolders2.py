import filecmp

a = "../Practise"
b = "../AutoComareConf2"
result1 = filecmp.dircmp(a, b)
print(result1)
