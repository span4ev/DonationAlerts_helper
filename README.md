# DonationAlerts_helper

Этот скрипт предназначен для суммирования донатов от пользователей, подсчёта общей суммы донатов, вывода полной информации о донатах. Подробнее ниже. 

Скрипт выполняет 2 функции:

### Опция 1
- Читает файл `donations.txt`.
- Подсчитывает все донаты от одних и тех же пользователей и суммирует их
- Сортирует донаты по пяти разным категориям.
- Выводит все или установленное вами кол-во строк с донатами (по желанию).
- Выводит донаты выше установленной вами минимальной суммы (по желанию).
- Подсчитывает сумму всех донатов в отдельной строке.
- Добавляет (по желанию) ключевое слово после суммы донатов (например - валюту)

> Есть нюанс:
Скрипт чувствителен к регистру в никнеймах, так что для него span4ev, Span4ev, spaN4ev - разные люди.
Например в случае со Span4ev и span4ev - донаты не будут просуммированы. 
Это обусловлено тем, что нельзя предугадать какой из ников будет истинно верным (оригинальным). К тому же не исключено, что span4ev и Span4ev (как пример) - действительно разные люди, т.к. указанный никнейм при отправке доната не является уникальным (как ник на твиче) и можно указать абсолютно любое имя, даже чужой никнейм.


### Опция 2. 
Читает HTML файл со всеми донатами (то же, что и окно в `OBS` со всеми донатами с `DA`) и сохраняет в файл всю имеющуюся информацию:
- Имя отправителя
- Сумма доната
- Покрытие комиссии (символ ♥)
- Сообщение с донатом (если есть)
- Названия видео (если есть), если включена опция "прикрепить видеоролик к сообщению"
- Ссылка на видео (если есть), если включена опция "прикрепить видеоролик к сообщению"
- Прошедшее время с отправки доната (по желанию)


> Учтите, что скрипт находится в стадии тестирования. Из-за отсутствия получения опыта всех возможных донатов, стикеров к сообщению и прочего возможного - скрипт не умеет с этим работать и могут возникнуть непредвиденные результаты или конечный файл не будет создан. Чтобы обрабатывать такие обстоятельства я должен с ними столкнуться или получить чужой файл с донатами, в котором есть новые условия, которые нужно обрабатывать.
На всякий случай сообщаю, что скрипт не собирает никаких данных, так что если у вас возникли ошибки или образовалась какая-то нестандартная ситуация, вы можете со мной связаться и объяснить что пошло не так.



### Опция 1
Для этой опции вам понадобится файл с вашими донатами с сайта [Donation Alerts](https://www.donationalerts.com/dashboard).
Для того чтобы получить этот файл, перейдите на эту страницу [Donation Alerts](https://www.donationalerts.com/dashboard/activity-feed/donations) или выберите в боковом меню пункт `Последние сообщения`. 
Далее - `Экспорт`. 
При экспорте выберите формат `.txt HTML список`.
Поместите скачанный файл `donations.txt` в папку проекта и запустите исполняемый файл `DonationAlerts_helper.exe`.

При выборе этой опции в папке проекта будет создан файл `_DONATION_SUMMATION_RESULT_.txt`

Пример результата:
```sh
    НеПалатка - 20 ₽ 
    Это я - 100 ₽ 
    Rosie from America - 60 ₽ 
    Аноним - 40 ₽ 

    Общая сумма - 220 ₽
```


### Опция 2

Для этой опции вам понадобится `HTML` файл с вашими донатами. Как правило, файл называется `Last alerts - DonationAlerts.html`. Если название или расширение будет отличаться - вы скачали не тот файл или не тем образом и скрипт не выполнит свою работу.

Получить этот файл очень просто и пусть вас не смущает перечень действий:

- Откройте `OBS`.
- Включите отображение окна с донатами, если оно не включено. Отобразить окно можно через Док-панели.
- Нажмите ПКМ по окну с донатами и выберите `Копировать текущий адрес`. Адрес будет выглядеть примерно так:
   `https://www.donationalerts.com/widget/lastdonations?alert_type=1,4,13,15,11,16,14,2,3,5,12&limit=50&token=ВАШ_ТОКЕН`
- Вставьте скопированную в буфер обмена ссылку в любой браузер и перейдите по ней. Во вкладке браузера откроется такое же окно с донатами, как в `OBS`.
- Нажмите ПКМ в любом месте страницы (или `CTRL+S`) и обязательно сохраните `HTML` в том виде, который предлагает браузер по умолчанию, то есть `Веб-страница полностью (*.htm;*.html)`. Другие варианты работать не будут из-за специфики разметки. 
Вместе с `HTML` файлом скачается папка, её можно сразу же удалять. 
- Поместите скачанный `HTML` файл в папку проекта. Если вы перенеслив папку проекта `HTML` файл вместе с одноимённой папкой, скрипт сам её удалит.

Обратите внимание, что сохранять файл нужно именно как `Веб-страница полностью (*.htm;*.html)` - то есть вариант по умолчанию, а не `Веб-страница, только HTML (*.html;*.htm)` или `Веб-страница, один файл (*.mhtml)`

(Необходимо подключение к интернету, т.к. информация о донатах подгружается с сайта DA динамически)


При выборе этой опции, в папке проекта будет создан файл `_FULL_DOTATIONS_INFO_.txt`

Пример результата:

```sh
(19 минут назад)
Mike : 50 RUB
«Miyagi & Andy Panda - Там Ревели Горы (Mood Video)»
https://www.youtube.com/watch?v=MzI_CIYSsfQ
```

```sh
(10 дней назад)
Rosie from America : 150 RUB ♥ 
— Не дал, но мог дать. Как не хэдшот?!
«Rag'n'Bone Man - Human (Official Video)»
https://www.youtube.com/watch?v=L3wKzyIN1yk
```

### Содержимое папки проекта

- `__main__.py` - Скрипт для запуска
- `class.ui` - Файл `PyQt5 Designer`
- `config.txt` - Файл конфигурации, в который скрипт записывает текущие настройки
- `da.py` - Основной скрипт
- `DonationAlerts_helper.exe` - Исполняемый файл скрипта
- `README.md` - Ридми файл
- `widget.py` - Виджет `PyQt5`
- `generate_test_donates.py` - файл для генерации тестового файла с донатами типа `donations.txt`. Нужен исключительно для тестов. Через графический интерфейс не запускается, только как скрипт Python, через IDE или CMD. Если вам это не нужно, можете удалить этот файл.

### Запуск скрипта

После того как вы поместили в папку проекта скачанные файлы, запустите исполняемый файл `DonationAlerts_helper.exe`. Откроется окно с графическим интерфейсом, в котором вы можете выбрать действия скрипта и различные настройки. После нажатия кнопки `OK` скрипт запустится, выполнит выбранную вами функцию, создаст текстовый файл (в зависимости от выбранной опции) и окно автоматически закроется. Скрипт может выполнять только 1 функцию за раз: либо подсчёт донатов, либо вывод полной информации. Если вам нужно создать файл с суммированными донатами и файл с информацией о донатах, запустите скрипт дважды.  
Вы можете запускать `DonationAlerts_helper.exe` любое кол-во раз. При каждом запуске создаваемые скриптом файлы и файл `config.txt` будут перезаписываться.

Теперь вы можете открыть файл `_DONATION_SUMMATION_RESULT_.txt` или `_FULL_DOTATIONS_INFO_.txt` и скопировать оттуда данные.

> В папке присутствуют все скрипты, на основе которых был скомпилирован `.exe` файл - если вы хотите изучить скрипты или скомпилировать собственный экзешник. Функционал экзешника и `Python` скриптов - индетичен. Исполняемый файл нужен для людей, у которых не установлен `Python`.


#### Файл `config.txt`

В этот файл сохраняются текущие выбранные настройки и используются для установления значений при открытии виджета.
При желании, вы можете менять настройки напрямую в этом файле. 
При выборе нестандартных значений в файле `config.txt` после знака равно, будут использованы значения по умолчанию из атрибута `default_settings` класса `App` в файле `widget.py`. 

##### Установленные настройки по умолчанию:
- Включена опция "Подсчёт общей суммы всех донатов"
- Все донаты от каждого донатера суммируются - это неизменно.
- Донаты сортируются по большей сумме.
- После суммы указан символ рубля
- Выводятся все строки с донатами
- Включена генерация строки с общей суммой всех донатов
- Отключена информации о времени доната 

### Настройки окна графического интерфейса:
##### Функция скрипта
1. Подсчёт общей суммы всех донатов
2. Вывод полной информации о донатах

Информация об этом указана выше. 

##### Метод сортировки

Варианты на выбор:
```sh
    0 - Сортировка по умолчанию
    1 - Сортировка по умолчанию (инвертированная)
    2 - Сортировка по большей сумме
    3 - Сортировка по меньшей сумме
    4 - Сортировка по алфавиту
```

> Если у вас есть предложения о том, какие можно добавить методы сортировки, дайте мне знать.

Для примера возьмём вот такой список донатов, указанных в порядке поступления:
```sh
    Аноним - 10
    Аноним - 10
    Это я - 100
    Rosie from America - 15
    Rosie from America - 15
    НеПалатка - 20
    Rosie from America - 15
    Аноним - 10
    Rosie from America - 15
    Аноним - 10
 ```


##### 1 - Сортировка по умолчанию - в порядке получения доната.
Результат:
 ```sh
    Аноним - 40  
    Rosie from America - 60  
    Это я - 100  
    НеПалатка - 20
 ```

##### 2 - Сортировка по умолчанию - в порядке получения доната (то же, что и 1, но инвертированная)
Результат:
```sh
    НеПалатка - 20  
    Это я - 100  
    Rosie from America - 60  
    Аноним - 40  
 ```

##### 3 - Сортировка по большей сумме
Результат:
```sh
    Это я - 100  
    Rosie from America - 60  
    Аноним - 40  
    НеПалатка - 20  
 ```
 
##### 4 - Сортировка по меньшей сумме
Результат:
```sh
    НеПалатка - 20  
    Аноним - 40  
    Rosie from America - 60  
    Это я - 100  
 ```

##### 5 - Сортировка по алфавиту
Результат:
```sh
    Rosie from America - 60  
    Аноним - 40  
    НеПалатка - 20  
    Это я - 100  
 ```
 
##### Строка в конце списка с общей суммой всех донатов
В последней строке будет указана общая сумма всех имеющихся в файле `donations.txt` донатов.
Доступны два варианта: Вкл и Выкл.

Результат:
```sh
    НеПалатка - 20 ₽ 
    Это я - 100 ₽ 
    Rosie from America - 60 ₽ 
    Аноним - 40 ₽ 

    Общая сумма - 220 ₽
```

##### Показывать, когда пришёл донат
(Опция только для вывода полной информации о донатах с помощью опции №2)

В верхней строке будет указано, когда пришёл донат. Пример:
```sh
(19 минут назад)
Mike : 50 RUB
«Miyagi & Andy Panda - Там Ревели Горы (Mood Video)»
https://www.youtube.com/watch?v=MzI_CIYSsfQ
```

```sh
(10 дней назад)
Rosie from America : 150 RUB ♥ 
— Не дал, но мог дать. Как не хэдшот?!
«Rag'n'Bone Man - Human (Official Video)»
https://www.youtube.com/watch?v=L3wKzyIN1yk
```


#### Минимальная сумма доната для вывода:
Укажите минимальную сумму, от которой нужно выводить донаты либо в поле для ввода текста, либо с помощью ползунка.
Укажите `0` в поле для ввода, чтобы не указывать ограничение по минимальной сумме

#### Кол-во строк с донатами, которые нужно выводить:
Укажите кол-во строк с донатами, которые нужно выводить либо в поле для ввода текста, либо с помощью ползунка.
Укажите `0` в поле для ввода, чтобы выводить все строки

#### Подставить ключевое слово после суммы доната
(по умолчанию указан символ рубля - "₽")

Для того чтобы указать любое другое слово/символ, укажите его в соответствующем поле без кавычек. Или оставьте поле пустым, чтобы ничего не указывать после суммы доната.

#### Кнопки:
- `ОК` - применяет текущие настройки? запускает скрипт и закрывает окно интерфейса. Так же записывает выбранные настройки в файл `config.txt`
- `Cancel` - закрывает окно без применения изменений.
- `RESET` - сбрасывает все настройки на установленные по умолчанию и записывает их в файл `config.txt`


### Важно! 
Есть одна функция о которой следует упомянуть на случай, чтобы никого не смутило поведение скрипта.
Если у вас есть несколько файлов `donations.txt` или `Last alerts - DonationAlerts.html` в папке проекта - скрипт будет использовать файл с последней датой создания, остальные удалять. 


Представим, что вы хотите использовать свежий файл `donations.txt` или `Last alerts - DonationAlerts.html`, но в папке сохранения у вас уже есть файл с таким именем.
В таком случае новому файлу будет присвоено имя, например - `donations (1).txt`. 
Чтобы вам не пришлось каждый раз переименовывать такие файлы в `donations.txt` или `Last alerts - DonationAlerts.html`, скрипт сделает это автоматически.

Как это происходит:
- скрипт ищет в папке проекта все файлы с упоминанием нужных имён файлов в названии и с нужным расширением. 
- Далее среди всех таких файлов находит файл с последней датой создания.
- Затем удаляет все остальные файлы (более старые).
- Переименовывает самый свежий файл в `donations.txt` или в `Last alerts - DonationAlerts.html`.
- В случае с `Last alerts - DonationAlerts.html` скрипт так же удаляет папку `Last alerts - DonationAlerts`.


Таким образом, не важно сколько у вас будет файлов с упоминанием (для примера) `donations` в названии: `donations (1).txt`, `donations (2).txt`, `donations - (копия).txt`, `donations_1.txt`и т.п., в папке проекта на момент запуска скрипта - он всё равно будет использовать самый свежий, а остальные удалит.
Удаление происходит для того, чтобы не захламлять папку проекта старыми копиями файлов с неактуальной информацией. 

Функция сделана исключительно для удобства и вам не обязательно вникать в то, как это работает. Просто учтите, что старые файлы с донатами будут удалены. Если они по какой-то причине вам необходимы, их следует сохранять вне папки проекта.


### Запуск `generate_test_donates.py`

Генерирует файл `_random_donates_example_.txt` такого же типа, как и файл `donations.txt` для теста.
Для использования сгенерированного файла для подсчёта суммы донатов, переименуйте файл `_random_donates_example_.txt` в `donations.txt`. Автоматического переименования не происходит, чтобы не перезаписывать ваш файл с донатами.


