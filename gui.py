import tkinter
from tkinter.messagebox import *
from tkinter.filedialog import *
import threading
import os
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
        for index in range(len(list)):
            text = list[index]
            if text.find('.') != -1:
                x = text.split('.')
                if x[1].lower() == 'mp4':
                    mp4_list.append(text)
            print(result)
        if result == False:
            for x in range(len(mp4_list)):
                os.system('adb.exe push \"' + mp4_list[x] + '\" /sdcard/DCIM/video')
t = tkinter.Tk()
t.title("mp4 in XiaoTianCao")
t.geometry("500x300")
t.resizable(0,0)
tkinter.Label(t,text = "小天才mp4写入",font = ('楷体',25)).place(x = 134,y = 40)
tkinter.Button(t,text = "检查设备",command = jiancha).place(x = 210,y = 100)
tkinter.Button(t,text = "结束adb",command = killadb).place(x = 211,y = 150)
tkinter.Button(t,text = "写入mp4",command = main).place(x = 209,y = 200)
t.mainloop()
