import curses
import math
import time
from rich import print
from abc import ABC, abstractmethod

def plot(choice):
    try:
        mywindow = curses.initscr()
        curses.noecho()
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_GREEN, -1)
        strategy = get_sorting_strategy(choice, mywindow)
        strategy.sort([5,4,3,2,1])
    except Exception:
        print("Error occurred when plotting...")
    finally:
        curses.endwin()

def get_sorting_strategy(choice, window):
    match choice:
        case 1:
            return BubbleSort(window)
        case 2:
            return MergeSort(window)
        case 3:
            return InsertionSort(window)
        case _:
            return None

class SortingStrategy(ABC):
    def __init__(self, window) -> None:
        self.window = window

    def print_stars(self, numbers, index=-2):
        for i, number in enumerate(self.normalize_stars(numbers)):
            if i == index or i == index+1:
                self.window.addstr(i, 0, '*'*number + '\n', curses.color_pair(1))
            else:
                self.window.addstr(i, 0, '*'*number + '\n')

        self.window.refresh()
        time.sleep(1)

    def normalize_stars(self, numbers):
        total = sum(numbers)
        return [round((n/total)*100) for n in numbers]

    @abstractmethod
    def sort(self, numbers):
        pass

class BubbleSort(SortingStrategy):
    def sort(self, numbers):
        print("Sorting using: Bubble Sort")
        sorted = False
        while(not sorted):
            sorted = True
            for index in range(len(numbers)):
                if index + 1 >= len(numbers):
                    continue
                if(numbers[index] > numbers[index+1]):
                    sorted = False
                    temp = numbers[index]
                    numbers[index] = numbers[index+1]
                    numbers[index+1] = temp
                    self.print_stars(numbers, index)

class MergeSort(SortingStrategy):
    def sort(self, numbers):
        print("Sorting using: Merge Sort")
        self.original = numbers
        res = self.aux(numbers)
        print(res)

    def aux(self, numbers):
        n = len(numbers)
        if(n == 1):
            return numbers
        half = math.ceil(n/2)
        h1 = self.aux(numbers[0:half])
        h2 = self.aux(numbers[half:n])

        i = 0
        j = 0
        merge = []
        while(i < len(h1) and j < len(h2)):
            if(h1[i] < h2[j]):
                merge.append(h1[i])
                i+=1
            if(h2[j] < h1[i]):
                merge.append(h2[j])
                j+=1

        while(i < len(h1)):
            merge.append(h1[i])
            i+=1

        while(j < len(h2)):
            merge.append(h2[j])
            j+=1

        return merge


class InsertionSort(SortingStrategy):
    def sort(self, numbers):
        print("Sorting using: Insertion Sort")
