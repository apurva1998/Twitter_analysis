import datetime
import random
import time
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient('mongodb://localhost:27017/')

db = client['twitter']

dict1 = {0:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},1:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},2:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},3:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},4:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},5:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},6:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0}}
dict2 = {0:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},1:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},2:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},3:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},4:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},5:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},6:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0}}

geo_tagged = db['geo_tagged']

for obj in geo_tagged.find():
	x = time.strftime("%a;%w-%H:%M", time.localtime(int(dumps(obj)[28])))
	day = int(x[x.index(';')+1])+1
	y = (x.index('-')+1)
	hour = int(x[y:(y+2)])
	if x[-5]==0:
		hour = int(x[y+1])
	min = int(x[(y+3):(y+5)])
	if min<30:
		dict1[(day-1)][hour]=dict1[(day-1)][hour]+1
	else:
		dict2[(day-1)][hour]=dict2[(day-1)][hour]+1
			
follow = db.follow

print("Entered follow db")

for obj in follow.find():
	x = time.strftime("%a;%w-%H:%M", time.localtime(int(dumps(obj)[28])))
	day = int(x[x.index(';')+1])+1
	y = (x.index('-')+1)
	hour = int(x[y:(y+2)])
	if x[-5]==0:
		hour = int(x[y+1])
	min = int(x[(y+3):(y+5)])
	if min<30:
		dict1[(day-1)][hour]=dict1[(day-1)][hour]+10
	else:
		dict2[(day-1)][hour]=dict2[(day-1)][hour]+10
		
keywordcollection = db.keywordcollection

print("Entered keyword db")

for obj in keywordcollection.find():
	x = time.strftime("%a;%w-%H:%M", time.localtime(int(dumps(obj)[28])))
	day = int(x[x.index(';')+1])+1
	y = (x.index('-')+1)
	hour = int(x[y:(y+2)])
	if x[-5]==0:
		hour = int(x[y+1])
	min = int(x[(y+3):(y+5)])
	if min<30:
		dict1[(day-1)][hour]=dict1[(day-1)][hour]+4
	else:
		dict2[(day-1)][hour]=dict2[(day-1)][hour]+4
		
merged = db.merged

for d in range(0,7):
	for h in range(0,24):
		for s in range(0,2):
			if d==0:
				q='Sun'
			if d==1:
				q='Mon'
			if d==2:
				q='Tue'
			if d==3:
				q='Wed'
			if d==4:
				q='Thu'
			if d==5:
				q='Fri'
			if d==6:
				q='Sat'
			if random.random()<=(1/3):
				rand = 'L'
			else:
					if random.random()>(2/3):
						rand = 'H'
					else:
						rand = 'M'
			if s==0:
				merged_obj = {'day':q,'hour':'H'+str(h),'minute':'M0','tweetden':dict1[d][h],'class':rand}
			else:
				merged_obj = {'day':q,'hour':'H'+str(h),'minute':'M30','tweetden':dict2[d][h],'class':rand}
				
			merged.insert_one(merged_obj).inserted_id