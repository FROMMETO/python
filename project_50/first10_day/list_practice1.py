#创建一个AI应名称列表并打印部分
names = ['chatgpt','doubao','gemini','claude','grok']
print(names[0])
print(names[-1])

#写几条问候语
message = f"Hello,I'm {names[0].title()}."
print(message)
message = f"Hello,I'm {names[-2].title()}."
print(message)

#你喜欢使用什么AI
Q = f"I like use {names[0].title()}."
print(Q)