import json
import os

def load_app_categories():
    try:
        with open(os.path.join('data', 'app_categories.json'), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Warning: app_categories.json not found. Using empty categories.")
        return {}

def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

def is_productive_app(app_name, productive_apps):
    return app_name in productive_apps

def calculate_productivity_score(productive_time, total_time):
    if total_time == 0:
        return 0
    return (productive_time / total_time) * 100
