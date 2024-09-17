import json
import os
from datetime import datetime

class DataManager:
    def __init__(self, data_dir='data'):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

    def save_daily_data(self, date, data):
        filename = os.path.join(self.data_dir, f"{date.strftime('%Y-%m-%d')}.json")
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_daily_data(self, date):
        filename = os.path.join(self.data_dir, f"{date.strftime('%Y-%m-%d')}.json")
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return None

    def get_data_range(self, start_date, end_date):
        data = {}
        current_date = start_date
        while current_date <= end_date:
            daily_data = self.load_daily_data(current_date)
            if daily_data:
                data[current_date.strftime('%Y-%m-%d')] = daily_data
            current_date += datetime.timedelta(days=1)
        return data
