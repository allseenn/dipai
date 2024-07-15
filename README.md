# Диплом

## Задачи 

1. Выборать добавить или убрать датасеты по экологии - сейчас в проекте их 20 штук (см. [Экологические датасеты](#Экологические-датасеты))


## Структура репы

Диплом  [https://github.com/allseenn/dipai/](https://github.com/allseenn/dipai/)

Приватная репа означает, что доступ к ней имеем только мы.

Репа помимо основной ветки имеет еще 3:

- slava
- dima
- alex

По хорошему каждый работает в своей ветке, по ходу, ее мерджим в main.

## Описание 

При наличии яндекс токенов, достаточно одного main.ipynb файла и проект сам скачает все датасеты, распакует их, заполнит геоданными, на выхлопе получаем exams.csv - это тот файл с которым можно работать, далее. Если токенов нет, то нужен еще файл geo_cache.json.

Наш блокнот по сути будет дипломом. Сейчас он потихоньку заполняется, потом из него можно будет легко сверстать pdf-ку. И диплом готов.  

На выхлопе у нас должен получится датасет на основе exams, в котором будет еще не один, а возможно несколько столбцов: ближайшее расстояние до загрязнения, количество загрязнений например, в радиусе километра, тип загрязнения. и т.д. 

Когда датасет будет готов, мы его по классике жанра делим на два - обучающий и тестовый. На обучающем тренируем нейронку. А потом скармливаем ей тест. Если она его успешно решает, например более 0.7 как на библиотеках говорили, то взаимосвязь с грязью есть. И чем выше этот показатель предсказания, тем больше эта связь.


Для полного доступа к порталу data.mos.ru регистрируемся и получаем api-ключ с помощью которого можно получать доступ к данным с помощью АПИ. 
Ключик прописываем в модуле tokens.py в переменную DATA_MOS_RU, не забываем этот модуль спрятать.
Так же, можно скачать данные с помощью веб-браузера в различных форматах, в том числе и CSV.


## Описание папок и файлов проекта

- [README.md](README.md)
- [main.ipynb](main.ipynb) - дипломная работа
- [requirements.txt](requirements.txt) - по многочисленным просьбам
- [geo_cache.json](geo_cache.json) - кэш запросов к яндексу
- [tokens.py] - символическая ссылка на токены, держим в надежном месте!


## Датасеты школа

###  data-2072-2024-04-15.csv

https://data.mos.ru/opendata/2072

Набор данных «Результаты ЕГЭ» позволяет получить информацию об общих результатах государственной итоговой аттестации по программам среднего общего образования (далее – ГИА-11) каждой образовательной организации города Москвы.

В наборе представлены данные:

- об административных округах, районах, полных наименованиях образовательных организаций;
- о периоде, за который сдавался единый государственный экзамен (далее – ЕГЭ);
- о количестве участников, набравших не менее 200 баллов за 3 экзамена;
- о количестве участников, набравших более 160 баллов за 3 экзамена.

Результаты планируется публиковать ежегодно, таким образом можно будет проследить динамику повышения качества образования в Москве.

###  data-2263-2024-07-08.csv

https://data.mos.ru/opendata/2263/

Набор данных содержит информацию об образовательных организациях города Москвы: адреса, контактные телефоны, местоположение на карте, адреса интернет-сайтов учреждений, а также информацию о доступности зданий для лиц с ограниченными возможностями.

## Экологические датасеты

###  1. data-2457-2024-05-03.csv

https://data.mos.ru/opendata/2457

Набор данных позволяет получить информацию о месте отбора проб атмосферного воздуха, дате проведения отбора, основных результатах исследования. Для удобства ориентирования предусмотрена возможность просмотра местоположения контрольной точки исследования атмосферного воздуха на карте города Москвы.

2. Датасет шума
3. Датасет загрязнения почвы
4. Датасет среднемесячного состояния воздуха
5. Датасет землянных работ
6. Датасет по капремонту
7. Датасет ремонтных работ ЖКХ
8. Датасет ремонта поликлиник
9. Датасет дорожных работ
10. Датасет благоустройства парков
11. Датасет благоустройства транспартной инфраструктуры
12. Датасет по благоустройству городских пространств
13. Датасет по благоустройству жилой застройки
14. Датасет по благоустройству улиц
15. Датасет по помойкам
16. Датасет промышленный предприятий
17. Датасет рынков
18. Датасет автовокзалов и автостанций
19. Датасет некачественных автозаправок
20. Датасет автозапровок