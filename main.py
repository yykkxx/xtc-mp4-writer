import os
list = os.listdir()
jpgl = []
for index in range(len(list)):
    text = list[index]
    if text.find('.') != -1:
        x = text.split('.')
        if x[1].lower() == 'mp4':
            jpgl.append(text)
for x in range(len(jpgl)):
    print(os.system('adb.exe push \"' + jpgl[x] + '\" /sdcard/DCIM/video'))
