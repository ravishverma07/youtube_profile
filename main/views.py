from django.shortcuts import render 
from videos.search import search_youtube_videos
from videos.youtube import get_youtube_videos
from videos.shorts  import shorts_videos




api_key = 'AIzaSyDk_TOIY8o-oFxeqZ27fJjC9xW2vBE0fjU'
channel_id = 'UC0Gyc4vwq_--RhJFxCfofZQ'

def home(request):
    page_token = request.GET.get('page_token')
    previous_page_token = request.GET.get('previous_page_token')

    if page_token == 'previous':
        page_token = request.session.get('previous_page_token', '')

    videos, next_page_token = get_youtube_videos(page_token)

    if page_token != 'previous':
        if previous_page_token:
            request.session['previous_page_token'] = previous_page_token
        else:
            request.session.pop('previous_page_token', None)

    context = {
        'videos': videos,
        'next_page_token': next_page_token,
        'page_token': page_token,
        'previous_page_token': previous_page_token,
    }

    return render(request, 'homepage.html', context)





def youtube_videos(request):
    page_token = request.GET.get('page_token')
    previous_page_token = request.GET.get('previous_page_token')

    if page_token == 'previous':
        page_token = request.session.get('previous_page_token', '')

    videos, next_page_token = get_youtube_videos(page_token)

    if page_token != 'previous':
        if previous_page_token:
            request.session['previous_page_token'] = previous_page_token
        else:
            request.session.pop('previous_page_token', None)

    context = {
        'videos': videos,
        'next_page_token': next_page_token,
        'page_token': page_token,
        'previous_page_token': previous_page_token,
    }

    return render(request, 'videos/index.html', context)

def shorts(request):
    videos = shorts_videos()
    context = {
        'videos': videos
    }

    return render(request, 'shorts.html', context)



def about(request):
    return render(request,'about.html') 


def search(request):
    search_query = request.GET.get('search')
    videos= search_youtube_videos(api_key,channel_id,search_query)
    videos = {
        'videos': videos , 'search_query':search_query
    }

    return render(request, 'search.html', videos)
