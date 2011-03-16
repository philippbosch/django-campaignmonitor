from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from createsend import BadRequest

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
    return render_to_response(template_name, context, context_instance=RequestContext(request))


def create_draft(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    context = {
        'campaign': campaign
    }
    try:
        campaign.create_draft()
    except BadRequest, e:
        context.update({'error': e})
    return render_to_response('campaignmonitor/draft-created.html', context, context_instance=RequestContext(request))
