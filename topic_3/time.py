# import time
#
# current_time = time.time()
# print(f"Поточний час: {current_time}")


# import time
#
# print("Початок паузи")
# time.sleep(5)
# print("Кінець паузи")


# import time
#
# current_time = time.time()
# print(f"Поточний час: {current_time}")
#
# readable_time = time.ctime(current_time)
# print(f"Читабельний час: {readable_time}")

#
# import time
#
# current_time = time.time()
# print(f"Поточний час: {current_time}")
#
# local_time = time.localtime(current_time)
# print(f"Місцевий час: {local_time}")


# import time
#
# # Записуємо час на початку виконання
# start_time = time.perf_counter()
#
# # Виконуємо якусь операцію
# for _ in range(1_000_000):
#     pass  # Просто проходить цикл мільйон разів
#
# # Записуємо час після виконання операції
# end_time = time.perf_counter()
#
# # Розраховуємо та виводимо час виконання
# execution_time = end_time - start_time
# print(f"Час виконання: {execution_time} секунд")




import random

num = random.random(1, 10)
print(num)


# import random
#
# items = ['яблуко', 'банан', 'вишня', 'диня']
# chosen_item = random.choices(items, k=2)
# print(chosen_item)


# import random
#
# participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
# team = random.sample(participants, 11)
# print(f"Команда: {team}")
