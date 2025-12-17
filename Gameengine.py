# game_engine.py

import random
import time
from models import Batter, Pitcher, Team # <--- models.py에서 필요한 클래스들을 불러옵니다.

class GameEngine:
    def __init__(self, home_team, away_team):
        self.home = home_team
        self.away = away_team
        self.inning = 1
        self.top_bottom = "초" 
        self.outs = 0
        self.bases = [None, None, None]
        self.current_batter_idx = {home_team: 0, away_team: 0}

    # 이전 코드의 print_scoreboard, trigger_random_event, resolve_at_bat, 
    # handle_hit, play_inning, is_game_over 메서드를 그대로 여기에 옮깁니다.
    
    # 예시: print_scoreboard 메서드
    def print_scoreboard(self):
        print(f"\n=== {self.inning}회 {self.top_bottom} ===")
        print(f"[{self.away.name}] {self.away.score} vs {self.home.score} [{self.home.name}]")
        # ... 이하 생략 ...

    # 예시: resolve_at_bat 메서드
    def resolve_at_bat(self, batter, pitcher, strategy="normal"):
        # ... 이하 이전 코드와 동일 ...
        pass
    
    # ... 나머지 모든 경기 로직 메서드들을 여기에 붙여넣습니다. ...
    
    def play_inning(self):
        # ... 이하 이전 코드와 동일 ...
        pass
        
    def is_game_over(self):
        return self.inning > 9
