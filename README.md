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

