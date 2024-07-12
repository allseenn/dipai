# Диплом

Коллабораторы, приветствую на приватной репе дипломного проекта "Анализ влияния экологических факторов на результаты ЕГЭ в г.Москвы" на основе открытых данных с портала data.mos.ru"

Приватная репа означит, что доступ к ней имеют только приглашенные.

Для полного доступа к порталу data.mos.ru регаемся и получаем api-ключ с помощью которого можно получать доступ к данных с помощью АПИ. 
Ключик прописываем в модуле tokens.py в переменную DATA_MOS_RU, не забываем этот модуль спрятать.
Либо, можно скачать данные через вебинтерфейс в различных форматах, в том числе и CSV.

## Структура репы

Репа помимо основной ветки имеет еще 3:

- slava
- dima
- alex

По хорошему каждый работает в своей ветке, по ходу, ее мерджим в main.

## Описание директорий проекта

docs - содержит различную документацию, пока там лежат правила оформления дипломной работы
datasets.json - список имеющихся датасетов на портале data.mos.ru
datasets.py - скрипт для получения списка датасетов
