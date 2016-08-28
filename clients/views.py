from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from clients.models import Client

@login_required
def list(request):
    """Display list of clients"""
    return render(request, 'clients/list.html', {})

def view(request, client_id):
    """Display a certain client"""
    client = Client.objects.get(id=client_id)
    client_index_path = "clients/{0}/index.html".format(client.package_name)
    is_embeded = client.is_embeded

    return render(request, 'clients/view.html', {'client_id':client_id, 'client_index_path':client_index_path, 'is_embeded':is_embeded})

