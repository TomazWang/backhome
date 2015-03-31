# backhome/admin.py

from django.contrib import admin
from page.models import Member
from page.models import Group
from page.models import Decision

# Register your models here.
admin.site.register(Member)
admin.site.register(Group)
admin.site.register(Decision)

