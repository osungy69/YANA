from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]

def hello_world(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world'))
        else:
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

    else:
        return HttpResponseRedirect(reverse('accountapp:login'))


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

    def dispatch(self, request, *args, **kwargs):
        # 로그인된 상태라면 기본 경로로 리디렉션
        if request.user.is_authenticated:
            return redirect(reverse_lazy('accountapp:hello_world'))
        # 비로그인 상태라면 원래의 LoginView 동작 수행
        return super().dispatch(request, *args, **kwargs)


class CustomLoginView(LoginView):
    def get_redirect_url(self):
        redirect_to = self.request.GET.get('next')
        # next가 로그인 페이지라면 기본 경로로 리디렉션
        if redirect_to == reverse_lazy('accountapp:login'):
            return reverse_lazy('accountapp:hello_world')
        return redirect_to or reverse_lazy('accountapp:hello_world')

    def dispatch(self, request, *args, **kwargs):
        # 로그인된 상태라면 기본 경로로 리디렉션
        if request.user.is_authenticated:
            return redirect(reverse_lazy('accountapp:hello_world'))
        # 비로그인 상태라면 원래의 LoginView 동작 수행
        return super().dispatch(request, *args, **kwargs)


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'