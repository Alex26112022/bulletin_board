from django.db import models

from users.models import User

options = {'blank': True, 'null': True}


class Bulletin(models.Model):
    """ Модель объявления.  """
    title = models.CharField(max_length=255, verbose_name='Название',
                             help_text='Введите название!')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена',
                                        help_text='Введите цену!')
    description = models.TextField(verbose_name='Описание',
                                   help_text='Введите описание товара!',
                                   **options)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='bulletins',
                               verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Время и дата создания объявления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comment(models.Model):
    """ Модель комментариев к объявлениям. """
    text = models.TextField(verbose_name='Текст комментария',
                            help_text='Введите текст комментария!')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments', verbose_name='Автор')
    ad = models.ForeignKey(Bulletin, on_delete=models.CASCADE,
                           related_name='comments', verbose_name='Объявление',
                           help_text='Выберите объявление!')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Время и дата создания отзыва')

    def __str__(self):
        return f'Комментарий {self.pk} от {self.author}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
