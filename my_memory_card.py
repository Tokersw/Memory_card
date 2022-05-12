#импортируем библ-ки
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QPushButton, QWidget, QApplication, QMessageBox, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton ,QButtonGroup
from random import shuffle, randint
#Функция окна "Следующий вопрос"
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
def next_question():
    
    main_win.total += 1
    cur_question = randint(0, len(question_list) -1)
    q = question_list[cur_question]
    ask(q)

def click_ok():
    if btn.text() == "Ответить":
        check_answer()
    else:
        next_question()

def resultat(a,b):
    return (a/b)*100

def show_result():
    groupa.hide()
    groupa2.show()
    btn.setText("Следующий вопрос")

def show_question():
    groupa.show()
    groupa2.hide()
    btn.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_answer1.setChecked(False)
    rbtn_answer2.setChecked(False)
    rbtn_answer3.setChecked(False)
    rbtn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    result.setText(q.right_answer)
    show_question()

def show_correct(res1):
    res.setText(res1)
    show_result()
def check_answer():

    if answers[0].isChecked():
        show_correct('Правильно!')
        print("\n")
        print('Верно!')
        print("\n")
        main_win.score += 1
        print("Статистика")
        print("-Всего вопросов:", main_win.total)
        print("-Правильных ответов:", main_win.score)
        print("Рейтинг:",resultat(main_win.score, main_win.total),"%")

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Наверное!')
            print("\n")
            print('Неверно')
            print('\n')
            print("Статистика")
            print("-Всего вопросов:", main_win.total)
            print("-Правильных ответов:", main_win.score)
            print("Рейтинг:",resultat(main_win.score, main_win.total),"%")
            
#Создание приложения, окна и размер окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card")
main_win.resize(600,400)
question_list = []

q1 = Question('Какой национальности не существует?', 'Энцы','Чулымцы','Смурфы','Алеуты')
q2 = Question('Название этой нелетающей птицы из Австралии состоит из двух нот. Что это за птица?', 'Додо','Мими','Рере','Фафа')
q3 = Question('Из какого вечнозеленого дерева делают пианино и скрипки?', 'Ель','Тропическое дерево','Дуб','Вельвичия')
q4 = Question('С латинского языка название этого инструмента переводится как «дуновение»', 'Флейта', 'труба','валторна','сузафон')
q5 = Question('Какая богиня в Древней Греции покровительствовала музыкальному искусству?', 'Эвтерпа','Гера','Афродита','Афина')
q6 = Question('Какой металл является самым тугоплавким?', "Вольфрам","Осмий","Алюминий","Барий")
q7 = Question('Какая жидкость самая легкая?', "Сжиженный водород","Ртуть","Жидкий азот","Вода")
q8 = Question("Какое поле появляется вокруг любого предмета?", "Гравитационное","Электрослабое ","Магнитное","Электромагнитное поле")
q9 = Question('Зимой – серый, летом – белый. Кто это?', "Заяц","Волк","Лиса","Крот")
q10 = Question('Сколько лучей у обычной снежинки?', "6","3","12","13")

question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)
question_list.append(q9)
question_list.append(q10)



btn = QPushButton("Ответить")
#вопрос(ы)
question = QLabel('Какой национальности не существует?')

groupa = QGroupBox('Варианты ответов:')
rbtn_answer1 = QRadioButton('Энцы')
rbtn_answer2 = QRadioButton('Чулымцы')
rbtn_answer3 = QRadioButton('Смурфы')
rbtn_answer4 = QRadioButton('Алеуты')
answers = [rbtn_answer1, rbtn_answer2, rbtn_answer3, rbtn_answer4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_answer1)
RadioGroup.addButton(rbtn_answer2)
RadioGroup.addButton(rbtn_answer3)
RadioGroup.addButton(rbtn_answer4)

#Создание линий (H,V)
layoutH1 = QHBoxLayout()
layoutV1 = QVBoxLayout()
layoutV2 = QVBoxLayout()

#Прикрепляем кнопки(rbtn_answer(1,2,3,4)) к линиям(latout(H,V)(1,2))) 
layoutV1.addWidget(rbtn_answer1, alignment=Qt.AlignLeft)
layoutV1.addWidget(rbtn_answer2, alignment=Qt.AlignLeft)
layoutV2.addWidget(rbtn_answer3, alignment=Qt.AlignLeft)
layoutV2.addWidget(rbtn_answer4, alignment=Qt.AlignLeft)
#Прикрепляем линии(V1)
layoutH1.addLayout(layoutV1)
layoutH1.addLayout(layoutV2)

groupa.setLayout(layoutH1)


groupa2 = QGroupBox('Результат теста:')
res = QLabel("Прав ты или нет")
result = QLabel("Ответ будет тут!")

layoutV3 = QVBoxLayout()


layoutV3.addWidget(res, alignment=Qt.AlignLeft)
layoutV3.addWidget(result, alignment=Qt.AlignCenter)
groupa2.setLayout(layoutV3)


groupa2.hide()

l2 = QHBoxLayout()
l3 = QHBoxLayout()
layout_ans = QVBoxLayout()

l2.addWidget(question, alignment=Qt.AlignCenter)
layout_ans.addLayout(l2)

layout_ans.addWidget(groupa)
layout_ans.addWidget(groupa2)
l3.addWidget(btn)
layout_ans.addLayout(l3)

layout_ans.setSpacing(15)
main_win.setLayout(layout_ans)

btn.clicked.connect(click_ok)

main_win.total = 0
main_win.score = 0 

next_question()

main_win.show()
app.exec_()