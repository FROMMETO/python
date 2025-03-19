#练习1，嘉宾名单
names = ['chatgpt','gemini','claude','grok']
#修改嘉宾名单
# 指出哪个嘉宾无法赴约
print(f"无法赴约的嘉宾是{names[2].title()}。")
#修改嘉宾名单
names[2] = 'doubao'
#向每一位嘉宾发出邀请信息
invitations_1 = f"{names[0].title()},Would you like to accept my invitation"
invitations_2 = f"{names[1].title()},Would you like to accept my invitation"
invitations_3 = f"{names[2].title()},Would you like to accept my invitation"
invitations_4 = f"{names[3].title()},Would you like to accept my invitation"
print(invitations_1)
print(invitations_2)
print(invitations_3)
print(invitations_4)
#添加嘉宾
print("我们找到了更多的位置")
#使用insert()将一位嘉宾添加到名单开头
names.insert(0,'deepseek')
#使用上列同样的方法添加因为嘉宾到名单中间
names.insert(2,'qwen')
#使用append()将最后一个嘉宾添加到名单末尾
names.append('ai studio')
#打印一系列消息向每位嘉宾发出邀请
invitations_1 = f"{names[0].title()},Would you like to accept my invitation"
invitations_2 = f"{names[1].title()},Would you like to accept my invitation"
invitations_3 = f"{names[2].title()},Would you like to accept my invitation"
invitations_4 = f"{names[3].title()},Would you like to accept my invitation"
invitations_5 = f"{names[4].title()},Would you like to accept my invitation"
invitations_6 = f"{names[5].title()},Would you like to accept my invitation"
invitations_7 = f"{names[6].title()},Would you like to accept my invitation"
print(invitations_1)
print(invitations_2)
print(invitations_3)
print(invitations_4)
print(invitations_5)
print(invitations_6)
print(invitations_7)
#缩短名单
print("抱歉，因为一些原因我们只能邀请两位嘉宾")
#使用 pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。
#每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知道你很抱歉
deleted_names = names.pop(2)
apologies = f"{deleted_names},I'm really sorry about we can not invite you."
print(apologies)
deleted_names = names.pop(0)
apologies = f"{deleted_names},I'm really sorry about we can not invite you."
print(apologies)
deleted_names = names.pop(-1)
apologies = f"{deleted_names},I'm really sorry about we can not invite you."
print(apologies)
deleted_names = names.pop(-1)
apologies = f"{deleted_names},I'm really sorry about we can not invite you."
print(apologies)
deleted_names = names.pop(2)
apologies = f"{deleted_names},I'm really sorry about we can not invite you."
print(apologies)
print(f"{names[0]},Fortunately,you are still in the queue.")
print(f"{names[1]},Fortunately,you are still in the queue.")
#使用 del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实名单在程序结束时确实是空的。
del names[0]
print(names)
del names[0]
print(names)
