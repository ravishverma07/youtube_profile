from googleapiclient.discovery import build

def search_youtube_videos(api_key, channel_id, search_query, max_results=9):
    youtube = build('youtube', 'v3', developerKey=api_key)
    search_response = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        q=search_query,
        maxResults=max_results
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

    return videos
