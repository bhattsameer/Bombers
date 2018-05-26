from numspy import Way2sms

try:
	w2s = Way2sms()

	mobile_number= int(input("Enter the 10 digit Mobile number on which you want bomb: "))
	message= input("Enter message: ")
	n = int(input("How many messsages you want to send? (limit is 100/day): "))

	username = input("Your way2sms username: ")
	password = input("Your way2sms password: ")
	w2s.login(username,password)

	for i in range(0,n):
		w2s.send(mobile_number,message)
		print(str(i+1)+" messages sent!")

	w2s.logout()
except Exception as e: 
	print("Something is wrong try again!")
