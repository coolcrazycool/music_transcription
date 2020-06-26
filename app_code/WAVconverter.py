from scipy.io import wavfile
from collections import deque
from scipy.fft import fft, ifft
import numpy as np

# путь к рандомному файлу
audio_way = '../dataset/sound.wav'
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
    segments = len(audio) // frame_length
    frames = []
    for i in range(segments):
        frames.append(list(audio[frame_length*i:frame_length*i+frame_length]))
    frames = np.array(frames)
    return frames


def estimate_pitch(y, sr, fmin=10.0, fmax=1000.0):
    max_size = None
    axis = -1
    # Compute autocorrelation of input segment.
    if max_size is None:
        max_size = y.shape[axis]

    max_size = int(min(max_size, y.shape[axis]))

    # Compute the power spectrum along the chosen axis
    # Pad out the signal to support full-length auto-correlation.
    powspec = np.abs(fft(y, n=2 * y.shape[axis] + 1, axis=axis)) ** 2

    # Convert back to time domain
    autocorr = ifft(powspec, axis=axis)

    # Slice down to max_size
    subslice = [slice(None)] * autocorr.ndim
    subslice[axis] = slice(max_size)

    autocorr = autocorr[tuple(subslice)]

    if not np.iscomplexobj(y):
        autocorr = autocorr.real

    # Define lower and upper limits for the autocorrelation argmax.
    i_min = sr / fmax
    i_max = sr / fmin
    autocorr[:int(i_min)] = 0
    autocorr[int(i_max):] = 0

    # Find the location of the maximum autocorrelation.
    i = autocorr.argmax()
    f0 = float(sr) / i
    return f0


def matrix_converter(data):
    pd_matr = [[data[0], 1]]
    for i in range(1, len(data)):
        if data[i] != data[i-1]:
            pd_matr. append([data[i], 1])
            continue
        pd_matr[-1][1] += 1
    return pd_matr


def audio_analyzer(audio_path):
    sr, audio = wavfile.read(audio_path)
    audio = np.array(audio[:, 0]).transpose()
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
    print(audio_analyzer('../dataset/test3.wav'))
    # base_spectrogram('../dataset/sound.wav')

