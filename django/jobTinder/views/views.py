from django.shortcuts import render


def candidatos_list(request):
    return render(request, 'jobTinder/candidatos_list.html', {})
