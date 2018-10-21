import webbrowser
import time

total_breaks = 4
breaks_count = 0

while (breaks_count<=total_breaks) :
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=oQDLAoPs-as")
    breaks_count= breaks_count+1
