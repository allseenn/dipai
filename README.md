# Диплом

ТЕМА: Экологические факторы и результаты ЕГЭ в Москве.


## Задачи 

1. Выбрать или добавить датасеты по экологии - сейчас в проекте их более 20 штук (см. [Экологические датасеты](#Экологические-датасеты))
2. Определиться с какими временными рамками будем работать, в датасете exams.csv  информация за несколько лет, необходимо определится какие месяцы мы берем для расчета. Предварительно по закону об ЕГЭ с марта по сентябрь включительно.
4. Делаем выборку по месяцу и учебному году из каждого экологического датасета. Необходимо написать функцию, которая будет добавлять в датасет exams.csv новые параметры (столбцы) по названию события, например выброс паров ртути или земляные работы или капитальный ремонт и т.д. предлагаю в этот столбец заносить сразу геоданные, их можно будет привести к другому виду.
5. Выбор стратегии по преобразованию геоданных, т.к. их несколько видов. Есть точки, есть полигоны, есть где-то ограничивающие рамки. См. geojson.org
6. Подсчет расстояний до экологических геоданных до конкретной школы (в радиусе км). 
Расчет индекса совокупных факторов 1-(произведение расстояний переведенный в десятичную дробь)
Перевед расстояний в десятичную дробь: Если расстояние 800 метров, то десятичная запись -0.8, если 100 меторов, то  -0.1, чем ближе тем выше индекс уровень воздействия.
В случае нескольких однотипных фактров, то их модули перемножаются и вычитаются из единици.
Из примера выше 1-(0.8*0.1) = 0.9199999999999999. 
Если один из факторов произошел непосредственно в школе, то следовательно расстояние ноль и как итог:
1-(0*0.1*0.8) = 1 будет максимальный фактор единица. Например если в школе сверлят перфоратором, заниматься не возможно и это максимальный уровень, если же в школе одновременно еще и штробят стены, заниматся также не возможно не смотря что оба по отдельности имеют по 1, в итоге максимальная шкала останется 1. это позволяет нормализовать значания от -1 до 1, что рекомендуется в машинном обучении.
Но, выописанное относится к одной фиче (параметру) все фичи не суммируются, по нескольким причинам. Основная, мы хотим найти наиболее влиятельный параметр из 20-ти экологических факторов. Другая причина, мы точно не знаем в какие дни прошли занятия и в какие ремонт и т.д. Наша задача, найти взаимосвязь. Повлиял ли тот или иной фактор экологии на успеваемость
7. Итоговая таблица (датасет) содержит имена школ, соотношение отличников к двоечникам или наоборот, т.к. у нас всего две оценки (менее 160 баллов и более 220). Координаты школы, и столбцы с расстоянием до загрязнения, на сегодняшний день их 20. т.е. с учетом вышеперечисленного будет около 21 параметр + 1 целевая переменная - это соотношение кол-ва двоечников к отличникам
8. Разбиение датасета exams.csv с экологическими данными на тестовый и обучающий
9. Подбор модели нейросети
10. Оценка качества модели
11. Два последних пункта 10 и 11 циклические, до достижения оптимального результата.
12. Выводы
13. Оформление дипломной работы
14. Сдача дипломного проекта

## Проделанная работа

### 20240628

  - from_stroi - возможно самая большая функция в данной работе
  - взаимосвясь между датасетами buildgrounds и stroi

### 20240626

 - https://stroi.mos.ru/construction/6224   (2000 - 6899)
 ```
  <div class="map-widget"                                 data-polygon="[[[37.531442629112,55.81964686555],[37.531652009335,55.819678958265],[37.531746983115,55.819443203078],[37.531499548269,55.819421835107],[37.531442629112,55.81964686555]]]"                                  data-icon ="industrial"
                                data-point="37.531587420902,55.819545062916" >
                            </div>
 ```

### 20240625

- ecology - завершено формирование сводного экологического датасета, можно переходить к следующему этапу - создание 03.ipynb
- cache - реогранизован кэш
- рефакторинг почти всех функций 02.ipynb, необходимо сделать для 01.ipynb. Так реализуется эффективный кэш запросов к API.
- README.md - обновление

### 20240623

- добавлены и изменены вспомогательные функции
- live_area после 8 часов скрейпинга, все записи заполнены списками геоданных из maps.co, но в списках встречаются ключи словарей boundingbox: None, из-за неправильно внесенных адресов составителями датасетов, например: "Усачёва улица с Б/Н". Либо, не сокращенных ранее слов: владение, сооружение, земельный участок. 
- кэш maps.co сохранен. Нужно сократить слова из пункта выше и запустить сканирование повторно. Нужно создать функцию на основе short_address, в случае не успеха полный адрес чтоб проверялся яндексом.
- продуман алгоритм расчета индекса параметров, необходимо реализовать функцию


### 20240622

- найден способ поиска для live_area через openstreetmaps, для этого нужно адрес преобразовать в короткий формат
- short_address - функция преобразующая длинный адрес, приводит к виду "Москва улица Мира 3 к 1"
- обнаружено что графа ObjectAddress иногда содержит по несколько адресов, рефакторинг нескольких функций
- переделка фукнции to_geodata под универсальную, способную работать с разными геокодерами
- mos_co - функция реализующая АПИ к maps.co
- по предваретельным расчетам заполенение live_area займет несколько часов запросов с интервалом в 1 секунду.
- глабальный словарь cache - для аварийного завершения
- save_cache() - функция аварийного сброса дампа кэша в файл

### 20240621

- множественные изменения фунций и имен файлов
- победил почти все экологические датасеты, кроме одного live_area - самый большой (сотни тысяч записей)


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

## Структура репозитория

Диплом  [https://github.com/allseenn/dipai/](https://github.com/allseenn/dipai/)

Приватная репа означает, что доступ к ней имеем только мы.

Репа помимо основной ветки имеет еще 3:

- slava
- dima
- alex

По хорошему каждый работает в своей ветке, по ходу, ее мерджим в main.

## Файлы репозитория

- [sets](sets) - папка с датасетами
- [README.md](README.md) - этот файл
- [01.ipynb](01.ipynb) - обработка школ
- [02.ipynb](02.ipynb) - обработка экологии
- [requirements.txt](requirements.txt) - по многочисленным просьбам
- [cache.json](cache.gz) - кэш запросов к яндексу и maps.co
- [tokens.py] - символическая ссылка на токены, держим в надежном месте!

## Описание 

Задействовано 23 датасета с портала data.mos.ru, 21 из которых экологический.
1. Основная проблема заключается в том, что имеются разные форматы, в частности в датасете Школ не указаны ни их координаты, ни их адрес. Частично решена с помощью датасета со списком школ и их координат. Но, там указаны не все школы.
Найден один условно-бесплатный способ поиска геоданных по названию организации - через API Яндекса. В сутки дается 500 запросов бесплатно. Этот API отличается от Яндекс.Геокодера - позволяет находит координаты по адресу. Но, помним? ни адресов ни координат нет в инзачальном датасете по ЕГЭ. 
2. Вторая проблема: не во всех экологических датасетах указаны координаты. Но, почти во всех указаны адреса объектов. 
3. Третья проблема: Яндекс Геокодер предоставляет тысячу запросов в сутки бесплатно. Например только в одном датасете live_area около 200 тысяч записей. Но, есть бесплатные геокодоры типа OSM.
4. Четвертая проблема: Бесплатные геокодоры позволяют обращатся по апи с интервалом в одну секунду. 200 тысяч секунда на live_area.
5. Пятая проблема: Разный формат адресов в разных датасетах.

- В виде строки с указанием улицы и дома:

```
Ленинские Горы, дом 1, строение 27
```

- В виде строки с укзанием города, улицы и дома:

```
город Москва, Волгоградский проспект, дом 42
```

- В виде полноадресной строки:

```
Российская Федерация, город Москва, внутригородская территория муниципальный округ Даниловский, 1-й Кожуховский проезд, дом 15
```

- В виде объекта JSON с одним адресом:

```
[{'is_deleted': 0,
  'global_id': 3587,
  'Address': 'Российская Федерация, город Москва, внутригородская территория муниципальный округ Замоскворечье, Люсиновская улица, дом 8, строение 2',
  'UNOM': '2101811'}]
```

- В виде объекта JSON с нескольими адресами:

```
[{'is_deleted': 0, 'global_id': 1905133, 'Address': 'Российская Федерация, город Москва, внутригородская территория муниципальный округ Восточное Дегунино, Дубнинская улица, дом 2, корпус 1', 'UNOM': '7138'}, {'is_deleted': 0, 'global_id': 1905134, 'Address': 'Российская Федерация, город Москва, внутригородская территория муниципальный округ Восточное Дегунино, Дубнинская улица, дом 2, корпус 2', 'UNOM': '7139'}, {'is_deleted': 0, 'global_id': 1905135, 'Address': 'Российская Федерация, город Москва, внутригородская территория муниципальный округ Восточное Дегунино, Дубнинская улица, дом 2, корпус 4', 'UNOM': '7141'}, {'is_deleted': 0, 'global_id': 1905136, 'Address': 'Российская Федерация, город Москва, внутригородская территория муниципальный округ Восточное Дегунино, Дубнинская улица, дом 2, корпус 3', 'UNOM': '7140'}, {'is_deleted': 0, 'global_id': 1905137, 'Address': 'Российская Федерация, город Москва, внутригородская территория муниципальный округ Восточное Дегунино, Дубнинская улица, дом 2, корпус 5', 'UNOM': '7142'}]
```

6. Проблема шесть. Бесплатные геокодоры не понимают запросов ни в одном вышеперечисленном формате. Т.е. их нужно преобразовать к виду:

```
Москва Ленинские Горы 1 с 27
```

7. Проблема семь: не все адреса бесплатные геокодеры знают и возвращают с них координаты
8. Проблема восемь: разные форматы геоданных в итоговых датасетах exams и ecology. 

Все, кроме восьмой проблемы, практически решены. Восьмую предстоит решать.

185829 записей в экологическом датасете ecology необходимо состыковать с 4884 записей из датасета exams. 

Наш блокнот по сути будет дипломом. Сейчас он потихоньку заполняется, потом из него можно будет легко сверстать pdf-ку. И диплом готов.  

На выхлопе у нас должен получится датасет на основе exams, в котором будет еще не один, а возможно несколько столбцов: ближайшее расстояние до загрязнения, количество загрязнений например, в радиусе километра, тип загрязнения. и т.д. 

Когда датасет будет готов, мы его по классике жанра делим на два - обучающий и тестовый. На обучающем тренируем нейронку. А потом скармливаем ей тест. Если она его успешно решает, например более 0.7 как на библиотеках говорили, то взаимосвязь с грязью есть. И чем выше этот показатель предсказания, тем больше эта связь.

### Типы геоданных в датасетах

Точка (Point):

```
{"coordinates":[37.505049,55.523081],"type":"Point"}
```

или

```
{"type": "Point", "coordinates": [37.775102, 55.806463]}
```

Несколько точек (MultyPoint):

```
{"coordinates":[[37.58037861,55.825088698],[37.580234128,55.824253023],[37.579996
429,55.824365685],[37.58015831,55.82440844],[37.580110955,55.824520978],[37.579997166,55.824724637],[37.579883299,55.824890793],[37.581054021,55.824932887],[37.580624454,55.8243117
],[37.580910526,55.824579387],[37.580834711,55.824734804],[37.580720825,55.824890246],[37.580606916,55.825034973],[37.580558908,55.82483142],[37.580520562,55.824697508]],"type":"MultiPoint"}
```

Рамка (boundingbox):


```
{"boundingbox":["55.6519879","55.6522925","37.7501636","37.7505766"]}
```

Ломанная линия (MultiLineString):

```
{"coordinates":[[[37.636096932,55.872757589],[37.635454436,55.872703212],[37.6355
08176,55.872504232],[37.635426154,55.87239721],[37.635479989,55.872225772],[37.636496897,55.871949219],[37.636534859,55.871909392],[37.636565665,55.871912656],[37.636618858,55.8717
73],[37.636961989,55.871799406],[37.636965382,55.87191735],[37.636966046,55.871936853],[37.637545107,55.871988443],[37.637528583,55.872031321],[37.636779133,55.871962677],[37.63675
6362,55.871974816],[37.63655118,55.871950683],[37.636543324,55.871971309],[37.635829634,55.872250687],[37.635687305,55.872686137],[37.635521575,55.872670514],[37.635560958,55.87248
698],[37.635501808,55.872382798],[37.635551735,55.872248253],[37.63655118,55.871950683],[37.636565665,55.871912656],[37.636763557,55.871933621]],[[37.636285173,55.872742567],[37.63
5687305,55.872686137],[37.636119945,55.872726918]],[[37.636215263,55.872847282],[37.636081819,55.872836715],[37.636110022,55.872726856],[37.636253004,55.872740091],[37.636220028,55
.872847277]],[[37.636767681,55.871944891],[37.636756362,55.871974816],[37.636693534,55.87200831],[37.636608799,55.872300385],[37.636453179,55.87275862],[37.63629113,55.872742728]]]
,"type":"MultiLineString"}
```

Мултиполигон (MultiPolygon):

```
{'coordinates': [[[[37.710083127, 55.825085846], [37.709884644, 55.825088859], [37.70991683, 55.825557425], [37.710107267, 55.825552906], [37.710083127, 55.825085846]]], [[[37.710971466, 55.824666254], [37.710390321, 55.824675741], [37.710401249, 55.824826407], [37.710980407, 55.824816363], [37.710971466, 55.824666254]]], [[[37.710757032, 55.82506651], [37.710557953, 55.825070528], [37.710585371, 55.825566047], [37.710780874, 55.825561359], [37.710757032, 55.82506651]]], [[[37.707049481, 55.825154524], [37.707242202, 55.825149502], [37.707241209, 55.825030085], [37.70704054, 55.82503176], [37.707049481, 55.825154524]]], [[[37.710930347, 55.825726055], [37.711380243, 55.825718823], [37.711373091, 55.825557312], [37.711369514, 55.825539635], [37.710924625, 55.825550081], [37.710924625, 55.825570973], [37.710930347, 55.825726055]]], [[[37.583026114, 55.832647996], [37.582666499, 55.832611174], [37.582629743, 55.832706019], [37.582630736, 55.832758463], [37.58344732, 55.83284717], [37.583486063, 55.832741167], [37.583481096, 55.83270044], [37.583129428, 55.832659155], [37.583156251, 55.832582163], [37.584034426, 55.832677566], [37.584082109, 55.83255092], [37.584084096, 55.832518561], [37.583018166, 55.832398051], [37.582968496, 55.832531393], [37.582976443, 55.832562078], [37.583054923, 55.832573236], [37.583026114, 55.832647996]]], [[[37.709097862, 55.825586152], [37.70911789, 55.825928458], [37.70928669, 55.825930065], [37.709272385, 55.825774179], [37.70981884, 55.825766144], [37.709795952, 55.825566867], [37.709097862, 55.825586152]]]], 'type': 'MultiPolygon'}
```

Геометрическая коллекция (GeometryCollection), может включать все вышеперечисленные типы в одном наборе:

```
{"geometries":[{"coordinates":[[[37.506825543,55.685344001],[37.506928632,55.6855
10346],[37.507208483,55.686142464],[37.507031932,55.686841148],[37.506516704,55.687365182],[37.505898373,55.687739503],[37.505309432,55.687781118],[37.504926623,55.68783104],[37.50
4823565,55.687897584],[37.504722591,55.687800154],[37.504604802,55.687804911],[37.504318751,55.687890474],[37.504209387,55.687999794],[37.504184152,55.688056829],[37.504200993,55.6
88180404],[37.504091615,55.688170902],[37.503940157,55.688047332],[37.503822355,55.687928514],[37.503704562,55.687895247],[37.503494223,55.687895253],[37.503258638,55.68782872],[37
.503115606,55.687814465],[37.503073531,55.687719408],[37.503048282,55.687610092],[37.502821107,55.687467511],[37.502661247,55.687410481],[37.50239202,55.687458015],[37.502408852,55
.687543567],[37.502248995,55.687534064],[37.502139623,55.687591101],[37.502072321,55.687690912],[37.501575927,55.687771719],[37.501289868,55.687795487],[37.501146839,55.687843017],
[37.500852367,55.687914313],[37.500339139,55.687852528],[37.500154041,55.687852529],[37.499960529,55.687952339],[37.4996324,55.687961845],[37.499405236,55.687838269],[37.49917807,5
5.687838268],[37.498892003,55.688061651],[37.498908826,55.688213744],[37.498833103,55.688237507],[37.49865642,55.688123437],[37.49834512,55.688061645],[37.498185265,55.688009361],[
37.497705702,55.687819238],[37.497419651,55.687662388],[37.497285029,55.687757443],[37.498084299,55.688080653],[37.498479732,55.688208986],[37.498799447,55.688313553],[37.498959305
,55.688337319],[37.499068685,55.688208992],[37.499060273,55.688147204],[37.499043446,55.68812344],[37.499211721,55.68799036],[37.499295858,55.687933326],[37.499531437,55.688042644]
,[37.500027838,55.688037891],[37.500179282,55.68801888],[37.500229764,55.687966598],[37.50057472,55.687990361],[37.500978573,55.688018875],[37.50142449,55.687933319],[37.501466556,
55.687900048],[37.501786274,55.687966584],[37.502249013,55.687833496],[37.502291075,55.687733684],[37.502274242,55.687638627],[37.502392032,55.687652883],[37.502543471,55.687600598
],[37.502585532,55.68750554],[37.502947327,55.687705153],[37.50297258,55.687861997],[37.503208163,55.687904767],[37.503325954,55.687919022],[37.503628849,55.68799506],[37.503704572
,55.68799981],[37.503898105,55.688204178],[37.504100037,55.688256453],[37.504251488,55.688303977],[37.504369262,55.688156633],[37.504335599,55.688075836],[37.504461791,55.687971268
],[37.504621642,55.687914227],[37.504840398,55.687942736],[37.505160102,55.687857171],[37.505496642,55.687842897],[37.505908896,55.68778109],[37.506169691,55.687624232],[37.5067080
97,55.687291502],[37.506952033,55.686992057],[37.507170729,55.686716377],[37.507221161,55.686459718],[37.507263166,55.686131766],[37.507178997,55.685927397],[37.507094829,55.685727
781],[37.506918095,55.685395089],[37.506876016,55.685319046],[37.506825542,55.68533806]]],"type":"MultiLineString"},{"coordinates":[[[37.501735789,55.68787628],[37.5020555,55.68780
4982],[37.502005015,55.687738442],[37.501651651,55.687819247],[37.501735789,55.68787628]]],"type":"Polygon"}],"type":"GeometryCollection"}
```


## Глоссарий

**Машинное обучение** — дисциплина, заключающаяся в извлечении знаний из известных данных. Это раздел математики, поэтому в нём мы будем, помимо всего прочего, работать с формулами.

**Объект**  — то, для чего надо сделать предсказание. Экологических фактор (шум, выброс, выхлоп, утечка и т.д). Объекты обозначаются буквой 𝑥. Множество всех объектов, для которых могут потребоваться предсказания, называется пространством объектов и обозначается 𝕏.

**Признак** — это некая числовая характеристика объекта. Совокупность всех признаков объекта 𝑥=(𝑥1,𝑥2,...,𝑥𝑑) называется его признаковым описанием. Оно считается 𝑑-мерным вектором, то есть к нему можно применять все операции, описанные линейной алгеброй.

**Ответ** (целевая переменная) — то, что надо предсказать. Успеваемость как соотношение Результаты ЕГЭ. Ответы обозначаются буквой 𝑦. 

**Обучения с учителем** - контролироемое обучение (supervised learning). Такой метод заключается в восстановлении общей закономерности по конечному числу известных примеров.

**Обучающая выборка** - это примеры, на основе которых мы планируем строить общую закономерность. Она обозначается $X$ и состоит из $l$ пар объектов $x_{i}$ и известных ответов $y_{i}$:

$$X = (x^{i}, y_{i})^l_{i=1}.$$

**Модель (алгоритм) предсказания** - функция, отображающая пространство объектов $\mathbb{X}$ в пространство ответов $\mathbb{Y}$, помогающая нам делать предсказания, обозначается $a(x)$. Она принимает на вход объект и выдаёт ответ.

$$a(x) = sign(w_{0} + w_{1}x^{1}+w_{2}x^{2}+...+w_{d}x^{d}).$$

**Функция потерь** (функционал ошибки loss function) $Q(a, X)$ - используется для подбора подходящей модели предсказаний. Она принимает на вход модель и выборку и сообщает, насколько хорошо модель работает на указанной выборке. Задача обучения заключается в подборе такой модели, при которой функция потерь минимальна $Q(a, X)\rightarrow min.$

**Семейство моделей (алгоритмов)** $\mathbb{A}$ - это алгоритмы среди которых выбирают наилучший для достижения минимума функции потерь

**Модели семейства линейной регрессии** — это такие модели, которые сводятся к суммированию значений признаков с некоторыми весами:

$$a(x) = w_{0}+\sum^{d}_{i=1}w_{i}x^{i}.$$

### Статьи

#### Шум

[Источник](https://studfile.net/preview/7458361/page:7/#:~:text=%D0%95%D1%81%D0%BB%D0%B8%20%D1%80%D0%B0%D1%81%D1%81%D0%BC%D0%B0%D1%82%D1%80%D0%B8%D0%B2%D0%B0%D1%82%D1%8C%20%D1%88%D1%83%D0%BC%20%D0%BA%D0%B0%D0%BA%20%D1%8D%D0%BA%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9,%D1%88%D1%83%D0%BC%D0%B0%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%BF%D1%80%D0%B5%D0%B2%D1%8B%D1%88%D0%B0%D0%B5%D1%82%20%D1%81%D0%B0%D0%BD%D0%B8%D1%82%D0%B0%D1%80%D0%BD%D1%8B%D0%B5%20%D0%BD%D0%BE%D1%80%D0%BC%D1%8B)

Шум как экологический фактор.
Если рассматривать шум как экологический фактор, то он является одним из существенных загрязнителей окружающей среды в городах, оказывающих весьма неблагоприятное влияние на здоровье и трудоспособность человека. Источниками шума являются промышленные предприятия, средства наземного и воздушного транспорта, внутриквартальные и каммуникационные каммунально-бытовые источники уровни шума значительно превышает санитарные нормы. Особенно высокие шумовые нагрузки создает воздушный транспорт.

Воздействие шума на организм человека:

Воздействие шума: изменение конформации белков и вследствие этого замедление кровотока, дополнительная нагрузка на сердце.

На слух: снижение слуха.

На ЦНС: головная боль тупого характера, чувство тяжести и шума в голове, возникающие к концу рабочей смены или после работы, головокружение при перемене положения тела, повышенная раздражительность, быстрая утомляемость, снижение трудоспособности, внимания, повышенная потливость, особенно при волнениях, нарушение ритма сна.

Инфразвук: Возникающие под действием инфразвука, нервные импульсы нарушают согласную работу нервной системы. При колебании средней интенсивности может расстроиться пищеварение, сердечнососудистая и дыхательная система, нарушиться психика с самыми неожиданными последствиями Ультразвук влияет на человеческий организм гораздо менее существенней.

Насекомое во время полета так быстро ударяет крыльями, что производит последовательность небольших пульсаций воздуха и эти пульсации соединяются в музыкальный тон.

Голос моря инфразвуковые волны, возникающие над поверхностью моря при сильном ветре в результате вихреобразования за гребнями волн.

Растения близ аэродромов, с которых непрерывно стартуют реактивные самолеты, испытывают угнетение роста и даже отмечается исчезновение отдельных видов

https://ru.wikipedia.org/wiki/%D0%A8%D1%83%D0%BC%D0%BE%D0%B2%D0%BE%D0%B5_%D0%B7%D0%B0%D0%B3%D1%80%D1%8F%D0%B7%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5

https://top-technologies.ru/ru/article/view?id=21717
