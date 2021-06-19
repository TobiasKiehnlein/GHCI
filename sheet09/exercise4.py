from sheet09.exercise3 import blinks_per_seconds

activity = 'reading'

LINE_JUMP_THRESHOLD = 3
LEFT_RIGHT_JUMP_LOWER_THRESHOLD = 5
LEFT_RIGHT_JUMP_UPPER_THRESHOLD = 10
MAX_ALLOWED_BLINKS_PER_SECOND = .5


def print_result(res: bool):
    print(f'User is {"not" if not res else ""} {activity}')


def checkActivity(x: list[float], y: list[float], eye_closed: list[bool]):
    assert len(x) == len(y)

    for i in range(1, len(y)):
        """
        Hier wird überprüft, ob sich die y Werte maximal um einen gewissen Wert verändern.
        Dies ist dazu da, um sicherzustellen, dass der Nutzer gerade maximal in Zeilen springt
        und nicht einfach so im Raum auf und ab sieht (o.Ä.).
        """
        if abs(y[i] - y[i - 1]) > LINE_JUMP_THRESHOLD:
            return print_result(False)

        """
        Außerdem muss überprüft werden, dass die x Bewegung der Augen entweder relativ langsam ist (lesen einer Zeile)
        oder sehr sprunghaft ist (Springen von einer Zeile rechts in die neue Zeile links)
        """
        x_dif = abs(x[i] - x[i - 1])
        if LEFT_RIGHT_JUMP_LOWER_THRESHOLD < x_dif < LEFT_RIGHT_JUMP_UPPER_THRESHOLD:
            return print_result(False)

        """
        Wenn der Nutzer sehr häufig blinzelt ist das ein Zeichen dafür,
        dass er gerade nicht liest.
        """
        if blinks_per_seconds(eye_closed) > MAX_ALLOWED_BLINKS_PER_SECOND:
            return print_result(False)

        """
        Sollte keines der oben aufgetretenen Kriterien eingetroffen sein liest der Nutzer offensichtlich gerade.
        """
        print_result(True)
