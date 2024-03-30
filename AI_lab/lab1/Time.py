class Time:
    def __init__(self, hour=0, minute=0):
        # Ensure hour is in the range 0 to 29
        if not 0 <= hour <= 32:
            raise ValueError("Hour must be in the range 0 to 29")

        self.hour = hour
        self.minute = minute

    def __str__(self):
        if self.minute < 10:
            return f"{self.hour}:0{self.minute}"
        return f"{self.hour}:{self.minute}"

    def __repr__(self):
        return f"Time(hour={self.hour}, minute={self.minute})"

    def __eq__(self, other):
        if not isinstance(other, Time):
            return TypeError
        return self.hour == other.hour and self.minute == other.minute

    def __lt__(self, other):
        if not isinstance(other, Time):
            return TypeError
        return self.hour * 60 + self.minute < other.hour * 60 + other.minute

    def __le__(self, other):
        if not isinstance(other, Time):
            return TypeError
        return self.hour * 60 + self.minute <= other.hour * 60 + other.minute

    def __gt__(self, other):
        if not isinstance(other, Time):
            return TypeError
        return self.hour * 60 + self.minute > other.hour * 60 + other.minute

    def __ge__(self, other):
        if not isinstance(other, Time):
            return TypeError
        return self.hour * 60 + self.minute >= other.hour * 60 + other.minute

    def __ne__(self, other):
        if not isinstance(other, Time):
            return TypeError
        return self.hour != other.hour or self.minute != other.minute
