# coding:utf-8
import itchat

# 先登录
itchat.login()
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
for i in friends:
    # 获取个性签名
    # print(i)

    name = i['RemarkName']
    Province = i['Province']
    City = i['City']
    nickname = i['NickName']
    # 正则匹配过滤掉emoji表情，例如emoji1f3c3等
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji",
                                                                                        "")
    print(name + "," + nickname + "," + signature + "," + Province + "," + City)
