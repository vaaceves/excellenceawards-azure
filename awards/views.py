from .models import Award
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

# Create your views here.
# home
def home(request):
    last_award = Award.objects.latest('id')
    last_three_awards = Award.objects.filter(featured=True).order_by('-id')[:3]

    context_dic = {
        'last_three_awards': last_three_awards,
        'last_award': last_award,
    }

    try:
        featured_award = Award.objects.get(featured=True)  # traemos los detalles
        context_dic['featured_award'] = featured_award

    except Award.DoesNotExist:
        context_dic['featured_award'] = None

    return render(request, 'index.html', context_dic)

# about
def about(request):
    return render(request, 'about.html')

# 404
def error_404(request):
    return render(request, '404.html')

# archive
class ArchiveView(ListView):
    template_name = 'archive.html'
    queryset = Award.objects.filter(featured=True).order_by('-id')

# award detail
class AwardView(DetailView):
    template_name = 'award.html'
    model = Award
    slug_field = 'slug'
