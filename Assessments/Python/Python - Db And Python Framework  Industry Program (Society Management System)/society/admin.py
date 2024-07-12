from django.contrib import admin
from .models import Role,Chairmans,Members,Watchmans,Notice,Event,Visitors

# Register your models here.
admin.site.register(Role)
admin.site.register(Chairmans)
admin.site.register(Members)
admin.site.register(Watchmans)
admin.site.register(Notice)
admin.site.register(Event)
admin.site.register(Visitors)