from memory_profiler import profile


class Subject:
    # @profile
    def __init__(self, name, startGrade, endGrade):
        self.name = name
        self.startGrade = startGrade
        self.endGrade = endGrade
