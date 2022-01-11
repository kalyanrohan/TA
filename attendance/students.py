from person import Person

class Student(Person):
    
    def __init__(self, name, age,sex, occupation,class_num):
        super().__init__(name, age,sex,occupation,class_num)
        self.attendance = False
        self.scores = {}
    
    
    def get_attendance(self):
        return self.attendance
    
    def add_scores(self,subject,score):
        self.scores[subject] = score
    
    def get_scores(self):
        return self.scores
    
    def get_scores_by_subject(self,subject):
        return self.scores[subject]
    

