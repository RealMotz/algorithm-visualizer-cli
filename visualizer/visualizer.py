import curses
import time

# options = ["Bubble Sort", "Merge Sort", "Insertion Sort"]
def plot(choice):
    try:
        mywindow = curses.initscr()
        curses.noecho()
        bubble([5,4,3,2,1], mywindow)
        bubble([1,4,3,2,5], mywindow)
        bubble([1,2,3,4,5], mywindow)
    except Exception:
        print("Error bbyyy")
    finally:
        curses.endwin()

def bubble(numbers, window):
    for index, number in enumerate(normalize_stars(numbers)):
        window.addstr(index, 0, '*'*number + '\n')
    window.refresh()
    time.sleep(1)

def normalize_stars(numbers):
    total = sum(numbers)
    return [round((n/total)*100) for n in numbers]