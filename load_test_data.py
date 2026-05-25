import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kittygram2.settings')
django.setup()

from django.contrib.auth import get_user_model
from cats.models import Cat, Achievement
from travels.models import Destination, Travel

User = get_user_model()

user = User.objects.filter(is_superuser=True).first()

if not user:
    print('Ошибка: суперпользователь не найден.')
    print('Сначала создайте его: python manage.py createsuperuser')
    exit(1)

ach1, _ = Achievement.objects.get_or_create(name='Ловкач')
ach2, _ = Achievement.objects.get_or_create(name='Чемпион')
ach3, _ = Achievement.objects.get_or_create(name='Красавец')

cat1, created = Cat.objects.get_or_create(
    name='Барсик', owner=user,
    defaults={'color': 'Black', 'birth_year': 2020}
)
if created:
    cat1.achievements.add(ach1, ach3)

cat2, created = Cat.objects.get_or_create(
    name='Мурзик', owner=user,
    defaults={'color': 'Ginger', 'birth_year': 2019}
)
if created:
    cat2.achievements.add(ach2)

cat3, created = Cat.objects.get_or_create(
    name='Снежок', owner=user,
    defaults={'color': 'White', 'birth_year': 2021}
)

dest1, _ = Destination.objects.get_or_create(
    name='Берлин', country='Германия',
    defaults={'description': 'Кото-столица Европы'}
)
dest2, _ = Destination.objects.get_or_create(
    name='Амстердам', country='Нидерланды',
    defaults={'description': 'Город каналов и котиков'}
)
dest3, _ = Destination.objects.get_or_create(
    name='Токио', country='Япония',
    defaults={'description': 'Мекка кото-кафе'}
)

import datetime
Travel.objects.get_or_create(
    cat=cat1, destination=dest1,
    defaults={
        'departure_date': datetime.date(2026, 8, 1),
        'arrival_date': datetime.date(2026, 8, 7),
        'status': 'planned',
        'notes': 'Первое путешествие Барсика'
    }
)
Travel.objects.get_or_create(
    cat=cat2, destination=dest2,
    defaults={
        'departure_date': datetime.date(2026, 9, 10),
        'arrival_date': datetime.date(2026, 9, 15),
        'status': 'planned',
        'notes': 'Мурзик едет в Амстердам'
    }
)

print('[OK] Тестовые данные загружены:')
print(f'  - 3 кошки (id: 1, 2, 3)')
print(f'  - 3 достижения')
print(f'  - 3 места назначения (id: 1=Берлин, 2=Амстердам, 3=Токио)')
print(f'  - 2 путешествия')
