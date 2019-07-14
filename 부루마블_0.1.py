import random
import numpy as np
from tkinter import *
from tkinter.simpledialog import *
from tkinter import messagebox

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


class City:
    price = 0
    structure = [0, 0, 0]

    def build(self, val_city, val_num, val_many):
        try:
            if val_num == '별장':
                if val_many > 2:
                    messagebox.showwarning("경고!!!", "별장은 최대 2개까지 지을수 있습니다.")
                else:
                    self.structure[0] = val_many
                    messagebox.showinfo("%s 건물 현황"%val_city, "%s의 현황 별장 %d개, 빌딩 %d개, 호텔 %d개"
                                        % (val_city, self.structure[0], self.structure[1], self.structure[2]))
            elif val_num == '빌딩':
                if val_many > 1:
                    messagebox.showwarning("경고!!!", "빌딩은 최대 1개까지 지을수 있습니다.")
                else:
                    self.structure[1] = val_many
                    messagebox.showinfo("%s 건물 현황"%val_city, "%s의 현황 별장 %d개, 빌딩 %d개, 호텔 %d개"
                                        % (val_city, self.structure[0], self.structure[1], self.structure[2]))
            elif val_num == '호텔':
                if val_many > 1:
                    messagebox.showwarning("경고!!!", "호텔은 최대 1개까지 지을수 있습니다.")
                else:
                    self.structure[2] = val_many
                    messagebox.showinfo("%s 건물 현황"%val_city, "%s의 현황 별장 %d개, 빌딩 %d개, 호텔 %d개"
                    %(val_city, self.structure[0], self.structure[1], self.structure[2]))

        except:
            messagebox.showerror("잘못 입력하셨습니다.", "입력하신 정보가 잘못되었습니다.")

    def get_price(self, city_num):
        if self.structure[0] + self.structure[1] + self.structure[2] == 0:
            return price[city_num][0]
        else:
            total = self.structure[0]*price[city_num][1] + self.structure[1]*price[city_num][2] + self.structure[2]*price[city_num][3]
            return total

    def go_new(self):
        self.structure = [0, 0, 0]

    #def get_name


def do_turn():
    messagebox.showinfo("죄송합니다", "아직 작업중 입니다.")


def get_input():
    global value, city_name, str_type, str_num
    value = askstring("건축 정보 수정", "도시, 건물유형, 갯수를 입력해주세요.\nex)뉴욕 호텔 1")
    try:
        city_name, str_type, str_num = value.split(' ')
        cities_list[cities_dic[city_name]].build(city_name, str_type, int(str_num))
    except:
        messagebox.showerror("잘못 입력하셨습니다.", "정보는 띄워쓰기로 구분해 주세요.")


def do_reset():
    global value
    value = askstring("리셋 정보 입력", "리셋시킬 도시 이름을 입력해 주세요.")
    try:
        cities_list[cities_dic[city_name]].go_new
        messagebox.showinfo("도시 리셋", "%s의 정보 리셋에 성공했습니다." %value)
    except:
        messagebox.showerror("경고!!!", "값을 잘못 입력하였습니다.")

def show_graph():
    messagebox.showinfo("죄송합니다", "아직 작업중 입니다.")


price = [[0.2, 1.0, 9.0, 25.0],  # 타이베이      #[등락폭,, 전등락폭, 전전등락폭, 토지값, 별장하나, 빌딩, 호텔]
         [0.4, 2.0, 18.0, 45.0],  # 홍콩
         [0.4, 2.0, 18.0, 45.0],  # 마닐라
         [0.6, 3.0, 27.0, 55.0],  # 싱가폴
         [0.6, 3.0, 27.0, 55.0],  # 카이로
         [0.8, 4.0, 30.0, 60.0],  # 이스탄불
         [1.0, 5.0, 45.0, 75.0],  # 아테네
         [1.2, 6.0, 50.0, 90.0],  # 코펜하겐
         [1.2, 6.0, 50.0, 90.0],  # 스톡홀름
         [1.4, 7.0, 50.0, 95.0],  # 취리히
         [1.4, 7.0, 50.0, 95.0],  # 베를린
         [1.6, 8.0, 55.0, 100.0],  # 몬트리올
         [1.8, 9.0, 70.0, 105.0],  # 부에노스 아이레스
         [2, 10.0, 75.0, 110.0],  # 상파울루
         [2, 10.0, 75.0, 110.0],  # 시드니
         [2.2, 11.0, 80.0, 115.0],  # 하와이
         [2.2, 11.0, 80.0, 115.0],  # 리스본
         [2.4, 12.0, 85.0, 120.0],  # 마드리드
         [2.6, 13.0, 90.0, 127.0],  # 도쿄
         [2.8, 15.0, 100.0, 140.0],  # 파리
         [2.8, 15.0, 100.0, 140.0],  # 로마
         [3.5, 17.0, 110.0, 150.0],  # 런던
         [3.5, 17.0, 110.0, 150.0],  # 뉴욕
         [30.0],  # 제주도
         [30.0],  # 콩코드
         [60.0],  # 부산
         [200.0],  # 서울
         [25.0],  # 퀸
         [40.0]]  # 콜롬비아호

cities_dic = {'타이베이': 0,
          '홍콩': 1,
          '마닐라': 2,
          '싱가폴': 3,
          '카이로': 4,
          '이스탄불': 5,
          '아테네': 6,
          '코펜하겐': 7,
          '스톡홀름': 8,
          '취리히': 9,
          '베를린': 10,
          '몬트리올': 11,
          '부에노스 아이레스': 12,
          '상파울루': 13,
          '시드니': 14,
          '하와이': 15,
          '리스본': 16,
          '마드리드': 17,
          '도쿄': 18,
          '파리': 19,
          '로마': 20,
          '런던': 21,
          '뉴욕': 22,
          '제주도':23,
          '콩코드':24,
          '부산':25,
          '서울':26,
          '퀸':27,
          '콜롬비아호':28
}

cities_list = []
value = ""
city_name = ""
str_type = ""
str_num = 0


# 도시생성
for i in range(29):
    ct = City()
    cities_list.append(ct)
print(cities_list)

# main window
win = Tk()
win.title("부루마블 보조 프로그램")

# main menu
main_menu = Menu(win)
win.config(menu=main_menu)

# sub menu
menu1 = Menu(main_menu)

main_menu.add_cascade(label="File", menu=menu1)

menu1.add_command(label="프로그램 종료")



try:
    # jawoos mark
    img_bgr = PhotoImage(file="background.png")
    la_img2 = Label(win, image=img_bgr)
    la_img2.place(x=0, y=0)

    # label
    la_str0 = Label(win, text="", height=9, width=25)
    la_str0.grid(row=0, column=0)

    la_str1 = Label(win, text="턴 진행",)
    la_str1.grid(row=2, column=0)

    la_str2 = Label(win, text="시세 그래프")
    la_str2.grid(row=2, column=1)

    la_str3 = Label(win, text="건물 매매")
    la_str3.grid(row=4, column=0)

    la_str4 = Label(win, text="도시 리셋")
    la_str4.grid(row=4, column=1)

    # jawoos mark
    img_bgr = PhotoImage(file="background.png")
    la_img2 = Label(win, image=img_bgr)
    la_img2.place(x=0, y=0)


    # button
    img_next = PhotoImage(file="next.png")
    btn_turn = Button(win, image=img_next, command=do_turn)
    btn_turn.grid(row=1, column=0)

    img_bars = PhotoImage(file="bars.png")
    btn_turn = Button(win, image=img_bars, command=show_graph)
    btn_turn.grid(row=1, column=1)

    img_build = PhotoImage(file="build.png")
    btn_build = Button(win, image=img_build, command=get_input)
    btn_build.grid(row=3, column=0)

    img_reset = PhotoImage(file="settings.png")
    btn_reset = Button(win, image=img_reset, command=do_reset)
    btn_reset.grid(row=3, column=1)

except KeyError:
    messagebox.showwarning("경고!!!", "잘못 입력하였습니다.")


win.mainloop()
