from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=(
        "автор"), on_delete=models.CASCADE)
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст")
    created_date = models.DateTimeField(
        ("Дата создания"), default=timezone.now)
    published_date = models.DateTimeField(
        ("дата публикации"), blank=True, null=True)
    meta_title = models.TextField(max_length=60)
    meta_description = models.TextField(
        "description", max_length=160, default="description")

    def publish(self):
        self.publish_date = timezone.now()
        self.save()
        return True
    publish.boolean = True
    publish.short_description = 'Опубликовано'
    publish.admin_order_field = 'published_date'

    def __str__(self):
        return self.title
