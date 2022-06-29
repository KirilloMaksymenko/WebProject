from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Server_Board, UserProfile
from .forms import TaskForm, ServerForm,EditProfileForm, AuthUserForm, RegisterUserForm
from django.views.generic import DeleteView, UpdateView, DetailView, CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404


###____Local____###

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/Local/my-board.html', {'title': 'Главная', 'tasks':tasks })

def delete_note (request, pk):
    error = ''
    post = get_object_or_404(Task, pk=pk)
    tasks = Task.objects.order_by('-id')

    if request.method == 'POST' and "succes-delete-btn" in request.POST:

        Task.objects.get(pk=pk).delete()

        return redirect('home')

    if request.method == 'POST' and "cancel-delete-btn" in request.POST:
        return redirect(f'/my-board/{pk}/views')

    form = TaskForm()
    context = {
        'post': post,
        'form': form,
        'tasks': tasks,
        'error': error
    }
    return render(request, 'main/Local/Delete_Notes.html', context)

def view_note(request, pk):
    error = ''
    post = get_object_or_404(Task, pk=pk)
    tasks = Task.objects.order_by('-id')


    form = TaskForm()
    context = {
        'post': post,
        'form': form,
        'tasks': tasks,
        'error' :error
    }
    return render(request, 'main/Local/Notes_view.html', context)

class create(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login-page')
    model = Task
    template_name = 'main/Local/Create.html'
    form_class = TaskForm
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        kwargs['list_notes'] = Task.objects.order_by('-id')
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


###____Server____###

class server_view_note(DetailView):
    model = Server_Board
    template_name = 'main/Server/server-view.html'
    context_object_name = 'post'


    def get_context_data(self, **kwargs):
        context = super(server_view_note, self).get_context_data(**kwargs)
        stuff = get_object_or_404(Server_Board, id=self.kwargs['pk'])
        total_reactions = stuff.total_likes()
        context['users'] = User.objects.all()
        context['list_notes'] = Server_Board.objects.order_by('-id')
        context['total_reactions'] = total_reactions
        return context


def index_server(request):
    tasks = Server_Board.objects.order_by('-id')

    return render(request, 'main/Server/server-board.html', {'title': 'Главная', 'tasks':tasks,})

class server_create(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login-page')
    model = Server_Board
    template_name = 'main/Server/server-create.html'
    form_class = ServerForm
    success_url = reverse_lazy('server-board-view')
    def get_context_data(self, **kwargs):
        kwargs['list_notes'] = Server_Board.objects.order_by('-id')
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class server_delete_note(LoginRequiredMixin ,DeleteView):
    model = Server_Board
    template_name = 'main/Server/server-delete.html'
    success_url = reverse_lazy('server-board-view')
    context_object_name = 'post'
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object.author)
        print(self.request.user)
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        kwargs['list_notes'] = Server_Board.objects.order_by('-id')
        return super().get_context_data(**kwargs)

class server_account_view(DetailView):
    model = User
    template_name = 'main/Server/server-account-view.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(server_account_view, self).get_context_data(**kwargs)
        print(self.object)
        num_post = Server_Board.objects.filter(author=self.object)
        reactions_num = 0
        for post in num_post:
            stuff = get_object_or_404(Server_Board, id=post.pk)
            total_reactions = stuff.total_likes()
            reactions_num = total_reactions + reactions_num
        context['all_count_reactions'] = reactions_num
        context['list_notes'] = Server_Board.objects.order_by('-id')
        return context

def server_reaction_view(request, pk):
    notes = get_object_or_404(Server_Board, id=request.POST.get('notes_id'))
    notes.reaction_count_in_post.add(request.user)
    return HttpResponseRedirect(reverse('server-views-notes', args=[str(pk)]))



###____Login____###

class LogoutUser(LogoutView):
    next_page = 'home'

class LoginUser(LoginView):
    template_name = 'main/Account/Login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')
    def get_success_url(self):
        return self.success_url

class ProfileUser(ListView):
    model = User
    template_name = 'main/Account/Account-cabinet.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(ProfileUser, self).get_context_data(**kwargs)
        num_post = Server_Board.objects.filter(author=self.request.user)
        reactions_num = 0
        for post in num_post:
            stuff = get_object_or_404(Server_Board, id=post.pk)
            total_reactions = stuff.total_likes()
            reactions_num = total_reactions + reactions_num
        context['all_count_reactions'] = reactions_num
        context['list_notes'] = Server_Board.objects.order_by('-id')
        return context

class EditProfil(UpdateView):
    model = UserProfile
    form_class = EditProfileForm
    template_name = 'main/Account/Account-edit.html'
    success_url = reverse_lazy('profile-page')
    def get_context_data(self, **kwargs):
        context = super(EditProfil, self).get_context_data(**kwargs)
        num_post = Server_Board.objects.filter(author=self.request.user)
        reactions_num = 0
        for post in num_post:
            stuff = get_object_or_404(Server_Board, id=post.pk)
            total_reactions = stuff.total_likes()
            reactions_num = total_reactions + reactions_num
        context['all_count_reactions'] = reactions_num
        context['list_notes'] = Server_Board.objects.order_by('-id')
        return context

class RegisterUser(CreateView):
    model = User
    template_name = 'main/Account/Register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        aut_user = authenticate(username=username, password=password)

        login(self.request,aut_user)
        return form_valid


###____Other____###


