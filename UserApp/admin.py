from django.contrib import admin
from .models import User

class UnfoldAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')  # Faoliyatlar uchun o'qilishi mumkin bo'lgan maydonlar
    list_display = ('username', 'email', 'phone_number', 'created_at', 'updated_at')  # Adminda ko'rsatiladigan maydonlar
    list_filter = ('created_at', 'updated_at')  # Filtrlarni qo'shish

admin.site.register(User, UnfoldAdmin)
