from datetime import timedelta

from django.utils.translation import gettext_lazy as _


class BaseStatsStorage:
    PERIOD_HOUR = "hour"
    PERIOD_DAY = "day"
    PERIOD_MONTH = "month"

    PERIODS = (
        (PERIOD_DAY, _("day")),
        (PERIOD_HOUR, _("hour")),
        (PERIOD_MONTH, _("month")),
    )

    FORMAT = {PERIOD_HOUR: "%H:%M", PERIOD_DAY: "%H:00", PERIOD_MONTH: "%d"}

    PERIOD_DELTA = {
        PERIOD_HOUR: timedelta(hours=1),
        PERIOD_DAY: timedelta(days=1),
        PERIOD_MONTH: timedelta(days=30),
    }

    PERIOD_STEP = {
        PERIOD_HOUR: timedelta(minutes=1),
        PERIOD_DAY: timedelta(hours=1),
        PERIOD_MONTH: timedelta(days=1),
    }

    @classmethod
    def store_events(cls, environment, events):
        pass

    @classmethod
    def read_stats(cls, environment, event, period):
        pass