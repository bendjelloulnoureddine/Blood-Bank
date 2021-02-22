from django.contrib import admin

from .models import Person

class PersonModelAdmin(admin.ModelAdmin):
    list_display = ('__str__','phone_number')
    list_filter = ('blood_type', 'person_type')

admin.site.register(Person,PersonModelAdmin)
