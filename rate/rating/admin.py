# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import University,Faculty,Doctor


# Register your models here.
admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Doctor)