#管理列表,默认全小写
#sort()方法能永久地修改列表元素的排列顺序。
lists = ['c','a','b','d']
lists.sort()
print(lists)
#话可以按字母顺序相反的顺序排列元素
lists = ['c','a','b','d']
lists.sort(reverse=True)
print(lists)#也是永久修改

#使用sorted()函数 对列表进行临时排序
lists = ['c','a','b','d']
print('这是原来的顺序：')
print(lists)

print ('这是sorted列表：')
print(sorted(lists))

print('这是原来的顺序：')
print(lists)

#反向打印列表，reverse()方法
print('\n')
lists = ['c','a','b','d']
print(lists)
lists.reverse()
print(lists)

#确定列表的长度
#使用len()函数可快速获取列表长度
print("\n")
lists = ['c','a','b','d']
len(lists)
print(len(lists))