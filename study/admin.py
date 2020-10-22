from django.contrib import admin
from .models import Contact, CLass_1, CLass_2, CLass_3, CLass_4, CLass_5, CLass_6, CLass_7, CLass_8, CLass_9, CLass_10


@admin.register(CLass_1)
class Class_1Admin(admin.ModelAdmin):
    list_display = ['file_name', 'subject', 'timestamp']


@admin.register(CLass_2)
class Class_2Admin(admin.ModelAdmin):
    list_display = ['file_name', 'subject', 'timestamp']


@admin.register(CLass_3)
class Class_3Admin(admin.ModelAdmin):
    list_display = ['file_name', 'subject', 'timestamp']


@admin.register(CLass_4)
class Class_4Admin(admin.ModelAdmin):
    list_display = ['file_name', 'subject', 'timestamp']


@admin.register(CLass_5)
class Class_5Admin(admin.ModelAdmin):
    list_display = ['file_name', 'subject', 'timestamp']


@admin.register(CLass_6)
class Class_6Admin(admin.ModelAdmin):
    list_display = ['file_name', 'subject', 'timestamp']


@admin.register(CLass_7)
class Class_7Admin(admin.ModelAdmin):
    list_display = ['file_name', 'subject', 'timestamp']


@admin.register(CLass_8)
class Class_8Admin(admin.ModelAdmin):
    list_display = ['file_name', 'subject', 'timestamp']


@admin.register(CLass_9)
class Class_9Admin(admin.ModelAdmin):
    list_display = ['file_name', 'subject', 'timestamp']


@admin.register(CLass_10)
class Class_10Admin(admin.ModelAdmin):
    list_display = ['file_name', 'subject', 'timestamp']
