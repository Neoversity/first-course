# text = "hello word"
# result = text.split()
#
# print(result)
#
# text = "apple,banana,cherry"
# result = text.split(',')
# print(result)  # Виведе: ['apple', 'banana', 'cherry']


# list_of_strings = ['Hello', 'world']
# result = ' , '.join(list_of_strings)
# print(result)  # Виведе: 'Hello world'

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)