

class Televition:
    def __init__(self):
        self.channel = int(1)
        self.volume = int(50)
        self.on = bool(False)

    def turn_on(self):
        self.on = True
        print("The TV is now on")

    def turn_off(self):
        self.on = False
        print("TV is now off")

    def volume_up(self, amount=1):
        if self.on:
            if self.volume + amount > 100:
                self.volume = 100
            else:
                self.volume += amount
        print(self.volume)


    def volume_down(self, amount=1):
        if self.on:
            if self.volume - amount < 0:
                print("Volume is at min")
            else:
                self.volume -= amount
        print(self.volume)

    def channel_up(self, amount=1):
        if self.on:
            if self.channel + amount > 999:
                self.channel = 999
            else:
                self.channel += amount
        print(self.channel)

    def channel_down(self, amount=1):
        if self.on:
            if self.channel + amount > 999:
                self.channel = 999
            else:
                self.channel += amount
        print(self.channel)

    def __str__(self) -> str:
        return f"Channel: {self.channel} Volume: {self.volume} On: {self.on}"

tv = Televition()
tv.turn_on()
tv.volume_up(100)
tv.channel_up(1000)
print(tv)
tv.volume_down(5)
tv.channel_down(60)
print(tv)
tv.turn_off()
tv.volume_up(100)
print(tv)