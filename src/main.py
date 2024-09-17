import sys
from PyQt5.QtWidgets import QApplication
from activity_monitor import ActivityMonitor
from notifications import NotificationManager
from analytics import AnalyticsManager
from ui import MainWindow
from data_manager import DataManager

class ProductivityTracker:
    def __init__(self):
        self.data_manager = DataManager()
        self.activity_monitor = ActivityMonitor()
        self.notification_manager = NotificationManager()
        self.analytics_manager = AnalyticsManager()
        self.main_window = MainWindow(self.analytics_manager)

    def run(self):
        self.activity_monitor.start()
        self.notification_manager.schedule_reminders()
        self.analytics_manager.start_periodic_update()
        self.main_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tracker = ProductivityTracker()
    tracker.run()
    sys.exit(app.exec_())
