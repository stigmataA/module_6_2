class Vehicle:
    """Класс автомобилей"""
    __COLOR_VARIANTS = ['red', 'blue', 'yellow', 'green', 'black', 'white']  # список возможных цветов

    def __init__(self, owner: str, model: str, engine_power: int, color: str):  # атрибуты класса автомобилей
        self.owner = owner  # владелец автомобиля можем менять
        self.__model = model  # модель автомобиля не может менять
        self.__engine_power = engine_power  # мощность двигателя не может менять
        self.__color = color  # цвет автомобиля не может менять

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):  # метод вывода информации о автомобиле
        print(self.get_model())
        print(self.get_color())
        print(self.get_horsepower())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):  # метод изменения цвета автомобиля
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    """Класс седан, дочерний класс автомобилей"""
    __PASSENGERS_LIMIT = 5  # атрибут класса Седан  - максимальное количество пассажиров

    def __init__(self, owner, model, engine_power, color):  # атрибуты класса Седан
        super().__init__(owner, model, engine_power, color)

    def get_passengers_limit(self):
        return f'Максимальное кол-во пассажиров: {self.__PASSENGERS_LIMIT}'


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')  # Создание объекта
vehicle1.print_info()

vehicle1.set_color('Pink')  # Смена цвета на Pink
vehicle1.set_color('BLACK')  # Смена цвета на BLACK
vehicle1.owner = 'Vasyok'  # имя владельца

vehicle1.print_info()

