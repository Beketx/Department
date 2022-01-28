from django.db import models

from utils.utils import generate_client_id, generate_entity_id, generate_department_id
from utils.consts import GENDER_CHOICES, TYPE_OF

class Client(models.Model):
    id = models.CharField(primary_key=True, default=generate_client_id, unique=True, max_length=255)
    mobile_phone = models.IntegerField(unique=True, null=True, blank=True, max_length=25)
    mobile_additional = models.ForeignKey('MobilePhone', on_delete=models.SET_NULL, null=True)
    surname = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    familyname = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField('Дата и время регистрации', null=True, blank=True)
    updated_at = models.DateTimeField('Дата и время изменения', null=True, blank=True)
    status_updated_at = models.DateTimeField('Дата и время изменения статуса', null=True, blank=True)
    status = models.BooleanField(default=False)
    type_of = models.IntegerField(choices=TYPE_OF)
    email = models.ForeignKey('Email', on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    timezone = models.ForeignKey('Timezone', null=True, verbose_name='Временная зона', on_delete=models.SET_NULL)
    social_network = models.ForeignKey('SocialAccount', on_delete=models.CASCADE, null=True)

class Timezone(models.Model):
    name = models.CharField('Название', max_length=100, null=True, help_text='Например: `Asia/Almaty`')
    description = models.CharField('Описание', max_length=100, null=True, help_text='(UTC+06:00) Алматы')

    class Meta:
        verbose_name = 'Временная зона'
        verbose_name_plural = 'Временная зона'

    def __str__(self):
        return self.description


class MobilePhone(models.Model):
    client = models.ForeignKey(Client)
    mobile_phone = models.CharField()

class Email(models.Model):
    client = models.ForeignKey(Client)
    email = models.EmailField()
    primary = models.BooleanField()

class SocialAccount(models.Model):
    vk = models.ForeignKey('VKAccount', on_delete=models.CASCADE, null=True)
    fb = models.ForeignKey('FBAccount', on_delete=models.CASCADE, null=True)
    ok = models.CharField(max_length=255, null=True)
    instagram = models.CharField(max_length=255, null=True)
    telegram = models.CharField(max_length=255, null=True)
    whatsapp = models.CharField(max_length=255, null=True)
    viber = models.CharField(max_length=255, null=True)

class VKAccount(models.Model):
    social_account = models.ForeignKey()
    vk_link = models.CharField()

class FBAccount(models.Model):
    social_account = models.ForeignKey()
    fb_link = models.CharField()

class LegalEntity(models.Model):
    id = models.CharField(primary_key=True, default=generate_entity_id, unique=True, max_length=255)
    created_at = models.DateTimeField('Дата и время регистрации', null=True, blank=True)
    updated_at = models.DateTimeField('Дата и время изменения', null=True, blank=True)
    name = models.CharField(max_length=255, null=True)
    short_name = models.CharField(max_length=20, null=True)
    inn = models.CharField(max_length=255, null=True)
    kpp = models.CharField(max_length=255, null=True)

class Department(models.Model):
    id = models.CharField(primary_key=True, default=generate_department_id, unique=True, max_length=255)
    name = models.CharField(max_length=255, null=True)
