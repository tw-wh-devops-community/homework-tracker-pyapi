from app.model.ResponseBean import ResponseBean
from app.constants import WxConstants as wxconstants
from app.constants import HttpConstants as httpconstants


def create_assignment_message(req):
    message = wxconstants.CREATE_ASSIGNMENT_TEMPLATE.format(
        req['interviewName'],
        req['candidateName'],
        req['candidateRole'],
        req['publishDate'],
        req['expireDate'])
    print(message)
    return message


def success(response):
    res = ResponseBean(httpconstants.SUCCESS_RETURN_CODE, httpconstants.SUCCESS_RETURN_MSG, response)
    return res


def ok():
    return ResponseBean(httpconstants.SUCCESS_RETURN_CODE, httpconstants.SUCCESS_RETURN_MSG)


def fail(message):
    res = ResponseBean(httpconstants.FAIL_RETURN_CODE, message, None)
    return res