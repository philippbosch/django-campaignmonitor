from warnings import warn

from django.conf import settings


API_KEY = getattr(settings, 'CAMPAIGNMONITOR_API_KEY', None)
if API_KEY is None:
    warn("Please add the CAMPAIGNMONITOR_API_KEY setting in your projects settings.py")

CLIENT_ID = getattr(settings, 'CAMPAIGNMONITOR_CLIENT_ID', None)
if CLIENT_ID is None:
    warn("Please add the CAMPAIGNMONITOR_CLIENT_ID setting in your projects settings.py")

CONTENT_MODELS = getattr(settings, 'CAMPAIGNMONITOR_CONTENT_MODELS', ('cmexample.simplenewsletter',))
DEFAULT_TEMPLATE_HTML = getattr(settings, 'CAMPAIGNMONITOR_DEFAULT_TEMPLATE_HTML', 'campaignmonitor/campaign_base.html')
DEFAULT_TEMPLATE_TEXT = getattr(settings, 'CAMPAIGNMONITOR_DEFAULT_TEMPLATE_TEXT', 'campaignmonitor/campaign_base.txt')

LISTS = getattr(settings, 'CAMPAIGNMONITOR_LISTS', ())

SEGMENTS = []
for list in LISTS:
    try:
        for segment in list[2]:
            SEGMENTS.append((segment[0], "%s :: %s" % (list[1], segment[1])))
    except IndexError:
        pass
