from collections import OrderedDict
import datetime
import time 
import speech_recognition as sr
r = sr.Recognizer()


notes = {}
def menu_loop():
    choice = None
    while choice != 'q':
        for key, value in menu.items():
            print('%s) %s' % (key, value))
        choice = raw_input('Action: ').lower().strip()
        if choice in menu:
            menu[choice](notes)

def add_entry(notes):
	now_time = time.strftime("%Y-%m-%d-%H-%M")
	#time = str(datetime.datetime.now())
	#while True:
	dec = raw_input("1.Now you will put in a note through typing or 2. talking(1 or 2)\n")
	
	if dec == "1": 
		takenote = raw_input("...")
		notes[now_time] = takenote
		print "Your note has been saved and stored securely"
		raw_input("")
		#return notes
		#menu_loop()
	if dec == "2":
		with sr.Microphone() as source:
			print("Speak up!")
			audio =r.listen(source)
			takenote = r.recognize_google(audio)
			print takenote
			dec2 = raw_input("1.Do you want to keep this or 2. have a do-over\n")
			if dec2 == "1":
				notes[now_time]=takenote 
				#raw_input('')
				print'Your note has been saved and stored securely'
				raw_input("")
				#return notes 
				#menu_loop()
			else:
				add_entry(notes)
				
				
			
def view_entries(notes):
	for i in notes:
		print i , notes[i]
		raw_input("Click any button to get back to the Next entry/Menu \n")
	
def search_entries(notes):
	query = raw_input("What day do you wish to look for YYYY-MM-DD-HH-MM \n")
	if query in notes:
		print notes[query]
		raw_input("Click any button to get back to the Menu \n")
	else:
		print "Sorry theres no medical note under that date"
		raw_input("Click any button to get back to the Menu \n")

	
	
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
])
#for i in range(0,5):
				#5-i
				#sleep(i)
				#audio = r.listen(source)


menu_loop()
