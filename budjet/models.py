from django.db import models


class Month(models.Model):
    name = models.CharField(max_length=150)


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)


class Year(models.Model):
    name = models.CharField(max_length=150)


class Account(models.Model):
    user = models.CharField(max_length=200)


class Bill(models.Model):
    pass
