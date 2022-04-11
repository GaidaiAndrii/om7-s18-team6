from django.shortcuts import render, redirect
from django.views.generic import ListView

from author.forms import AuthorForm
from order.models import Author

from rest_framework import viewsets
# from .serializers import AuthorSerializer

# # viewes for sprint_18
#
# class AuthorView(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# #___________________________



def author_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AuthorForm()
        else:
            try:
                author = Author.objects.get(pk=id)
            except Author.DoesNotExist:
                return redirect("not_found_404")
            form = AuthorForm(instance=author)
        return render(request, "author/author_form.html", {"form": form})
    else:
        if id == 0:
            form = AuthorForm(request.POST)
        else:
            author = Author.objects.get(pk=id)
            form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
        return redirect('author')


class AuthorList(ListView):
    model = Author
    template_name = "author/index.html"
    context_object_name = "authors"

    def get_context_data(self, **kwargs):
        context = super(AuthorList, self).get_context_data(**kwargs)
        context['title'] = 'Список авторів'
        context['content_title'] = 'Адміністрування бібліотеки / Автори книг'

        return context

    def get_queryset(self):
        queryset = Author.get_all()

        return queryset
