import itchat

itchat.auto_login()

@itchat.msg_register([itchat.content.TEXT])
def text_reply(msg):
#    print(msg)
    nickName = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    if nickName == '张芮溟' or nickName == 'No. L':
        itchat.send(('鸡年大吉'), msg['FromUserName'])

itchat.run()
