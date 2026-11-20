"""Notifiers: objects that deliver messages to library members."""
from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, member, message):
        """Deliver one message to a member."""

    def send_many(self, members, message):
        for member in members:
            self.send(member, message)


class ConsoleNotifier(Notifier):
    def send(self, member, message):
        print(f"To {member.name}: {message}")


class MemoryNotifier(Notifier):
    def __init__(self):
        self.messages = []

    def send(self, member, message):
        self.messages.append((member.member_id, message))


class LogMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = []

    def send(self, member, message):
        self.log.append(f"{member.member_id}: {message}")
        super().send(member, message)


class LoggingConsoleNotifier(LogMixin, ConsoleNotifier):
    pass
