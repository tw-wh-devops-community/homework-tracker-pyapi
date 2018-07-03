import unittest
from app.constants import WxConstants as wxconstants
from app.model.ResponseBean import ResponseBean


class HttpUtilsTest(unittest.TestCase):
    def test_create_assignment_message(self):
        message = {'interviewwxId': '陈玮', 'interviewName': '陈玮', 'candidateRole': 'DEV', 'candidateName': '胡红翔', 'publishDate': '2018-07-03T03:25:53.724Z', 'expireDate': '2018-07-06T03:25:53.724Z'}
        self.assertEqual('陈玮', message['interviewName'])


    def test_assignment_format(self):
        data = {'interviewwxId': '陈玮', 'interviewName': '陈玮', 'candidateRole': 'DEV', 'candidateName': '胡红翔', 'publishDate': '2018-07-03T03:25:53.724Z', 'expireDate': '2018-07-06T03:25:53.724Z'}
        message = wxconstants.CREATE_ASSIGNMENT_TEMPLATE.format(
            data['interviewName'],
            data['candidateName'],
            data['candidateRole'],
            data['publishDate'],
            data['expireDate'])
        print(message)


    def test_create_class_with_none(self):
        bean = ResponseBean('0000', 'success')
        print(bean)


if __name__ == '__main__':
    unittest.main()