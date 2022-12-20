import webbrowser
import time
import os

edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge))

for i in range(1, 35):
    webbrowser.get('edge').open('http://www.bing.com/search?btnG=1&q=' + 'bla' * i)
    time.sleep(3.2)

os.system("taskkill /im msedge.exe /f")