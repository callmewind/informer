from datetime import datetime, timedelta

import environ
import redis
from django.utils.module_loading import import_string
from redis.exceptions import ResponseError

from .base_stats_storage import BaseStatsStorage

env = environ.Env()


class RedisStatsStorage(BaseStatsStorage):
    KEY_TIME_FORMAT = {
        BaseStatsStorage.PERIOD_HOUR: "%Y%m%d%H%M",
        BaseStatsStorage.PERIOD_DAY: "%Y%m%d%H",
        BaseStatsStorage.PERIOD_MONTH: "%Y%m%d"
    }

    client = None

    @classmethod
    def get_connection(cls):
        if not cls.client:
            cls.client = redis.from_url(env.str("STATS_REDIS_URL"))
        return cls.client

    @classmethod
    def get_key(cls, environment, event, period, date):
        return f'count.{environment.site.pk}.{environment.slug}.{event}.{date.strftime(cls.KEY_TIME_FORMAT[period])}'

    @classmethod
    def store_events(cls, environment, events):
        pipeline = cls.get_connection().pipeline()
        now = datetime.now()
        for event in events:
            for period, time_format in cls.KEY_TIME_FORMAT.items():
                key = cls.get_key(environment, event, period, now)
                pipeline.incr(key)
                pipeline.expire(key, int((BaseStatsStorage.PERIOD_DELTA[period] + BaseStatsStorage.PERIOD_STEP[period]).total_seconds()))
        pipeline.execute()

    @classmethod
    def read_stats(cls, environment, event, period):
        pipeline = cls.get_connection().pipeline()
        now = datetime.now()
        date = now - BaseStatsStorage.PERIOD_DELTA[period]
        dates = []
        while date <= now:
            dates.append(date)
            pipeline.get(cls.get_key(environment, event, period, date))
            date = date + BaseStatsStorage.PERIOD_STEP[period]

        return [ (dates[i], int(value or 0)) for i, value in enumerate(pipeline.execute()) ]
