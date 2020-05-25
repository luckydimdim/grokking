from __future__ import print_function

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def find_employee_free_time2(schedule):
    '''
    For ‘K’ employees, we are given a list of intervals representing the working hours of each employee.
    Our goal is to find out if there is a free interval that is common to all employees.
    You can assume that each list of employee working hours is sorted on the start time.
    '''
    result = []
    intervals = []
    for hours in schedule:
        intervals += hours

    intervals.sort(key = lambda x: x.start)

    for i in range(1, len(intervals)):
        if intervals[i].start > intervals[i - 1].end:
            result.append(Interval(intervals[i - 1].end, intervals[i].start))

    return result

def find_employee_free_time(schedule):
    '''
    For ‘K’ employees, we are given a list of intervals representing the working hours of each employee.
    Our goal is to find out if there is a free interval that is common to all employees.
    You can assume that each list of employee working hours is sorted on the start time.
    '''
    result = []
    employees = []

    for intervals in schedule:
        employees += intervals

    employees.sort(key = lambda x: x.start)

    for i in range(1, len(employees)):
        if employees[i].start > employees[i - 1].end:
            result.append(Interval(employees[i - 1].end, employees[i].start))

    return result

def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
