from django.shortcuts import render
from django.views.generic import View
from awards.models import Award


# home
def home(request):
    last_award = Award.objects.latest('id')
    last_three_awards = Award.objects.all().order_by('-id')[:3]

    context_dic = {
        'last_three_awards': last_three_awards,
        'last_award': last_award,
    }
    return render(request, 'index.html', context_dic)


# about
def about(request):
    return render(request, 'about.html')


# 404
def error_404(request):
    return render(request, '404.html')