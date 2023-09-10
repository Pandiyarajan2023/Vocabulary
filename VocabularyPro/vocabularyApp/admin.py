from django.contrib import admin
from vocabularyApp.models import vocabulary

# Register your models here.

class vocabularyAdmin(admin.ModelAdmin):
    list_display = ['Word','Meaning','Example','Name']
admin.site.register(vocabulary,vocabularyAdmin)