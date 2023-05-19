from __future__ import annotations
from threedeebeetree import Point
from ratio import Percentiles


def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    order_ratio = 1 / 7 * 100  # get ratio in percent

    def make_ordering_aux(current, remaining):
        if len(remaining) <= 6:  # O(1)  # todo check if this is correct for 2 or any other number
            current += remaining

        # else (overall O(nlog(n) + o))
        else:
            x = Percentiles()
            y = Percentiles()
            z = Percentiles()

            for _p in remaining:  # O(n * 3 * log(n)) = O(nlog(n))
                x.add_point((_p[0], _p))
                y.add_point((_p[1], _p))
                z.add_point((_p[2], _p))

            # output_x = x.ratio(order_ratio, order_ratio)  # 3 times O(log(n) + o) = O(log(n) + o)
            # output_y = y.ratio(order_ratio, order_ratio)
            # output_z = z.ratio(order_ratio, order_ratio)
            #
            # # ratio(): 3 times O(log(n) + o) = O(log(n) + o)
            # selected = remaining[0]  # fallback if no common point is found

            # for _p in output_x:  # find a point that is in all 3 lists
            #     if any(_p[1] in tup for tup in output_y) \
            #             and any(_p[1] in tup for tup in output_z):
            #         selected = _p[1]
            #         break

            output_x = x.ratio(order_ratio, order_ratio)  # 3 times O(log(n) + o) = O(log(n) + o)
            output_y = y.ratio(order_ratio, order_ratio)
            output_z = z.ratio(order_ratio, order_ratio)

            lst_x = {_p[1] for _p in output_x}  # O(3 * n) = O(n)
            lst_y = {_p[1] for _p in output_y}
            lst_z = {_p[1] for _p in output_z}

            common = list(lst_x.intersection(lst_y, lst_z))  # 2 times O(min(m, n)) = O(?)
            # print('common: ', common)

            # get the first common point, or the first point in the list
            selected = common[0] if common else remaining[0]  # O(1)

            current.append(selected)  # O(1)
            remaining.remove(selected)  # O(1)

            # create a 2x2x2 list, essentially 8 different lists for each octant
            # assign each point to a list based on the x, y, and z coordinates of the selected point
            lst = [[[[] for _ in range(2)] for _ in range(2)] for _ in range(2)]

            for _p in remaining:  # this is super advanced by gpt, might need to change
                x_index = int(_p[0] >= selected[0])
                y_index = int(_p[1] >= selected[1])
                z_index = int(_p[2] >= selected[2])
                lst[x_index][y_index][z_index].append(_p)

            # for each octant, recursively call make_ordering_aux to get the ordering of the points in that octant
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        make_ordering_aux(current, lst[i][j][k])
        return current

    return make_ordering_aux([], my_coordinate_list)


def make_ordering2(my_coordinate_list: list[Point]) -> list[Point]:
    ratio = 1 / 7 * 100  # get ratio in percent

    def make_ordering_aux(current, remaining):
        if len(remaining) <= 1:  # O(1)  # todo check if this is correct
            current += remaining
            return current

        # else (overall O(nlog(n) + o))
        else:
            x = Percentiles()
            y = Percentiles()
            z = Percentiles()

            for _p in remaining:  # O(n * 3 * log(n)) = O(nlog(n))
                x.add_point((_p[0], _p))
                y.add_point((_p[1], _p))
                z.add_point((_p[2], _p))

            output_x = x.ratio(ratio, ratio)  # 3 times O(log(n) + o) = O(log(n) + o)
            output_y = y.ratio(ratio, ratio)
            output_z = z.ratio(ratio, ratio)

            lst_x = {_p[1] for _p in output_x}  # O(3 * n) = O(n)
            lst_y = {_p[1] for _p in output_y}
            lst_z = {_p[1] for _p in output_z}

            common = list(lst_x.intersection(lst_y, lst_z))  # 2 times O(min(m, n)) = O(?)
            # print('common: ', common)

            # get the first common point, or the first point in the list
            selected = common[0] if common else remaining[0]  # O(1)

            current.append(selected)  # O(1)
            # print('selected is ', selected)

            remaining.remove(selected)  # O(1)

            # split remaining into 8 lists
            # assign each point to a list based on the x, y, and z coordinates of the selected point

            lst = [[], [], [], [], [], [], [], []]

            for _p in remaining:  # O(n)
                # below all O(1)
                if _p[0] < selected[0]:
                    if _p[1] < selected[1]:
                        if _p[2] < selected[2]:
                            lst[0].append(_p)
                        else:
                            lst[1].append(_p)
                    else:
                        if _p[2] < selected[2]:
                            lst[2].append(_p)
                        else:
                            lst[3].append(_p)
                else:
                    if _p[1] < selected[1]:
                        if _p[2] < selected[2]:
                            lst[4].append(_p)
                        else:
                            lst[5].append(_p)
                    else:
                        if _p[2] < selected[2]:
                            lst[6].append(_p)
                        else:
                            lst[7].append(_p)

            # print out ratios (O(1))
            print(len(lst[0]), ' ', len(lst[1]), ' ', len(lst[2]), ' ', len(lst[3]), ' ', len(lst[4]), ' ', len(lst[5]),
                  ' ', len(lst[6]), ' ', len(lst[7]))
            print('---\n')
            # the number of divisions stages is, at worst case, log(n) (base 8)
            # if we start with 64(65) points, we will have 8 lists of 8 points
            # then we will have 8 lists of 1 points each

            # then, the cost of the recursion is O(log(n) * 8 * 1) = O(log(n))
            for sub_lst in lst:  # O(8 * 1) = O(1)
                make_ordering_aux(current, sub_lst)  # O(???) (n log n)

        return current

    return make_ordering_aux([], my_coordinate_list)


def make_ordering3(my_coordinate_list: list[Point]) -> list[Point]:
    ratio = 1 / 7 * 100  # get ratio in percent

    def make_ordering_aux(current, remaining):
        if len(remaining) <= 1:  # O(1)  # todo check if this is correct for 2 or any other number
            current += remaining
            return current

        # else (overall O(nlog(n) + o))
        else:
            x = Percentiles()
            y = Percentiles()
            z = Percentiles()

            for _p in remaining:  # O(n * 3 * log(n)) = O(nlog(n))
                x.add_point((_p[0], _p))
                y.add_point((_p[1], _p))
                z.add_point((_p[2], _p))

            # ratio(): 3 times O(log(n) + o) = O(log(n) + o)
            selected = remaining[0]  # fallback if no common point is found
            for _p in x.ratio(ratio, ratio):  # find a point that is in all 3 lists
                if any(_p[1] in tup for tup in y.ratio(ratio, ratio)) and any(
                        _p[1] in tup for tup in z.ratio(ratio, ratio)):
                    selected = _p[1]
                    break

            current.append(selected)  # O(1)
            remaining.remove(selected)  # O(1)

            # split remaining into 8 lists
            # assign each point to a list based on the x, y, and z coordinates of the selected point

            lst = [[], [], [], [], [], [], [], []]

            for _p in remaining:  # O(n)
                # below all O(1)
                if _p[0] < selected[0]:
                    if _p[1] < selected[1]:
                        if _p[2] < selected[2]:
                            lst[0].append(_p)
                        else:
                            lst[1].append(_p)
                    else:
                        if _p[2] < selected[2]:
                            lst[2].append(_p)
                        else:
                            lst[3].append(_p)
                else:
                    if _p[1] < selected[1]:
                        if _p[2] < selected[2]:
                            lst[4].append(_p)
                        else:
                            lst[5].append(_p)
                    else:
                        if _p[2] < selected[2]:
                            lst[6].append(_p)
                        else:
                            lst[7].append(_p)

            # then, the cost of the recursion is O(log(n) * 8 * 1) = O(log(n))
            for sub_lst in lst:  # O(8 * 1) = O(1)
                current = make_ordering_aux(current, sub_lst)  # O(???) (n log n)

        return current

    return make_ordering_aux([], my_coordinate_list)


if __name__ == "__main__":  # todo remove test below
    import random

    # random.seed(10239123)
    points = []
    coords = list(range(6000))
    random.shuffle(coords)
    for i in range(1500):
        point = (coords[3 * i], coords[3 * i + 1], coords[3 * i + 2])
        points.append(point)

    ordering = make_ordering(points)
    from threedeebeetree import ThreeDeeBeeTree

    tdbt = ThreeDeeBeeTree()
    for i, p in enumerate(ordering):
        tdbt[p] = i

    from tests.test_balancing import collect_worst_ratio

    ratio, smaller, axis = collect_worst_ratio(tdbt.root)
    print(ratio, 7, f"Axis {axis} has ratio 1:{ratio}.")
    pass
