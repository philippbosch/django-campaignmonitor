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
    list_display = ('name', 'subject', 'preview_link', 'create_draft_link', 'send_campaign_link')
    readonly_fields = ('cm_id',)
    inlines = [RecipientsInline,]
    
    def preview_link(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (reverse('campaign_content_html', kwargs={'id': instance.id}), capfirst(_("preview")))
    preview_link.short_description = _("preview")
    preview_link.allow_tags = True
    
    def create_draft_link(self, instance):
        return '<a href="%s" class="button">%s</a>' % (reverse('campaign_create_draft', kwargs={'id': instance.id}), capfirst(_("create draft")))
    create_draft_link.short_description = _("create draft")
    create_draft_link.allow_tags = True
    
    def send_campaign_link(self, instance):
        if not instance.cm_id:
            return ""
        return '<a href="%s" class="button" onclick="if (!confirm(\'Are you sure you want to send this campaign?\')) return false;">%s</a>' % (reverse('campaign_send_campaign', kwargs={'id': instance.id}), capfirst(_("send campaign")))
    send_campaign_link.short_description = _("send campaign")
    send_campaign_link.allow_tags = True

admin.site.register(Campaign, CampaignAdmin)
