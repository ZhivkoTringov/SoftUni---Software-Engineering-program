class Smartphone:
    apps = []
    is_on = False

    def __init__(self, memory):
        self.memory = memory

    def power(self):
        if not Smartphone.is_on:
            Smartphone.is_on = True

    def install(self, app, app_memory):
        if Smartphone.is_on and app_memory <= self.memory:
            Smartphone.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"
        elif not Smartphone.is_on and app_memory <= self.memory:
            return f"Turn on your phone to install {app}"
        return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(Smartphone.apps)}. Memory left: {self.memory}"