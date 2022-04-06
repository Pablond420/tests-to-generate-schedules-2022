from numpy import true_divide
import models as m

class DataProcessing ():
    students_data_frame = None
    major_data_frame = None
    subject_data_frame = None
    group_data_frame = None
    majors = []
    students = []
    groups = []

    def __init__(self,stu_df,m_df,sub_df,g_df):
        self.students_data_frame = stu_df
        self.major_data_frame = m_df
        self.subject_data_frame = sub_df
        self.group_data_frame = g_df

    def df_to_classes(self):

        # Relleno de materias en cada carrera y crea lista de carreras
        for i in self.major_data_frame.index: 
            major = m.Major(self.major_data_frame["id_carrera"][i],
                    self.major_data_frame["nombre"][i])
            for j in self.subject_data_frame.index:
                if major.id_major == self.subject_data_frame["id_carrera"][j]:
                    major.subjects.append( m.Subject(
                        self.subject_data_frame["id_materia"][j],
                        self.subject_data_frame["nombre"][j]))
            self.majors.append(major)

        #  relleno de carreras en cada estudiante y crea lista de estudiantes
        for i in self.students_data_frame.index:
            student = m.Student(self.students_data_frame["cve_unica"][i],
                    self.students_data_frame["id_carrera"][i])
            for major in self.majors:
                if major.id_major == student.id_major:
                    student.major = major
                    break
            self.students.append(student)
        
        # relleno de grupos
        for i in self.group_data_frame.index:
            group = m.Group(
                self.group_data_frame["id_materia"][i],
                self.group_data_frame["grupo"][i],
                self.group_data_frame["maestro"][i],
                self.group_data_frame["cupo"][i],
                self.group_data_frame["lunes_inicio"][i],
                self.group_data_frame["lunes_final"][i],
                self.group_data_frame["martes_inicio"][i],
                self.group_data_frame["martes_final"][i],
                self.group_data_frame["miercoles_inicio"][i],
                self.group_data_frame["miercoles_final"][i],
                self.group_data_frame["jueves_inicio"][i],
                self.group_data_frame["jueves_final"][i],
                self.group_data_frame["viernes_inicio"][i],
                self.group_data_frame["viernes_final"][i],
                self.group_data_frame["sabado_inicio"][i],
                self.group_data_frame["sabado_final"][i],
            )
            self.groups.append(group)
        if True:
            pass


    
        


        

