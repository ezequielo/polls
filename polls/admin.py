from django.contrib import admin
from polls.models import Choice, Poll

class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)

