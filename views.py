from django.shortcuts import render
from django.template.defaultfilters import slugify

def home(request):
    return render(request, 'content/home.html')

def news(request):
    return render(request, 'content/news.html')

def about(request):
    return render(request, 'content/about.html')

def products(request):
    return render(request, 'content/products.html')

def photos(request, slug):
    photos = [
            {'id': '71', 'name': 'Young Earl', 'style': 'top: 0;', 'date': 'Jun 6 2011 9:39 AM'},
            {'id': '70', 'name': 'Unplugged', 'style': 'top: 0.5px;', 'date': 'Jun 6 2011 9:39 AM'},
            {'id': '69', 'name': 'Studio', 'style': 'top: 0;', 'date': 'Jun 6 2011 9:39 AM'},
            {'id': '68', 'name': 'Rosette', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:39 AM'},
            {'id': '67', 'name': 'Playing10', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:39 AM'},
            {'id': '66', 'name': 'Playing9', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:39 AM'},
            {'id': '65', 'name': 'Playing8', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:39 AM'},
            {'id': '64', 'name': 'Playing7', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:40 AM'},
            {'id': '63', 'name': 'Playing6', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:40 AM'},
            {'id': '62', 'name': 'Playing5', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:40 AM'},
            {'id': '61', 'name': 'Playing4', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:40 AM'},
            {'id': '60', 'name': 'Playing3', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:40 AM'},
            {'id': '59', 'name': 'Playing2', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:40 AM'},
            {'id': '58', 'name': 'Playing1', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:40 AM'},
            {'id': '57', 'name': 'Outside', 'style': 'top: 0;', 'date': 'Jun 6 2011 9:40 AM'},
            {'id': '56', 'name': 'Headstock2', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:40 AM'},
            {'id': '55', 'name': 'Headstock1', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:40 AM'},
            {'id': '54', 'name': 'Earl Drum', 'style': 'top: 13px;', 'date': 'Jun 6 2011 9:41 AM'},
            {'id': '53', 'name': 'Earl3', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:41 AM'},
            {'id': '52', 'name': 'Earl2', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:41 AM'},
            {'id': '51', 'name': 'Earl1', 'style': 'top: 20.5px;', 'date': 'Jun 6 2011 9:42 AM'},
            {'id': '49', 'name': 'Bo Bice', 'style': 'top: 15px;', 'date': 'Jun 6 2011 9:45 AM'},
    ]
    if slug is None:
        return render(request, 'content/photos/gallery.html', {"photos": photos})
    else:
        for photo in photos:
            if slug == slugify(photo['name']):
                return render(request, 'content/photos/photo.html', {'photo': photo})
