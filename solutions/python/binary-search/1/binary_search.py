def find(search_list, value):
    start = 0
    end = len(search_list) - 1
    mid = (start + end) // 2
    if not search_list:
        raise ValueError("value not in array")
    if value > search_list[end] or value < search_list[start]:
        raise ValueError("value not in array")

    while end >= start:
        mid = (start + end) // 2
        if start == end:
            if search_list[start] != value:
                raise ValueError("value not in array")
            else:
                return start
        if start + 1 == end:
            print('start + 1 = end')
            if search_list[start] == value:
                return start
            elif search_list[end] == value:
                return end
            else:
                raise ValueError("value not in array")
        if search_list[mid] == value:
            print('found')
            return mid
        elif search_list[mid] < value:
            start = mid
            print(f"start = mid -- new start is {start}, {mid}, {end}")
        else:
            end = mid
            print(f"end = mid -- new end is {end}, {start}, {mid}")

    raise ValueError("value not in array")

# print(find([1, 3, 4, 6, 8, 9, 11], 7))