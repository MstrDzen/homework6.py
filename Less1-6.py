my_dict = {'orange': 'апельсин', 'apple': 'яблоко', 'banana': 'банан', 'kiwi': 'киви', 'plum': 'слива', 'lemon': 'лимон'}
print('Словарь: ', my_dict)

print(my_dict['orange'])
print(my_dict.get('watermelon', 'Отсутствует в словаре'))

my_dict.update({'watermelon': 'арбуз', 'peach': 'персик'})
my_dict.setdefault('pear', 'груша') # Но, как я понял, так только одну пару за раз можно добавить.
print('Дополненный словарь: ', my_dict)

a = my_dict.pop('apple')
print('Удалённое значение: ', a)
print('Изменённый словарь', my_dict)

my_set = {5, 6, 'tut', 'tam', 7.62, 5, 6, 'tut', 'tam', 7.62}
print('Список: ', my_set)
my_set.add((8, 9, 10))
my_set.update({'3,14'})
my_set.discard(6)
print('Изменённый список: ', my_set)


