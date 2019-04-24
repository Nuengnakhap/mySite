from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PollForm, PollModelForm
from polls.models import Poll, Question, Answer


# Create your views here.
def index(request):

    poll_list = Poll.objects.all()

    for poll in poll_list:
        question_count = Question.objects.filter(poll_id=poll.id).count()
        poll.question_count = question_count

    context = {
        'page_title': "My Polls",
        'poll_list': poll_list
    }
    return render(request, template_name='polls/index.html', context=context)

@login_required
@permission_required('polls.view_poll')
def detail(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    for question in poll.question_set.all():
        name = 'choice'+str(question.id)
        choice_id = request.GET.get(name)
        if choice_id:
            try:
                ans = Answer.objects.get(question_id=question.id)
                ans.choice_id=choice_id
            except Answer.DoesNotExist:
                Answer.objects.create(
                    choice_id=choice_id,
                    question_id=question.id
                )

    return render(request, 'polls/detail.html', { 'poll':poll })


@login_required
@permission_required('polls.add_poll')
def create(request):

    if request.method == 'POST':
        form = PollModelForm(request.POST)

        if form.is_valid():
            form.save()
            # poll = Poll.objects.create(
            #     title=form.cleaned_data.get('title'),
            #     start_date=form.cleaned_data.get('start_date'),
            #     end_date=form.cleaned_data.get('end_date'),

            # )
            # for i in range(1, form.cleaned_data.get('no_questions')+1):
            #     Question.objects.create(
            #         text='QQQQ'+str(i),
            #         type='01',
            #         poll=poll
            #     )
    else:
        form = PollModelForm()


    context = {
        'form': form,
    }

    return render(request, 'polls/create.html', context=context)

@login_required
@permission_required('polls.change_poll')
def update(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method == 'POST':
        form = PollModelForm(request.POST, instance=poll)
        if form.is_valid():
            form.save()
    else:
        form = PollModelForm(instance=poll)


    context = {
        'form': form,
        'poll': poll
    }

    return render(request, 'polls/update.html', context=context)


def mylogin(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')

            return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, 'polls/login.html', context=context)

def mylogout(request):
    logout(request)
    return redirect('login')