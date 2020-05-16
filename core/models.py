# -*- coding: utf-8 -*-
from django.db import models
# from django.db.models.signals import pre_save
# from django.conf import settings
# from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


User = get_user_model()


class Contact(models.Model):
    user = models.CharField(max_length=30, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.content}"




