# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번:21024
# 프로젝트 주제: rpg
def play_game(chapters, character):
    print(f"\n✨ {character['name']}의 인생 시뮬레이션을 시작합니다. ✨")
    
    # [1단계] 과거 업보(2번 또는 4번)를 고른 횟수를 기억할 카운트 변수
    karma_choices_count = 0
    
    # [2단계] 2차원 리스트의 행(질문) 개수만큼 순서대로 반복구조 짜기
    for i in range(len(chapters)):
        scene = chapters[i]
        
        print("\n" + "=" * 60)#줄 넘기고 텍스트 상자 표현
        print(scene[0]) # 질문 출력
        print("-" * 60)
        print(scene[1]) # 선택지 1
        print(scene[2]) # 선택지 2
        print(scene[3]) # 선택지 3
        
        #카르마 조건문
        if i >= 4 and karma_choices_count < 2:
            print("[4번 선택지는 특정 업보 스텟 이상이여야만 고를 수 있습니다.]")
        else:
            print(scene[4])

        print("=" * 60)
        
        # 대답 처리
        while True:
            choice = input("당신의 선택은? (1, 2, 3, 4 중 입력): ")
            
            # 4번 잠겼을때
            if i >= 4 and choice == "4" and karma_choices_count < 2:
                print("⚠ 업보 스텟이 부족하여 이 선택을 할 수 없습니다. 다른 번호를 고르세요.")
                continue
                
            if choice in ["1", "2", "3", "4"]:
                break
            print("⚠ 잘못된 입력입니다. 1부터 4 사이의 숫자만 입력해 주세요.")

        # 선택한 선택지+4=해당 선택지 결과(스토리 보드 리스트 참고)
        result_index = int(choice) + 4
        print(f"\n▶ 결과: {scene[result_index]}")
        
        # 카르마 스텍 쌓는 코드
        if i < 4 and (choice == "2" or choice == "4"):
            karma_choices_count += 1
            
        # 스텟 증가 코드
        if choice == "1":
            if i in [0, 1]:    # 유년기
                character["power"] += 25
            elif i in [2, 3]:  # 청소년기
                character["power"] += 30
            else:              # 청년기
                character["power"] += 35
                
        elif choice == "2":
            if i in [0, 1]:    # 유년기
                character["power"] += 5
                character["intelligence"] += 15
                character["krama"] += 15
            elif i in [2, 3]:  # 청소년기
                # ✏️ [빈칸] 청소년기 2번 선택지 스탯을 직접 채워보세요.
                character["power"] += 10
                character["intelligence"] += 15
                character["krama"] += 15
            else:              # 청년기
                # ✏️ [빈칸] 청년기 2번 선택지 스탯을 직접 채워보세요.
                character["power"] += 15
                character["intelligence"] += 20
                character["krama"] += 20
                
        elif choice == "3":
            if i in [0, 1]:    # 유년기
                character["intelligence"] += 15
                character["tenacity"] += 15
            elif i in [2, 3]:  # 청소년기
                character["intelligence"] += 20
                character["tenacity"] += 20
            else:              # 청년기
                character["intelligence"] += 25
                character["tenacity"] += 25
                
        elif choice == "4":
            if i in [0, 1]:    # 유년기
                character["power"] += 10
                character["krama"] += 20
            elif i in [2, 3]:  # 청소년기
                character["power"] += 20
                character["krama"] += 30
            else:              # 청년기
                character["power"] += 25
                character["krama"] += 40
                
        # 매 라운드가 끝날 때마다 현재 스탯 상황을 예쁘게 출력
        print(f"📊 [현재 스탯] power: {character['power']} | intelligence: {character['intelligence']} | tenacity: {character['tenacity']} | krama: {character['krama']}")

def ending(character):
    print("you made choices and its time to look back.")

    # 5. 히든 엔딩: 성군 (power, intelligence, tenacity가 모두 높은 경우) [cite: 23]
    if character["power"] >= 40 and character["intelligence"] >= 40 and character["tenacity"] >= 40:
        print("👑 [엔딩 5: 성군] 👑")
        print("겉보기에 당신은 문무와 끈기, 인품을 모두 갖춘 완벽한 성인이 되었습니다. 왕국을 다스리는 위대한 성군이 됩니다.")
    
    # 2. 마왕 (power와 krama가 높은 경우) [cite: 23]
    elif character["power"] >= 70 and character["krama"] >= 70:
        print("😈 [엔딩 2: 마왕] 😈")
        print("어둠의 힘과 업보에 굴복한 당신은 왕국을 무너뜨리고 세계를 공포에 몰아넣는 마왕이 되었습니다.")
        
    # 1. 국왕 (intelligence와 tenacity가 높은 경우) [cite: 23]
    elif character["intelligence"] >= 60 and character["tenacity"] >= 60:
        print("📜 [엔딩 1: 통치자] 📜")
        print("현명한 지혜와 백성들을 이끄는 강인한 끈기로 왕국의 정당한 왕이 되어 국가를 번영시킵니다.")
        
    # 3. 용사 (power가 가장 높은 경우)
    elif character["power"] >= character["intelligence"] and character["power"] >= character["tenacity"]:
        print("⚔️ [엔딩 3: 용사] ⚔️")
        print("왕위에는 뜻이 없습니다. 강인한 힘을 바탕으로 대륙의 평화를 지키는 전설적인 용사가 됩니다.")
        
    # 4. 현자 (intelligence가 가장 높은 경우)
    elif character["intelligence"] >= character["krama"] and character["power"] >= character["tenacity"]:
        print("🔮 [엔딩 4: 현자] 🔮")
        print("세상의 모든 진리를 깨달은 당신은 숲속의 탑에 은거하며 학문과 마법을 연구하는 대현자가 되었습니다.")
    # 4+. 머저리 (지성마저 낮을때)
    else:
        print("🔮 [엔딩 6: 머저리] 🔮")
        print("그 많은 선택지들을 뚫고 결국 그 무엇도 달성하지 못하여 왕위계승에서 밀려났습니다.")

story_chapters = [
    # ------------------ 🌱 유년기 (0~1번 인덱스) ------------------
    [
        "🌱 [유년기 1] 골목길에서 맹견이 나타나 동네 아이들을 위협하고 있습니다.",
        "1. 맨손으로 맹견과 맞서 싸워 아이들을 구한다.",
        "2. 주변의 도구를 이용해 맹견을 유인한 뒤 가둔다.",
        "3. 아이들을 진정시키고 차분하게 안전한 곳으로 대피시킨다.",
        "4. 돌을 던져 맹견을 화나게 만든 뒤, 맹견이 다른 곳을 공격하게 유도한다.",
        "온몸이 상처투성이가 되었지만 근육과 힘이 붙었습니다! (power +25)",
        "도구를 쓰는 법과 맹견의 움직임을 계산하며 잔머리를 굴렸습니다. (power +5, intelligence +15, krama +15)",
        "아이들을 무사히 대피시키며 강한 책임감과 지혜를 얻었습니다. (intelligence +15, tenacity +15)",
        "맹견은 쫓아냈지만 마을 다른 곳이 난장판이 되어 원망을 듣습니다. (power +10, krama +20)"
    ],
    [
        "🌱 [유년기 2] 서당에서 스승님이 잠시 자리를 비운 사이, 시험 답안지를 발견했습니다.",
        "1. 답안지를 보는 대신 마당으로 나가 무거운 돌을 들며 체력을 기른다.",
        "2. 답안지를 훔쳐보고 다음 시험 1등을 차지하기 위해 내용을 외운다.",
        "3. 정직하게 자리에 앉아 스승님이 내주신 어려운 문제를 끝까지 풀어낸다.",
        "4. 답안지를 제자리에 두고, 라이벌인 친구의 가방에 몰래 답안지 사본을 넣어 곤경에 빠뜨린다.",
        "스승님께 혼났지만 기초 체력이 단단해졌습니다. (power +25)",
        "답안지를 훔쳐보며 치밀하게 스탯을 올렸습니다. (power +5, intelligence +15, krama +15)",
        "정직함과 인내심으로 스스로 정답을 찾아냈습니다. (intelligence +15, tenacity +15)",
        "라이벌을 제거하고 그 사이에 혼자 훈련을 감행했습니다. (power +10, krama +20)"
    ],

    # ------------------ 🌿 청소년기 (2~3번 인덱스) ------------------
    [
        "🌿 [청소년기 1] 무술 대회 도중, 상대방이 절대 이길 수 없을 정도로 강력한 비기를 준비해 왔습니다.",
        "1. 정면 돌파다! 온 힘을 다해 상대의 비기와 무력으로 맞부딪힌다.",
        "2. 반칙 약물을 몰래 마시고 상대의 기술적 약점을 파고들어 승리한다.",
        "3. 상대의 초식을 관찰하며 방어에 집중해 약점이 나올 때까지 버틴다.",
        "4. 경기 전날 밤, 상대의 무기를 몰래 망가뜨려 놓고 경기장에서 압도적인 힘으로 짓누른다.",
        "엄청난 충격을 견뎌내며 신체 한계를 초월했습니다. (power +30)",
        "약물의 힘과 계산된 수로 상대를 제압했습니다. (power +10, intelligence +15, krama +15)",
        "상대의 움직임을 읽는 지혜와 끈기로 승리를 따냈습니다. (intelligence +20, tenacity +20)",
        "상대는 허무하게 무너졌고 당신은 비열한 승리를 거두었습니다. (power +20, krama +30)"
    ],
    [
        "🌿 [청소년기 2] 왕궁 아카데미 도서관 깊은 곳에서 저주받은 마법 검을 발견했습니다.",
        "1. 저주를 무시하고 오직 검의 순수한 무게와 위력을 지배하기 위해 휘두른다.",
        "2. 저주의 파괴적인 메커니즘을 분석하여 내 힘으로 흡수한다.",
        "3. 검에 걸린 고대 봉인 마법을 해독하고 도서관장에게 안전하게 인도한다.",
        "4. 검의 금기된 봉인을 완전히 풀어 유령들을 깨운 뒤, 그 혼란을 틈타 검을 훔친다.",
        "검의 저주가 육체를 단련시켜 파괴적인 힘을 얻었습니다. (power +30)",
        "금단의 지식과 어둠의 힘이 뇌리에 박힙니다. (power +10, intelligence +15, krama +15)",
        "마법적 지식과 깊은 인품을 증명하여 학자들의 신뢰를 얻습니다. (intelligence +20, tenacity +20)",
        "아카데미가 유령들로 발칵 뒤집혔지만 강대한 무기를 손에 넣었습니다. (power +20, krama +30)"
    ],

    # ------------------ 🔥 청년기 (4~5번 인덱스) ------------------
    [
        "🔥 [청년기 1] 이웃 영지의 군대가 국경을 침범하여 백성들이 약탈당하고 있습니다.",
        "1. 곧바로 기사단을 이끌고 전장의 최전선으로 돌격하여 적들을 궤멸시킨다.",
        "2. 적의 복급로를 끊는 독극물 작전을 제안하고, 퇴로를 차단해 전멸시킨다.",
        "3. 피해를 최소화하기 위해 평화 협상안을 도출하고 끈기 있게 설득한다.",
        "4. 아군 병사들을 미끼로 던져 적들을 방심하게 만든 뒤, 적장의 목을 베어 공을 독차지한다.",
        "전장을 지배하며 대륙 최강의 무력을 증명했습니다. (power +35)",
        "냉혹한 전략으로 아군의 피해 없이 승리를 거두었습니다. (power +15, intelligence +20, krama +20)",
        "훌륭한 외교적 지혜와 인내심으로 전쟁을 막아냈습니다. (intelligence +25, tenacity +25)",
        "수많은 병사가 희생되었지만 적들의 군세를 완벽히 꺾어버렸습니다. (power +25, krama +40)"
    ],
    [
        "🔥 [청년기 2] 성인식을 앞두고, 국왕인 아버지가 위독해지자 간신들이 정변을 일으켰습니다.",
        "1. 궁궐 문을 부수고 들어가 간신들의 목을 직접 베어 아버지를 구한다.",
        "2. 간신들의 약점을 쥐고 있는 세력과 밀약을 맺고 궁중 정치로 권력을 빼앗는다.",
        "3. 간신들의 핍박 속에서도 충신들을 모아 끈기 있게 법적인 정당성을 확보한다.",
        "4. 왕실의 비밀 군대를 동원해 궁궐 전체를 불태워 간신과 반대파를 모두 몰살한다.",
        "반역자들을 힘으로 제압하며 왕국의 진정한 우두머리로 우뚝 섭니다. (power +35)",
        "보이지 않는 피의 군주로서 궁정을 장악했습니다. (power +15, intelligence +20, krama +20)",
        "백성들과 충신들의 거대한 지지를 받으며 정당한 군주로 통치할 준비를 마칩니다. (intelligence +25, tenacity +25)",
        "수많은 피를 흘린 끝에 공포의 군주로 등극하게 됩니다. (power +25, krama +40)"
    ]
]
character = {
    "name": " ",
    "power": 0,          
    "krama": 0,          
    "intelligence": 0,   
    "tenacity": 0        
}

N = input("what is your name?")
character["name"] = N

play_game(story_chapters, character)

ending(character)