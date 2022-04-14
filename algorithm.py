import methods as m
import data_processing as dp

def algorithm():
    for student in dp.DataProcessing.students:
        for subject in student.major.subjects:
            id_group = m.earliest_group(subject,student.schedule)
            id_group = m.group_with_more_slots(subject,student.schedule) if id_group is None else id_group
            group = m.get_group(id_group) 
            if group:
                student.schedule.enroll_subject(group)
                student.schedule.groups.append(group)
                m.decrease_slots(id_group)
        print('hola')
