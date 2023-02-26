class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on
        # the same as:
        # if self.is_on:
        #     self.is_on = False
        # else:
        #     self.is_on = True

    def install(self, app, app_memory):
        if self.is_on:
            if app_memory <= self.memory:
                self.apps.append(app)
                self.memory -= app_memory
                return f"Installing {app}"

            return f"Not enough memory to install {app}"

        return f"Turn on your phone to install {app}"

    def status(self):
        total_apps_count = len(self.apps)
        memory_left = self.memory
        return f"Total apps: {total_apps_count}. Memory left: {memory_left}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
