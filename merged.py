import datetime
import random
import time
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['twitter']

dict1 = {0:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},1:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},2:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},3:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},4:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},5:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},6:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0}}
dict2 = {0:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},1:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},2:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},3:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},4:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},5:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0},6:{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0}}

geo_tagged = db.geo_tagged

for obj in geo_tagged.find():
	x = time.strftime("%A-%H:%M", time.localtime(int(obj.distinct('timestamp_ms'))))
	day = x[:3]
	hour = x[4:2]
	min = x[-2:]
	if day==0:
		if min<30:
			dict1[0][hour]=dict1[0][hour]+1
		else:
			dict2[0][hour]=dict2[0][hour]+1
	if day==1:
		if min<30:
			dict1[1][hour]=dict1[1][hour]+1
		else:
			dict2[1][hour]=dict2[1][hour]+1
	if day==2:
		if min<30:
			dict1[2][hour]=dict1[2][hour]+1
		else:
			dict2[2][hour]=dict2[2][hour]+1
	if day==3:
		if min<30:
			dict1[3][hour]=dict1[3][hour]+1
		else:
			dict2[3][hour]=dict2[3][hour]+1
	if day==4:
		if min<30:
			dict1[4][hour]=dict1[4][hour]+1
		else:
			dict2[4][hour]=dict2[4][hour]+1
	if day==5:
		if min<30:
			dict1[5][hour]=dict1[5][hour]+1
		else:
			dict2[5][hour]=dict2[5][hour]+1
	if day==6:
		if min<30:
			dict1[6][hour]=dict1[6][hour]+1
		else:
			dict2[6][hour]=dict2[6][hour]+1
		
follow = db.follow

for obj in follow.find():
	x = time.strftime("%A-%H:%M", time.localtime(int(obj.distinct('timestamp_ms'))))
	day = x[:3]
	hour = x[4:2]
	min = x[-2:]
	if day==0:
		if min<30:
			dict1[0][hour]=dict1[0][hour]+10
		else:
			dict2[0][hour]=dict2[0][hour]+10
	if day==1:
		if min<30:
			dict1[1][hour]=dict1[1][hour]+10
		else:
			dict2[1][hour]=dict2[1][hour]+10
	if day==2:
		if min<30:
			dict1[2][hour]=dict1[2][hour]+10
		else:
			dict2[2][hour]=dict2[2][hour]+10
	if day==3:
		if min<30:
			dict1[3][hour]=dict1[3][hour]+10
		else:
			dict2[3][hour]=dict2[3][hour]+10
	if day==4:
		if min<30:
			dict1[4][hour]=dict1[4][hour]+10
		else:
			dict2[4][hour]=dict2[4][hour]+10
	if day==5:
		if min<30:
			dict1[5][hour]=dict1[5][hour]+10
		else:
			dict2[5][hour]=dict2[5][hour]+10
	if day==6:
		if min<30:
			dict1[6][hour]=dict1[6][hour]+10
		else:
			dict2[6][hour]=dict2[6][hour]+10
		
keywordcollection = db.keywordcollection

for obj in keywordcollection.find():
	x = time.strftime("%A-%H:%M", time.localtime(int(obj.distinct('timestamp_ms'))))
	day = x[:3]
	hour = x[4:2]
	min = x[-2:]
	if day==0:
		if min<30:
			dict1[0][hour]=dict1[0][hour]+4
		else:
			dict2[0][hour]=dict2[0][hour]+4
	if day==1:
		if min<30:
			dict1[1][hour]=dict1[1][hour]+4
		else:
			dict2[1][hour]=dict2[1][hour]+4
	if day==2:
		if min<30:
			dict1[2][hour]=dict1[2][hour]+4
		else:
			dict2[2][hour]=dict2[2][hour]+4
	if day==3:
		if min<30:
			dict1[3][hour]=dict1[3][hour]+4
		else:
			dict2[3][hour]=dict2[3][hour]+4
	if day==4:
		if min<30:
			dict1[4][hour]=dict1[4][hour]+4
		else:
			dict2[4][hour]=dict2[4][hour]+4
	if day==5:
		if min<30:
			dict1[5][hour]=dict1[5][hour]+4
		else:
			dict2[5][hour]=dict2[5][hour]+4
	if day==6:
		if min<30:
			dict1[6][hour]=dict1[6][hour]+4
		else:
			dict2[6][hour]=dict2[6][hour]+4
	
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
				merged_obj = {"day":q,"hour":'H'+h,"minute":'M0',"tweetden":dict1[d][h],"class":rand}
			else:
				merged_obj = {"day":q,"hour":'H'+h,"minute":'M30',"tweetden":dict2[d][h],"class":rand}
				
			merged.insert_one(merged_obj).inserted_id
























