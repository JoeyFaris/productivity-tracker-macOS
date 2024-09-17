import json
from datetime import datetime, timedelta
from PyQt5.QtCore import QTimer
from utils import load_app_categories

class AnalyticsManager:
    def __init__(self):
        self.app_usage = {}
        self.app_categories = load_app_categories()
        self.update_timer = QTimer()

    def start_periodic_update(self):
        self.update_timer.timeout.connect(self.update_analytics)
        self.update_timer.start(5 * 60 * 1000)  # Update every 5 minutes

    def update_analytics(self):
        # This method would be called periodically to update analytics
        # It should interact with ActivityMonitor to get current data
        print("Updating analytics...")

    def record_app_usage(self, app_name, duration):
        if app_name not in self.app_usage:
            self.app_usage[app_name] = 0
        self.app_usage[app_name] += duration

    def get_daily_summary(self):
        total_time = sum(self.app_usage.values())
        category_time = self._categorize_usage()
        return {
            "total_time": total_time,
            "category_breakdown": category_time,
            "most_used_apps": self._get_top_apps(5)
        }

    def _categorize_usage(self):
        category_time = {}
        for app, duration in self.app_usage.items():
            category = self.app_categories.get(app, "Uncategorized")
            if category not in category_time:
                category_time[category] = 0
            category_time[category] += duration
        return category_time

    def _get_top_apps(self, n):
        sorted_apps = sorted(self.app_usage.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_apps[:n])

    def generate_heatmap_data(self):
        # Placeholder for generating heatmap data
        # This would return data structured for easy heatmap visualization
        return {}

    def generate_productivity_report(self, start_date, end_date):
        # Generate a report for a specific time range
        report = {
            "total_time": self.get_total_time(start_date, end_date),
            "productivity_score": self.calculate_productivity_score(start_date, end_date),
            "most_productive_day": self.get_most_productive_day(start_date, end_date),
            "category_breakdown": self.get_category_breakdown(start_date, end_date),
            "top_apps": self.get_top_apps(5, start_date, end_date)
        }
        return report

    def calculate_productivity_score(self, start_date, end_date):
        # Calculate productivity score based on app categories
        productive_time = sum(duration for app, duration in self.app_usage.items() 
                              if self.app_categories.get(app, "Uncategorized") in ["Productivity", "Development"])
        total_time = sum(self.app_usage.values())
        return (productive_time / total_time) * 100 if total_time > 0 else 0

    def get_most_productive_day(self, start_date, end_date):
        # Placeholder: Return the day with the highest productivity score
        return start_date  # For now, just return the start date

    def get_category_breakdown(self, start_date, end_date):
        # Similar to _categorize_usage, but for a specific date range
        return self._categorize_usage()  # Simplified for now

    def get_total_time(self, start_date, end_date):
        # Calculate total tracked time for the given date range
        return sum(self.app_usage.values())  # Simplified for now

    def get_top_apps(self, n, start_date, end_date):
        # Placeholder: Return the top apps for the given date range
        return self._get_top_apps(n)
