# import collections

# Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

# cat = Cat('Simon', 4, 'Krabat')

# print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}')


# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = {}
# for mark in student_marks:
#     if mark in mark_counts:
#         mark_counts[mark] += 1
#     else:
#         mark_counts[mark] = 1

# print(mark_counts)



# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts)



# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)

# print(mark_counts.most_common())
# print(mark_counts.most_common(1))
# print(mark_counts.most_common(4))

# from collections import Counter

# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_count = Counter(words)

# Виведення слова та його частоти
# for word, count in word_count.items():
#     print(f"{word}: {count}")




# from collections import defaultdict

# # Створення defaultdict з list як фабрикою за замовчуванням
# d = defaultdict(list)

# # Додавання елементів до списку для кожного ключа
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)

# print(d)


# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = {}

# for word in words:
#     char = word[0]
#     if char not in grouped_words:
#         grouped_words[char] = []
#     grouped_words[char].append(word)

# print(grouped_words)



# from collections import defaultdict

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = defaultdict(list)

# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)

# print(dict(grouped_words))








# # Створення стеку
# def create_stack():
#     return []

# # Перевірка на порожнечу
# def is_empty(stack):
#     return len(stack) == 0

# # Додавання елементу
# def push(stack, item):
#     stack.append(item)

# # Вилучення елементу
# def pop(stack):
#     if not is_empty(stack):
#         return stack.pop()
#     else:
#         print("Стек порожній")

# # Перегляд верхнього елемента
# def peek(stack):
#     if not is_empty(stack):
#         return stack[-1]
#     else:
#         print("Стек порожній")


# stack = create_stack()
# push(stack, 'a')
# push(stack, 'b')
# push(stack, 'c')

# print(peek(stack))  # Виведе 'c'





# from collections import deque

# # Створення черги
# queue = deque()

# # Enqueue: Додавання елементів
# queue.append('a')
# queue.append('b')
# queue.append('c')

# print("Черга після додавання елементів:", list(queue))

# # Dequeue: Видалення елемента
# print("Видалений елемент:", queue.pop())

# print("Черга після видалення елемента:", list(queue))



# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# gen = my_generator()

# # Використання next()
# print(next(gen))  # Виведе 1
# print(next(gen))  # Виведе 2
# print(next(gen))  # Виведе 3
# print(next(gen))



def count_down(start):
    while start > 0:
        yield start
        start -= 1

for number in count_down(5):
    print(number)
