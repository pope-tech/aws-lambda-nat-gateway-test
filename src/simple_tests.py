import boto3
from botocore.exceptions import ClientError

import urllib.request
import json


def http(event):
    url = event['url']
    response = urllib.request.urlopen(url)

    return json.loads(response.read())


def email(event):
    client = boto3.client('ses',region_name='us-east-1')

    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    event['to'],
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': "<b>Hello</b> from <i>lambda</i>",
                    },
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': "Hello from lambda",
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': "Testing Lambda",
                },
            },
            Source=os.environ['FROM_EMAIL'],
            # If you are not using a configuration set, comment or delete the
            # following line
            #ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

    return response


def sns(event):
    client = boto3.client('sns')

    response = client.publish(
        PhoneNumber=event['to'],
        Message='TEST from lambda',
    )

    return response

def telnet(event):
    import telnetlib

    HOST = event.get('host', 'towel.blinkenlights.nl')
    PORT = event.get('port', None)

    try:
        tn = telnetlib.Telnet(HOST, PORT)
        response = {'success':str(tn.read_some())}

    except ConnectionRefusedError as error:
        response = {'error':str(error)}

    return response
