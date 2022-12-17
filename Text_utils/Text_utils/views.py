# I have created this file  - Faizan
import string

from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def remove_punctuation(request):
    punctuation = request.POST.get('remove_punc', 'default')
    cap_first = request.POST.get('cap_first', 'default')
    remove_space = request.POST.get('remove_space', 'default')
    new_line = request.POST.get('new_line', 'default')
    data = request.POST.get('data', 'default')
    if punctuation == 'on':
        data = data.translate(str.maketrans('', '', string.punctuation))
    if remove_space == 'on':
        data = ' '.join(data.split())
    if cap_first == 'on':
        data = data.capitalize()
    if new_line == 'on':
        data = ' '.join(data.strip().split())
    return render(request, 'remove_punc.html', {'data': data})
