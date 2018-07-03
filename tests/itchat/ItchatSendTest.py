import unittest
import itchat


class ItchatTest(unittest.TestCase):
    def test_send_html_message(self):
        message = '<p style="color: red;">hello world</p>'
        itchat.auto_login()
        friend = itchat.search_friends(nickName='Ryn')
        friend[0].send(message)


if __name__ == '__main__':
    unittest.main()