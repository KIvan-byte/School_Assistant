import math
import SQLvar as ask
import sqlite3


def nok(a,b):
	m = a*b
	while a != 0.0 and b != 0.0:
		if a> b:
			a %= b
		else:
			b %= a
	return (m // (a+b))
class A:
	def Giron(self,a):
		a.sort()
		if float(a[0])+float(a[1])>float(a[2]):
			p=(((float(a[0])+float(a[1])+float(a[2]))/2*((float(a[0])+float(a[1])+float(a[2]))/2-float(a[0]))*((float(a[0])+float(a[1])+float(a[2]))/2-float(a[1]))*((float(a[0])+float(a[1])+float(a[2]))/2- float(a[2])))**0.5)
			return str(round(p,3))
		else:
			return'Такого треугольника не существует!!!'
	def NOD(self,a):
		for i in range(int(min(a)),0,-1):	
			if len(list(filter(lambda x: x%i==0,a)))==len(a):
				return '[b]'+'НОД: '+'[/b]'+ str(i)
	def NOK(self,a):
		l=a[::]
		while len(l)!=1:
				w=nok(l.pop(),l.pop())			
				l.append(w)
		return '[b]'+'НОK: '+'[/b]'+str(int(l[0]))
		
	
	def trink(self,a):
		a=float(a[0])
		return '[b]'+'sin: '+'[/b]'+str(round(math.sin(math.radians(a)),5))+'[b]'+'\ncos: '+'[/b]'+str(round(math.cos(math.radians(a)),5))+'[b]'+'\ntan: '+'[/b]'+str(round(math.tan(math.radians(a)),5))+'[b]'+'\nctg: '+'[/b]'+str(round(1/(math.tan(math.radians(a))),5))+'\n'
	def artr(self,k):
		a=float(k[0])
		if -1<=a<=1:
			return '[b]'+ '\narcsin: '+'[/b]'+str(round(math.degrees(math.asin(a)),5))+'[b]'+'\narccos: '+'[/b]'+str(round(math.degrees(math.acos(a)),5))+'[b]'+'\narctg: '+'[/b]'+str(round(math.degrees(math.atan(a)),5))+'[b]'+'\narcctg: '+'[/b]'+str(round(math.degrees(math.pi/2-math.atan(a)),5))+'\n'
		else:
			return '[b]'+ '\narctg: '+'[/b]'+str(round(math.degrees(math.atan(a)),5))+'[b]'+'\narcctg: '+'[/b]'+str(round(math.degrees(math.pi/2-math.atan(a)),5))+'\n'
	def prrr(self,a):
		s=0
		for i in a:
			if i>=0:
				s+=1
		if s==len(a): return True
	
class B(A):				
	def historyy_call(self,a):
		with sqlite3.connect('mult.db') as con:
			answer=ask.get_from_db(con,a.lower())[:15]
			ans,res='',''
			for definition in answer:
				res=definition[0].title()
				ans=definition[1]
				if ans=='':
					yield '',''
				else: 
					yield ans,res
	def mathlb(self,a):
		try:
			var=[float(i) for i in a.split()]
			s,res='',''					
			if len(var)==1:
				s+=str(self.trink(var))
				s+=self.artr(var)
			if len(var)==3:
				s+='[b]'+'Площадь треугольника: ''[/b]'+str(self.Giron(var))+'\n\n'
			if len(var)>1 and self.prrr(var):
				s+=str(self.NOK(var))+'\n\n'
				s+=str(self.NOD(var))+'\n'
			
			return s
		except:
			return 'Неправильный ввод!'
	def ad_s(self,data):
		with sqlite3.connect('mult.db') as con:
			ask.write_data_to_db(con,data)
	def dell_s(self,name):
		with sqlite3.connect('mult.db') as con:
			ask.deletef(con,name)
	def up_s(self,fro,to):
		with sqlite3.connect('mult.db') as con:
			ask.update(con,fro,to)
	def all_sub(self, subject):
		with sqlite3.connect('subjects.db') as con:
			cur = con.cursor()
			cur.execute(f"SELECT * FROM {subject}")
			return cur.fetchall()[:30]
