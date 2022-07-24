# xtc-mp4-writer
这是一个可以把视频传输到小天才手表上的软件  
  
需要使用小天才4点数据线  
  
详细介绍:`https://space.bilibili.com/489759920`  
  
可以使用网络传输  
  
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
  
使用说明:  
  
点击  
`检查设备`  
  
以检查设备是否就绪  
  
点击  
`结束adb`  
  
以重启adb  
  
点击  
`写入mp4`  
  
以传入文件  
  
程序会自动检查当前目录下的mp4文件  
  
并将其文件名记录下来  
  
最后将其传入`/sdcard/DCIM/video`

注意:  
  
不要再传输过程中移动设备  
  
请在检查设备后再进行传输  
  
