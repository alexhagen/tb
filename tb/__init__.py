import rumps
import datetime

class TimeBlocker:
    def __init__(self):
        self.config = dict(app_name='TimeBlocker')
        self.app = rumps.App(self.config['app_name'])
        self.timer = rumps.Timer(self.on_tick, 5)
        self.set_up_menu()
        #buttons
        #self.app.menu = [buttons]

    def on_tick(self, sender):
        now = datetime.datetime.now()
        if now.weekday() <= 5:
            if ((now.minute >= 25 and now.minute <= 29) or 
                (now.minute >= 55 and now.minute <= 59)):
                    if self.app.title == 'work':
                        rumps.notification("Break", "Time to take a break", "ok")
                    self.app.title = 'break'
            else:
                if self.app.title == 'break':
                    rumps.notification("Work", "Time to work", "ok")
                self.app.title = 'work'

    def set_up_menu(self):
        self.app.title = "work"
        self.timer.start()

    def run(self):
        self.app.run()

def _run_cli():
    tb = TimeBlocker()
    tb.run()

if __name__ == "__main__":
    _run_cli()