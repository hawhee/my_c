temper = {}
with open("temper_stat.txt") as file:
    for line in file:
        line = float(line.strip("\n"))
        try:
            temper[line] += 1
        except KeyError:
            temper[line] = 1
    max_temper = str(max(temper.keys()))
    min_temper = str(min(temper.keys()))
    average_temper = str(round(sum(temper.keys()) / len(temper),1))
    unique_temper = str(len(temper))
print("Уникальных: " + unique_temper)
print("Максимальное значение: " + max_temper)
print("Минимальное значение: " + min_temper)
print("Среднее значение: " + average_temper)
