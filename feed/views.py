from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Feed, Comment

# Create your views here.
def feed(request):
    if request.method == 'POST':
        name = request.POST['name']
        content = request.POST['content']
        feed = Feed.objects.create(name=name, content=content)
        return redirect('feed')
    else:
        feeds = Feed.objects.order_by('-created_at')
        return render(request, 'feed.html', {'feeds': feeds})

def detail(request, id):
    feed = get_object_or_404(Feed, pk=id)
    return render(request, 'detail.html', {'feed': feed})

def clearfeed(request):
    feeds = Feed.objects.all()
    feeds.delete()
    return redirect('feed')

def createcomment(request, id):
    feed = get_object_or_404(Feed, pk=id)
    if request.method=='POST':
        name=request.POST['name']
        content=request.POST['content']
        comment = Comment.objects.create(name=name, content=content, feed=feed)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))