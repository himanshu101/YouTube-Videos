import json

from django_cron import CronJobBase, Schedule


class SearchYoutubeVideos(CronJobBase):
    RUN_EVERY_MINS = 1  # run every minute
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'catalog.fetch_youtube_videos'

    def do(self):
        from .services.youtube_videos import YoutubeVideoSearch
        YoutubeVideoSearch().youtube_search()

