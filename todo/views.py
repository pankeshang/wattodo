# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
import django.http as http
from django.template import RequestContext

import math
import random

from todo.models import Todo
import todo.models as models

# Create your views here.

from django.views.generic import View
from django.core.urlresolvers import reverse


def index(request):
    return render_to_response("todo/index.html", locals(), context_instance=RequestContext(request))


def add_item(request):

    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return http.HttpResponseRedirect(reverse("items"))
    return render_to_response("todo/item.html", locals(), context_instance=RequestContext(request))


def delete_item(request, item_id):
    try:
        item = Todo.objects.get(pk=item_id)
    except:
        return http.HttpResponseNotFound('no item found')
    item.delete()
    return http.HttpResponseRedirect(reverse('items'))


class ItemsView(View):
    def get(self, request):
        items = models.Todo.objects.filter(status="active")
        form = ItemForm()
        return render_to_response("todo/items.html", locals(), context_instance=RequestContext(request))

    def post(self, request):
        form = ItemForm(request.POST or None)
        if form.is_valid():
            form.save()


class ItemView(View):
    def get(self, request, item_id):
        try:
            item = Todo.objects.get(pk=item_id)
        except Todo.DoesNotExist:
            return http.HttpResponseNotFound('no item found')
        form = ItemForm(instance=item)
        return render_to_response("todo/item.html", locals(), context_instance=RequestContext(request))

    def post(self, request, item_id):
        try:
            item = Todo.objects.get(pk=item_id)
        except Todo.DoesNotExist:
            return http.HttpResponseNotFound('no item found')
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return http.HttpResponseRedirect(reverse('items'))

        return render_to_response("todo/item.html", locals(), context_instance=RequestContext(request))            

def recommend(request):
    todos = models.Todo.objects.filter(status="active")
    todo_pks = [i.pk for i in todos]
    rand_choice = random.choice(todo_pks)
    todo = todos.get(pk=rand_choice)
    return render_to_response("todo/recommend.html", locals(), context_instance=RequestContext(request))


import django.forms as forms
class ItemForm(forms.ModelForm):
    class Meta:
        model=models.Todo
        fields=['title', 'desc', 'expected_time', 'minimum_timeslot', 'status']
        fields = ['title', 'desc', 'minimum_timeslot']
