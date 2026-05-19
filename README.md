# Kittygram — REST API для Кото-путешествий

Курсовая работа: **«Разработка и развертывание REST API-сервиса для Кото-путешествия в рамках проекта Kittygram на основе Django Rest Framework»**

REST API-сервис для управления котами и их путешествиями. Поддерживает JWT-аутентификацию, фильтрацию, пагинацию, разграничение прав доступа и автоматическую документацию (Swagger / Redoc).

---

## Вариант 1 — Запуск на Windows (PowerShell)

**Требования:** Python 3.10+

```powershell
# 1. Клонировать репозиторий
git clone https://github.com/Aizenhaim/kittygram-coursework.git
cd kittygram-coursework

# 2. Создать и активировать виртуальное окружение
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Применить миграции
python manage.py migrate

# 5. Создать суперпользователя
python manage.py createsuperuser

# 6. Загрузить тестовые данные
python load_test_data.py

# 7. Запустить сервер
python manage.py runserver
```

Открыть в браузере: http://127.0.0.1:8000/swagger/

---

## Вариант 2 — Запуск на Linux / macOS

**Требования:** Python 3.10+

```bash
# 1. Клонировать репозиторий
git clone https://github.com/Aizenhaim/kittygram-coursework.git
cd kittygram-coursework

# 2. Создать и активировать виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Применить миграции
python manage.py migrate

# 5. Создать суперпользователя
python manage.py createsuperuser

# 6. Загрузить тестовые данные
python load_test_data.py

# 7. Запустить сервер
python manage.py runserver
```

Открыть в браузере: http://127.0.0.1:8000/swagger/

---

## Вариант 3 — Запуск через Docker

**Требования:** Docker Desktop (Windows/macOS) или Docker Engine + docker-compose (Linux)

```bash
# 1. Клонировать репозиторий
git clone https://github.com/Aizenhaim/kittygram-coursework.git
cd kittygram-coursework

# 2. Создать и открыть файл переменных окружения
cp .env.example .env
notepad .env
```

Заполнить в открывшемся файле:
```
SECRET_KEY=любой-случайный-набор-символов
DB_PASSWORD=придумайте-пароль
```
Сохранить файл (Ctrl+S) и закрыть.

```bash
# 3. Собрать и запустить контейнеры
docker-compose up --build -d

# 4. Проверить, что всё запущено
docker-compose ps

# 5. Создать суперпользователя
docker-compose exec web python manage.py createsuperuser

# 6. Загрузить тестовые данные
docker-compose exec web python load_test_data.py
```

Открыть в браузере: http://localhost/swagger/

Остановить:
```bash
docker-compose down
```

---

## Проверка API

Последовательность запросов для проверки работы «Кото-путешествий».
Используйте Postman-коллекцию `Kittygram_Travels_API.postman_collection.json` («Кото-путешествия API») или curl-команды ниже.

> Для Docker замените `http://127.0.0.1:8000` на `http://localhost`

### 1. Регистрация и аутентификация

```bash
# Регистрация
curl -s -X POST http://127.0.0.1:8000/api/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{"username":"traveler","password":"Travel1234!","re_password":"Travel1234!"}'

# Получить токен (сохранить значение access)
curl -s -X POST http://127.0.0.1:8000/api/auth/jwt/create/ \
  -H "Content-Type: application/json" \
  -d '{"username":"traveler","password":"Travel1234!"}'
```

### 2. Создание кота и места назначения

```bash
TOKEN="вставить_access_токен"

# Создать кота
curl -s -X POST http://127.0.0.1:8000/api/cats/ \
  -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" \
  -d '{"name":"Путешественник","color":"Gray","birth_year":2021}'

# Создать место назначения
curl -s -X POST http://127.0.0.1:8000/api/destinations/ \
  -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" \
  -d '{"name":"Амстердам","country":"Нидерланды","description":"Город каналов"}'
```

### 3. Путешествия

```bash
# Создать путешествие (cat и destination_id — id из предыдущих запросов)
curl -s -X POST http://127.0.0.1:8000/api/travels/ \
  -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" \
  -d '{"cat":1,"destination_id":1,"departure_date":"2026-08-01","arrival_date":"2026-08-07","status":"planned"}'

# Список путешествий
curl -s http://127.0.0.1:8000/api/travels/ -H "Authorization: Bearer $TOKEN"

# Фильтрация по статусу
curl -s "http://127.0.0.1:8000/api/travels/?status=planned" -H "Authorization: Bearer $TOKEN"

# Мои путешествия
curl -s http://127.0.0.1:8000/api/travels/my/ -H "Authorization: Bearer $TOKEN"
```

### 4. Проверка ошибок доступа и валидации

```bash
# 401 — /travels/my/ без токена
curl -s http://127.0.0.1:8000/api/travels/my/

# 403 — создать путешествие для чужого кота
curl -s -X POST http://127.0.0.1:8000/api/travels/ \
  -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" \
  -d '{"cat":1,"destination_id":1,"departure_date":"2026-09-01","status":"planned"}'

# 400 — дата прибытия раньше отправления
curl -s -X POST http://127.0.0.1:8000/api/travels/ \
  -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" \
  -d '{"cat":1,"destination_id":1,"departure_date":"2026-08-10","arrival_date":"2026-08-05","status":"planned"}'
```

---

## Автотесты

Автоматизированные тесты в текущей версии не реализованы. Функциональность проверяется вручную через Postman-коллекцию и curl-команды (см. раздел «Проверка API»).

Направления для развития: pytest-django, тесты на права доступа (403), валидацию дат и фильтрацию.

---

## API-эндпоинты

| Метод | URL | Права | Описание |
|-------|-----|-------|----------|
| POST | `/api/auth/users/` | AllowAny | Регистрация |
| POST | `/api/auth/jwt/create/` | AllowAny | Получение JWT-токена |
| POST | `/api/auth/jwt/refresh/` | AllowAny | Обновление токена |
| GET / POST | `/api/cats/` | GET — все, POST — авториз. | Список котов / создание |
| GET / PUT / DELETE | `/api/cats/{id}/` | PUT/DELETE — только владелец | Управление котом |
| GET / POST | `/api/achievements/` | IsAuthenticated | Достижения |
| GET / POST | `/api/destinations/` | GET — все, POST — авториз. | Места назначения |
| GET / POST | `/api/travels/` | GET — все, POST — авториз. | Путешествия |
| GET | `/api/travels/my/` | IsAuthenticated | Путешествия своих котов |
| GET / PUT / DELETE | `/api/travels/{id}/` | PUT/DELETE — владелец кота | Управление путешествием |
| GET | `/swagger/` | AllowAny | Swagger UI |
| GET | `/redoc/` | AllowAny | Redoc |

## Технологический стек

Python 3.10 · Django 3.2 · Django REST Framework 3.12 · SimpleJWT · djoser · drf-yasg · django-filter · PostgreSQL 14 · Docker · nginx · gunicorn
