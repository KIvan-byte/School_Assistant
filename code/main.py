from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, ListProperty
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.screenmanager import Screen
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
# from kivy.core.window import Window
from N import B
from Parser import Parser
import time
import wikipedia

# Window.size = (480, 853)

KV = '''

<Diary>:
    label0: label0
    BoxLayout:
        
        boxlayout:boxlayout
        orientation: 'vertical'
        BoxLayout:
            id: boxlayout
            login: login
            password: password
            size_hint: 1,0.3
            # pos_hint: {'top':1}
            orientation: 'vertical'  
            spacing: '2dp'       
            GridLayout:
                size_hint: 1,0.8
                cols: 1
                padding: '15dp',0,'15dp',0         
                MDTextField:
                    id: login
                    font_size: 55
                    size_hint: 1,0.5
                    hint_text: 'login     '
                    mode: "rectangle"
                MDTextField:
                    font_size: 50
                    id: password
                    size_hint: 1,0.5
                    hint_text: 'password    '
                    mode: "rectangle"
            MDRaisedButton:
                size_hint: 1,0.4
                text: 'Вывести домашние задания'
                on_press: root.pars(login.text,password.text)

        # ScrollView:
        #     # size_hint: 1,0.85
        #     MDGridLayout:
        #         id: box
        #         cols: 1
        #         adaptive_height: True
        ScrollView:		       
		    size_hint: 1,1
	        MDLabel:
	        	text: ''
	        	id: label0
	        	size_hint_y: None
	    		text_size: self.width, None
	    		height: self.texture_size[1]
	    		#font_size: 57
	    		markup: True

                

<Main>:
    Image:
        size_hint: 1,1
        source: "main.png"
<Wikipedia>:
    labelwik: labelwik
    tef:tef
    padding: '5dp','5dp',0,'5dp'
    orientation: 'vertical'
    GridLayout:
        padding: '15dp',0,'2dp',0
        spacing: '1dp'
        rows: 1
        pos_hint: {'top':1}
        size_hint: 1,0.1
        BoxLayout:
            size_hint: 0.8,1
            padding: 0,0,'14dp',0
            MDTextField:
                id: tef
                font_size: 70
                size_hint:1,1                  
                hint_text: "Введите текст"
                mode: "rectangle"
        BoxLayout:
            size_hint: 0.2,1
            padding: 0,'5dp',0,0
            MDRaisedButton:
                on_press: root.wiki_call(tef.text)
                text: 'wiki'
                size_hint: 1,1
    ScrollView:		       
        size_hint: 1,0.9
        MDLabel:
            text: ''
            id: labelwik
            size_hint_y: None
            text_size: self.width, None
            height: self.texture_size[1]
            #font_size: 57
            markup: True


<History>:
    on_enter: root.start()
    hr:hr
    ScrollView:	    
	    size_hint: 1,1
	    MDGridLayout:
	        id: hr
	        cols: 1
	        adaptive_height: True

<Biology>:
    on_enter: root.start()
    br:br
    ScrollView:	    
	    size_hint: 1,1
	    MDGridLayout:
	        id: br
	        cols: 1
	        adaptive_height: True


<Obch>:
    on_enter: root.start()
    obr:obr
    ScrollView:	    
	    size_hint: 1,1
	    MDGridLayout:
	        id: obr
	        cols: 1
	        adaptive_height: True

<Help>:
    Image:
        size_hint: 1,1
        source: "help.png"


<Content>:
    size_hint_y: None
    height: self.minimum_height
    
    
    MDCard:  	
    	orientation: "vertical"
        padding: "8dp"
        size_hint: self.parent.size_hint_x, None
        size: "280dp",'200dp'
        MDLabel:
        	
        	bold: True
        	text: root.title
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]
        MDSeparator:         
            height: "1dp"
        MDLabel:          
            text: root.body

<Screen2>:
    rv:rv
    bbox: bbox
    tf:tf
    padding: '5dp','5dp','5dp','5dp'
    orientation: 'vertical'
    GridLayout:
        padding: '15dp',0,'2dp',0
        spacing: '1dp'
        id: bbox
        rows: 1
        pos_hint: {'top':1}
        size_hint: 1,0.1
        BoxLayout:
            padding: 0,0,'14dp',0
            MDTextField:
                id: tf
                font_size: 70
                size_hint:1,1    
                on_text: root.call(self.text)
                hint_text: "Введите текст"
                mode: "rectangle"
    ScrollView:     
        size_hint: 1,0.9
        MDList:
            size_hint: 1,1
            id: rv
            cols: 1
            adaptive_height: True

<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"
	#md_text_color: 1,0,0,1
    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "80dp", "80dp"
            source: "book.png"

    MDLabel:
        font_size: 70
        text: "School Assistant"
        #font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        MDList:
            id: md_list
            OneLineIconListItem:
				theme_text_color: "Custom"			
				text: 'Главная'
				on_press:
					root.nav_drawer.set_state("close")
	                root.screen_manager.current = "main"
                IconLeftWidget:
                    icon: 'apps-box' 
                    theme_text_color: "Custom"
            OneLineIconListItem:
				theme_text_color: "Custom"
				
				text: 'История'
				on_press:
					root.nav_drawer.set_state("close")
	                root.screen_manager.current = "hist"
                IconLeftWidget:
                    icon: 'book' 
                    theme_text_color: "Custom"
            OneLineIconListItem:
				theme_text_color: "Custom"
				
				text: 'Биология'
				on_press:
					root.nav_drawer.set_state("close")
	                root.screen_manager.current = "bio"
                IconLeftWidget:
                    icon: "biohazard"
                    theme_text_color: "Custom"
            OneLineIconListItem:
				theme_text_color: "Custom"
				
				text: 'Обществознание'
				on_press:
					root.nav_drawer.set_state("close")
	                root.screen_manager.current = "obch"
                IconLeftWidget:
                    icon: "nature-people"
                    theme_text_color: "Custom"
            OneLineIconListItem:
				theme_text_color: "Custom"
				
				text: 'Дневник'
				on_press:
					root.nav_drawer.set_state("close")
	                root.screen_manager.current = "diary"
                IconLeftWidget:
                    icon: 'library-books' 
                    theme_text_color: "Custom"
            OneLineIconListItem:
				theme_text_color: "Custom"
				text: 'Помощь'
				on_press:
					root.nav_drawer.set_state("close")
                    root.screen_manager.current = "help" 
                IconLeftWidget:
                    icon: 'help-circle' 
                    theme_text_color: "Custom"   

					
Screen:
		
    NavigationLayout:
    	screen_manager: screen_manager.__self__
    	MDToolbar:
			id: toolbar
		    pos_hint: {"top": 1}
		    elevation: 10
		    title: "School Assistant"
		    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
			right_action_items: [["wikipedia", lambda x: app.change_screen('wiki')],['magnify',lambda x: app.change_screen('search')]]
		
        ScreenManager:
        	size_hint_y: None
        	height: root.height-toolbar.height
			id: screen_manager
            Main:
                name: "main"
                
            Screen2:              
                name: "search"
                
            History:              
                name: "hist"

            Biology:
                name: 'bio'

            Obch:
                name: 'obch'
            Diary:
                name: 'diary'
            Help:
                name: 'help'
            Wikipedia:
                name: 'wiki'
            
            
                
                
                	

        MDNavigationDrawer:
            id: nav_drawer
			type: "standard"			
            ContentNavigationDrawer:
                id: content_drawer
                screen_manager: screen_manager.__self__
                nav_drawer: nav_drawer      	 
			    
'''


class Content(BoxLayout):
    title=StringProperty()
    body=StringProperty()

class Diary(Screen):
    def pars(self, login,password):
        # self.box.clear_widgets()

        if login != '' and password != '':
            output2 = self.SchoolBy('2',login, password)
            output1 = self.SchoolBy('1',login, password)
            # self.box.add_widget(MDLabel(text=output))
            self.label0.text = 'Домашнее задание на сегодня:' + "\n" + output1+'\n\n'+'Домашнее задание на завтра:'+ '\n' + output2
    def SchoolBy(self,text,log,pas):
        # Разворачиваем дату для библиотеки datetime
        day = list(map(int,text.split('.')))[::-1]
        login = log
        password = pas
        parser = Parser(login, password)
        output = ''
        #  Проверяем день
        if day == [1]:
            answer = parser.school(1)
        elif day == [2]:
            answer = parser.school(2)
        else:
            answer = parser.school(day)
        if answer == None:
            return 'Ошибка, перепроверьте ввод.'
        elif answer == 403:
            return 'Неправильный логин или пароль'
        for lesson in answer:
            output += f'{lesson[0]}\nДомашнее задание: {lesson[1]}. \nОценка за урок: {lesson[2]}' + '\n\n'
        return output
class Main(Screen):
    pass

class Wikipedia(Screen):
    def wiki_call(self, text):
        self.labelwik.text = ''
        inf = [text, self.wikipedia(text)]
        self.labelwik.text = inf[1]
    def wikipedia(self,search):
        try:
            wikipedia.set_lang('ru')
            res=wikipedia.summary(search)
            return 'Информация взята из Википедии:'+ '\n\n'+res
        except:
            return ('Ничего не найдено!')

class History(Screen):
    count = True
    def start(self):
        if self.count:
            global defenitions_hist
            for inf in defenitions_hist:
                self.hr.add_widget(MDExpansionPanel(content=Content(title=inf[0][0].upper()+inf[0][1:],body=inf[1][0].upper()+inf[1][1:]),icon='sub.png',panel_cls=MDExpansionPanelOneLine(text=inf[0].title())))
            self.count = False
        
class Biology(Screen):
    count = True
    def start(self):
        if self.count:
            global defenitions_bio
            for inf in defenitions_bio:
                self.br.add_widget(MDExpansionPanel(content=Content(title=inf[0][0].upper()+inf[0][1:],body=inf[1][0].upper()+inf[1][1:]),icon='sub.png',panel_cls=MDExpansionPanelOneLine(text=inf[0].title())))
            self.count = False


class Obch(Screen):
    count = True
    def start(self):
        if self.count:
            global defenitions_obch
            for inf in defenitions_obch:
                self.obr.add_widget(MDExpansionPanel(content=Content(title=inf[0][0].upper()+inf[0][1:],body=inf[1][0].upper()+inf[1][1:]),icon='sub.png',panel_cls=MDExpansionPanelOneLine(text=inf[0].title())))
            self.count = False

class Help(Screen):
    pass

class Screen2(Screen,B):
    def call(self,text=''):
        ans = self.historyy_call(text)
        if text!='' and len(text)>=3:
            self.rv.clear_widgets()
            for inf in ans:
                self.rv.add_widget(MDExpansionPanel(content=Content(title=inf[1],body=inf[0][0].upper()+inf[0][1:]),icon='2021-01-06-08-25-31.png',panel_cls=MDExpansionPanelOneLine(text=inf[1])))
        else:
            self.rv.clear_widgets()
    
class ContentNavigationDrawer(BoxLayout):
    pass



defenitions_obch = []
defenitions_hist = []
defenitions_bio = []
class TestNavigationDrawer(MDApp,B):
    def change_screen(self,name):
        self.root.ids.screen_manager.current=name
    def build(self):
        return Builder.load_string(KV)
    def on_start(self):
        global defenitions_obch, defenitions_bio, defenitions_hist
        defenitions_bio = sorted(self.all_sub('biology'), key=lambda x: x[0][0])
        defenitions_obch = sorted(self.all_sub('lrnppl'), key=lambda x: x[0][0])
        defenitions_hist = sorted(self.all_sub('history'), key=lambda x: x[0][0])

        

if __name__ == '__main__':
    TestNavigationDrawer().run()