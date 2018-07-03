import itchat
from app.constants import WxConstants
from app.util import HttpUtils as httputils


# 查询是否添加该微信号
def is_friend(nick_name):
    friend_lists = itchat.search_friends(nickName=nick_name)
    if friend_lists is None or len(friend_lists) < 1:
        return False
    return True


# 添加好友的请求
def add_friend(user_name, verify_content):
    content = verify_content
    if verify_content is None:
        content = WxConstants.VERIFY_CONTENT.format(user_name)
    is_success = itchat.add_friend(userName=user_name, verifyContent=content)
    print(is_success)
    return is_success


# 退出登录重连
def keep_login():
    itchat.auto_login(exitCallback=keep_login)


# 向某个好友发送消息
def send_message(user_name, message):
    if itchat.check_login is not 200:
        keep_login()
    friends = itchat.search_friends(nickName=user_name)
    send_resp = friends[0].send(message)
    print(str(send_resp))
    if send_resp and send_resp['BaseResponse']['Ret'] == 0:
        return httputils.ok()
    else:
        return httputils.fail(send_resp.BaseResponse.ErrMsg)


# 查找好友
def find_firends(nick_name):
    return itchat.search_friends(nickName=nick_name)


# 群发接口
def send_batch_message(user_lists, message_template):
    for user_name in user_lists:
        send_message(user_name, message_template.format(user_name))

