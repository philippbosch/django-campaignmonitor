from createsend import CreateSend, Campaign as CSCampaign, BadRequest
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
    STATUS_NEW = 1
    STATUS_DRAFT = 2
    STATUS_SENT = 3
    STATUS_CHOICES = (
        (STATUS_NEW, _("new")),
        (STATUS_DRAFT, _("draft")),
        (STATUS_SENT, _("sent")),
    )
    cm_id = models.CharField(verbose_name=_("Campaign Monitor ID"), max_length=32, blank=True, editable=True)
    name = models.CharField(verbose_name=_("name"), max_length=255)
    subject = models.CharField(verbose_name=_("subject"), max_length=255)
    from_name = models.CharField(verbose_name=_("from name"), max_length=255)
    from_email = models.EmailField(verbose_name=_("email"))
    content_type = models.ForeignKey(ContentType, limit_choices_to=Q(app_label__in=[m[0] for m in get_content_models()], model__in=[m[1] for m in get_content_models()])) # TODO: Check also the combination of app_label and model
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    status = models.PositiveSmallIntegerField(verbose_name=_("status"), choices=STATUS_CHOICES, default=STATUS_NEW, editable=False)
    
    class Meta:
        verbose_name = _("campaign")
        verbose_name_plural = _("campaigns")
        app_label = 'campaignmonitor'
    
    def __unicode__(self):
        return u"%s" % self.name
    
    @property
    def html_url(self):
        return "http://%s%s" % (Site.objects.get_current().domain, reverse('campaign_content_html', kwargs={'id':self.id}))
    
    @property
    def text_url(self):
        return "http://%s%s" % (Site.objects.get_current().domain, reverse('campaign_content_text', kwargs={'id':self.id}))
    
    @property
    def list_ids(self):
        ids = []
        for r in self.recipients_set.all():
            if len(r.list_id) and r.list_id not in ids:
                ids.append(r.list_id)
        return ids
    
    @property
    def segment_ids(self):
        list_ids = self.list_ids
        ids = []
        for r in self.recipients_set.all():
            if len(r.segment_id) and r.segment_id not in ids:
                ids.append(r.segment_id)
        return ids
    
    def create_draft(self, preview_recipients=[]):
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
            list_ids=self.list_ids,
            segment_ids=self.segment_ids,
        )
        try:
            campaign_id = campaign.create(**attrs)
            self.cm_id = campaign_id
            self.status = self.STATUS_DRAFT
            self.save()
        except BadRequest, e:
            raise
        if len(preview_recipients):
            campaign = CSCampaign(campaign_id)
            campaign.send_preview(preview_recipients)
    
    def send(self, confirmation_email):
        if not self.cm_id:
            raise ValueError("No draft created yet")
        CreateSend.api_key = settings.API_KEY
        campaign = CSCampaign(self.cm_id)
        campaign.send(confirmation_email=confirmation_email)
        self.status = self.STATUS_SENT
        self.save()


class Recipients(models.Model):
    LIST_CHOICES = [(l[0], l[1]) for l in settings.LISTS]
    SEGMENT_CHOICES = [(s[0], s[1]) for s in settings.SEGMENTS]
    campaign = models.ForeignKey(Campaign, verbose_name=_("campaign"))
    list_id = models.CharField(verbose_name=_("list"), max_length=32, blank=True, choices=LIST_CHOICES)
    segment_id = models.CharField(verbose_name=_("segment"), max_length=32, blank=True, choices=SEGMENT_CHOICES, editable=len(SEGMENT_CHOICES) > 0)
    
    class Meta:
        verbose_name = _("recipients")
        verbose_name_plural = _("recipients")
        app_label = 'campaignmonitor'
    
    def clean(self):
        if self.list_id and self.segment_id:
            raise ValidationError(_("Select either a list or a segment but not both"))
        
        if not self.list_id and not self.segment_id:
            raise ValidationError(_("Select either a list or a segment"))
