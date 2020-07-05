from datetime import datetime, timedelta
import os
import json

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from ..models import Video
from ..utils import log


class YoutubeVideoSearch:

    """
        Initalizes a youtube search object
    """
    def __init__(self):
        self.DEVELOPER_KEYS = os.environ.get('FAMPAY_DEVELOPER_KEYS').split(',')
        self.DEVELOPER_KEY = self.DEVELOPER_KEYS[0]
        self.YOUTUBE_API_VERSION = 'v3'
        self.YOUTUBE_API_SERVICE_NAME = 'youtube'
        self.SEARCH_TERM = 'cricket'
        self.SEARCH_TYPE = 'video'
        self.MAX_RESULTS = 50
        self.MAX_RETRIES = int(os.environ.get('FAMPAY_SEARCH_MAX_RETRIES'))

    """
        Calls Youtube Search API and stores data in DB. Support for Multiple API Keys to handle quota exceeded.
    """
    def youtube_search(self, retry=0):
        try:
            youtube = build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION,
                            developerKey=self.DEVELOPER_KEY)
            if self.is_video_exist():
                published_after = (datetime.now() - timedelta(minutes=1)).isoformat() + 'Z'
            else:
                published_after = (datetime.now() - timedelta(days=100)).isoformat() + 'Z'

            # Call the search.list method to retrieve results matching the specified
            # query term.
            search_response = youtube.search().list(
                q=self.SEARCH_TERM,
                type=self.SEARCH_TYPE,
                part='id,snippet',
                maxResults=self.MAX_RESULTS,
                publishedAfter=published_after
            ).execute()

            for search_result in search_response.get('items', []):
                self.save_video(search_result)
        except HttpError as ex:
            if ex.resp.status == 403 and json.loads(ex.content.decode()).get('error').get('errors')[0].get('domain') == 'youtube.quota' \
                    and retry <= self.MAX_RETRIES and self.change_api_key():
                self.youtube_search(retry + 1)

            log('Fetching Youtube videos', format(ex), 'error')
        except Exception as ex:
            log('Fetching Youtube videos', format(ex), 'error')

    """
        Check whether any record exist in db or not
    """
    @classmethod
    def is_video_exist(cls):
        return Video.objects.exists()

    """
        Saves video details in DB
    """
    @classmethod
    def save_video(cls, video_result):
        video = Video()
        try:
            snippet = video_result.get('snippet')
            video.title = snippet.get('title')
            video.description = snippet.get('description')
            video.thumbnails = snippet.get('thumbnails')
            video.published_at = snippet.get('publishedAt')
            video.video_id = video_result.get('id').get('videoId')
            video.save()
        except Exception as ex:
            log('Saving Youtube video', format(ex), 'error')

    """
        If API Key limit is exceeded, changes the API Key
    """
    def change_api_key(self):
        index = self.DEVELOPER_KEYS.index(self.DEVELOPER_KEY)
        if index + 1 < len(self.DEVELOPER_KEYS):
            self.DEVELOPER_KEY = self.DEVELOPER_KEYS[index + 1]
            return True

        return False
