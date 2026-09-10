from django.contrib import admin

from .models import (
    Dog,
    Vitality,
    PawMood,
    PawMatch,
    PawFind
)


admin.site.register(Dog)

admin.site.register(Vitality)

admin.site.register(PawMood)

admin.site.register(PawMatch)

admin.site.register(PawFind)