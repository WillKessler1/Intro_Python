import webbrowser
import time

total_breaks = 4
breaks_count = 0

print("This program started on "+time.ctime())
while (breaks_count<=total_breaks) :
    time.sleep(2*3600)
    webbrowser.open("https://www.youtube.com/watch?v=oQDLAoPs-as")
    breaks_count= breaks_count+1
    
