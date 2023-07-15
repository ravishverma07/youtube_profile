from googleapiclient.discovery import build
def shorts_videos():
    
 
    api_key = 'AIzaSyDk_TOIY8o-oFxeqZ27fJjC9xW2vBE0fjU'
    playlist_id="PLSraGa7yDc_RE3eT1c8Yu-YRWpxuTJdtL"

    youtube = build('youtube', 'v3', developerKey=api_key)
    playlist_items = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50
    ).execute()


    videos = []
    for item in playlist_items['items']:
        video_title = item['snippet']['title']
        video_id = item['snippet']['resourceId']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        videos.append({'title': video_title, 'id': video_id, 'url': video_url})

    return videos
