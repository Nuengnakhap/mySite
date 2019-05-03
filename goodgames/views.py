from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
    }

    try:
        context['dayoff_list'] = None
        context['user'] = None
    except:
        context['dayoff_list'] = None

    return render(request, 'goodgames/index.html', context=context)
