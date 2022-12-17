# I have created this file  - Faizan
import string

from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def remove_punctuation(request):
    punctuation = request.GET.get('remove_punc', 'default')
    spaces = request.GET.get('remove_spaces', 'default')
    cap_first = request.GET.get('cap_first', 'default')
    remove_space = request.GET.get('remove_space', 'default')
    new_line = request.GET.get('new_line', 'default')
    char_count = request.GET.get('char_count', 'default')
    count = 0
    data = request.GET.get('data', 'default')
    if punctuation == 'on':
        data = data.translate(str.maketrans('', '', string.punctuation))
    if spaces == 'on':
        data = ' '.join(data.split())
    if cap_first == 'on':
        data = data.capitalize()
    if remove_space == 'on':
        data = data.replace('  ', '')
    if new_line == 'on':
        data = data.strip()
    if char_count == 'on':
        count = len(data)

    return render(request, 'remove_punc.html', {'data': data, 'count': count})
