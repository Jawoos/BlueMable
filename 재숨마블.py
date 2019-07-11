import random
import time


'''
도시 번호
          '타이베이': 0
          '홍콩': 1
          '마닐라': 2,
          '싱가폴': 3
          '카이로': 4
          '이스탄불': 5
          '아테네': 6
          '코펜하겐': 7
          '스톡홀름': 8
          '취리히': 9
          '베를린': 10
          '몬트리올': 11
          '부에노스 아이레스': 12
          '상파울루': 13
          '시드니': 14
          '하와이': 15
          '리스본': 16
          '마드리드': 17
          '도쿄': 18
          '파리': 19
          '로마': 20
          '런던': 21
          '뉴욕': 22
          '제주도':23
          '콩코드':24
          '부산':25
          '서울':26
          '퀸':27
          '콜롬비아호':28
          
'''

def trade():
    try:
        ply_out = input("돈을 인출할 플레이어를 입력해 주세요: ")
        ply_in = input("돈을 받을 플레이어를 입력해 주세요: ")
        money = float(input("금액을 만원 단위로 입력해 주세요: "))

        player[ply_out] = float(player[ply_out])
        player[ply_in] = float(player[ply_in])

        player[ply_out] -= money
        player[ply_in] += money

        print("%s 플레이어의 거래 후 현금 보유액은 %.2f만원 입니다. " % (ply_out, player[ply_out]))
        print("%s 플레이어의 거래 후 현금 보유액은 %.2f만원 입니다. " % (ply_in, player[ply_in]))
    except:
        print("잘못입력하였습니다.")


def withdraw(x):
    try:
        money = float(input("지불해야 할 금액을 입력해 주세요: "))
        player[x] = float(player[x])
        player[x] -= money
        print("%s 플레이어의 현금 보유액은 %.2f만원 입니다. " % (x, player[x]))
    except:
        print("잘못입력하였습니다.")


def pay(x):
    try:
        money = float(input("지급할 금액을 입력해 주세요: "))
        player[x] = float(player[x])
        player[x] += money
        print("%s 플레이어의 현금 보유액은 %.2f만원 입니다. " % (x, player[x]))
    except:
        print("잘못입력하였습니다.")




def build(x):
    try:
        print("어떠한 건물을 지으시겠습니까?\n1.별장\n2.빌딩\n3.호텔")
        structure = int(input())
        if structure == 1:
            home = int(input("몇개 지으시겠습니까? : "))
            if home >= 3:
                print("별장은 최대 2개까지 지을수 있습니다.")
            else:
                cities[x][3] = home
                print("%s도시의 건물 현황은 별장 %d개, 빌딩 %d개, 호텔 %d개 입니다." % (x, cities[x][3], cities[x][4], cities[x][5]))
        elif structure == 2:
            cities[x][4] = 1
            print("%s도시의 건물 현황은 별장 %d개, 빌딩 %d개, 호텔 %d개 입니다." % (x, cities[x][3], cities[x][4], cities[x][5]))
        elif structure == 3:
            cities[x][5] = 1
            print("%s도시의 건물 현황은 별장 %d개, 빌딩 %d개, 호텔 %d개 입니다." % (x, cities[x][3], cities[x][4], cities[x][5]))
    except:
        print("잘못입력하였습니다.")


def toll(x):                 #통행료 계산, 인자로 도시 이름을 받음
    list_0 = cities.get(x)   #도시 정보 리스트로 저장
    num = list_0[0]          #입력 받은 도시의 도시번호
    if list_0[3] ==0 and list_0[4] == 0 and list_0[5] == 0:
        num_1 = price[num][3]
    else:
        num_1 = float(price[num][4])*int(list_0[3]) + float(price[num][5])*int(list_0[4]) + float(price[num][6])*int(list_0[5])
    return num_1*price[num][0]


def sell(y):                    #판매 가격을 확인, 인자로 도시 이름을 받음
    list_1 = cities.get(y)      #도시 정보 리스트로 저장
    num = list_1[0]             #도시의 번호
    if 0 <= num <= 5:
        if num == 0:
            num_1 = 5 + int(list_1[3]) * 5 + int(list_1[4]) * 15 + int(list_1[5]) * 25
        elif 1<= num <= 2:
            num_1 = 8 + int(list_1[3]) * 5 + int(list_1[4]) * 15 + int(list_1[5]) * 25
        elif 3<= num <= 4:
            num_1 = 10 + int(list_1[3]) * 5 + int(list_1[4]) * 15 + int(list_1[5]) * 25
        elif num == 5:
            num_1 = 12 + int(list_1[3]) * 5 + int(list_1[4]) * 15 + int(list_1[5]) * 25
    elif 6 <= num <= 11:
        if num == 6:
            num_1 = 14 + int(list_1[3]) * 10 + int(list_1[4]) * 30 + int(list_1[5]) * 50
        elif 7<= num <= 8:
            num_1 = 16 + int(list_1[3]) * 10 + int(list_1[4]) * 30 + int(list_1[5]) * 50
        elif 9<= num <= 10:
            num_1 = 18 + int(list_1[3]) * 10 + int(list_1[4]) * 30 + int(list_1[5]) * 50
        elif num == 11:
            num_1 = 20 + int(list_1[3]) * 10 + int(list_1[4]) * 30 + int(list_1[5]) * 50
    elif 12 <= num <= 17:
        if num == 12:
            num_1 = 22 + int(list_1[3]) * 15 + int(list_1[4]) * 45 + int(list_1[5]) * 75
        elif 13<= num <= 14:
            num_1 = 24 + int(list_1[3]) * 15 + int(list_1[4]) * 45 + int(list_1[5]) * 75
        elif 15<= num <= 16:
            num_1 = 26 + int(list_1[3]) * 15 + int(list_1[4]) * 45 + int(list_1[5]) * 75
        elif num == 17:
            num_1 = 28 + int(list_1[3]) * 15 + int(list_1[4]) * 45 + int(list_1[5]) * 75
    elif 18 <= num <= 22:
        if num == 18:
            num_1 = 30 + int(list_1[3]) * 20 + int(list_1[4]) * 60 + int(list_1[5]) * 100
        elif 19<= num <= 20:
            num_1 = 32 + int(list_1[3]) * 20 + int(list_1[4]) * 60 + int(list_1[5]) * 100
        elif 21<= num <= 22:
            num_1 = 35 + int(list_1[3]) * 20 + int(list_1[4]) * 60 + int(list_1[5]) * 100
    elif 23 <= num <= 28:
        if num == 23:
            num_1 = 30
        elif num == 24:
            num_1 = 30
        elif num == 25:
            num_1 = 60
        elif num == 26:
            num_1 = 200
        elif num == 27:
            num_1 = 25
        elif num == 28:
            num_1 = 40
    return num_1*price[num][0]


def tp():       #시세를 랜덤으로 조정
    for i in range(0, 29):
        if price[i][0] > 1:
            r = random.randint(0, 100)
            if r > 90:
                price[i][2] = price[i][1]
                price[i][1] = price[i][0]
                price[i][0] *= (random.randint(90, 135) / 100)
            elif r == 23:
                price[i][2] = price[i][1]
                price[i][1] = price[i][0]
                price[i][0] *= (random.randint(70, 170) / 100)
            else:
                price[i][2] = price[i][1]
                price[i][1] = price[i][0]
                price[i][0] *= (random.randint(95, 120) / 100)
        elif price[i][0] == 1:
            r = random.randint(0, 100)
            if r > 90:
                price[i][2] = price[i][1]
                price[i][1] = price[i][0]
                price[i][0] *= (random.randint(80, 120) / 100)
            elif r == 23:
                price[i][2] = price[i][1]
                price[i][1] = price[i][0]
                price[i][0] *= (random.randint(50, 150) / 100)
            else:
                price[i][2] = price[i][1]
                price[i][1] = price[i][0]
                price[i][0] *= (random.randint(95, 110) / 100)
        elif price[i][0] < 1:
            r = random.randint(0, 100)
            if r > 90:
                price[i][2] = price[i][1]
                price[i][1] = price[i][0]
                price[i][0] *= (random.randint(65, 110) / 100)
            elif r == 23:
                price[i][2] = price[i][1]
                price[i][1] = price[i][0]
                price[i][0] *= (random.randint(30, 120) / 100)
            else:
                price[i][2] = price[i][1]
                price[i][1] = price[i][0]
                price[i][0] *= (random.randint(80, 105) / 100)


stack = 0       #시세 실행 차수 저장
num = 0
num_pl = 1      #플레이어 수
menu = 10       #메뉴선택 입력 받는 숫
player = {}     #플레이어 정보 저장할 딕셔너리
name = ""       #플레이어 이름을 전달할 문자열
city = ""       #시세를 확인할 도시 이름
list_0 = []     #받은 도시정보 임시 전달
price = []      #도시 변동사항 & 상황별 통행료
list_name = []  #플레이어 전체 이름 저장


price = [[1, 1, 1, 0.2, 1, 9, 25],         #타이베이      #[등락폭,, 전등락폭, 전전등락폭, 토지값, 별장하나, 빌딩, 호텔]
         [1, 1, 1, 0.4, 2, 18, 45],        #홍콩
         [1, 1, 1, 0.4, 2, 18, 45],        #마닐라
         [1, 1, 1, 0.6, 3, 27, 55],        #싱가폴
         [1, 1, 1, 0.6, 3, 27, 55],        #카이로
         [1, 1, 1, 0.8, 4, 30, 60],        #이스탄불
         [1, 1, 1, 1, 5, 45, 75],          #아테네
         [1, 1, 1, 1.2, 6, 50, 90],        #코펜하겐
         [1, 1, 1, 1.2, 6, 50, 90],        #스톡홀름
         [1, 1, 1, 1.4, 7, 50, 95],        #취리히
         [1, 1, 1, 1.4, 7, 50, 95],       #베를린
         [1, 1, 1, 1.6, 8, 55, 100],      #몬트리올
         [1, 1, 1, 1.8, 9, 70, 105],      #부에노스 아이레스
         [1, 1, 1, 2, 10, 75, 110],       #상파울루
         [1, 1, 1, 2, 10, 75, 110],       #시드니
         [1, 1, 1, 2.2, 11, 80, 115],     #하와이
         [1, 1, 1, 2.2, 11, 80, 115],     #리스본
         [1, 1, 1, 2.4, 12, 85, 120],     #마드리드
         [1, 1, 1, 2.6, 13, 90, 127],     #도쿄
         [1, 1, 1, 2.8, 15, 100, 140],    #파리
         [1, 1, 1, 2.8, 15, 100, 140],    #로마
         [1, 1, 1, 3.5, 17, 110, 150],    #런던
         [1, 1, 1, 3.5, 17, 110, 150],    #뉴욕
         [1, 1, 1, 30],                   #제주도
         [1, 1, 1, 30],                   #콩코드
         [1, 1, 1, 60],                   #부산
         [1, 1, 1, 200],                  #서울
         [1, 1, 1, 25],                   #퀸
         [1, 1, 1, 40]]                   #콜롬비아호


cities = {'타이베이': [0, 0, 0, 0, 0, 0],       #[도시 번호, 통행료, 매매가, 별장, 빌딩, 호텔]
          '홍콩': [1,0, 0, 0, 0, 0],
          '마닐라': [2, 0, 0, 0, 0, 0],
          '싱가폴': [3, 0, 0, 0, 0, 0],
          '카이로': [4, 0, 0, 0, 0, 0],
          '이스탄불': [5, 0, 0, 0, 0, 0],
          '아테네': [6, 0, 0, 0, 0, 0],
          '코펜하겐': [7, 0, 0, 0, 0, 0],
          '스톡홀름': [8, 0, 0, 0, 0, 0],
          '취리히': [9, 0, 0, 0, 0, 0],
          '베를린': [10, 0, 0, 0, 0, 0],
          '몬트리올': [11, 0, 0, 0, 0, 00],
          '부에노스 아이레스': [12, 0, 0, 0, 0, 0],
          '상파울루': [13, 0, 0, 0, 0, 0],
          '시드니': [14, 0, 0, 0, 0, 0],
          '하와이': [15, 0, 0, 0, 0, 0],
          '리스본': [16, 0, 0, 0, 0, 0],
          '마드리드': [17, 0, 0, 0, 0, 0],
          '도쿄': [18, 0, 0, 0, 0, 0],
          '파리': [19, 0, 0, 0, 0, 0],
          '로마': [20, 0, 0, 0, 0, 0],
          '런던': [21, 0, 0, 0, 0, 0],
          '뉴욕': [22, 0, 0, 0, 0, 0],
          '제주도': [23, 0, 0, 0, 0, 0],
          '콩코드': [24, 0, 0, 0, 0, 0],
          '부산': [25, 0, 0, 0, 0, 0],
          '콜롬비아호': [28, 0, 0, 0, 0, 0],
          '서울': [26, 0, 0, 0, 0, 0],
          '퀸': [27, 0, 0, 0, 0, 0]}


num_pl = int(input("게임을 플레이할 플레이어 수를 입력해 주세요(0 입력시 종료) : "))


if num_pl == 0:
    print("프로그램을 종료합니다...\n다음에 다시 뵈요~")


else:

    for i in range (0, num_pl):
        name = input("%d번째 플레이어 이름을 입력해 주세요 : "%(i+1))
        player[name] = 300

    print("게임을 시작합니다!!!")
    t1 = time.time()

    while True:
        print("\n")
        print("**********"*3)
        print("다음중 진행할 것을 선택해 주세요.\n0. 턴 진행\n1. 시세확인\n2. 건물추가\n3. 돈 지급\n4. 돈 감소\n"
              "5. 돈 거래\n6. 모든 플레이어 현금 보유액 확인\n7. 게임 종료")
        try:
            menu = int(input())
        except:
            print("잘못입력하였습니다. 다시 입력해주세요.")

        if menu == 0:
            print("턴을 진행합니다.")
            stack += 1
            tp()
            print("시세변동을 확인하세요!!!")
            print("**********"*12)
            print("%d차 시세" %stack)
            print("노란색\t\t\t\t하늘색\t\t\t\t군청색\t\t\t\t빨강색\t\t\t한국\t\t\t\t탈것")
            print("타이베이: %.2f\t\t아테네: %.2f   \t\t부에노스: %.2f\t\t도쿄: %.2f\t\t제주도: %.2f\t\t콩코드 여객기: %.2f"
                  %(price[0][0], price[6][0], price[12][0], price[18][0], price[23][0], price[24][0]))
            print("홍콩: %.2f\t\t\t코펜하겐: %.2f\t\t상파울루: %.2f\t\t파리: %.2f\t\t부산: %.2f\t\t퀸 엘리자베스 호: %.2f"
                  %(price[1][0], price[7][0], price[13][0], price[19][0], price[25][0], price[27][0]))
            print("마닐라: %.2f   \t\t스톡홀름: %.2f\t\t시드니: %.2f\t\t    로마: %.2f\t\t서울: %.2f\t\t콜롬비아호: %.2f"
                  %(price[2][0], price[8][0], price[14][0], price[20][0], price[26][0], price[28][0]))
            print("싱가폴: %.2f   \t\t취리히: %.2f   \t\t하와이: %.2f   \t\t런던: %.2f"
                  %(price[3][0], price[9][0], price[15][0], price[21][0]))
            print("카이로: %.2f   \t\t베를린: %.2f   \t\t리스본: %.2f   \t\t뉴욕: %.2f"
                  %(price[4][0], price[10][0], price[16][0], price[22][0]))
            print("이스탄불: %.2f\t\t몬트리올: %.2f\t\t마드리드: %.2f"
                  %(price[5][0], price[11][0], price[17][0]))
            print("**********"*12)

        elif menu == 1:
            try:
                city = input("시세를 확인할 도시 이름을 입력해 주세요 : ")
                print("%s의 정보\n통행료: %f \n매매가: %f \n별장: %d, 빌딩: %d, 호텔: %d"
                      % (city, toll(city), sell(city), cities.get(city)[3], cities.get(city)[4], cities.get(city)[5]))
            except:
                 print("도시이름을 잘못 입력하였습니다.")
        elif menu == 2:
            city = input("건물을 지을 도시 이름을 입력해 주세요 : ")
            build(city)
        elif menu == 3:
            name = input("돈을 지급할 플레이어의 이름을 입력해 주세요.: ")
            pay(name)
        elif menu == 4:
            name = input("돈을 지불할 플레이어의 이름을 입력해 주세요.: ")
            withdraw(name)
        elif menu == 5:
            trade()
        elif menu == 6:
            list_name = list(player.keys())
            for i in range(0, num_pl):
                print("%s 플레이어의 현금 보유액은 %.2f만원 입니다. " % (list_name[i], player[list_name[i]]))
        elif menu ==  7:
            print("게임을 종료합니다!")
            t2 = time.time()
            hours = (t2 - t1)//3600
            mins = ((t2 - t1) % 60) // 60
            secs = ((t2 - t1) % 60) % 60
            print("지금까지 플레이한 시간은 %d시간 %d분 %d초입니다." %(hours, mins, secs))
            break

