import time
import datetime
import os


class Pomodoro:
    '''
    pomodoro timer
    '''
    current_pom=0
    def __init__(self,work_time,rest_time):
        self.work=work_time   #work time in minutes
        self.rest=rest_time   #rest time in minutes
        self.work_sec= self.work * 60

    def run_timer(self):
        os.system('clear')
        
        while Pomodoro.current_pom <=3:
            for s in range(self.work_sec):
                print(f'Cycle no. {Pomodoro.current_pom+1}')
                print(s)
                time.sleep(1)
                os.system('clear')           
            Pomodoro.current_pom+=1
        print('Pomodoro cant run anymore')

timer=Pomodoro(1,5)

timer.run_timer()