# 2. Вам дается файл task2_input.txt, в нем лежит список. Каждый элемент на новой строке, и последняя строка - значение
# искомого элемента el.
# Напишите функцию, которая будет принимать имя этого файла, читать данные из него и создавать файл task2_output.txt,
# куда будет записывать часть списка ДО первого места, где попался el.
# Пример: в функцию передан файл с числами -1, 3, 2, 5, 1, 6, 2 (каждый с новой строки, здесь через запятую
# для краткости). В таком случае значение el - 2 (последняя строка), и ваша функция должна записать в файл
# список -1, 3 (каждый элемент с новой строки).
# Если значение, равное el, стоит на первом месте списка, запишите в файл слово "Empty".
# Если значения, равного el, в списке не нашлось, запишите в файл слово "Error"

def get_sublist(file_name):
    pass
def write_output_file(input_task2_input,output_task2_input):
    with open('task2_input.txt', 'r') as input_file, open('task2_input.txt', 'w') as output_file:
        lines = input_file.readlines()
        el = lines[-1].strip()  # получение последнего элемента из строки
        list_values = lines[:-1]  # получить список значений из всех, кроме последней строки
        try:
            index = list_values.index(el)  # найти индекс первого вхождения el
            if index == 0:
                output_file.write("Empty")  # если el первый елемент, написать "Empty"
            else:
                output_file.write(''.join(list_values[:index]))  #написать часть списка перед el
        except ValueError:
            output_file.write("Error")  # Если эл нет в списке, напишите "Error"
#
#

# 3. В функцию передается CSV файл task3_input.csv, c заголовком city,score. Ниже в нем информация в
# виде "название города,кол-во балов" (делимитер - запятая).
# Функция должна вернуть CSV файл task3_output.csv следующего вида:
#     score_sum,avg_score,best_city
#     1,2,3
# где:
# 1 - сумма очков всех городов
# 2 - среднее арифметичское всех очков (сумма, деленная на количество элементов)
# 3 - название города, у которого максимальное количество очков

def city_rating(file_name):
    pass

import csv

def process_csv_file(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        city_scores = []
        for row in reader:
            city_scores.append((row[0], int(row[1])))

    score_sum = sum(score for _, score in city_scores)
    avg_score = score_sum / len(city_scores)
    best_city = max(city_scores, key=lambda x: x[1])[0]

    with open('task3_output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['score_sum', 'avg_score', 'best_city'])
        writer.writerow([score_sum, avg_score, best_city])

process_csv_file('task3_input.csv')


# 4. Вам дается файл task4_input.csv с заголовком name,swimming,chess,guitar и контентом следующего вида:
# имя ребенка и через запятую три значения - 1, если ребенок посещает соответствующий кружок, 0 - если нет.
# Пример:
#     name,swimming,chess,guitar
#     Emma,1,0,0
# У Эммы 1 только в колонке swimming, следовательно, она посещает только плавание.
# На основе этих данных вам нужно вычислить детей, которые не знают никого, кроме одногруппников из своего кружка
# (то есть они не пересекаются с детьми из других кружков).
# Результат запишите в файл task4_output.txt, где каждое имя из вычисленного множества - на новой строке

def not_busy_children(file_name):
    pass


def process_csv_file(csv_file_path):
    with open(csv_file_path, 'r') as file:
        lines = file.readlines()[1:]
    data = {}
    for line in lines:
        name, swimming, chess, guitar = line.strip().split(',')
        data[name] = {
            'swimming': int(swimming),
            'chess': int(chess),
            'guitar': int(guitar)
        }

    unique_children = set()
    for name1, activities1 in data.items():
        overlaps = False
        for name2, activities2 in data.items():
            if name1 != name2 and any(a1 & a2 for a1, a2 in zip(activities1.values(), activities2.values())):
                overlaps = True
                break
        if not overlaps:
            unique_children.add(name1)

    with open('task4_output.txt', 'w') as file:
        for name in unique_children:
            file.write(name + '\n')

process_csv_file('task4_input.csv')


# ===========================================================================
# КОД НИЖЕ МЕНЯТЬ НЕЛЬЗЯ
# ===========================================================================

def get_result_list(file_name):
    output = open(file_name)

    result_list = []
    for line in output:
        result_list.append(line.strip())
    return result_list


def get_city_rating_result(file_name):
    output = open(file_name)

    # skip the header
    output.readline()

    result = output.readline().strip().split(",")
    return tuple(result)


def test_get_sublist():
    get_sublist("task2_input.txt")
    result_list = get_result_list("task2_output.txt")
    result_list = [int(item) for item in result_list]

    assert result_list == [1, 5, 3]


def test_city_rating():
    city_rating("task3_input.csv")
    result_list = get_city_rating_result("task3_output.csv")
    result = tuple(result_list)

    assert result == ("366", "61.0", "Munich")


def test_not_busy_children():
    not_busy_children("task4_input.csv")
    result_list = get_result_list("task4_output.txt")
    result = set(result_list)

    assert result == {"Emma", "Caroline", "Pam", "Sam"}


if __name__ == '__main__':
    test_get_sublist()
    test_city_rating()
    test_not_busy_children()
    print("Well done!!!")