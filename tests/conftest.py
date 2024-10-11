import pytest

from bulletins.models import Ad, Comment
from users.models import User


@pytest.fixture
def user():
    user = User.objects.create(email='testuser@mail.com',
                               password='testpassword')
    return user


@pytest.fixture
def create_ad(user):
    return Ad.objects.create(title='Сдаю квартиру', description='Посуточно',
                             price=25000, author=user)


@pytest.fixture
def create_comment(user, create_ad):
    Comment.objects.create(text='Новый комментарий', ad=create_ad, author=user)
