from django.contrib import admin
from .models import VoteSubject, Vote

# Register your models here.


admin.site.register(VoteSubject)
admin.site.register(Vote)