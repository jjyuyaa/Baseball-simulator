# main.py

import random
from models import Batter, Pitcher, Team # <--- models.py 에서 Team/Player 클래스를 불러옴
from game_engine import GameEngine      # <--- game_engine.py 에서 GameEngine 클래스를 불러옴

# --- 헬퍼 함수들 (팀 생성) ---

def create_random_team(name):
    t = Team(name, is_human=False)
    # 랜덤 타자 9명
    for i in range(1, 10):
        t.add_batter(Batter(f"{name}타자{i}", random.randint(50,90), random.randint(50,90), random.randint(50,90), random.randint(50,90)))
    # 랜덤 투수 5명
    for i in range(1, 6):
        t.add_pitcher(Pitcher(f"{name}투수{i}", random.randint(60,95), random.randint(60,95), random.randint(130,160), 100))
    return t

def create_user_team():
    # ... 사용자 입력 및 팀 생성 로직 (이전 코드와 동일) ...
    name = input("구단 이름을 입력하세요: ")
    t = Team(name, is_human=True)
    # ... 이하 타자/투수 생성 로직 ...
    
    return t

# === 메인 실행 ===
if __name__ == "__main__":
    print("⚾ Python Baseball Manager 2025 ⚾")
    mode = input("모드 선택 (1.커스텀 팀 만들기  2.빠른 시작): ")
    
    if mode == '1':
        my_team = create_user_team()
    else:
        my_team = create_random_team("플레이어팀")
        my_team.is_human = True 

    opp_team = create_random_team("AI_Robots")

    # GameEngine 클래스를 사용하여 게임 객체 생성
    game = GameEngine(my_team, opp_team) 
    
    print(f"\n📢 플레이볼! {my_team.name} vs {opp_team.name}\n")
    
    while not game.is_game_over():
        game.play_inning()

    print("\n=== 경기 종료 ===")
    if my_team.score > opp_team.score:
        print(f"🎉 {my_team.name} 승리! 🎉")
    # ... 이하 결과 출력 로직 ...
