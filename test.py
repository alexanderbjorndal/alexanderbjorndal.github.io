from firebase import firebase

FBConn = firebase.FirebaseApplication('https://undervisningsopplegg-f15fa.firebaseio.com/', None)

while True:
	temperature = int(input("What is the temperature? "))

	data_to_upload = {
		'Temp' : temperature
	}
	
	result = FBConn.post('/MyTestData', data_to_upload)

	print(result)