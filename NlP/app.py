from tkinter import *
from mydb import Database
from my_API import API
from tkinter import messagebox
class NLPApp:
    def __init__(self) :
        # database /API obj
        self.db=Database()
        self.api=API()
        # login ka GuI
        self.root=Tk()
        self.root.title('NLP APP')
        icon = PhotoImage(file='resourses/android-icon-36x36.png')
        self.root.iconphoto(False, icon)
        self.root.geometry('350x600')
        self.root.configure(bg='#15304e')
        self.login_gui()

        self.root.mainloop()
    
    def login_gui(self):
        self.clear()
        heading=Label(self.root,text="NLP APP",bg="#15304e",fg="white")
        heading.pack()
        heading.pack(pady=(30,30))
        heading.configure(font=('Comic Sans MS', 24, 'bold'))

        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=30)
        self.email_input.pack(pady=(5,10),ipady=3)

        label2=Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.pass_input=Entry(self.root,width=30,show='*')
        self.pass_input.pack(pady=(10,10),ipady=3)

        login_btn=Button(self.root,text='Login',width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3=Label(self.root,text='Not Registered?')
        label3.pack(pady=(10,10))
        
        redirect_btn=Button(self.root,text='Redirect',width=11,command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def register_gui(self):
        self.clear()
        heading=Label(self.root,text="NLP APP",bg="#15304e",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('Comic Sans MS', 24, 'bold'))

        label0=Label(self.root,text='Enter Name')
        label0.pack(pady=(10,10))

        self.name_input=Entry(self.root,width=30)
        self.name_input.pack(pady=(5,10),ipady=3)

        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=30)
        self.email_input.pack(pady=(10,10),ipady=3)

        label1=Label(self.root,text='Enter Password')
        label1.pack(pady=(10,10))

        self.pass_input=Entry(self.root,width=30,show='*')
        self.pass_input.pack(pady=(10,10),ipady=3)

        register_btn=Button(self.root,text='Register',width=30,height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        label3=Label(self.root,text='Already Login?')
        label3.pack(pady=(10,10))
        
        redirect_btn=Button(self.root,text='Login Now',width=11,command=self.login_gui)
        redirect_btn.pack(pady=(10,10))


    
    def clear(self):
        # clear
        for  i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.pass_input.get()
        response=self.db.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success','You Can login Now!')
            print("reg success")
        else:
            messagebox.showerror('Email Exist','Try agin!')
            print("eamil exist")
        
        
    def perform_login(self):
        email=self.email_input.get()
        password=self.pass_input.get()
        response=self.db.search(email,password)

        if response:
            messagebox.showinfo('success','Login successful!')
            print('success')
            self.home_gui()
        else:
            messagebox.showerror('error','Login Failed!')
            print('unsuccess')
            
        

    def home_gui(self):
        self.clear()
        heading=Label(self.root,text="NLP APP",bg="#15304e",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('Comic Sans MS', 24, 'bold'))

        senti_btn=Button(self.root,text='Sentiment Analysis',width=30,height=2,command=self.sentiment_gui)
        senti_btn.pack(pady=(10,10))

        NER_btn=Button(self.root,text='Named Entity Recognition',width=30,height=2,command=self.NER_gui)
        NER_btn.pack(pady=(10,10))

        emotion_btn=Button(self.root,text='Language Detection',width=30,height=2,command=self.lang_gui)
        emotion_btn.pack(pady=(10,10))

        logout_btn=Button(self.root,text='Logout',command=self.login_gui)
        logout_btn.pack(pady=(10,10))
    
    def sentiment_gui(self):
        self.clear()
        heading=Label(self.root,text="NLP APP",bg="#15304e",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('Comic Sans MS', 24, 'bold'))

        heading1=Label(self.root,text="Sentiment Analysis",bg="#15304e",fg="white")
        heading1.pack(pady=(10,30))
        heading1.configure(font=('Comic Sans MS', 24))
        
        label=Label(self.root,text='Enter the text')
        label.pack(pady=(10,10))

        self.senti_input=Entry(self.root,width=30)
        self.senti_input.pack(pady=(10,10),ipady=3)

        senti_btn=Button(self.root,text='Analyse',command=self.do_sentiment_analysis)
        senti_btn.pack(pady=(10,10))
        
        self.result=Label(self.root,text='',bg="#15304e",fg="white")
        self.result.pack(pady=(10,10))
        self.result.configure(font=('Comic Sans MS', 16))

        goback_btn=Button(self.root,text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(10,10))
    
    def do_sentiment_analysis(self):
         text=self.senti_input.get()
         result=self.api.get_sentiment(text)
         
         self.result['text']=result



    def NER_gui(self):
        self.clear()
        heading=Label(self.root,text="NLP APP",bg="#15304e",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('Comic Sans MS', 24, 'bold'))

        heading1=Label(self.root,text="Named Entity Recognition",bg="#15304e",fg="white")
        heading1.pack(pady=(10,30))
        heading1.configure(font=('Comic Sans MS', 24))
        
        label=Label(self.root,text='Enter the text')
        label.pack(pady=(10,10))

        self.Ner_input=Entry(self.root,width=30)
        self.Ner_input.pack(pady=(10,10),ipady=3)

        senti_btn=Button(self.root,text='Analyse',command=self.do_NER)
        senti_btn.pack(pady=(10,10))
        
        self.result=Label(self.root,text='',bg="#15304e",fg="white")
        self.result.pack(pady=(10,10))
        self.result.configure(font=('Comic Sans MS', 16))

        goback_btn=Button(self.root,text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(10,10))

    def do_NER(self):
         text=self.Ner_input.get()
         result=self.api.get_NER(text)
         self.result.configure(text=f'Entity_group:{result["entity_group"]}\nScore:{result["score"]}\nWord:{result["word"]}')
         print(result)


    def lang_gui(self):
        
        self.clear()
        heading=Label(self.root,text="NLP APP",bg="#15304e",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('Comic Sans MS', 24, 'bold'))

        heading1=Label(self.root,text="Language Detection",bg="#15304e",fg="white")
        heading1.pack(pady=(10,30))
        heading1.configure(font=('Comic Sans MS', 24))
        
        label=Label(self.root,text='Enter the text')
        label.pack(pady=(10,10))

        self.Ner_input=Entry(self.root,width=30)
        self.Ner_input.pack(pady=(10,10),ipady=3)

        senti_btn=Button(self.root,text='Analyse',command=self.do_lang)
        senti_btn.pack(pady=(10,10))
        
        self.result=Label(self.root,text='',bg="#15304e",fg="white")
        self.result.pack(pady=(10,10))
        self.result.configure(font=('Comic Sans MS', 16))

        goback_btn=Button(self.root,text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(10,10))

    def do_lang(self):
         text=self.Ner_input.get()
         result=self.api.get_lang(text)
         self.result.configure(text=f'label:{result[0]}')
         print(result)

nlp=NLPApp()