import json
import base64
import pickle

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404

from app.models import File

def __store_session_query(request, query_set):
    request.session['current_query'] = pickle.dumps(query_set.query)
    return query_set

def __load_session_query(request, query_set):
    current_query = request.session['current_query']
    query_set.query = pickle.loads(str(current_query))
    return query_set

def home(request):
    context = {}
    return render(request, 'home.html', context)

def get_file(request, id=None):
    f = get_object_or_404(File, pk=id)
    f_data = None
    with open(f.file_path, 'rb') as fh:
        f_data = fh.read()
    response = HttpResponse(f_data, content_type=f.mime_type)
    response['Content-Disposition'] = 'attachment; filename="%s"' % (f.file_path.split('/')[-1],)
    return response

def images_index(request):
    query = __store_session_query(request, File.get_all_images())
    context = {'files': query}
    return render(request, 'images/index.html', context)

def images_view(request, id=None):
    if not id:
        return render(request, 'images/view.html', {})
    image = File.objects.get(pk=id)
    context = {'image': image}
    return render(request, 'images/view.html', context)

def images_getthis(request, id):
    query = __load_session_query(request, File.objects.all())
    id_list = list(query.values_list('id', flat=True))
    obj = File.objects.get(id=id)
    context = {
        'id': id,
        'number': id_list.index(id) + 1,
        'count': len(id_list),
        'name': obj.file_path.split('/')[-1],
    }
    response = HttpResponse(json.dumps(context), content_type='application/json')
    return response

def images_getnext(request, id):
    query = __load_session_query(request, File.objects.all())
    id_list = list(query.values_list('id', flat=True))
    try:
        next_id = id_list[id_list.index(id) + 1]
        number = id_list.index(id) + 2
    except IndexError:
        # does not take into account a list of size 0, todo: test!
        next_id = id_list[0]
        number = 1

    obj = File.objects.get(id=next_id)
    context = {
        'id': obj.id,
        'number': number,
        'count': len(id_list),
        'name': obj.file_path.split('/')[-1],
    }
    response = HttpResponse(json.dumps(context), content_type='application/json')
    return response

def images_getprev(request, id):
    query = __load_session_query(request, File.objects.all())
    id_list = list(query.values_list('id', flat=True))
    try:
        next_id = id_list[id_list.index(id) - 1]
        number = id_list.index(id)
    except IndexError:
        # does not take into account a list of size 0, todo: test!
        next_id = id_list[-1]
        number = len(id_list)

    obj = File.objects.get(id=next_id)
    context = {
        'id': obj.id,
        'number': number,
        'count': len(id_list),
        'name': obj.file_path.split('/')[-1],
    }
    response = HttpResponse(json.dumps(context), content_type='application/json')
    return response

def audio_index(request):
    context = {}
    return render(request, 'home.html', context)

def videos_index(request):
    context = {}
    return render(request, 'home.html', context)
