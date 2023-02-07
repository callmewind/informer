from datetime import timedelta

from django.utils.translation import gettext_lazy as _


class BaseSeriesStorage:
    PERIOD_HOUR = "hour"
    PERIOD_DAY = "day"
    PERIOD_MONTH = "month"

    PERIODS = (
        (PERIOD_DAY, _("day")),
        (PERIOD_HOUR, _("hour")),
        (PERIOD_MONTH, _("month")),
    )

    FORMATS = {PERIOD_HOUR: "%H:%M", PERIOD_DAY: "%H:%M", PERIOD_MONTH: "%d"}

    PERIOD_DELTAS = {
        PERIOD_DAY: timedelta(days=1),
        PERIOD_HOUR: timedelta(hours=1),
        PERIOD_MONTH: timedelta(days=30),
    }

    PERIOD_STEPS = {
        PERIOD_HOUR: timedelta(minutes=1),
        PERIOD_DAY: timedelta(minutes=30),
        PERIOD_MONTH: timedelta(days=1),
    }

    @classmethod
    def store_event(cls, environment, event):
        pass

    @classmethod
    def read_series(cls, environment, event, period):
        pass
