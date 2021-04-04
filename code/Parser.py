import requests
from bs4 import BeautifulSoup
import datetime

class Parser:
	def __init__(self,input_login,input_password):
		ua = 'Mozilla/5.0 (X11; Linux i686; rv:84.0) Gecko/20100101 Firefox/84.0'
		self.months = {(9,10): '41',(11,12): '42',(1,2,3): '43',(4,5): '44'}
		self.__crsftoken = 'vWokxFiZ3XsViQeSS1nHdc76W5w7BMp8'
		self.link = "https://schools.by/login"
		self.__user_data = {'username': input_login,'password': input_password,"csrfmiddlewaretoken": self.__crsftoken}
		self.__header = {'user-agent': ua,"referer": 'https://schools.by/', 'cookie': f'csrftoken={self.__crsftoken}'}

	def __getMonday(self,day):
		while datetime.datetime.isoweekday(day) != 1:
			day = day - datetime.timedelta(days=1)
		return str(day.strftime("%Y-%m-%d"))

	def getMonth(self,date):
		for mon in self.months:
			if date.month in mon:
				return self.months[mon]

	def whatDay(self,day):
		return datetime.datetime.isoweekday(day)

	def __requestPost(self,current_date):
		try:
			mysession = requests.session()
			pupil = mysession.post(self.link, data=self.__user_data,headers= self.__header, timeout=5)
		except Exception as e:
			# print("!!! " + str(e))
			return None
		try:
			pup = pupil.url.split('/')[-1]
			response = mysession.get(f'https://gymn192.schools.by/pupil/{pup}/dnevnik/quarter/{self.getMonth(current_date)}/week/{self.__getMonday(current_date)}')
			if response.status_code == 200:
				return response.text
			else:
				return 403
		except Exception as e:
			# print("!!! " + str(e))
			return None

	def __home(self,current_date):
		self.getMonth(current_date)
		lessons_dict = {}
		response = self.__requestPost(current_date)
		if response == 403:
			return 403
		elif response == None:
			# print("!!! None")
			return None
		try:
			soup = BeautifulSoup(response, 'lxml')
		except Exception as e:
			return None
		current_date = current_date.strftime("%d.%m.%Y")
		current_date = current_date[:-4]+current_date[-2:]
		block = soup.find('table', id = f'db_table_{current_date}')
		try:
			lessons = block.find_all('tr')
		except Exception as e:
			# print("!!! " + str(e))
			return None
		lessons_list = []

		for lesson in lessons:
			try:
				name = ''.join(lesson.find('span').text.split())
				task = lesson.find(class_='ht-text')
				mark = lesson.find('strong')
				if task != None:
					task = ' '.join(task.text.split())
				if mark != None:
					mark = ','.join(mark.text.split())
				lessons_list.append([name,task,mark])
			except:
				pass
		lessons_dict[f'{current_date}'] = lessons_list
		return self.__handle(lessons_dict[f'{current_date}'])
	def __handle(self,data):
		new_date = []
		for datum in data:
			if len(datum[0]) > 5:
				element = []
				for el in datum:
					if el == None:
						element.append('Отсутствует')
						continue
					element.append(el)
				new_date.append(element)
		return new_date
	def school(self,our_today):
		if our_today == 1:
			# Today homework
			now = datetime.datetime.today()
			if self.whatDay(now) != 7:
				return self.__home(now)
			else:
				return None
		elif our_today == 2:
			# next day homework
			now = datetime.datetime.today() + datetime.timedelta(days=1)
			if self.whatDay(now) != 7:
				return self.__home(now)
			else:
				# print('school')
				return None
		else:
			# homework on some day
			year, month, day = our_today
			date = datetime.date(year,month,day)
			if self.whatDay(date) != 7:
				return self.__home(date)
			else:
				return None
	
	

