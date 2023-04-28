import time

def focus_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("时间到！")

focus_time = int(input("请输入您想要专注的秒数："))
focus_timer(focus_time)
