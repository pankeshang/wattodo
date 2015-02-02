from django.contrib import admin
import todo.models

# Register your models here.
admin.site.register(todo.models.Todo, admin.ModelAdmin)
