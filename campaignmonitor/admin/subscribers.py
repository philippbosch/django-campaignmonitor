from django.contrib import admin

from ..models.subscribers import Subscriber, SubscriberCustomField


class SubscriberCustomFieldInline(admin.TabularInline):
    model = SubscriberCustomField


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'name', 'date', 'state')
    inlines = [SubscriberCustomFieldInline,]

admin.site.register(Subscriber, SubscriberAdmin)
