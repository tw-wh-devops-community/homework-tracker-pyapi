import itchat
from app.constants import WxConstants, HttpConstants as httpconstants
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
    itchat.auto_login(hotReload=True)


# 统一发送消息接口
def send_message(wx_id, message, is_jump):
    if itchat.check_login != 200:
        try:
            keep_login()
        except:
            return httputils.fail("登录异常")
    friends = itchat.search_friends(remarkName=wx_id)
    if friends is None or len(friends) < 1:
        return httputils.fail(httpconstants.NOT_FOUND_FRIENDS)
    send_resp = friends[0].send(message)
    print(send_resp)
    is_send_success = (send_resp is not None and send_resp['BaseResponse']['Ret'] == 0)
    print('success = ' + str(is_send_success))
    if is_send_success and is_jump == '1':
        image_result = send_image(friend=friends[0])
        if image_result is not None and image_result['BaseResponse']['Ret'] == 0:
            return httputils.ok()
        else:
            return httputils.fail(image_result['BaseResponse']['ErrMsg'])
    elif is_send_success and is_jump == '0':
        return httputils.ok()
    else:
        return httputils.fail(send_resp['BaseResponse']['ErrMsg'])


# 发送小程序的二维码
def send_image(friend, image=None):
    if image is None:
        image = httpconstants.JUMP_IMAGE_PATH
    return itchat.send_image(image, toUserName=friend['UserName'])


# 向某个好友发送消息
# def send_message(user_name, message):
#     if itchat.check_login is not 200:
#         keep_login()
#     friends = itchat.search_friends(nickName=user_name)
#     send_resp = friends[0].send(message)
#     print(str(send_resp))
#     if send_resp and send_resp['BaseResponse']['Ret'] == 0:
#         return httputils.ok()
#     else:
#         return httputils.fail(send_resp.BaseResponse.ErrMsg)


# 查找好友
def find_firends(nick_name):
    return itchat.search_friends(nickName=nick_name)


# 群发接口
def send_batch_message(user_lists, message_template):
    for user_name in user_lists:
        send_message(user_name, message_template.format(user_name))
