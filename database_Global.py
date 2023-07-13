Class Database:
    def __init__(database_name):
        _connected_to_database= False
    
    def get_connected_to_database(_connected_to_database):
    
    def set_connected_to_database(connection_state):
        print("Неможливо змінити значення connected_to_database за допомогою присвоєння. Використайте метод connect_to_database")
    
    def get_database_name():
    
    def set_database_name():
        
        #see https://apps.prometheus.org.ua/learning/course/course-v1:GlobalLogic+QAAUTO101+2023_T1/block-v1:GlobalLogic+QAAUTO101+2023_T1+type@sequential+block@d51705863f9e483cae576b9316e5309f/block-v1:GlobalLogic+QAAUTO101+2023_T1+type@vertical+block@385ff3572a4949c6bd2fed64655ba57e
        
    
    

'''Завдання 10.1
0.0/3.0 points (graded)
Описати клас БазаДанних (Database), який задовольняє наступні умови:

Конструктор класу приймає обов'язковий параметр "Ім'я бази даних" (database_name) і зберігає його значення як приватний атрибут об'єкту без використання сеттера для збереження цього значення.
В конструкторі оголошений прихований атрибут об'єкту "Під'єднано до бази даних" (_connected_to_database), який за замовчування має значення False.
Клас має наступні методи об'єкту:
Геттер(get_connected_to_database) та сеттер (set_connected_to_database) для атрибуту _connected_to_database:
Сеттер приймає параметр "стан з'єднання" (connection_state);
Сеттер має вивести повідомлення на екран "Неможливо змінити значення connected_to_database за допомогою присвоєння. Використайте метод connect_to_database"
Геттер (get_database_name) та сеттер (set_database_name) для атрибуту __database_name:
Сеттер приймає параметр "значення" (value) та змінює значення атрибуту __database_name на value;
Сеттер має змінювати регістр атрибуту __database_name на "Всі літери - великі"
Під'єднатися до бази даних (connect_to_database), задача якого змінити значення атрибуту об'єкта _connected_to_database на True та вивести на екран повідомлення "Під'єднано до бази даних"
Додаткові умови:
Ім'я бази даних (input_database_name) вводиться користувачем з клавіатури;
Нове ім'я бази даних (new_database_name) вводиться користувачем з клавіатури;
Конструктор має лише два параметри: self та database_name;
Використовуйте запропоновані назви методів і класів.
Очікуваний результат виконання програми:

Для набору вхідних даних ("Користувачі", "Зарплата") – текст на екрані:
False
False
"Неможливо змінити значення connected_to_database за допомогою присвоєння. Використайте метод connect_to_database"
"Під'єднано до бази даних"
True
True
"Користувачі"
"ЗАРПЛАТА"
Для набору вхідних даних ("Зарплата", "Виробництво") – текст на екрані:
False
False
"Неможливо змінити значення connected_to_database за допомогою присвоєння. Використайте метод connect_to_database"
"Під'єднано до бази даних"
True
True
"Зарплата"
"ВИРОБНИЦТВО"
Увага!

Не змінюйте наведений стартовий код. Своє рішення набирайте під коментарем # your code goes here
Для позначення блоків коду використовуйте відступи в 4 пробіли.
Будьте уважні з вхідними даними.
Не використовуйте без нагальної потреби будь-які зайві символи в тексті, який ви виводите на екран - можуть виникати непередбачувані помилки під час автоматичної перевірки.
Стартовий код:

input_database_name = input("Введіть ім'я бази даних ")
new_database_name  = input("Введіть нове ім'я бази даних ")

class Database:
   # your code goes here

db = Database(input_database_name)
print(db._connected_to_database)
print(db.get_connected_to_database())
db.set_connected_to_database(True)

db.connect_to_database()
print(db._connected_to_database)
print(db.get_connected_to_database())

print(db.get_database_name())
db.set_database_name(new_database_name)
print(db.get_database_name())

Code Editor
1
input_database_name = input("Введіть ім'я бази даних ")
2
new_database_name  = input("Введіть нове ім'я бази даних ")
3
​
4
class Database:
5
   # your code goes here
6
​
7
​
8
db = Database(input_database_name)
9
print(db._connected_to_database)
10
print(db.get_connected_to_database())
11
db.set_connected_to_database(True)
12
​
13
db.connect_to_database()
14
print(db._connected_to_database)
15
print(db.get_connected_to_database())
16
​
17
print(db.get_database_name())
18
db.set_database_name(new_database_name)
19
print(db.get_database_name())
20'''
