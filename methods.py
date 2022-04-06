import data_processing as dp


def get_student(cve_unica):
    student = None
    for i in dp.DataProcessing.students:
        if i.id == cve_unica:
            student = i
            break
    return student



