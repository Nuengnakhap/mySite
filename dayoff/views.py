from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from dayoff.models import DayOff
from dayoff.forms import DayOffForm

# Create your views here.

def index(request):
    context = {
    }

    try:
        context['dayoff_list'] = DayOff.objects.all().filter(created_by=User.objects.get(username=request.user.username))
        context['user'] = User.objects.get(username=request.user.username)
    except:
        context['dayoff_list'] = None

    return render(request, template_name='dayoff/index.html', context=context)

def create(request):
    context = {}

    if request.method == 'POST':
        form = DayOffForm(request.POST)
        if form.is_valid():
            DayOff.objects.create(
                reason=form.cleaned_data.get('reason'),
                type=form.cleaned_data.get('type'),
                date_start=form.cleaned_data.get('date_start'),
                date_end=form.cleaned_data.get('date_end'),
                approve_status=2,
                created_by=User.objects.get(username=request.user.username)
            )
            context['success'] = 'Request successfully submitted'

            form = DayOffForm()
    else:
        form = DayOffForm()

    context['form'] = form
    context['error'] = form.error

    return render(request, template_name='dayoff/create.html', context=context)