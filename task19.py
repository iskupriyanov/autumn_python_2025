#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm

import csv
data = ["C4.5" , "k - means" , "Метод опорных векторов" ,
             "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
             "Наивный байесовский классификатор", "CART" ]
with open("task19.csv", 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['id'])
    for value in data:
        writer.writerow([value])
print("'task19.csv' создан успешно")
