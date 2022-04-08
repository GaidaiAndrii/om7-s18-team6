from django.shortcuts import render, redirect
from order.models import Order
from authentication.models import CustomUser
from authentication.forms import CustomUserForm
from django.db.models.functions import Now
from django.db.models import Q
from django.views.generic import ListView


def user_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CustomUserForm()
        else:
            try:
                author = CustomUser.objects.get(pk=id)
            except CustomUser.DoesNotExist:
                return redirect("/random")
            form = AuthorForm(instance=author)
        return render(request, "authentication/user_form.html", {"form": form})
    else:
        if id == 0:
            form = CustomUserForm(request.POST)
        else:
            author = CustomUser.objects.get(pk=id)
            form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('user')

    return redirect("reconstruction")


class UserList(ListView):
    model = CustomUser
    template_name = "authentication/index.html"
    context_object_name = "users"

    def get(self, request, *args, **kwargs):
        return ListView.get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserList, self).get_context_data(**kwargs)
        context['title'] = 'Список читачів'
        context['content_title'] = 'Адміністрування бібліотеки / Читачі'

        return context

    def get_queryset(self):
        queryset = CustomUser.get_all()

        return queryset


def overdue(request):
    users = CustomUser.objects.filter(Q(order__plated_end_at__lte=Now()) & Q(order__end_at__isnull=True))

    context = {}
    context['title'] = 'Список читачів'
    context['content_title'] = 'Адміністрування бібліотеки / Читачі'
    context['users'] = users

    return render(request, 'authentication/index.html', context)
