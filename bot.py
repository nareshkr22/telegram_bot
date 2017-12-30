import telepot
import sys
import datetime
import time 
import httplib
 
def handle(msg): 
	print '=============================='
	for key in msg:
		print "key: %s , value: %s" % (key, msg[key])
	content_type, chat_type, chat_id = telepot.glance(msg)
	print 'Content_type %s'  % content_type
	if content_type == 'text':
		command = msg['text']  
	print 'Received Command : %s' % command
	check_command(command,chat_id)
	print '...............................'

def check_command(command,chat_id):
	if len(command.split(" ")) > 1:
		is_sub = 1		
		mobile_no = command.split(" ")[:2][1] 		
		message = " ".join(command.split(" ")[2:])
		command = command.split(" ")[:2][0]
		print message
		 
	else:
		command = command
	if command == '/turnon'	:
		#connect with rasberry pi and turn it on	
		bot.sendMessage(chat_id,'Computer Will Turn on in Few Minutes')
	elif command == '/time':
		#get the system time
		bot.sendMessage(chat_id,str(datetime.datetime.now()))
	elif command == '/sendsms':
		#send user to request mobile number
                bot.sendMessage(chat_id, 'Enter Mobile Number /send mobilenumber')
	elif command == '/send':
		#send sms to the users mobile
		if is_sub:
	                bot.sendMessage(chat_id, 'Sending Message ....')
			send_sms(mobile_no,message)
		else:
			bot.sendMessage(chat_id, 'Enter Mobile Number /send mobilenumber')
		
 
def send_sms(number,message):
	conn = httplib.HTTPConnection("api.msg91.com")
	query_string = "/api/sendhttp.php?sender=MSGIND&route=4&mobiles="+ str(number)+ "&authkey=190441AX5WGH2Npn5a466395&country=91&message="+message+" "

	print query_string
	conn.request("GET", query_string)

	res = conn.getresponse()
	data = res.read()

	print(data.decode("utf-8"))

bot = telepot.Bot('540503841:AAEXRRApl8Lc4NDJDRDC3V3JnFrroOJET_E')
bot.message_loop(handle)


print "I am listening..."

while(1):
	time.sleep(10)
