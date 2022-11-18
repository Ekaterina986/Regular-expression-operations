from pprint import pprint
import re
import csv

# читаем исходный файл


with open("text.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# разделение ФИО по калонкам

for contact in contacts_list:
    contact_join = ' '.join(contact[0:3])
    pattern = r"\s+"
    format = " "
    contact_join = re.sub(pattern, format, contact_join)
    contact_arr = contact_join.split()
    for k,v in enumerate(contact_arr):
        contact[k] = v

# удаление дублей

del_index_list = []
for i1, contact1 in enumerate(contacts_list):
    for i2, contact2 in enumerate(contacts_list):
        if i1 < i2 and contact1[0] == contact2[0] and contact1[1] == contact2[1]:
            del_index_list.append(i2)
            for column_index, value in enumerate(contact2):
                if value:
                    contact1[column_index] = value

del_index_list.reverse()
for del_index in del_index_list:
    contacts_list.pop(del_index)

# pprint(contacts_list)


# изменение формата номера телефона

pattern = r"(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"

format_new = r"+7(\2)-\3-\4-\5 \6 \7"

for contact in contacts_list:
    contact[-2] = re.sub(pattern, format_new, contact[-2])

# pprint(contacts_list)

# сохранение данных в файл


with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)




