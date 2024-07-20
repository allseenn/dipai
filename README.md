# Диплом

## Задачи 

1. Выбрать или добавить датасеты по экологии - сейчас в проекте их 20 штук (см. [Экологические датасеты](#Экологические-датасеты))
2. Определиться с какими временными рамками будем работать, в датасете exams.csv  информация за несколько лет, необходимо определится какие месяцы мы берем для расчета.
4. Делаем выборку по месяцу и учебному году из каждого экологического датасета. Необходимо написать функцию, которая будет добавлять в датасет exams.csv новые параметры (столбцы) по названию события, например выброс паров ртути или земляные работы или капитальный ремонт и т.д. предлагаю в этот столбец заносить сразу геоданные, их можно будет привести к другому виду.
5. Выбор стратегии по преобразованию геоданных, т.к. их несколько видов. Есть точки, есть полигоны, есть где-то ограничивающие рамки.
6. Создание алгоритма, который переведет данные в расстояние до ближайшего источника загрязнения.
7. Итоговая таблица (датасет) содержит имена школ, соотношение отличников к двоечникам или наоборот, т.к. у нас всего две оценки (менее 160 баллов и более 220). Координаты школы, и столбцы с расстоянием до загрязнения, на сегодняшний день их 20. т.е. с учетом вышеперечисленного будет около 21 параметр + 1 целевая переменная - это соотношение кол-ва двоечников к отличникам
8. Разбиение датасета exams.csv с экологическими данными на тестовый и обучающий
9. Подбор модели нейросети
10. Оценка качества модели
11. Два последних пункта 10 и 11 циклические, до достижения оптимального результата.
12. Выводы
13. Оформление дипломной работы
14. Сдача дипломного проекта

## Проделанная работа

### 20240620

- нашел описание стандарта geoData https://geojson.org/
- изменил функция get_dataset - принимает разные форматы и кодировку
- допилина функция fill_ecology
- добавлена функция get_geo_data - преобразует адрес в геоданные нужне клуч Яндекс.Геокодер, не путать с Яндекс.Организации
- добавлена функция get_geo_json - по ключу data.mos.ru позволяет получить датасет с геоинформацией
- расширена таблица экологических датасетов и вынесена в начало
- в таблицу экологических датасетов добавлены ссылки на датасеты в блокноте
- сменил заголовки датасетов и добавли ссылку возврата к таблице датасетов
- скорректировал ключевые слова и ключевые поля в таблице датасетов
- удалось решить проблему некоторых "красных" датасетов
- добавлено несколько cache*.json файлов - будет больше

### 20240619

- добавлена функция fill_ecology для создания единого экодатасета
- добавлен столбец в аналитическую таблицу, будет содержат ключевые слова для фильтрации

### 20240618

- Добавлен заголовок первого уровня - тема диплома в 01.ipynb
- Добавлен раздел ЭГЭ, сылка на закон и даты проведения на 2024 год
- Продуман механизм (функция) переноса данных из разрозненных экологических датасетов в единый


### 20240617

- анализ образцоев данных их экологических датасетов

### 20240616

- разделение на два блокното: 01.ipynb, 02.ipynb
- создана функция для полностью автоматической загрузки датасетов
- добавлены датасеты по стройкам
- откорректированны некоторые ссылки и текст в описаниях датасетов
- проведен первичный анализ данных в экологических датасетах
- составлена таблица экологических датасетов с полями, которые можно будет перенести в общий датасет ecology

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