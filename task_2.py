class Tester:

    def __init__(self, name): #Не было аргумента self для присвоения объектам класса значений
        self.name = name
        # self.deadline = True в принципе можно убрать эту строчку из класса т.к. аргумент deadline передается в функции для объекта через self что удовлетворяет условию задания

    def work_hard(self, deadline=True):
        if deadline: # Здесь убрал self т.к. нужно проверять значение аргумента подаваемого в функцию а не переменную класса
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!'