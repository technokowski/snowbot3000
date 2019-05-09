from django.contrib import admin
from mainapp.models import Jokes,Wisdom,Sing
# Register your models here.
admin.site.register(Jokes)
admin.site.register(Wisdom)
admin.site.register(Sing)

# super user: administrator, snowbot3000, administrator@apple.com
