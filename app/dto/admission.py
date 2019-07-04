class AdmissionDto:

    def __init__(self, number, unit="暂无", re_subject="暂无", re_grade="暂无"):
        self.number = number
        self.unit = unit
        self.re_subject = re_subject
        self.re_grade = re_grade


class AdmissionDtoList:

    def __init__(self, admissions):
        self.enter_list = []
        self.numbers = []
        for admission in admissions:
            self.enter_list.append(AdmissionDto(number=admission.number, unit=admission.unit,
                                                re_subject=admission.re_subject, re_grade=admission.re_grade))
            self.numbers.append(admission.number)

    def judge_records(self, records):
        for record in records:
            if record.number not in self.numbers:
                self.enter_list.append(AdmissionDto(number=record.number))
                self.numbers.append(record.number)

    # def __iter__(self):
    #     return next(self)
    #
    # def __next__(self):
    #     for data in self.enter_list:
    #         if data:
    #             yield data
    #         else:
    #             raise StopIteration
