import pickle
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("Курлык")

class Mammal(Animal):
    def make_sound(self):
        print("Ррррррррррр")

class Reptile(Animal):
    def make_sound(self):
        print("Шшшшшшшшш")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_new_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в список")

    def add_new_staff(self, new_staff):
        self.staff.append(new_staff)
        print(f"Сотрудник {new_staff} добавлен в список")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Информация о зоопарке сохранена в файл {filename}")

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'rb') as file:
                zoo = pickle.load(file)
            print(f"Информация о зоопарке загружена из файла {filename}")
            return zoo
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Создан новый зоопарк.")
            return Zoo()

class ZooKeeper():
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian():
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

bird1 = Bird("Голубь", 1)
tiger1 = Mammal("Тигр", 4)
snake1 = Reptile("Гадюка", 1)

zoo_list1 = Zoo()
keeper1 = ZooKeeper("Игорь")
vet1 = Veterinarian("Константин")

zoo_list1.add_new_animal(bird1)
zoo_list1.add_new_animal(tiger1)
zoo_list1.add_new_animal(snake1)

zoo_list1.add_new_staff(keeper1)
zoo_list1.add_new_staff(vet1)

animal_sound(zoo_list1.animals)

keeper1.feed_animal(bird1)
vet1.heal_animal(snake1)

zoo_list1.save_to_file('zoo_data.pkl')

#Для згарузки сохраненного ранее зоопарка прописываем следующую строчку:
#zoo_list1 = Zoo.load_from_file('zoo_data.pkl')

