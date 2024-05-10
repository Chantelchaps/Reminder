import unittest
from unittest.mock import patch
from io import StringIO
from reminder_manager import ReminderManager

class TestReminderManager(unittest.TestCase):
    def setUp(self):
        self.test_file_path = "test_reminders.csv"

    def test_save_and_get_reminder(self):
        manager = ReminderManager(self.test_file_path)
        manager.save_reminder("email", "test@example.com", "Test Email Reminder")
        manager.save_reminder("sms", "123456789", "Test SMS Reminder")
        manager.save_reminder("audio", "test_audio.mp3")
        reminders = manager.get_reminders()
        self.assertEqual(len(reminders), 3)
        self.assertIsInstance(reminders[0], EmailReminder)
        self.assertIsInstance(reminders[1], SMSReminder)
        self.assertIsInstance(reminders[2], AudioReminder)

    def test_save_and_get_reminder_file_operations(self):
        manager = ReminderManager(self.test_file_path)
        manager.save_reminder("email", "test@example.com", "Test Email Reminder")
        manager.save_reminder("sms", "123456789", "Test SMS Reminder")
        manager.save_reminder("audio", "test_audio.mp3")
        reminders = manager.get_reminders()
        with open(self.test_file_path, "r") as file:
            csv_content = file.read()
            self.assertIn("email,test@example.com,Test Email Reminder\n", csv_content)
            self.assertIn("sms,123456789,Test SMS Reminder\n", csv_content)
            self.assertIn("audio,test_audio.mp3\n", csv_content)

if __name__ == "__main__":
    unittest.main()
