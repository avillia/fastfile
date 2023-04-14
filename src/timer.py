from datetime import datetime, timezone


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self):
        self.started_at: datetime | None = None
        self._finished_at: datetime | None = None

    def start(self) -> None:
        if self.started_at is not None:
            raise TimerError("Timer was already started!")
        if self._finished_at is not None:
            raise TimerError("Timers are not reusable; instantiate a new one.")
        self.started_at = datetime.now(timezone.utc)

    def stop(self) -> None:
        if self.started_at is None:
            raise TimerError("Timer was never started!")
        if self._finished_at is not None:
            raise TimerError("Timers are not reusable; instantiate a new one.")
        self._finished_at = datetime.now(timezone.utc)

    @property
    def _time_difference(self):
        return self.started_at - self._finished_at

    def __elapsed__(self):
        return self.started_at and self._finished_at and self._time_difference

    def __float__(self):
        if self.started_at is None:
            raise TimerError("Timer was never started!")
        if self._finished_at is None:
            raise TimerError("Timer was never stopped!")
        return self._time_difference

    def __format__(self, format_spec):
        return self.__float__().__format__(format_spec)

    def __str__(self):
        return str(self.__float__())

    def __repr__(self):
        return (
            f"Timer("
            f"{self.started_at=}, "
            f"{self._finished_at=}, "
            f"{self.__elapsed__()=}"
            f")"
        )
