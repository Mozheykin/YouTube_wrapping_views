from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Video, Work
from .forms import VideoForm
from threading import Thread
# from ..app import main
from app.main import add_proxy, start_view_video


def not_found(request):
    return render(request, 'statistic/404.html')

@login_required(login_url='not_found')
def statistic(request):
    videos = Video.objects.all()
    work = Work.objects.all()
    context = {'videos': videos, 'work': work}
    return render(request, 'statistic/basic.html', context=context)


@login_required(login_url='not_found')
def add_video(request):
    form = VideoForm

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('main')
    
    context = {'form': form}
    return render(request, 'statistic/add.html', context)


@login_required(login_url='not_found')
def  delete(request, pk):
    video = Video.objects.get(video_id=pk)

    if request.method == 'POST':
        video.delete()
        return redirect('main')
    
    context = {'video': video}
    return render(request, 'statistic/delete.html', context)


@login_required(login_url='not_found')
def change(request, pk):
    video = Video.objects.get(video_id=pk)
    form = VideoForm(instance=video)

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
        return redirect('main')
    

    context = {'form': form}
    return render(request, 'statistic/change.html', context)

def start_app():
    start_view_video('Play:/home/legal/github/youtube_viewer_all/youtube_viewer/db.sqlite3')
    # add_proxy('/home/legal/github/youtube_viewer_all/youtube_viewer/app/proxy_list.txt:/home/legal/github/youtube_viewer_all/youtube_viewer/db.sqlite3')


@login_required(login_url='not_found')
def Play(request):

    if request.method == 'POST':
        startApp = Thread(target=start_app)
        startApp.start()
        return redirect('main')
    
    return render(request, 'statistic/play.html', {})
    