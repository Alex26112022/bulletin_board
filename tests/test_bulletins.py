import pytest
from django.urls import reverse

from rest_framework.test import APIClient, force_authenticate

logout_user = APIClient()


@pytest.mark.django_db
def test_get_ads(create_ad):
    response = logout_user.get(reverse('bulletins:ads_list'))
    assert response.status_code == 200
    assert response.data['results'][0].get('title') == 'Сдаю квартиру'


@pytest.mark.django_db
def test_create_ad(user):
    payload = {'title': 'Сдаю квартиру', 'description': 'Описание квартиры'}
    logout_user.force_authenticate(user=user)
    response = logout_user.post(reverse('bulletins:ad_create'), payload)
    assert response.status_code == 201
    assert response.data.get('description') == 'Описание квартиры'


@pytest.mark.django_db
def test_get_ad(user, create_ad):
    logout_user.force_authenticate(user=user)
    response = logout_user.get(reverse('bulletins:ad_detail', args=(3,)))
    assert response.status_code == 200
    assert response.data.get('title') == 'Сдаю квартиру'


@pytest.mark.django_db
def test_update_ad(user, create_ad):
    payload = {'title': 'Сдаю квартиру срочно!'}
    logout_user.force_authenticate(user=user)
    response = logout_user.patch(reverse('bulletins:ad_update', args=(4,)),
                                 payload)
    assert response.status_code == 200
    assert response.data.get('title') == 'Сдаю квартиру срочно!'


@pytest.mark.django_db
def test_delete_ad(user, create_ad):
    logout_user.force_authenticate(user=user)
    response = logout_user.delete(reverse('bulletins:ad_delete', args=(5,)))
    assert response.status_code == 204


@pytest.mark.django_db
def test_get_comments(create_comment):
    response = logout_user.get(reverse('bulletins:comments_list'))
    assert response.status_code == 200
    assert response.data[0].get('text') == 'Новый комментарий'


@pytest.mark.django_db
def test_create_comment(user, create_ad):
    payload = {'text': 'Хороший комментарий', 'ad': create_ad.pk}
    logout_user.force_authenticate(user=user)
    response = logout_user.post(reverse('bulletins:comment_create'), payload)
    assert response.status_code == 201
    assert response.data.get('text') == 'Хороший комментарий'


@pytest.mark.django_db
def test_update_comment(user, create_comment):
    payload = {'text': 'Обновленный комментарий'}
    logout_user.force_authenticate(user=user)
    response = logout_user.patch(reverse('bulletins:comment_update', args=(3,)),
                                 payload)
    assert response.status_code == 200
    assert response.data.get('text') == 'Обновленный комментарий'


@pytest.mark.django_db
def test_delete_comment(user, create_comment):
    logout_user.force_authenticate(user=user)
    response = logout_user.delete(reverse('bulletins:comment_delete', args=(4,)))
    assert response.status_code == 204
