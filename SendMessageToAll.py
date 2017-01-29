import itchat

itchat.auto_login()
all_friends = itchat.get_friends()
for friend in all_friends:
    msg = friend['NickName'] + "，新年快乐，鸡年大吉[From yongqi's WeChat Robot]"
    user_name = friend['UserName']
    itchat.send(msg, toUserName=user_name)
#    itchat.send(msg, toUserName='filehelper')

