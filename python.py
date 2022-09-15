import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/alexandebj/Downloads/undervisningsopplegg-f15fa-firebase-adminsdk-3fqor-298059bacf.json")
firebase_admin.initialize_app(cred)

default_app = firebase_admin.initialize_app('https://undervisningsopplegg-f15fa.firebaseio.com/', None)


FBConn = firebase_admin.FirebaseApplication('https://undervisningsopplegg-f15fa.firebaseio.com/', None)

while True:
	temperature = int(input("What is the temperature? "))

	data_to_upload = {
		'Temp' : temperature
	}
	
	result = FBConn.post('/MyTestData', data_to_upload)

	print(result)