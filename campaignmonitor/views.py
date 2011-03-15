from django.shortcuts import get_object_or_404, render_to_response

from . import settings
from .models import Campaign


def campaign_content_html(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    template_name = settings.DEFAULT_TEMPLATE_HTML
    context = {
        'campaign': campaign,
    }
    return render_to_response(template_name, context)


def campaign_content_text(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    template_name = settings.DEFAULT_TEMPLATE_TEXT
    context = {
        'campaign': campaign,
    }
    return render_to_response(template_name, context)
