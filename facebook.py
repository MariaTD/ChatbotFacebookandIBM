import json

def responderFacebook():
    sender_psid=1111
    response='texto'
    request_body = {
        'recipient':
            {
                'id': sender_psid
            },
        'message': response
    }
    json_str=json.dumps(request_body,indent=4)
    print(json_str)

responderFacebook()