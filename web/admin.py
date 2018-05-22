# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Expense, InCome, Note

# Register your models here.
admin.site.register(Expense)
admin.site.register(InCome)
admin.site.register(Note)
