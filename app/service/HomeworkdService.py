import itchat


class HomeworkService:
    def new_homework_notify(self):
        itchat.auto_login()
        # 查询是否已经添加该微信号
        friendList = itchat.get_friends(update=True)[1:]
        for friend in friendList:
            print(friend['NickName'])


if __name__ == '__main__':
    HomeworkService().new_homework_notify()