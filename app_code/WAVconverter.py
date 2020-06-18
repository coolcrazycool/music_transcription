import librosa
from collections import deque
# import pandas as pd

# путь к рандомному файлу
audio_way = '../dataset/test3.wav'
# время одного сегмента
segment_time = 0.05

notesList = [[40, 80, 84],
             [41, 85, 89],
             [42, 91, 95],
             [43, 96, 100],
             [44, 101, 107],
             [45, 108, 112],
             [46, 114, 118],
             [47, 119, 125],
             [48, 127, 134],
             [49, 136, 142],
             [50, 145, 150],
             [51, 153, 158],
             [52, 160, 168],
             [53, 169, 177],
             [54, 180, 189],
             [55, 190, 200],
             [56, 204, 213],
             [57, 215, 224],
             [58, 229, 238],
             [59, 241, 252],
             [60, 258, 266],
             [61, 272, 282],
             [62, 290, 300],
             [63, 306, 317],
             [64, 324, 338],
             [65, 342, 355],
             [66, 366, 378],
             [67, 388, 398],
             [68, 408, 422],
             [69, 436, 446],
             [70, 460, 478],
             [71, 485, 510],
             [72, 515, 535],
             [73, 540, 565],
             [74, 570, 605],
             [75, 610, 638],
             [76, 645, 670]]


def segmentation(audio, sr):
    frame_length = round(sr * segment_time)
    frames = librosa.util.frame(audio, frame_length=frame_length, hop_length=frame_length, axis=0)
    return frames


def estimate_pitch(segment, sr, fmin=10.0, fmax=1000.0):

    # Compute autocorrelation of input segment.
    r = librosa.autocorrelate(segment)

    # Define lower and upper limits for the autocorrelation argmax.
    i_min = sr / fmax
    i_max = sr / fmin
    r[:int(i_min)] = 0
    r[int(i_max):] = 0

    # Find the location of the maximum autocorrelation.
    i = r.argmax()
    f0 = float(sr) / i
    return f0


def matrix_converter(data):
    pd_matr = [[data[0], 1]]
    for i in range(1, len(data)):
        if data[i] != data[i-1]:
            pd_matr. append([data[i], 1])
            continue
        pd_matr[-1][1] += 1

    # for el in pd_matr[::-1]:
        # pd_matr[pd_matr.index(el)][1] *= int(segment_time*1000)
    return pd_matr


def audio_analyzer(audio_path):
    audio, sr = librosa.load(audio_path)
    frames = segmentation(audio, sr)
    data = deque()
    for frame in frames:
        freq = estimate_pitch(frame, sr)
        for el in notesList:
            if el[1] <= freq <= el[2]:
                data.append(el[0])
                break
            elif el[0] == 76:
                data.append(-1)
    note_list = matrix_converter(data)
    return note_list


if __name__ == '__main__':
    print(audio_analyzer('../dataset/test2.wav'))
