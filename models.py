
class Student ():
    id = None
    id_major = None
    schedule = None
    major = None

    def __init__(self, id , id_major):
        self.id = id
        self.id_major = id_major


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
    groups = []

    def __init__(self, id_subject, name):
        self.id_subject = id_subject
        self.name = name

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