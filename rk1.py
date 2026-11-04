# Используется для сортировки
from operator import itemgetter

class Kaf:
    """Кафедра (вместо Сотрудник)"""
    def __init__(self, id, name, budget, fac_id):
        self.id = id
        self.name = name
        self.budget = budget  # Количественный признак
        self.fac_id = fac_id

class Fac:
    """Факультет (вместо Отдел)"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class KafFac:
    """
    'Кафедры факультета' для реализации
    связи многие-ко-многим
    """
    def __init__(self, fac_id, kaf_id):
        self.fac_id = fac_id
        self.kaf_id = kaf_id

# Факультеты
facs = [
    Fac(1, 'Информатика и системы управления'),
    Fac(2, 'Фундаментальные науки'),
    Fac(3, 'Радиоэлектроника и лазерная техника'),
    Fac(11, 'Аэрокосмический факультет'),
]

# Кафедры
kafs = [
    Kaf(1, 'Автоматизированные системы управления', 75000, 1),
    Kaf(2, 'Аналитическая химия', 35000, 2),
    Kaf(3, 'Высшая математика', 60000, 2),
    Kaf(4, 'Информационные системы', 45000, 1),
    Kaf(5, 'Физика', 50000, 2),
]

kafs_facs = [
    KafFac(1, 1),
    KafFac(2, 2),
    KafFac(2, 3),
    KafFac(1, 4),
    KafFac(2, 5),
    
    KafFac(11, 1),
    KafFac(11, 4),
]

def main():
    """Основная функция"""
    
    # Соединение данных один-ко-многим
    one_to_many = [(k.name, k.budget, f.name)
                   for f in facs
                   for k in kafs
                   if k.fac_id == f.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(f.name, kf.fac_id, kf.kaf_id)
                         for f in facs
                         for kf in kafs_facs
                         if f.id == kf.fac_id]
    
    many_to_many = [(k.name, k.budget, fac_name)
                    for fac_name, fac_id, kaf_id in many_to_many_temp
                    for k in kafs if k.id == kaf_id]

    print('Задание В1')
    # Список всех кафедр, у которых название начинается с буквы «А», и названия их факультетов
    res_11 = [(k_name, f_name) for k_name, _, f_name in one_to_many if k_name.startswith('А')]
    print(res_11)

    print('\nЗадание В2')
    # Список факультетов с минимальным бюджетом кафедр на каждом, отсортированный по минимальному бюджету
    res_12_unsorted = []
    for f in facs:
        # Список кафедр факультета
        f_kafs = list(filter(lambda i: i[2] == f.name, one_to_many))
        if len(f_kafs) > 0:
            # Бюджеты кафедр факультета
            f_budgets = [budget for _, budget, _ in f_kafs]
            # Минимальный бюджет
            f_budget_min = min(f_budgets)
            res_12_unsorted.append((f.name, f_budget_min))
            
    # Сортировка по минимальному бюджету
    res_12 = sorted(res_12_unsorted, key=itemgetter(1))
    print(res_12)

    print('\nЗадание В3')
    # Список всех связанных кафедр и факультетов (многие-ко-многим), отсортированный по кафедрам
    res_13 = sorted(many_to_many, key=itemgetter(0))
    print(res_13)

if __name__ == '__main__':
    main()
