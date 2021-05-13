<h2>Task description </h2>
Cпроектировать и разработать API для системы опросов пользователей.

Функционал для администратора системы:

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя
<h2> Run project </h2>
Clone repo by:

git clone https://github.com/davert0/SurveyApp.git

<h3> With Docker </h3>

Run the next commands to run docker and start the project:

    docker-compose build
    docker-compose up

Api documentation is under http://127.0.0.1:8000/swagger or http://127.0.0.1:8000/redoc

<h3> Without Docker </h3>
Set environment <br>
Under the project folder install the dependencies:

    $ source venv/bin/activate
    (venv)$ pip install -r requirements.txt
Requirements:

Python3
venv
pip
Create testing user
Running the next command, a form will be prompt to set user credentials for basic authentication:

    (venv) backend$ python createsuperuser
Run project
    (venv) backend$ python manage.py runserver
