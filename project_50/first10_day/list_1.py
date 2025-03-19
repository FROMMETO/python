#列表通常包含多种元素，因此给列表指定一个表示复数的名称

#访问列表元素

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0])

#可以使用各种方法让元素的格式更准确
print(bicycles[0].title())

#索引的第一个元素是0而不是1，python为了访问最后一个列表元素提供了一种特殊语法，通过索引指定能够为-1
print(bicycles[-1])

#可以使用列表中的各个值
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#修改、添加和删除元素
#修改任意位置的元素
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
bicycles[0] = 'a'
print(bicycles)

#添加元素,分别在(append)末尾、（insert）任意
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
bicycles.append('b')#也可以在空列表中添加元素
print(bicycles)

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
bicycles.insert(0,'c')
print(bicycles)

#从列表中删除元素

#1.使用del语句删除元素：如果知道要删除的元素在列表中的位置，可使用del语句
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
del bicycles[0]
print(bicycles)#使用del语句后就将该值永久从列表中删除了

#2.使用pop()方法删除元素：有时需要删除列表中的元素并使用它的值
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
poped_bicycles = bicycles.pop()#把弹出的值赋给变量
print(bicycles)
print(poped_bicycles)#弹出的是列表中最后一个值

#2.1 删除列表中任意位置的元素，pop()方法也可以删除任意值
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
first_bicycles = bicycles.pop(0)
print(first_bicycles)

#如果不知何时判断使用del语句还是pop方法，下面有一个简易的判断标准
#如果列表中删除一个元素且不再以任何方式使用它，就使用del语句
#如果删除后继续使用它，就使用pop()方法

#根据值删除元素remove（）方法，可用在只知道元素的值，且不清楚列表中该值的位置在哪的情况
#使用remove（）方法从列表删除元素后，也可以继续使用它的值
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
too_expensive = 'trek'
bicycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me.")












