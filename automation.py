from selenium import webdriver 
import pyttsx3
import speech_recognition as sr
import time
import pyautogui


class Voice:
	@staticmethod
	def t2s(text):
		e = pyttsx3.init()
		e.say(text)
		e.runAndWait()

	@staticmethod
	def s2t():
		r = sr.Recognizer()
		with sr.Microphone() as source:
			r.pause_threshold=1
			Voice.t2s("listening")
			print("listening")
			audio = r.listen(source)
		text = r.recognize_google(audio)
		return text 


class Iiitb:
	def __init__(self):
		self.username = '//*[@id="username"]'
		self.u = 'IMT2020545'
		self.driver = webdriver.Safari()
		self.url = 'https://lms.iiitb.ac.in'
		self.password = '//*[@id="password"]'
		self.p = '9441213540@Jan'
		self.loginbutton = '//*[@id="loginbtn"]'


	def browse(self):
		self.driver.get(self.url)



	def login2lms(self):
		box1 = self.driver.find_element_by_xpath(self.username)
		box1.send_keys(self.u)

		box2 = self.driver.find_element_by_xpath(self.password)
		box2.send_keys(self.p)


		button = self.driver.find_element_by_xpath('//*[@id="loginbtn"]')
		button.click()


	@staticmethod
	def caller():
		b = Iiitb()
		b.browse()
		b.login2lms()

	
class Amazon:
	def __init__(self):
		self.driver = webdriver.Safari()


	def browse(self):
		self.driver.get('https://amazon.in')	
		

	def search(self,text):
		box1 = self.driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
		box1.send_keys(text)

		button = self.driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
		button.click()

	def scroll_up(self):
		pyautogui.scroll(1)


def main():
	Voice.t2s("software Initilized tell me which website youwant to browser")
	text = Voice.s2t()
	if 'learning' in text.lower():
		Iiitb.caller()
		time.sleep(60)

	elif 'amazon' in text.lower():
		B = Amazon()
		B.browse()
		text = Voice.s2t()
		B.search(text)
		time.sleep(1000)
		

main()



		






    












