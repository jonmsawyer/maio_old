import json
import base64
import pickle
import random
import logging
import inspect
import time

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import maio
from maio_core.models import File
from maio_core.context import pre_populate_context_dict, post_populate_context_dict

logger = logging.getLogger(__name__)

def __log_info(txt):
    logger.info('%.6f %s' % (time.time(), txt))

def __store_session_query(request, query_set):
    #    if 'current_query' in request.session and request.session['current_query'] != None:
    request.session['current_query'] = pickle.dumps(query_set.query)
    return query_set

def __load_session_query(request, query_set):
    current_query = request.session['current_query']
    query_set.query = pickle.loads(current_query)
    return query_set

def __set_session_id_list(request, query, id=None):
    id_list = [str(x) for x in list(query.values_list('id', flat=True))]
    request.session['id_list'] = id_list
    return request.session['id_list']

def __load_session_id_list(request, query, id=None):
    try:
        id_list = request.session['id_list']
    except KeyError as e:
        id_list = __set_session_id_list(request, query, id)
    return id_list

def __reload_session_id_list(request, query, id=None):
    id_list = __set_session_id_list(request, query, id)
    return id_list

def __load_random_list(request, query):
    try:
        id_list = request.session['random_list']
    except:
        ob_list = list(query.values_list('id', flat=True))
        id_list = []
        while len(ob_list) is not 0:
            rand_max = len(ob_list)
            rand_min = 0
            id_list.append(ob_list.pop(random.randrange(rand_min, rand_max)))
        id_list = [str(x) for x in id_list]
        request.session['random_list'] = id_list
    return id_list

def home(request):
    context = pre_populate_context_dict()
    return render(request, 'home.html', context)

def get_file(request, id=None, tn=None):
    f = get_object_or_404(File, pk=id)
    f_data = None
    if tn == 'tn':
        with open(f.tn_path, 'rb') as fh:
            f_data = fh.read()
    else:
        with open(f.file_path, 'rb') as fh:
            f_data = fh.read()
    response = HttpResponse(f_data, content_type=f.mime_type)
    response['Content-Disposition'] = 'attachment; filename="tn_%s"' % (f.file_path.split('/')[-1],)
    try:
        f.views = f.views + 1
        f.save()
    except:
        raise
    return response

def images_index(request):
    context = pre_populate_context_dict()
    query = __store_session_query(request, File.get_all_images())
    try:
        del request.session['random_list']
    except KeyError:
        pass
    try:
        del request.session['id_list']
    except KeyError:
        pass
    per_page = 24
    paginator = Paginator(query, per_page)
    page = request.GET.get('page')
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
        page = 1
    except EmptyPage:
        files = paginator.page(paginator.num_pages)
        page = paginator.num_pages
    page = int(page)

    page_range = []
    threshold = 10
    threshold_size = (threshold*2) + 1

    # build initial page range list
    for i in xrange(1, paginator.num_pages+1):
        if i+threshold >= page and i <= page:
            page_range.append(i)
        elif i-threshold <= page and i >= page:
            page_range.append(i)

    # if the length of page_range is less than the threshold size, add to it
    if len(page_range) < threshold_size:
        if page <= threshold:
            i = page_range[-1]
            while len(page_range) < threshold_size and i < paginator.num_pages:
                i = i + 1
                page_range.append(i)
        else:
            i = page_range[0]
            while len(page_range) < threshold_size and i > 1:
                i = i - 1
                page_range.insert(0, i)
    if page_range[0] != 1:
        page_range.insert(0, '...')
    if page_range[-1] != paginator.num_pages:
        page_range.append('...')

    i = per_page * (page-1) + 1
    for f in files:
        f.num = i
        i = i + 1

    context['files'] = files
    context['page_range'] = page_range
    if request.GET.get('view') == 'list':
        context['view'] = 'list'
    return render(request, 'images/index.html', context)

def images_view(request, id=None):
    context = pre_populate_context_dict()
    if not id:
        return render(request, 'images/view.html', context)
    image = File.objects.get(pk=id)
    context['image'] = image
    return render(request, 'images/view.html', context)

def images_rate(request, id, rating):
    try:
        obj = File.objects.get(id=id)
        rating = int(rating)
        if rating:
            obj.rating = rating
        else:
            obj.rating = None
        obj.save()
        context = {'ok': rating}
    except:
        context = {'error': 'Rating not set'}
    response = HttpResponse(json.dumps(context), content_type="application/json")
    return response

def images_getthis(request, id):
    query = __load_session_query(request, File.objects.all())
    id_list = __load_session_id_list(request, query, id)
    if not id in id_list:
        id_list = __reload_session_id_list(request, query, id)
    id_list = [str(x) for x in id_list]
    obj = File.objects.get(id=id)
    try:
        rating = int(obj.rating)
    except TypeError:
        rating = 0
    context = {
        'id': str(id),
        'number': id_list.index(str(id)) + 1,
        'count': len(id_list),
        'name': obj.file_path.split('/')[-1],
        'rating': rating,
        'views': obj.views,
    }
    response = HttpResponse(json.dumps(context), content_type='application/json')
    return response

def images_getrandom_next(request, id):
    query = __load_session_query(request, File.objects.all())
    id_list = __load_random_list(request, query)
    try:
        next_id = id_list[id_list.index(id) + 1]
        number = id_list.index(id) + 2
    except IndexError:
        # does not take into account a list of size 0, todo: test!
        next_id = id_list[0]
        number = 1

    obj = File.objects.get(id=next_id)
    context = {
        'id': str(obj.id),
        'number': number,
        'count': len(id_list),
        'name': obj.file_path.split('/')[-1],
    }
    response = HttpResponse(json.dumps(context), content_type='application/json')
    return response

def images_getrandom_prev(request, id):
    query = __load_session_query(request, File.objects.all())
    id_list = __load_random_list(request, query)
    try:
        next_id = id_list[id_list.index(id) - 1]
        number = id_list.index(id)
    except IndexError:
        # does not take into account a list of size 0, todo: test!
        next_id = id_list[-1]
        number = len(id_list)

    obj = File.objects.get(id=next_id)
    context = {
        'id': str(obj.id),
        'number': number,
        'count': len(id_list),
        'name': obj.file_path.split('/')[-1],
    }
    response = HttpResponse(json.dumps(context), content_type='application/json')
    return response

def images_unset_random(request):
    try:
        del request.session['random_list']
    except KeyError:
        pass
    context = {'ok': 'deleted random list'}
    response = HttpResponse(json.dumps(context), content_type='application/json')
    return response

def images_getnext(request, id):
    query = __load_session_query(request, File.objects.all())
    id_list = __load_session_id_list(request, query, id)
    try:
        next_id = id_list[id_list.index(id) + 1]
        number = id_list.index(id) + 2
    except IndexError, ValueError:
        # does not take into account a list of size 0, todo: test!
        next_id = id_list[0]
        number = 1

    obj = File.objects.get(id=next_id)
    context = {
        'id': str(obj.id),
        'number': number,
        'count': len(id_list),
        'name': obj.file_path.split('/')[-1],
    }
    response = HttpResponse(json.dumps(context), content_type='application/json')
    return response

def images_getprev(request, id):
    query = __load_session_query(request, File.objects.all())
    id_list = __load_session_id_list(request, query, id)
    try:
        next_id = id_list[id_list.index(id) - 1]
        number = id_list.index(id)
    except IndexError:
        # does not take into account a list of size 0, todo: test!
        next_id = id_list[-1]
        number = len(id_list)

    obj = File.objects.get(id=next_id)
    context = {
        'id': str(obj.id),
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
