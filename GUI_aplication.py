#Gui for aplication
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import threading
import speed
import concurrent.futures

#import funcionality
import Yt_Download_Script

class GUI():

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x525')
        self.root.title(" Youtube Video Downloader")
        self.root.iconbitmap('Yt_DW.ico')
        self.root.config(bg="#5c6c87")
        threading.Thread(target=self.test).start()



        self.photo = tk.PhotoImage(file='youtube.png') # definicja zdjęcia yt

        self.label = tk.Label(self.root,text="",height=1,bg="#5c6c87").pack()# przerwa dla dobrego wyggląu pusty lable
        self.label = tk.Label(self.root,text="",height=1,bg="#5c6c87").pack()# przerwa dla dobrego wyggląu pusty lable
        self.discription = tk.Label(self.root,
                                    text="Hey \n It is a video downloader application.\n\n In this App you just put link in to a gap\n and click download button to get free Yt video.\n When you click button you must choose place\n where you want file to be save.",
                                    font=('@Yu Gothic UI Semibold',15),
                                    fg='black',
                                    compound='bottom',
                                    bg="#5c6c87").pack() # opis definicja i wyświetlenie
        self.label = tk.Label(self.root,text="",bg="#5c6c87").pack()# przerwa dla dobrego wyggląu pusty lable
        self.label = tk.Label(self.root,image=self.photo,bg="#5c6c87").pack()# Wyświetlenie zdj


        self.label = tk.Label(self.root,text="",height=1,bg="#5c6c87").pack()# przerwa dla dobrego wyggląu pusty lable

        self.button = tk.Button(self.root,text="Download",bg="#5c6c87",font=('@MS Gothic',14,'bold'),pady=15,padx=50,fg="black",bd=1,relief="solid",command=self.variables).pack()
        self.label = tk.Label(self.root,text="",height=1,bg="#5c6c87").pack() # przerwa dla dobrego wyggląu pusty lable
        self.buttonHist = tk.Button(self.root,text="History",bg="#5c6c87",font=('@MS Gothic',12,'bold'),pady=15,padx=30,fg="black",bd=1,relief="solid",command=self.history).pack()


        self.path = "" #definicja dla ścieżki
        self.link = "" # definicja dla URL




        self.root.protocol("WM_DELETE_WINDOW",self.close)
        self.root.mainloop()

    def variables(self): # co sie dzieje po kliknięciu download
        self.new_window = tk.Toplevel()
        self.new_window.geometry("350x300")
        self.new_window.config(bg="#5c6c87")

        self.label1 = tk.Label(self.new_window,text="Put down URL to Youtube Video",bg="#5c6c87",font=('@MS Gothic',14,'bold')).pack()
        self.label = tk.Label(self.new_window,text="",bg="#5c6c87").pack()
        self.entry = tk.Entry(self.new_window,width=20,font=('@Yu Gothic UI Semibold',15),bg="#5c6c87",bd=1,relief='solid')
        self.entry.pack()
        self.label = tk.Label(self.new_window,text="",bg="#5c6c87").pack()
        #path = filedialog.askdirectory(title="Choose your videos folder",initialdir="C:/Users/Komputer/Downloads")
        self.bt1= tk.Button(self.new_window,text="Choose directory",bg="#5c6c87",font=('@MS Gothic',14,'bold'),pady=15,padx=50,fg="black",bd=1,relief="solid",command=self.directory).pack()
        self.label = tk.Label(self.new_window,text="",bg="#5c6c87").pack()
        self.bt2= tk.Button(self.new_window,text="Submit",bg="#5c6c87",font=('@MS Gothic',14,'bold'),pady=15,padx=50,fg="black",bd=1,relief="solid",command=self.subbmit).pack()









    def directory(self): # co się dzieje po kliknięciu choose directory
        self.path = filedialog.askdirectory(title="Choose your videos folder",initialdir="C:/Users/Komputer/Downloads")


    def subbmit(self): # co się dzieje po kliknięciu subbmit
        self.link = self.entry.get()
        if self.link != "" and self.path != "":
            if "https://www.youtube.com" in self.link:

                threading.Thread(target=Yt_Download_Script.download_YT,args=(self.link,self.path,self.return_value_speed)).start()
                #threading.Thread(target=Yt_Download_Script.speed, args=(self.link,)).start()

                file = open('history.txt','a')
                file.write(f'{self.link}\n')
                file.close()
                self.new_window.destroy()



            else:
                messagebox.showerror(title="Wrong URL!!!",message="Wrong URL!!!")

        elif self.link == "" and self.path != "":
            messagebox.showwarning(title="Empty URL.",message="URL input are empty!\n Enter URL")
        elif self.path == "" and self.link != "":
            messagebox.showwarning(title="Folder has not been selected",message="You must select folder!!!")
        else:
            messagebox.showwarning(title="Empty variable!!!",message="You must enter URL link and select folder to download video")

    def history(self):
        history_window = tk.Toplevel()
        history_window.geometry('400x450')
        history_window.config(bg="#5c6c87")
        history_window.resizable(False,False)



        self.label = tk.Label(history_window,text="",bg="#5c6c87")
        self.label.pack()

        self.label = tk.Label(history_window,text="Your videos URL",font=('@Yu Gothic UI Semibold',15),fg='black',bg="#5c6c87")
        self.label.pack()


        self.label = tk.Label(history_window,text="_________________________________________________________",bg="#5c6c87")
        self.label.pack()
        self.text = tk.Text(history_window,height=50,bg='#5c6c87')
        self.text.pack()


        file = open('history.txt','r')
        file_read = file.readlines()
        i=1
        for row in file_read:
            row = row.strip()
            position = f'{i}.0'
            self.text.insert(position,f'\n{row}\n\n');
            i+=1

        file.close()
    def test(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(speed.speed,)
            self.return_value_speed = future.result()


    def close(self):
        self.root.destroy()
        import os;os._exit(1)




GUI()
