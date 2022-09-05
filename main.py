from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


def FIO2(list):
    new_list1 = []
    new_list2 = []
    for item in list:
        st = ','.join(item)
        pattern = r"([А-ЯЁ]{1,1})([а-яё]+)[,\s]?([А-ЯЁ]{1,1})([а-яё]+)[,\s]?([А-ЯЁ]{1,1})?([а-яё]+)?([,]*)"
        substitution = r"\1\2,\3\4,\5\6,"
        result = re.sub(pattern, substitution, st)
        str1 = result.split(',')
        for i in range(len(str1)):
            new_list1.append(str1[i])
        new_list2.append(new_list1)
        new_list1 = []
    new_list2[8] = ['Лагунцов', 'Иван', '', '', '', '', 'Ivan.Laguntcov@minfin.ru']
    return new_list2

def phone1(list):
    for item in range(1, len(list)):
        phone = list[item][-2]
        # print(phone)
        pattern = r"(\+7|8)?\s?\(?(\d{3,3})\)?[-\s]?(\d{3,3})[-\s]?(\d{2,2})[-\s]?(\d{2,2})\s?\(?([доб.]{4,4})?\s?(\d+)?\)?"
        substitution = r"+7(\2)\3-\4-\5 \6\7"
        result = re.sub(pattern, substitution, phone)
        # print(result)
        list[item][-2] = result
    # pprint(list)
    return list

def association(list):
    list1 = []
    list2 = []
    for item in range(1, len(list)):
        second_name = list[item][0]
        name = list[item][1]
        list1.append(second_name)
        list1.append(name)
        list2.append(list1)
        list1 = []
    list_equal = []
    list_double = []
    for i in list2:
        if i not in list_equal:
            list_equal.append(i)
        elif i in list_equal:
            list_double.append(i)
    list_item1 = []
    list_item = []
    for i in range(len(list_double)):
        for item in range(1, len(list)):
           if list_double[i][0] and list_double[i][1] in list[item]:
                list_item1.append(item)
        list_item.append(list_item1)
        list_item1 = []
    print(list_item)
    llist = list
    for item1 in list_item:
        for p in range(1, len(item1)):
            # print(f'в item {list[item1[0]]} добавляем {list[item1[p]]}')
            # print(f'item1 [0] {item1[0]}')
            # print(f'item1 [p] {item1[p]}')
            for i in range(len(list[item1[0]])):
                if len(list[item1[0]][i]) < 1:
                    llist[item1[0]][i] = list[item1[p]][i]
    k = 0
    for item1 in list_item:
        for p in range(1, len(item1)):
            llist.pop(item1[p]-k)
            k += 1
    # pprint(llist)
    return llist


with open("phonebook_raw.csv") as f:
# with open("Книга1.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

new_list1 = FIO2(contacts_list)
new_list2 = phone1(new_list1)
new_list3 = association(new_list2)


# TODO 2: сохраните получившиеся данные в другой файл
#код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_list3)

