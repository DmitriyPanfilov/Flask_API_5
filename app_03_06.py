"""
Задание No3
📌 Создать API для добавления нового пользователя в базу данных. Приложение должно иметь возможность принимать POST запросы с данными нового пользователя и сохранять их в базу данных.
📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
📌 Создайте класс User с полями id, name, email и password.
📌 Создайте список users для хранения пользователей.
📌 Создайте маршрут для добавления нового пользователя (метод POST).
📌 Реализуйте валидацию данных запроса и ответа.

Задание No4
📌 Создать API для обновления информации о пользователе в базе данных. Приложение должно иметь возможность принимать PUT запросы с данными пользователей и обновлять их в базе данных.
📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
📌 Создайте класс User с полями id, name, email и password.
📌 Создайте список users для хранения пользователей.
📌 Создайте маршрут для обновления информации о пользователе (метод PUT).
📌 Реализуйте валидацию данных запроса и ответа.

Задание No5
📌 Создать API для удаления информации о пользователе из базы данных. Приложение должно иметь возможность принимать DELETE запросы и удалять информацию о пользователе из базы данных.
📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
📌 Создайте класс User с полями id, name, email и password.
📌 Создайте список users для хранения пользователей.
📌 Создайте маршрут для удаления информации о пользователе (метод DELETE).
📌 Реализуйте проверку наличия пользователя в списке и удаление его из списка.

Задание No6
📌 Создать веб-страницу для отображения списка пользователей. Приложение должно использовать шаблонизатор Jinja для динамического формирования HTML страницы.
📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
📌 Создайте класс User с полями id, name, email и password.
📌 Создайте список users для хранения пользователей.
📌 Создайте HTML шаблон для отображения списка пользователей. Шаблон должен содержать заголовок страницы, таблицу со списком пользователей и кнопку для добавления нового пользователя.
📌 Создайте маршрут для отображения списка пользователей (метод GET).
📌 Реализуйте вывод списка пользователей через шаблонизатор Jinja.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from fastapi.templating import Jinja2Templates


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
templates = Jinja2Templates(directory="seminar_5/DZ/templates")
app = FastAPI()


users = []


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


@app.get("/users/")
async def read_tasks():
    global users
    logger.info(f' Обработан запрос для users')
    return {"users": users}


@app.post("/users/")
async def add_users(user: User):
    users.append(user)
    logger.info(' Отработал POST запрос для создания задачи.')
    return users


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    for i in range(len(users)):
        if user[i].id == user_id:
            user[i] = user
    return user


@app.delete("/users/{task_id}")
async def delete_user(user_id: int):
    for i in range(len(users)):
        if users[i].id == user_id:
            return {"item_id": users.pop(i)}
    return HTTPException(status_code=404, detail='Task not found')

