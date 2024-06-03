from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Dream


# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

@login_required
def dream_index(request):
  dreams = Dream.objects.filter(user=request.user)
  return render(request, 'dreams/index.html', {'dreams':dreams} )

@login_required
def dream_detail(request, dream_id):
  dream = Dream.objects.get(id=dream_id)
  return render(request, 'dreams/detail.html', {'dream':dream})

class DreamCreate(LoginRequiredMixin, CreateView):
  model= Dream
  fields =['title', 'description', 'date', 'type']

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class DreamUpdate(LoginRequiredMixin, UpdateView):
  model = Dream
  fields =['title', 'description', 'date', 'type']

class DreamDelete(LoginRequiredMixin, DeleteView):
  model = Dream
  success_url = '/dreams/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)