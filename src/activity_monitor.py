import psutil
from AppKit import NSWorkspace
import Quartz
import time

class ActivityMonitor:
    def __init__(self):
        self.workspace = NSWorkspace.sharedWorkspace()
        self.last_active_app = None
        self.last_active_time = time.time()

    def start(self):
        # Start monitoring in a separate thread
        import threading
        self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.monitor_thread.start()

    def _monitor_loop(self):
        while True:
            current_app = self.get_active_application()
            current_time = time.time()
            
            if current_app != self.last_active_app:
                if self.last_active_app:
                    duration = current_time - self.last_active_time
                    # Record the usage of the previous app
                    self.record_app_usage(self.last_active_app, duration)
                
                self.last_active_app = current_app
                self.last_active_time = current_time
            
            time.sleep(1)  # Check every second

    def get_active_application(self):
        active_app = self.workspace.activeApplication()
        return active_app['NSApplicationName']

    def get_idle_time(self):
        idle_time = Quartz.CGEventSourceSecondsSinceLastEventType(
            Quartz.kCGEventSourceStateHIDSystemState,
            Quartz.kCGAnyInputEventType
        )
        return idle_time

    def get_screen_time(self):
        # This is a simplified version. You might want to track this over time.
        return time.time() - psutil.boot_time()

    def record_app_usage(self, app_name, duration):
        # This method should interact with AnalyticsManager
        # For now, we'll just print the information
        print(f"App used: {app_name} for {duration:.2f} seconds")
