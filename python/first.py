help=input('小精灵：您好，欢迎来到古灵阁，请问您需要帮助吗？需要or不需要？')
if help=='需要':
	choice=int(input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询'))
	if choice==1:
		print('推荐你去存取款窗口~')
	elif choice==2:
		money=input('请问您需要兑换多少金加隆呢？')
		print('金加隆和人民币的兑换率为 1:51.3，即一金加隆 =51.3 人民币')
		print('好的，我知道了，您需要兑换 '+money+' 金加隆。')
		print('那么，您需要付给我 '+str(int(money)*51.3)+' 人民币。')
	else:
		print('推荐你去咨询窗口~')
else:
	print('好的，再见。')