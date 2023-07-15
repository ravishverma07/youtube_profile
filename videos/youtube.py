from googleapiclient.discovery import build


def get_youtube_videos(page_token, max_result=10):
    api_key = 'AIzaSyDk_TOIY8o-oFxeqZ27fJjC9xW2vBE0fjU'
    youtube = build('youtube', 'v3', developerKey=api_key)
    search_response = youtube.search().list(
        part='snippet',
        channelId='UC0Gyc4vwq_--RhJFxCfofZQ',
        maxResults=max_result,
        pageToken=page_token
    ).execute()

    videos = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video = {
                'title': search_result['snippet']['title'],
                'video_id': search_result['id']['videoId'],
                'thumbnail': search_result['snippet']['thumbnails']['default']['url']
            }
            videos.append(video)

    next_page_token = search_response.get('nextPageToken')
    
    return videos, next_page_token


                                                                        