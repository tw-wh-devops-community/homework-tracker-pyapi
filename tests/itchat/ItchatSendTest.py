import itchat


class ItchatTest():
    @staticmethod
    def test_send_html_message(self):
        message = '<p style="color: red;">hello world</p>'
        itchat.auto_login()
        friend = itchat.search_friends(nickName='Ryn')
        friend[0].send(message)

    @staticmethod
    def once_send_mutiply_messages():
        messages = 5 * ['hello', 'world', 'hello', 'world', 'hello', 'world', 'hello', 'world', 'hello', 'world',
                        'hello', 'world', 'hello', 'world']
        itchat.auto_login(hotReload=True)
        friend = itchat.search_friends(nickName='Ryn')
        for item in messages:
            print(str(friend[0].send(item)))

    @staticmethod
    def get_contacts_info():
        itchat.auto_login(hotReload=True)
        print(len(itchat.get_friends(update=True)))
        print(str(itchat.get_friends()))


if __name__ == '__main__':
    # ItchatTest.once_send_mutiply_messages()
    # itchat.start_receiving
    ItchatTest.get_contacts_info()
