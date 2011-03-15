from django.db import models
from django.utils.translation import ugettext_lazy as _

class SimpleNewsletter(models.Model):
    title = models.CharField(verbose_name=_("title"), max_length=100)
    content = models.TextField(verbose_name=_("content"))
    
    class Meta:
        verbose_name = _("simple newsletter")
        verbose_name_plural = _("simple newsletters")
    
    def __unicode__(self):
        return u"%s" % self.title