from django.db import models
from django.utils.translation import ugettext_lazy as _

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
