
try:
	import os,time
	import speech_recognition as sr
	from gtts import gTTS
	import wolframalpha
	import playsound
	import subprocess
	import PyPDF2
except:
	os.system("sudo pip3 install SpeechRecognition")
	os.system("sudo pip3 install gtts")

num = 1

def assistant_read(read):
	global num
	num += 1
	print(read)
	toSpeak = gTTS(text = read,lang = 'en',slow = False)
	sound_file = str(num)+".mp3"
	toSpeak.save(sound_file)

	playsound.playsound(sound_file,True)
	os.remove(sound_file)


def audio():
	rObject = sr.Recognizer()
	audio = ''
	with sr.Microphone() as source:
		assistant_read("Lütfen Bekleyiniz")
		audio = rObject.listen(source,phrase_time_limit=7)
		print("Hazırlanıyor")
	try:
		txt = rObject.recognize_google(audio, language='en_US')
		print(txt)
		return txt
	except:
		assistant_read("Dosya yok")
		return 0



if __name__ == "__main__":
	
    file_name = str(input("Enter to file name : "))

    files = open(file_name+".txt","r")

    for file_read in files:
        assistant_read(file_read)
