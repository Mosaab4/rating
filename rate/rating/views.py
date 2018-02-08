# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Doctor,University,Faculty


class UniversityListView(ListView):
    model = University
    template_name = 'home.html'
    context_object_name = 'univs'


