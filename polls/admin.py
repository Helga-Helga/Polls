from django.contrib import admin

# Register your models here.
# these lines added:

from polls.models import Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information',{'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]

from polls.models import Polls
admin.site.register(Poll, PollAdmin)

