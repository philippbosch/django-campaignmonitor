# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.text import capfirst
from django.utils.translation import ugettext as _
from django.contrib import admin

from ..models import Campaign, Recipients


class RecipientsInline(admin.TabularInline):
    model = Recipients
    extra = 1

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'preview_link', 'create_draft_link',)
    inlines = [RecipientsInline,]
    
    def preview_link(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (reverse('campaign_content_html', kwargs={'id': instance.id}), capfirst(_("preview")))
    preview_link.short_description = _("preview")
    preview_link.allow_tags = True
    
    def create_draft_link(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (reverse('campaign_create_draft', kwargs={'id': instance.id}), capfirst(_("create draft")))
    create_draft_link.short_description = _("create draft")
    create_draft_link.allow_tags = True
    

admin.site.register(Campaign, CampaignAdmin)
