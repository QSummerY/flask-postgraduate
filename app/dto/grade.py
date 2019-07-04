class GradeDto:

    def __init__(self, number, name, politics="暂无", english="暂无", basis="暂无", profession_basis="暂无", profession="暂无"):
        self.number = number
        self.name = name
        self.politics = politics
        self.english = english
        self.basis = basis
        self.profession_basis = profession_basis
        self.profession = profession


class GradeDtoList:

    def __init__(self, grades):
        self.score_list = []
        self.numbers = []
        for grade in grades:
            self.score_list.append(GradeDto(number=grade.number, name=grade.name, politics=grade.politics, english=grade.english,
                                            basis=grade.basis, profession_basis=grade.profession_basis, profession=grade.profession))
            self.numbers.append(grade.number)

    def judge_records(self, records):
        for record in records:
            if record.number not in self.numbers:
                self.score_list.append(GradeDto(number=record.number, name=record.name))
                self.numbers.append(record.number)
