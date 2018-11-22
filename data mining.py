import vk
import json as js
import re
import time
class story:
	def __init__(self, txt, likes, views):
		self.text=txt
		self.ratio=likes/views
app_id="###"
token="###"
group_id="###"
session = vk.AuthSession(scope='groups, wall', app_id=app_id, user_login="####", user_password="####")
vk.api.access_token=token
api = vk.API(session)
off=0
story_list = list()
while(off<5000):
	stories=api.wall.get(owner_id=-group_id, offset=off, count=100,  v="5.78")
	#print(stories)
	reg = re.compile('[^a-zA-Z ]')
	
	for i in stories['items']:
		st=story(re.sub(r'[^\w\s]','',i['text']), i['likes']['count'], i['views']['count'])
		story_list.append(st)
	off+=100
	time.sleep(1)
	
f=open('dict.txt', 'w')
f.write('{')
for i in story_list:
	f.write("'"+i.text+"': ")
	f.write(str(i.ratio))
	f.write(",")
f=open('dict.txt', 'r')
d=f.read()
d=d[:-1]+'}'
d=d.replace('\n', ' ')
from ast import literal_eval

d= literal_eval(d)
f=open('dict.txt', 'w')
f.write(str(d))

