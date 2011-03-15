from createsend import CreateSend, Campaign as CSCampaign
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.sites.models import Site

from .. import settings
from ..utils import get_content_models


class Campaign(models.Model):
    cm_id = models.CharField(verbose_name=_("Campaign Monitor ID"), max_length=32, blank=True)
    name = models.CharField(verbose_name=_("name"), max_length=255)
    subject = models.CharField(verbose_name=_("subject"), max_length=255)
    from_name = models.CharField(verbose_name=_("from name"), max_length=255)
    from_email = models.EmailField(verbose_name=_("email"))
    content_type = models.ForeignKey(ContentType, limit_choices_to=Q(app_label__in=[m[0] for m in get_content_models()], model__in=[m[1] for m in get_content_models()])) # TODO: Check also the combination of app_label and model
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        verbose_name = _("campaign")
        verbose_name_plural = _("campaigns")
        app_label = 'campaignmonitor'
    
    @property
    def html_url(self):
        return "http://%s%s" % (Site.objects.get_current().domain, reverse('campaign_content_html', kwargs={'id':self.id}))
    
    @property
    def text_url(self):
        return "http://%s%s" % (Site.objects.get_current().domain, reverse('campaign_content_text', kwargs={'id':self.id}))
    
    def save(self, *args, **kwargs):
        new_campaign = not self.id
        obj = super(Campaign, self).save(*args, **kwargs)
        if new_campaign:
            CreateSend.api_key = settings.API_KEY
            campaign = CSCampaign()
            attrs = dict(
                client_id=settings.CLIENT_ID,
                subject=self.subject,
                name=self.name,
                from_name=self.from_name,
                from_email=self.from_email,
                reply_to=self.from_email, # TODO
                html_url=self.html_url,
                text_url=self.text_url,
                list_ids=['d222291923c83a64c3f758cdc011c65a'], # TODO
                segment_ids=[] # TODO
            )
            try:
                camp = campaign.create(**attrs)
            except Exception, e:
                raise ValidationError("Campaign Monitor API error %s: %s" % (e.data.Code, e.data.Message))
        return obj


class List(models.Model):
    cm_id = models.CharField(verbose_name=_("Campaign Monitor ID"), max_length=32, blank=True)
    title = models.CharField(verbose_name=_("title"), max_length=255)
    unsubscribe_page = models.URLField(verbose_name=_("unsubscribe page"), max_length=255)
    confirmed_opt_in = models.BooleanField(verbose_name=_("confirmed opt-in"), default=True)
    confirmation_success_page = models.URLField(verbose_name=_("confirmation success page"), max_length=255)
    
    class Meta:
        verbose_name = _("list")
        verbose_name_plural = _("lists")
        app_label = 'campaignmonitor'

