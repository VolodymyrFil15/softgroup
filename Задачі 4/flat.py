import math
import sys

class material:
    """Будівельні матеріали"""
    square = 0
    unit_price = 0


class wallpaper(material):
    """шпалери"""
    roll_width = 0
    roll_height = 0
    square = roll_height * roll_width


class paint(material):
    """Фарба"""
    weight = 0
    consumption = 0

        
class laminate(material):
    """Ламінат"""
    board_heihgt = 0
    board_width = 0
    packadge_quantity = 0
    square = board_width * board_heihgt * packadge_quantity


class room:
    """docstring for room"""
    def count_wallpapers(self):
        not_to_count = self.windows_width * self.height + self.doors_width * self.height
        walls_square = (self.width * 2 * self.height) + (self.length * 2 * self.height) - not_to_count
        return math.ceil(walls_square / wallpaper.square)

    
    def count_paint(self):
        ceiling_square = self.length * self.width
        return math.ceil((ceiling_square * paint.consumption) / paint.weight)


    def count_laminate(self):
        floor_square = self.length * self.width
        return math.ceil(floor_square / laminate.square)


    def count_estimation(self):
        count_wallpapers()
        count_paint()
        count_laminate()


    def __init__(self, length, width, height, windows_width=0, doors_width=0):
        super(room, self).__init__()
        self.length = length
        self.width = width
        self.height = height
        self.windows_width = windows_width
        self.doors_width = doors_width


class flat:
    """docstring for flat"""


    def room_add(self):
        length = float(input("Введіть довжину кімнати"))
        width = float(input("Введіть ширину кімнати"))
        height = float(input("Введіть висоту кімнати"))
        windows_width = float(input("Введіть ширину вікон кімнати"))
        doors_width = float(input("Введіть ширину дверей кімнати"))
        self.rooms.append(room(length, width, height, windows_width, doors_width))


    def room_remove(self):
        self.rooms.remove(float(input("Введіть номер кімнати")) + 1)


    def print_estimation(self):
        for i in self.rooms:
            print("[Кімната: ширина: {0} м, довжина: {1} м, висота: {2} м]".format(i.width, i.length, i.height))
            print("Шпалери\t\t{0} x {1} = {2} грн.".format(wallpaper.unit_price, i.count_wallpapers(),
                wallpaper.unit_price * i.count_wallpapers()))
            print("Фарба\t\t{0} x {1} = {2} грн.".format(paint.unit_price, i.count_paint(), 
                paint.unit_price * i.count_paint(),))
            print("Ламінат\t\t{0} x {1} = {2} грн.".format(laminate.unit_price, i.count_laminate(),
                laminate.unit_price * i.count_laminate()))


    def __init__(self, *args):
        super(flat, self).__init__()
        self.rooms = []
        for i in args:
            self.rooms.append(i)
        

def set_values():
    wallpaper.unit_price = float(input("Введіть ціну рулону шпалер\n"))
    wallpaper.roll_width = float(input("Введіть ширину рулону шпалер\n"))
    wallpaper.roll_height = float(input("Введіть довжину рулону шпалер\n"))
    wallpaper.square = wallpaper.roll_height * wallpaper.roll_width

    paint.unit_price = float(input("Введіть ціну банки фарби\n"))
    paint.consumption = float(input("Введіть розхід фарби(л/м2)\n"))
    paint.weight = float(input("Введіть об'єм банки фарби\n"))

    laminate.unit_price = float(input("Введіть ціну пачки ламінату\n"))
    laminate.board_width = float(input("Введіть ширину дошки ламінату\n"))
    laminate.board_heihgt = float(input("Введіть довжину дошки ламінату\n"))
    laminate.packadge_quantity = float(input("Введіть кількість дошок ламінату в пачці\n"))
    laminate.square = laminate.board_width * laminate.board_heihgt * laminate.packadge_quantity


def menu():
    selection = input("Запустити програму - 1\n Показати тест - 2\n")
    if selection == '2':
        test()
        sys.exit(0)
    elif selection != '1':
        print("помилка")
        sys.exit(0)

    set_values()
    menu = {}
    menu['1'] = "Додати кімнату" 
    menu['2'] = "Видалити кімнату"
    menu['3'] = "Показати кімнати"
    menu['4'] = "Розрахувати ціну"
    menu['5'] = "Вийти"
    while True: 
        for key in menu.keys(): 
            print(key, menu[key])

        selection = input("Виберіть дію:") 
        if selection =='1': 
            flat.room_add()
        elif selection == '2': 
            flat.room_remove()
        elif selection == '3':
            for i in range(len(flat.rooms)):
                print("[Кімната: ширина: {0} м, довжина: {1} м, висота: {2} м]".format(flat.rooms[i].width, 
                    flat.rooms[i].length, flat.rooms[i].height))
        elif selection == '4':
            flat.print_estimation()
        elif selection == '5':
            break
        else: 
            print("Невідома дія!") 


def test():
    a = room(3, 5, 2.4)
    b = room(3, 4, 2.4)
    c = room(3, 3, 2.4)

    abc = flat(a, b, c)

    wallpaper.unit_price = 400
    wallpaper.roll_width = 2.1
    wallpaper.roll_height = 10
    wallpaper.square = wallpaper.roll_height * wallpaper.roll_width

    paint.unit_price = 500
    paint.consumption = 0.2
    paint.weight = 6

    laminate.unit_price = 400
    laminate.board_width = 0.5
    laminate.board_heihgt = 5
    laminate.packadge_quantity = 10
    laminate.square = laminate.board_width * laminate.board_heihgt * laminate.packadge_quantity

    abc.print_estimation()


if __name__ == '__main__':
    menu()
