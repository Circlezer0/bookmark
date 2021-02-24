from django.shortcuts import render
from django.views.generic.list import ListView  # BookmarkListView관련
from .models import Bookmark
###############################
from django.views.generic.edit import CreateView  # Createview관련
from django.urls import reverse_lazy
###############################
from django.views.generic.detail import DetailView  # detailview 관련
###############################
from django.views.generic.edit import UpdateView  # Modifyview 관련
###############################
from django.views.generic.edit import DeleteView #Deleteview 관련


class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 3
    template_name = "bookmark/bookmark_list.html"


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list') #쓰기 완료 후 이동할 페이지
    template_name_suffix = '_create'


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')


