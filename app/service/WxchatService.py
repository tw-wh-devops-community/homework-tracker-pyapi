from app.util import WxchatUtils as wxutils


class WxChatService:
    @staticmethod
    def is_friens(request):
        return wxutils.is_friend(request.interviewwxId)

    @staticmethod
    def send_message(request):
        return wxutils.send_message(request.interviewwxId, request.message)