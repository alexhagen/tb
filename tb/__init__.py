#!/usr/env/bin python
"""TimeBlocker - a small menu app that changes title for time blocking."""
import datetime
import rumps

class TimeBlocker:
    """A small menu app object that changes title for time blocking."""
    def __init__(self):
        self.config = dict(app_name='TimeBlocker')
        self.app = rumps.App(self.config['app_name'])
        self.timer = rumps.Timer(self.on_tick, 5)
        self.config = dict(start='pause')
        self.pause = False
        self.start_pause_button = rumps.MenuItem(title='pause', callback=self.toggle_pause)
        self.set_up_menu()
        self.app.menu = [self.start_pause_button]
        #buttons
        #self.app.menu = [buttons]

    def toggle_pause(self, sender):
        """Toggle the menu from start to paused on click."""
        if self.pause:
            self.app.title = 'checking'
            sender.title = 'pause'
            self.pause = False
        else:
            self.app.title = 'paused'
            sender.title = 'start'
            self.pause = True

    def on_tick(self, _):
        """Check minute and perform actions if a break."""
        now = datetime.datetime.now()
        is_weekday = (now.weekday() <= 5)
        is_workhour = (now.hour >= 7 and now.hour <= 16)
        is_top_of_the_hour = (now.minute >= 25 and now.minute <= 29)
        is_bottom_of_the_hour = (now.minute >= 55 and now.minute <= 59)
        is_break = is_top_of_the_hour or is_bottom_of_the_hour
        if is_weekday and is_workhour and not self.pause:
            if is_break:
                if self.app.title == 'work':
                    rumps.notification("Break", "Time to take a break", "ok")
                self.app.title = 'break'
            else:
                if self.app.title == 'break':
                    rumps.notification("Work", "Time to work", "")
                self.app.title = 'work'

    def set_up_menu(self):
        """Set up the menu items for the menu bar."""
        self.app.title = "work"
        self.timer.start()

    def run(self):
        """Run the the main loop of the app."""
        self.app.run()

def _run_cli():
    time_blocker = TimeBlocker()
    time_blocker.run()

if __name__ == "__main__":
    _run_cli()