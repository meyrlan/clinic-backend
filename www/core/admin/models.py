from django.contrib import admin
from core.models import User
from django.utils.translation import ugettext_lazy as _
from rest_framework.reverse import reverse
from django.utils.html import format_html


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "phone",
    )
    search_fields = ["email", "phone"]
    fields = [
        "email",
        "phone",
    ]
