from createsend import CreateSend, Client as CSClient, List as CSList
from django.core.management.base import NoArgsCommand, CommandError

from ... import settings
from ...models import List

class Command(NoArgsCommand):
    help = 'Get the current subscriber lists from CampaignMonitor'
    
    def handle_noargs(self, **options):
        CreateSend.api_key = settings.API_KEY
        client = CSClient(client_id=settings.CLIENT_ID)
        lists = client.lists()
        for list_id in lists:
            list = CSList(list_id)
            import pdb; pdb.set_trace()
            data = list.list_id # WTF?!
            List.objects.create(
                cm_id=data.ListID,
                title=data.Name,
            )
        