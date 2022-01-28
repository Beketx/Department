from django.db import models

from utils.utils import generate_client_id, generate_entity_id, generate_department_id
from utils.consts import GENDER_CHOICES, TYPE_OF


class Client(models.Model):
    id = models.CharField(primary_key=True, max_length=50, null=True, blank=True, unique=True)
    mobile_phone = models.IntegerField('Мобильный номер', unique=True, null=True, blank=True, max_length=25)
    mobile_additional = models.ForeignKey('MobilePhone', on_delete=models.SET_NULL, null=True)
    surname = models.CharField('Фамилия', max_length=100, null=True)
    name = models.CharField('Имя', max_length=100, null=True)
    familyname = models.CharField('Очтчество', max_length=100, null=True)
    created_at = models.DateTimeField('Дата и время регистрации', null=True, blank=True)
    updated_at = models.DateTimeField('Дата и время изменения', null=True, blank=True)
    status_updated_at = models.DateTimeField('Дата и время изменения статуса', null=True, blank=True)
    status = models.BooleanField('MobilePhone', default=False)
    type_of = models.IntegerField('Статус', choices=TYPE_OF)
    email = models.ForeignKey('Email', on_delete=models.CASCADE, null=True)
    gender = models.CharField('Пол', max_length=1, choices=GENDER_CHOICES)
    timezone = models.ForeignKey('Timezone', null=True, verbose_name='Временная зона', on_delete=models.SET_NULL)
    social_network = models.ForeignKey('SocialAccount', on_delete=models.CASCADE, null=True)

    def save(self):
        if not self.id:
            self.id = generate_client_id()
            while Client.objects.filter(id=self.id).exists():
                self.id = generate_client_id()
        super(Client, self).save()

class Timezone(models.Model):
    name = models.CharField('Название', max_length=100, null=True, help_text='Например: `Asia/Almaty`')
    description = models.CharField('Описание', max_length=100, null=True, help_text='(UTC+06:00) Алматы')

    class Meta:
        verbose_name = 'Временная зона'
        verbose_name_plural = 'Временная зона'

    def __str__(self):
        return self.description


class MobilePhone(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True)
    mobile_phone = models.CharField('Описание', max_length=100, null=True)

class Email(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True)
    email = models.EmailField('Почта')
    primary = models.BooleanField('Основной', default=False)

class SocialAccount(models.Model):
    vk = models.ForeignKey('VKAccount', on_delete=models.CASCADE, null=True)
    fb = models.ForeignKey('FBAccount', on_delete=models.CASCADE, null=True)
    ok = models.CharField('OK', max_length=255, null=True)
    instagram = models.CharField('Insta', max_length=255, null=True)
    telegram = models.CharField('Tg', max_length=255, null=True)
    whatsapp = models.CharField('Wp', max_length=255, null=True)
    viber = models.CharField('Vb', max_length=255, null=True)

class VKAccount(models.Model):
    social_account = models.ForeignKey('SocialAccount', on_delete=models.CASCADE, null=True)
    vk_link = models.CharField('Ссылка вк', max_length=100, null=True)

class FBAccount(models.Model):
    social_account = models.ForeignKey('SocialAccount', on_delete=models.CASCADE, null=True)
    fb_link = models.CharField('Ссылка фб', max_length=100, null=True)

class LegalEntity(models.Model):
    id = models.CharField(primary_key=True, max_length=50, null=True, blank=True, unique=True)
    created_at = models.DateTimeField('Дата и время регистрации', null=True, blank=True)
    updated_at = models.DateTimeField('Дата и время изменения', null=True, blank=True)
    name = models.CharField('Название', max_length=255, null=True)
    short_name = models.CharField('Короткое имя', max_length=20, null=True)
    inn = models.CharField('ИНН', max_length=255, null=True)
    kpp = models.CharField('КПП', max_length=255, null=True)

    def save(self):
        if not self.id:
            self.id = generate_entity_id()
            while LegalEntity.objects.filter(id=self.id).exists():
                self.id = generate_entity_id()
        super(LegalEntity, self).save()

class Department(models.Model):
    id = models.CharField(primary_key=True, max_length=50, null=True, blank=True, unique=True)
    name = models.CharField('Имя', max_length=255, null=True)

    def save(self):
        if not self.id:
            self.id = generate_department_id()
            while Department.objects.filter(id=self.id).exists():
                self.id = generate_department_id()
        super(Department, self).save()
