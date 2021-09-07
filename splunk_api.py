import os
import sys

try:
    import splunklib
    import splunklib.client as connect
    import splunklib.results as results
except ImportError:
    print("Trying to install needed libraries:")
    os.system('pip install splunklib')
    os.system('pip install splunk-sdk')
    import splunklib
    import splunklib.client as connect
    import splunklib.results as results

# Notes:
# https://docs.splunk.com/Documentation/PythonSDK

class Splunk_API:

    def __init__(self):
        self.apps = None


    def setup_connection(self):
        HOST = "localhost"
        PORT = 8089
        USERNAME = ""
        PASSWORD = ""
        OWNER = "admin"
        service = splunklib.client.connect(host=HOST, port=PORT, username=USERNAME, password=PASSWORD, owner=OWNER)
        self.apps = service.apps

    def get_apps(self):
        for app in self.service.apps:
            print(app)

    def get_ready_apps(self):
        ready_apps = []
        for ready_app in self.service.apps.check_apps_ready():
            print(ready_app)
            ready_apps.append(ready_app)
        return ready_apps

    def delete_app(self,application):
        self.apps.delete(application)

    def controller(self):
        print("Setting up connection")
        self.setup_connection()  # Can't get an established connection
        print("Getting applications")
        self.get_apps()


if __name__ == '__main__':
    print("Starting Splunk API")
    splunk_obj = Splunk_API()
    splunk_obj.controller()
