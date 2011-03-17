from createsend import BadRequest
from django.conf import settings as django_settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

from . import settings
from .models import Campaign


def campaign_content_html(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    template_name = getattr(campaign.content_object, 'TEMPLATE_HTML', settings.DEFAULT_TEMPLATE_HTML)
    context = {
        'campaign': campaign,
    }
    return render_to_response(template_name, context, context_instance=RequestContext(request))


def campaign_content_text(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    template_name = getattr(campaign.content_object, 'TEMPLATE_TEXT', settings.DEFAULT_TEMPLATE_TEXT)
    context = {
        'campaign': campaign,
    }
    return render_to_response(template_name, context, context_instance=RequestContext(request), mimetype="text/plain")


def create_draft(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    
    preview_recipients = []
    if request.user.email:
        preview_recipients.append(request.user.email)
    
    try:
        campaign.create_draft(preview_recipients=preview_recipients)
        messages.success(request, _("The draft for campaign '%(name)s' was created successfully.") % {'name': campaign.name})
        if request.user.email:
            messages.info(request, _("A preview has been sent to %(email)s.") % {'email': request.user.email})
    except BadRequest, e:
        messages.error(request, _("An error occurred: %(code)s %(message)s") % {'code': e.data.Code, 'message': e.data.Message})
    
    return HttpResponseRedirect(reverse('admin:campaignmonitor_campaign_changelist'))


def send_campaign(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    try:
        campaign.send(request.user.email or django_settings.ADMINS[0][1])
        messages.success(request, _("The campaign '%(name)s' was sent successfully.") % {'name': campaign.name})
    except BadRequest, e:
        messages.error(request, _("An error occurred: %(code)s %(message)s") % {'code': e.data.Code, 'message': e.data.Message})
    
    return HttpResponseRedirect(reverse('admin:campaignmonitor_campaign_changelist'))
