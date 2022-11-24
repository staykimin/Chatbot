import json

x = input("Masukkan Pertanyaan : ")
y = "test/db.min"

def BukaDb(path):
	with open(path) as dataku:
		z = json.loads(dataku.read())
	
	return z

def ParseQuest(data):
	hasil = []
	for i in data.split(" "):
		hasil.append(i)
	return hasil

def Validasi(data, quest):
	total = 0
	for i in data:
		if i in quest:
			total +=1
	return total

def CekQuest(data, quest):
	for i in data:
		database = ParseQuest(i['quest'])
		valid = Validasi(database, quest)
		syarat = i['syarat']
		if valid >= int(syarat):
			return i['answer']

def HilangiSpesial(data):
	hasil=""
	for i in data:
		if i.isnumeric() or i.isalpha():
			hasil = hasil +i
	return hasil

def Clear(quest):
	data = quest.lower().split(" ")
	hasil = []
	for i in data:
		if i.isnumeric() or i.isalpha():
			hasil.append(i)
		else:
			data = HilangiSpesial(i)
			hasil.append(data)
			
	return hasil
	

text = Clear(x)
sin = BukaDb(y)
cos = CekQuest(sin['db'], text)
print(f"Jawab	: {cos}")