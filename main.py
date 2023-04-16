import tkinter
import os
import threading
from tkinter.messagebox import *
from tkinter.filedialog import *
def jiancha():
    text = os.popen("adb devices").read()
    if text == "List of devices attached\n\n":
        print("adb devices is not ok")
        showinfo("提示","设备未就绪")
    else:
        showinfo("提示","设备已就绪")
def killadb():
    os.system("adb.exe kill-server")
    showinfo("提示","已结束adb")
def main():
    list = os.listdir()
    mp4_list = []
    for index in list:
        if index.find('.') != -1:
            x = index.split('.')
            if x[1].lower() == 'mp4':
                mp4_list.append(index)
    for x in mp4_list:
        os.system('adb push \"' + x + '\" /sdcard/DCIM/video/')
t = tkinter.Tk()
t.title("mp4 in XiaoTianCao")
t.geometry("500x300")
t.resizable(0,0)
tkinter.Label(t,text = "小天才mp4写入",font = ('楷体',25)).pack()
tkinter.Button(t,text = "检查设备",command = jiancha).pack()
tkinter.Button(t,text = "结束adb",command = killadb).pack()
tkinter.Button(t,text = "写入mp4",command = main).pack()
def startt(e):
    index = e.get()
    e.delete(0,tkinter.END)
    path = index[31:43]
    os.system("you-get --format=dash-flv360 -o "+path+" "+index)
    listos = os.listdir(path)
    os.system("rename .\\" + path + "\\*.mp4 " + path + ".mp4")
    os.system("adb push .\\" + path + "\\" + path + ".mp4 /sdcard/DCIM/video/")
def run(e):
    threading.Thread(target = startt,args = (e,)).start()
e = tkinter.Entry(t)
e.pack()
b = tkinter.Button(t,text="下载并且写入mp4",command=lambda:run(e))
b.pack()
t.mainloop()
