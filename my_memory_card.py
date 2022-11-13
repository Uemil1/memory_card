from PyQt5.QtCore import Qt
from random import shuffle, randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question("Русский мем", "Рикардо милос", "Пепе", "Амогус", "Нам кэт"))
question_list.append(Question("Несуществующая приставка", "з", "с", "под", "от"))
question_list.append(Question("Когда выпустили Doom 4?", '2016', ' 2006', '1999', '2018'))

app = QApplication([])
vikrotina = QWidget()
window = QWidget()
window.setWindowTitle('Memory Card')
btn_OK = QPushButton('Ответить')
lb_Question = QLabel(";?")
rbtn_1 = QRadioButton('f')
rbtn_2 = QRadioButton('r')
rbtn_3 = QRadioButton('a')
rbtn_4 = QRadioButton('v')
RadioGroupBox = QGroupBox("Варианты ответов")
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)
result = QLabel('Здесь правильно/неправильно')
lb_Correct = QLabel('Ответ будет тут!')
AnsGroupBox = QGroupBox()
AnsGroupBox.hide()

layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line1.addStretch(1)
layout_line2.addWidget(btn_OK)
layout_line3.addStretch(1)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3)
layout_card.addStretch(1)
layout_card.setSpacing(5)
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
window.score = 0
window.total = 0
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked() == True:
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n Всего вопросво: ', window.total, '\n- Правильных ответов: ', window.score)
        print('Рейтпнг: ', (window.score/window.total*100), '%')

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')

def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

def next_question():
    window.total += 1
    print('Статистика\n Всего вопросво: ', window.total, '\n- Правильных ответов: ', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()



window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.cur_question = -1
next_question()
#btn_OK.clicked.connect(test)
btn_OK.clicked.connect(click_OK)
window.show()
app.exec()