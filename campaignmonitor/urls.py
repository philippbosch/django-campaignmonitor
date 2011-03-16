from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('campaignmonitor.views',
    url(r'^(?P<id>\d+)/html/$', 'campaign_content_html', name='campaign_content_html'),
    url(r'^(?P<id>\d+)/text/$', 'campaign_content_text', name='campaign_content_text'),
    url(r'^(?P<id>\d+)/create-draft/$', 'create_draft', name='campaign_create_draft'),
)
