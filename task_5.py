class TestCase:

    def __init__(self):
        self.steps = {}
        self.result = None
    
    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    def delete_step(self, step_number):
        del self.steps[step_number] # del - загуглил удаление шага из словаря по ключу

    def set_result(self, result):
        self.result = result
    
    # Тупил над выводом в данный метод, но GPT мне объяснил что print() сначала вычисляет переданное ему выражение, а уже потом выводит
    # Получается print() создает объект или проводит вычисления как бы "на лету" а потом уже вывод. Просто данный объект не сохраняется в какую-либо переменную
    # Оставил для себя примеры:
    # print(10)                    # число
    # print("Привет")              # строка
    # print([1, 2, 3])             # список
    # print({'a': 1, 'b': 2})      # словарь

    def get_test_case(self):
        print({
        'Шаги': self.steps,
        'Ожидаемый результат': self.result
    })

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()