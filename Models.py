# models.py

class Player:
    def __init__(self, name):
        self.name = name

class Batter(Player):
    def __init__(self, name, contact, power, speed, eye):
        super().__init__(name)
        self.contact = contact  # 컨택 (안타 확률)
        self.power = power      # 파워 (장타/홈런 확률)
        self.speed = speed      # 주력 (도루/추가 진루)
        self.eye = eye          # 선구안 (볼넷 확률)

class Pitcher(Player):
    def __init__(self, name, control, stuff, velocity, stamina):
        super().__init__(name)
        self.control = control  # 제구 (볼넷 억제/피안타 억제)
        self.stuff = stuff      # 구위 (삼진 확률/장타 억제)
        self.velocity = velocity # 구속 (기본 위압감)
        self.stamina = stamina  # 체력

class Team:
    def __init__(self, name, is_human=False):
        self.name = name
        self.batters = [] # 9명
        self.pitchers = [] # 5명
        self.score = 0
        self.hits = 0
        self.is_human = is_human

    def add_batter(self, batter):
        self.batters.append(batter)

    def add_pitcher(self, pitcher):
        self.pitchers.append(pitcher)

    def get_current_pitcher(self):
        # 현재는 간단하게 첫 번째 투수만 반환
        return self.pitchers[0]
