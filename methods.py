import data_processing as dp


def get_student(cve_unica):
    student = None
    for i in dp.DataProcessing.students:
        if i.id == cve_unica:
            student = i
            break
    return student

def get_group(id_group):
    group = None 
    if id_group is not None:
        for i in dp.DataProcessing.groups:
            if i.id_group == id_group:
                group = i
                break
    return group

def decrease_slots(id_group):
    for i in dp.DataProcessing.groups:
        if i.id_group == id_group:
            i.available_space -= 1

def group_with_more_slots(subject,schedule):
    id_group = None
    aux = 0
    for group in dp.DataProcessing.groups:
        if subject.id_subject != group.id_subject or group.available_space < 1:
            pass
        if schedule.is_busy(group):
            pass

        if group.available_space > aux:
            aux = group.available_space
            id_group = group.id_group
    return id_group

def earliest_group(subject,schedule):
    id_group = None
    aux = 30
        
    for group in dp.DataProcessing.groups:
        if subject.id_subject != group.id_subject or group.available_space < 1:
            pass
        if schedule.is_busy(group):
            pass
        if earliest_hour(group) < aux:
            aux = earliest_hour(group)
            id_group = group.id_group
    return id_group

        
def earliest_hour(group):
    aux = group.monday_start if group.monday_start != 0 \
        else group.tuesday_start if group.tuesday_start != 0 else group.wednesday_start\
            if group.wednesday_start != 0 else group.thursday_start if group.thursday_start != 0\
                else group.friday_start if group.friday_start != 0 else group.saturday_start
    
    aux = group.tuesday_start if group.tuesday_start != 0 and group.tuesday_start  < aux else aux
    aux = group.wednesday_start if group.wednesday_start != 0 and group.wednesday_start < aux else aux
    aux = group.thursday_start if group.thursday_start != 0 and group.thursday_start < aux else aux
    aux = group.friday_start if group.friday_start != 0 and group.friday_start < aux else aux
    aux = group.saturday_start if group.saturday_start != 0 and group.saturday_start < aux else aux
    
    return aux






