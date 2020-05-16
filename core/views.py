# -*- coding: utf-8 -*-
from django.contrib import messages
# from django.db.models import Q
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views import View

from .forms import *
# from django.views.generic import ListView, DetailView
from .models import *
from .parser import *


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = ParserForm(self.request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'home.html', context=context)

    def post(self, request, *args, **kwargs):
        form = ParserForm(self.request.POST or None)
        if form.is_valid():
            url = form.cleaned_data['url']
            titles, urls = youparser(url)
            if titles is not None:
                imgs = titles.get('thumbnail')
                title = titles.get('title')
                descriptions = titles.get('shortDescription')
                max_width = 0
                for img in imgs.get('thumbnails'):
                    if max_width < img.get('width'):
                        max_width = img.get('width')
                        title_url = img.get('url')
            else:
                title = 'Название не найдено'
                title_url = 'img/noavatar.png'
                descriptions = 'Описание не найдено'
                messages.info(request, "Не удалось спарсить...")
                return render(request, 'home.html', context={})
            video_set = []
            for url in urls:
                video_set.append({
                    'url': url.get('url'),
                    'quality': url.get('qualityLabel'),
                    'fps': url.get('fps'),
                    'bitrate': int(url.get('bitrate') / 1024),
                    'mimetype': url.get('mimeType')
                })
            context = {
                'form': form,
                'title': title,
                'descriptions': descriptions,
                'title_url': title_url,
                'videoset': video_set
            }
            return render(request, 'home.html', context=context)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm(self.request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'contacts.html', context=context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(self.request.POST or None)
        if form.is_valid():
            message = Contact()
            message.guest_user = form.cleaned_data['user']
            message.content = form.cleaned_data['content']
            message.save()
            return redirect('home_view_url', permanent=True)
