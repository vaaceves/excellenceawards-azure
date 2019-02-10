from django.contrib import admin
from .models import Award

# Register your models here.
class AwardAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp', 'country', 'site', )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Award, AwardAdmin)
