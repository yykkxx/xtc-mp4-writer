# xtc-mp4-writer
这是一个可以把视频传输到小天才手表上的软件  
Down-Kyi文件是一个可以从bilibili上把视频下载下来的软件  
  
主要原理:  
  
依据adb的push命令  
  
`adb push <file name(path)> <path>`  
  
使用python字符串拼接  
  
`'adb.exe push \"' + mp4_list[x] + '\" /sdcard/DCIM/video'`  
  
再用os库的system和popen函数  
  
`os.system('adb.exe push \"' + mp4_list[x] + '\" /sdcard/DCIM/video')`  
  
`os.system('adb.exe push \"' + mp4_list[x] + '\" /sdcard/DCIM/video').read()`  
  
其他:  
  
使用tkinter构建窗口  
  
`t = tkinter.Tk()`  
`t.title("mp4 in XiaoTianCao")`  
`t.geometry("500x300")`  
`t.resizable(0,0)`  
  
创建控件:  
  
`tkinter.Label(t,text = "小天才mp4写入",font = ('楷体',25)).place(x = 134,y = 40)`  
`tkinter.Button(t,text = "检查设备",command = jiancha).place(x = 210,y = 100)`  
`tkinter.Button(t,text = "结束adb",command = killadb).place(x = 211,y = 150)`  
`tkinter.Button(t,text = "写入mp4",command = main).place(x = 209,y = 200)`  
  
检查设备:  
  
`text = os.popen("adb devices").read()`  
`if text == "List of devices attached\n\n":`   
`    print("adb devices is not ok")`  
`    tkinter.showinfo("提示","设备未就绪")`  
`else:`  
`    tkinter.showinfo("提示","设备已就绪")`  
  
全部源码详见gui.py  
  
main.py提供了最简单的非图形界面  
