from __future__ import unicode_literals

from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    birth_date = models.DateField(verbose_name="День рождения", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"

class Mailing(models.Model):
    subject = models.CharField(max_length=255, verbose_name="Тема письма")
    html_template = models.TextField(verbose_name="HTML шаблон")
    scheduled_time = models.DateTimeField(verbose_name="Время отправки", null=True, blank=True)
    is_sent = models.BooleanField(default=False, verbose_name="Отправлено")

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"