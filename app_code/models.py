from copy import deepcopy

import abjad
from .WAVconverter import audio_analyzer


# import mingus.extra
# from mingus.containers import Bar


class Melody:
    def __init__(self, path):
        self.path = path
        self.data = None

    def dataToArray(self):
        self.data = audio_analyzer(self.path)

    def __str__(self):
        return str(self.data)

    def __iter__(self):
        return iter(self.data)

    def del_two_last(self):
        del self.data[-1]
        del self.data[-1]

    def for_test(self, data):
        self.data = data


# FREQ_NOTE = 4
# EPS=0.1
MIN_NOTE = 16  # Минимальная длительность будет приравниваться к этому числу. В данном случае, константа = 16,
# т.е. миннимальная нота при записи будет шестнадцатая, относительно нее все будет считаться.
# Для простановки других мин нот используйте степени 2. Восьмая - 8, тридцатьвторая - 32 и тд...
# функция abj_duration и strange_rythm и long_note сделано под 16! Надо справить проверку длительностей норм и нет
NOIZE_FILTER_TIME = 0  # Это учёт возможного шума или неточностей декодирования.
NOIZE_FILTER_PAUSE = 4
BASE_NOTE = 60
PATH_TO_PDF = "../media/pdf/"


# Исходя из того, что длительность звука не может быть равной 50мс или 25мс,
# т.е. если какой-то звук длится маленкое колиечество segment_time, то он не учитываетсяи записывается


class Notes:

    def __init__(self, melody):
        self.freqList = []
        self.filterData = []
        self.data = []
        self.notes = abjad.Container()
        self.inputData = deepcopy(melody.data)
        # self.freqList = []
        # for i, sound in enumerate(melody.data):
        #     if i == 0:
        #         self.inputData.append([sound, 1])
        #         # self.freqList.append(1)
        #     elif sound == self.inputData[len(self.inputData) - 1][0]:
        #         self.inputData[len(self.inputData) - 1][1] += 1
        #         # self.freqList[len(self.freqList) - 1] += 1
        #     else:
        #         self.inputData.append([sound, 1])
        #         # self.freqList.append(1)
        self.filter_noize()
        self.markup()

    def filter_noize(self):
        for [sound, time] in self.inputData:
            if len(self.filterData) == 0 and sound == -1:
                continue
            if (len(self.filterData) != 0 and time <= NOIZE_FILTER_TIME) or (
                    len(self.filterData) != 0 and time <= NOIZE_FILTER_PAUSE and sound == -1):
                self.filterData[len(self.filterData) - 1][1] += time
                self.freqList[len(self.freqList) - 1] += time
            else:
                self.filterData.append([sound, time])
                self.freqList.append(time)

    def markup(self):  # функция должна разбивать ноты на 16, 8 , честверти  тд, определив длительность и bmp-?
        mi = min(self.freqList)
        for [sound, time] in self.filterData:
            self.data.append([sound, round(time / mi)])

    def __str__(self):
        return str(self.data)

    def converteToPdf(self, filename):
        # this function will use special lib ans converte markuped array to really Notes notation, then it saves it
        # as pdf
        for note in self.data:
            norm, time = self.abj_duration(note[1])
            if norm:
                if note[0] < 0:
                    self.notes.append(abjad.Rest(abjad.Note(note[0] - BASE_NOTE, abjad.Duration(time, MIN_NOTE))))
                else:
                    self.notes.append(abjad.Note(note[0] - BASE_NOTE, abjad.Duration(time, MIN_NOTE)))
            else:
                # beg_tie = len(notes)
                if note[0] < 0:
                    for t in time:
                        self.notes.append(abjad.Rest(abjad.Note(note[0] - BASE_NOTE, abjad.Duration(t, MIN_NOTE))))
                        # abjad.attach(tie,notes[len(notes)-1])

                else:
                    tie = abjad.Tie()
                    for t in time:
                        self.notes.append(abjad.Note(note[0] - BASE_NOTE, abjad.Duration(t, MIN_NOTE)))
                        abjad.attach(tie, self.notes[len(self.notes) - 1])
                    del tie
        abjad.persist(self.notes).as_pdf(''.join([PATH_TO_PDF, filename]))
        # abjad.show(self.notes)
        # abjad.IOManager.save_last_pdf_as(r"../sound.pdf")

    def abj_duration(self, time):  # сделано под 16!!!
        if time > MIN_NOTE:
            return self.long_note(time)
        elif time != 14 and time != 10 and time % 2 == 0 or time == 3 or time == 1:
            return True, time
        return self.strange_rythm(time)

    def long_note(self, time):  # сделано под 16!!!
        short = time % MIN_NOTE
        counter = time - short
        one_long = []
        if short != 0 and short != 14 and short != 10 and short % 2 == 0 or short == 3 or short == 1:
            one_long.append(short)
        elif short != 0:
            one_long.append(self.strange_rythm(short)[1][0])
            one_long.append(self.strange_rythm(short)[1][1])
        while counter > 0:
            one_long.append(MIN_NOTE)
            counter -= MIN_NOTE
        return False, one_long

    def strange_rythm(self, time):  # сделано под 16!!!
        if time < 9:
            first = int(time / 2) * 2
            second = time - first
        else:
            first = int(time / 4) * 4
            second = time - first
        return False, [first, second]
