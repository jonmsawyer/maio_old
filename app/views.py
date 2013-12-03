import base64

from django.shortcuts import render
from django.http import HttpResponse

from app.models import File

def home(request):
    context = {}
    return render(request, 'home.html', context)

def get_file(request, id):
    f = File.objects.get(pk=id)
    f_data = None
    with open(f.file_path, 'rb') as fh:
        f_data = fh.read()
    response = HttpResponse(f_data, content_type=f.mime_type)
    response['Content-Disposition'] = 'attachment; filename="%s"' % (f.file_path.split('/')[-1],)
    return response

def images_index(request):
    context = {'files': File.get_all_images()}
    return render(request, 'images/index.html', context)

def images_view(request, id):
    image = File.objects.get(pk=id)
    context = {'image': image}
    return render(request, 'images/view.html', context)

def audio_index(request):
    context = {}
    return render(request, 'home.html', context)

def videos_index(request):
    context = {}
    return render(request, 'home.html', context)
