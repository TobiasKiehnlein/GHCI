from utils import get_euclidean_distance

n_samples = 150


def blinks_per_seconds(eye_closed: list[bool]) -> float:
    eye_closings = sum(int(not eye_closed[i - 1] and eye_closed[i]) for i in range(1, len(eye_closed))) + int(eye_closed[0])
    return eye_closings / n_samples * 5


def saccades_per_second(x: list[float], y: list[float]) -> float:
    assert len(x) == len(y)
    total_saccades = sum(int(get_euclidean_distance([x[i], y[i]], [x[i - 1], y[i - 1]]) > 3) for i in range(1, len(x)))
    return total_saccades / n_samples * 5


def avg_fixation_time(x: list[float], y: list[float]) -> float:
    assert len(x) == len(y)
    lengths = []
    for i in range(1, len(x)):
        if get_euclidean_distance([x[i], y[i]], [x[i - 1], y[i - 1]]) > 3:
            lengths.append(0)
        if get_euclidean_distance([x[i], y[i]], [x[i - 1], y[i - 1]]) <= 3:
            lengths[-1] += 1
    if lengths[-1] == 0:
        lengths.pop()
    return sum(lengths) / len(lengths) / n_samples * 5
