import csv
from abc import ABC, abstractmethod
import os


class Reminder(ABC):
    @abstractmethod
    def send(self):
        pass


class EmailReminder(Reminder):
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def send(self):
        print(f"Sending email to {self.recipient}: {self.message}")


class SMSReminder(Reminder):
    def __init__(self, phone_number, message):
        self.phone_number = phone_number
        self.message = message

    def send(self):
        print(f"Sending SMS to {self.phone_number}: {self.message}")


class AudioReminder(Reminder):
    def __init__(self, audio_file):
        self.audio_file = audio_file

    def send(self):
        print(f"Playing audio: {self.audio_file}")


class ReminderFactory(ABC):
    @abstractmethod
    def create_reminder(self, *args, **kwargs):
        pass


class EmailReminderFactory(ReminderFactory):
    def create_reminder(self, *args, **kwargs):
        return EmailReminder(*args, **kwargs)


class SMSReminderFactory(ReminderFactory):
    def create_reminder(self, *args, **kwargs):
        return SMSReminder(*args, **kwargs)


class AudioReminderFactory(ReminderFactory):
    def create_reminder(self, *args, **kwargs):
        return AudioReminder(*args, **kwargs)


class ReminderManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_reminder(self, reminder_factory, *args, **kwargs):
        reminder = reminder_factory.create_reminder(*args, **kwargs)
        with open(self.file_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([reminder_factory.__class__.__name__.replace("ReminderFactory", "").lower(), *args])

    def get_reminders(self):
        reminders = []
        with open(self.file_path, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                reminder_type = row[0]
                if reminder_type == "email":
                    reminder_factory = EmailReminderFactory()
                elif reminder_type == "sms":
                    reminder_factory = SMSReminderFactory()
                elif reminder_type == "audio":
                    reminder_factory = AudioReminderFactory()
                else:
                    raise ValueError("Invalid reminder type")
                reminder = reminder_factory.create_reminder(*row[1:])
                reminders.append(reminder)
        return reminders


if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_directory, "reminders.csv")
    manager = ReminderManager(file_path)

    manager.save_reminder(EmailReminderFactory(), "chantelchaps@gmail.com", "Happy Birthday!")
    manager.save_reminder(SMSReminderFactory(), "+370985767438", "Happy Birthday!")
    manager.save_reminder(AudioReminderFactory(), "birthday_song.mp3")

    reminders = manager.get_reminders()
    for reminder in reminders:
        reminder.send()
