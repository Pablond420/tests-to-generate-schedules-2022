
from sqlalchemy import false
import numpy as np

class Schedule ():

    schedule = np.zeros((14,6))
    groups = []

    def __init__(self) -> None:
        pass

    def set_hour(self, startTime, endTime, day):
        self.schedule[startTime-7,day] = 1
        if(endTime>startTime+1):
            if(endTime==startTime+2):
                self.schedule[endTime - (7 + 1),day] = 1
            elif(endTime==startTime+3):
                self.schedule[endTime - (7 + 1),day] = 1
                self.schedule[endTime - (7 + 2),day] = 1
    
    def quit_hour(self, startTime, endTime, day):
        self.schedule[startTime-7,day] = 0
        if(endTime>startTime+1):
            if(endTime==startTime+2):
                self.schedule[endTime - (7 + 1),day] = 0
            elif(endTime==startTime+3):
                self.schedule[endTime - (7 + 1),day] = 0
                self.schedule[endTime - (7 + 2),day] = 0

#Con base en los parametros que llegan checa en la matriz si tiene un 1 , si es asi
#esta ocupado.
    def is_day_busy(self, startTime,endTime,day):
        flag = True
        if(self.schedule[startTime-7,day] == 1):
          flag = False
        elif(self.schedule[endTime-8,day] == 1):
          flag = False
        return flag
    
    def is_busy(self,group):
        flag = False
        if not self.is_day_busy(group.monday_start,group.monday_end,0):
            flag = True
        elif not self.is_day_busy(group.tuesday_start,group.tuesday_end,1):
            flag = True
        elif not self.is_day_busy(group.wednesday_start,group.wednesday_end,2):
            flag = True
        elif not self.is_day_busy(group.thursday_start,group.thursday_end,3):
            flag = True
        elif not self.is_day_busy(group.friday_start,group.friday_end,4):
            flag = True
        elif not self.is_day_busy(group.saturday_start,group.saturday_end,5):
            flag = True
        return flag
    
    def enroll_subject(self, group):
        self.set_hour(group.monday_start,group.monday_end,0)
        self.set_hour(group.tuesday_start,group.tuesday_end,1)
        self.set_hour(group.wednesday_start,group.wednesday_end,2)
        self.set_hour(group.thursday_start,group.thursday_end,3)
        self.set_hour(group.friday_start,group.friday_end,4)
        self.set_hour(group.saturday_start,group.saturday_end,5)

    def quit_subject(self, group):
        self.quit_hour(group.monday_start,group.monday_end,0)
        self.quit_hour(group.tuesday_start,group.tuesday_end,1)
        self.quit_hour(group.wednesday_start,group.wednesday_end,2)
        self.quit_hour(group.thursday_start,group.thursday_end,3)
        self.quit_hour(group.friday_start,group.friday_end,4)
        self.quit_hour(group.saturday_start,group.saturday_end,5)

class Student ():
    id = None
    id_major = None
    schedule = Schedule()
    major = None

    def __init__(self, id , id_major):
        self.id = id
        self.id_major = id_major
        self.schedule = np.zeros((14,6))



class Major ():
    id_major = None
    name = None 
    subjects = []

    def __init__(self, id_major, name):
        self.id_major = id_major
        self.name = name


class Subject():
    id_subject = None
    name = None 
    is_enrolled = None
    groups = []

    def __init__(self, id_subject, name):
        self.id_subject = id_subject
        self.name = name
        self.is_enrolled = false

    def add_group(self, group):
        self.groups.append(Group())

class Group():
    id_subject = None
    id_group = None
    teacher = None
    available_space = None
    monday_start = None
    monday_end = None
    tuesday_start = None
    tuesday_end = None
    wednesday_start = None
    wednesday_end = None
    thursday_start = None
    thursday_end = None
    friday_start = None
    friday_end = None
    saturday_start = None
    saturday_end = None

    def __init__(
        self,
        id_subject,
        id_group,
        teacher,
        available_space,
        monday_start,
        monday_end,
        tuesday_start,
        tuesday_end,
        wednesday_start,
        wednesday_end,
        thursday_start,
        thursday_end,
        friday_start,
        friday_end,
        saturday_start,
        saturday_end
    ):
        self.id_subject  = id_subject,
        self.id_group = id_group
        self.teacher = teacher
        self.available_space = available_space
        self.monday_start = monday_start
        self.monday_end = monday_end
        self.tuesday_start = tuesday_start
        self.tuesday_end = tuesday_end
        self.wednesday_start = wednesday_start
        self.wednesday_end = wednesday_end
        self.thursday_start = thursday_start
        self.thursday_end = thursday_end
        self.friday_start = friday_start
        self.friday_end = friday_end
        self.saturday_start = saturday_start
        self.saturday_end = saturday_end