from simple_tests import http, email, sns, telnet


def lambda_handler(event, context):
    if 'action' in event:
        if event['action'] == 'email':
            response = email(event)
        elif event['action'] == 'sns':
            response = sns(event)
        elif event['action'] =='telnet':
            response = telnet(event)
        else:
            response = {'error':'unknown action', event:event}
            
    else:
        response = http(event)
        
        
    return response
