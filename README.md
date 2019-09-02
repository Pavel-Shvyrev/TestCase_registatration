# python_test

Запуск теста:
--------------------------

Для запуска теста требуется установленый пакет Python 3.6.4, пакет virtualenv не ниже версии 16.7.4  
Директорию содержащую тестовый проект рекомендуется переместить в корень диска "С".  
Таким образом путь до директории проекта `C:\python_test\`  

1. Запустить коммандную строку либо терминал linux перейти в директорию `\python_test`  
    `cd C:\python_test\`
2. Загрузить виртуальное окружение python  
    `env\Scripts\activate`
3. Перейти в под-директорию `\test`  
    `cd test`
4. При необходимости установить необходимые зависимости  
    `pip install selenium`  
    `pip install pytest`  
    `pip install string`  
    `pip install random`
5. Запустить тест, при необходимости указать путь до директории содержащей gecodriver, при помощи ключа `--browser_dir` (значение по умолчанию: `C:\python_test\geckodriver-v0.24.0-win64\geckodriver.exe`)  
    `py.test --browser_dir=C:\python_test\geckodriver-v0.24.0-win64\geckodriver.exe test_registration_user.py`  
    
    Если директория проекта рекомендуемая (`C:\python_test\`) то можно запустить тест без аргументов:  
    `py.test test_registration_user.py`  
    
***
Описание проекта:
----------------
Тест выполняет проверку сценария регистрации пользователя с последующим входом в систему под зарегистрированной учетной записью, после чего происходит выход из системы. Реализована проверка наличия и соответствия текста сообщения об успешной регистрации. Реализован механизм проверки наличия сообщения-предупреждения о невозможности регистрации пользователя с таким email в виду того что он уже зарегистрирован в системе. В этом случае тест пропускается 

Реализовано итеративная модель запуска теста. По умолчанию сценарий тест прогоняется три раза.
Тест параметризован - реализован генератор случайных значений регистрируемого пользователя для каждого прогона теста (файл ...`\python_test\model\user_generator.py`).
Количество "прогонов" теста так же можно изменить, изменив значение числа `range(3)`. Строка 30, файл `\python_test\model\user_generator.py` 
***   

Описание структуры проекта:
--------------------------
<strong>Файл test_registration_user.py</strong> (path: `\python_test\test\test_registration_user.py`)
Содержит сам сценарий теста

<strong>Файл conftest.py</strong> (path: `\python_test\conftest.py` )
В нем описана фикстура - она хранит путь до файла geckodriver.exe . Контролирует запуск и остановку драйвера в начале и конце теста 

<strong>Файл controller.py</strong> (path: `\python_test\fixture\controller.py`)
Содержит класс Controller, который в свою очередь инициализирует драйвер. В нем реализованы  методы  открытия стартовой страницы, а также настроек браузера
Передает инициализированный драйвер в классы RegistrationHelper, SessionHelper

<strong>Файл registration.py</strong> (path: `\python_test\fixture\registration.py`)
Содержит класс RegistrationHelper. В нем реализованы методы помощники для регистрации пользователя, отвечающие за взаимодействие теста со страницей регистрации 

<strong>Файл session.py</strong> (path: `\python_test\fixture\registration.py`)
Содержит класс SessionHelper. В нем реализованы методы помощники для входа и выхода из системы, отвечающие за взаимодействие теста со страницей логина и личным кабинетом 

<strong>Файл user.py</strong> (path: `\python_test\model\user.py`)
Содержит класс User который реализует пользователя системы 

<strong> Файл user.py </strong> (path: `\python_test\model\user.py`)
Содержит методы для реализации генератора случайных значений регистрируемого пользователя
***

Зависимости проекта:
------------------

        Package            Version
        ------------------ -------
        Python             3.6.4
        pytest             5.1.1
        selenium           3.141.0
        virtualenv         16.7.4
        atomicwrites       1.3.0
        attrs              19.1.0
        colorama           0.4.1
        importlib-metadata 0.19
        more-itertools     7.2.0
        packaging          19.1
        pip                19.2.3
        pluggy             0.12.0
        py                 1.8.0
        pyparsing          2.4.2
        setuptools         41.2.0
        six                1.12.0
        urllib3            1.25.3
        wcwidth            0.1.7
        wheel              0.33.6
        zipp               0.6.0
