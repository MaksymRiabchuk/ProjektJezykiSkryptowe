from memory_profiler import profile


class Grade:
    # @profile
    def __init__(self, subject, student, grade, teacher,
                 created_at, updated_at):
        self.subject = subject
        self.student = student
        self.grade = grade
        self.teacher = teacher
        self.created_at = created_at
        self.updated_at = updated_at
