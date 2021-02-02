import time
import datetime
import os


class Pomodoro:
    '''
    pomodoro timer
    '''
    cycle=0
    def __init__(self,work_time,rest_time):
        self.work=work_time   #work time in minutes
        self.rest=rest_time   #rest time in minutes
        self.work_sec= self.work * 60
        self.rest_sec= self.rest * 60

    def _takerest(self):
        for s in range(self.work_sec):
            print(f'Resting cycle No. {Pomodoro.cycle+1}')
            print(s)
            time.sleep(1)
            os.system('clear')           
    def run_timer(self):
        os.system('clear')
        
        while Pomodoro.cycle <=3:
            for s in range(self.work_sec):
                print(f'Cycle no. {Pomodoro.cycle+1}')
                print(s)
                time.sleep(1)
                os.system('clear')   
            self._takerest()        
            Pomodoro.cycle+=1


