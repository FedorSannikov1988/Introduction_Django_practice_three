#### Задание №1

- Изменяем задачу 8 из семинара 1 с выводом двух html страниц:
главной и о себе.
- Перенесите вёрстку в шаблоны.
- Представления должны пробрасывать полезную информацию в
шаблон через контекст.

#### Задание №2

- Доработаем задачу 1.
- Выделите общий код шаблонов и создайте родительский
шаблон base.html.
- Внесите правки в дочерние шаблоны.

#### Задание №3

- Доработаем задачу 7 из урока 1, где бросали монетку,
игральную кость и генерировали случайное число.
- Маршруты могут принимать целое число - количество
бросков.
- Представления создают список с результатами бросков и
передают его в контекст шаблона.
- Необходимо создать универсальный шаблон для вывода
результатов любого из трёх представлений.

#### Задание №4

- Доработаем задачи из прошлого семинара по созданию
моделей автора, статьи и комментария.
- Создайте шаблон для вывода всех статей автора в виде
списка заголовков.
- Если статья опубликована, заголовок должен быть
ссылкой на статью.
- Если не опубликована, без ссылки.
- Не забываем про код представления с запросом к базе
данных и маршруты.

#### Задание №5

- Доработаем задачу 4.
- Создай шаблон для вывода подробной информации о статье.
- Внесите изменения в views.py - создайте представление и в
urls.py - добавьте маршрут.
- Увеличивайте счётчик просмотра статьи на единицу при
каждом просмотре

#### Задание №6

- Измените шаблон для вывода заголовка и текста статьи, а
также всех комментариев к статье с указанием текста
комментария, автора комментария и даты обновления
комментария в хронологическом порядке.
- Если комментарий изменялся, дополнительно напишите 
“изменено”.
- Не забывайте про представление с запросом в БД и
маршруты. Проверьте, что они работают верно.

#### Задание №7

- Доработаем задачу 8 из прошлого семинара про клиентов,
товары и заказы.
- Создайте шаблон для вывода всех заказов клиента и
списком товаров внутри каждого заказа.
- Подготовьте необходимый маршрут и представление.
