from PyQt5.QtCore import QTimer
from plyer import notification

class NotificationManager:
    def __init__(self):
        self.timer = QTimer()

    def schedule_reminders(self):
        # Schedule periodic reminders
        self.timer.timeout.connect(self.send_reminder)
        self.timer.start(60 * 60 * 1000)  # Every hour

    def send_reminder(self):
        notification.notify(
            title="Productivity Reminder",
            message="Take a break and refocus!",
            app_icon=None,  # e.g. "path/to/icon.png"
            timeout=10,
        )

    def send_app_usage_alert(self, app_name, duration):
        notification.notify(
            title="Excessive App Usage",
            message=f"You've been using {app_name} for {duration} minutes.",
            app_icon=None,
            timeout=10,
        )
