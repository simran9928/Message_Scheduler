import plivo
import sys

client = plivo.RestClient(auth_id='MAZMEWYJY4NZC2ZGYYM2', auth_token='ODc2MzM4MDFkZmY1MjEwOGMxZTU4ZDMxYzU1MmVl')
# info = sys.argv[1]
for i in range(0,1):
    try:
        message_created = client.messages.create(
            src='+17272631094',
            dst='+919647641633',
            text=message
            # text=info
        )
    except:
        print("Invalid number")