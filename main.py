import threading
from pytube import YouTube
from tkinter import messagebox
from os.path import exists
from tkinter import *
from tkinter.ttk import *
import time


def download_YT(link,path,speed):
    def bar(time_of_task):
        def load(time_of_task):
            paint = 100 / time_of_task
            for i in range(int(time_of_task)):
                time.sleep(1)
                bar['value'] += paint
                bar_window.update_idletasks()
            bar['value'] += 100
            messagebox.showinfo(title="Succes",message="Succes!!! \n Your video is download")
            bar_window.destroy()



        bar_window = Tk()
        bar = Progressbar(bar_window,orient=HORIZONTAL,length=300)
        bar.pack(pady=10)
        threading.Thread(target=load,args=(time_of_task,)).start()
        bar_window.mainloop()


    yt=YouTube(link)
    yd_size = yt.streams.get_highest_resolution().filesize_mb
    file_size_MB=yd_size/8
    time_download = file_size_MB / speed
    print(time_download)



    yd = yt.streams.get_highest_resolution()
    path_video = f"{path}/{yt.title}.mp4"
    threading.Thread(target=bar,args=(time_download,)).start()

    yd.download(f'{path}')


download_YT('https://www.youtube.com/watch?v=TuLxsvK4svQ&list=WL&index=9&t=8356s','C:/Users/Komputer/Pictures/Saved Pictures',9.0)
    #if exists(path_video) == True:
     #   messagebox.showinfo(title="Succes",message="Succes!!! \n Your video is download")

    #else:
     #   messagebox.showerror(title="download fail",message="Download failed!!! Check URL")







