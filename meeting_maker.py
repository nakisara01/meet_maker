def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def minutes_to_time(minutes):
    hours, mins = divmod(minutes, 60)
    return f"{hours:02d}:{mins:02d}"

def find_empty_times(timetables):
    all_times = {}

    for day in ['월요일', '화요일', '수요일', '목요일', '금요일']:
        all_times[day] = [(9 * 60, 24 * 60)]

    for _, timetable in timetables:
        for timing in timetable:
            day, time_range = timing.split(' ')
            start_time, end_time = time_range.split('-')
            start_minutes = time_to_minutes(start_time)
            end_minutes = time_to_minutes(end_time)

            day_times = all_times[day]

            new_day_times = []
            for start, end in day_times:
                if start_minutes > start:
                    new_day_times.append((start, start_minutes))
                if end_minutes < end:
                    new_day_times.append((end_minutes, end))

            all_times[day] = new_day_times

    return all_times

def print_empty_times(empty_times):
    for day, day_times in empty_times.items():
        print(f"{day}의 빈 시간대:")
        if not day_times:
            print("없음")
        else:
            for start, end in day_times:
                print(f"{minutes_to_time(start)} ~ {minutes_to_time(end)}")

def input_timetables():
    num_people = int(input("참여하는 사람 수를 입력하세요: "))
    timetables = []

    for i in range(num_people):
        name = input(f"{i + 1}번째 사람의 이름을 입력하세요: ")
        timetable_str = input(f"{name}의 시간표를 입력하세요 (여러 개의 시간표를 쉼표로 구분): ")
        timetable = timetable_str.split(', ')
        timetables.append((name, timetable))

    return timetables

if __name__ == "__main__":
    print("참여하는 사람들의 시간표를 입력하세요.")
    timetables = input_timetables()
    all_times = find_empty_times(timetables)
    print_empty_times(all_times)