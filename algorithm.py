import methods as m
import data_processing as dp

def algorithm():
    for student in dp.DataProcessing.students:
        for subject in student.major.subjects:
            id_group = None
            id_group = m.earliest_group(subject,student)
            id_group = m.group_with_more_slots(subject,student)\
                 if id_group is None else id_group
            group = m.get_group(id_group,subject.groups) 
            if group:
                student.schedule.enroll_subject(group)
                student.schedule.groups.append(group)
                m.decrease_slots(id_group,subject.groups)
