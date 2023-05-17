from __future__ import annotations
from threedeebeetree import Point
from ratio import Percentiles

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    ratio = 1/7 * 100
    current_list = []

    def make_ordering_aux(current, remaining):
        # print('remaining: ', remaining)
        # print('current: ', current)
        if len(remaining) <= 2:
            current += remaining
            # print('final: ', current)
            return current
        else:
            x = Percentiles()
            y = Percentiles()
            z = Percentiles()
            for point in remaining:
                x.add_point((point[0],point))
                y.add_point((point[1],point))
                z.add_point((point[2],point))
            output_x = x.ratio(ratio, ratio)
            output_y = y.ratio(ratio, ratio)
            output_z = z.ratio(ratio, ratio)

            lst_x = {point[1] for point in output_x}
            lst_y = {point[1] for point in output_y}
            lst_z = {point[1] for point in output_z}

            # print('lst_x: ', lst_x)
            # print('lst_y: ', lst_y)
            # print('lst_z: ', lst_z)

            common = list(lst_x.intersection(lst_y, lst_z))
            print('common: ', common)

            if common == []:
                selected = remaining[0]
            else:
                selected = common[0]
            current.append(selected)
            print('selected is ', selected)


            remaining.remove(selected)


            # split remaining into 8 lists based on the x, y, and z coordinates of the selected point
            lst = [[],[],[],[],[],[],[],[]]
            for point in remaining:
                if point[0] < selected[0]:
                    if point[1] < selected[1]:
                        if point[2] < selected[2]:
                            lst[0].append(point)
                        else:
                            lst[1].append(point)
                    else:
                        if point[2] < selected[2]:
                            lst[2].append(point)
                        else:
                            lst[3].append(point)
                else:
                    if point[1] < selected[1]:
                        if point[2] < selected[2]:
                            lst[4].append(point)
                        else:
                            lst[5].append(point)
                    else:
                        if point[2] < selected[2]:
                            lst[6].append(point)
                        else:
                            lst[7].append(point)

            print('lst: ', lst)
            print(len(lst[0]), ' ', len(lst[1]), ' ', len(lst[2]), ' ', len(lst[3]), ' ', len(lst[4]), ' ', len(lst[5]), ' ', len(lst[6]), ' ', len(lst[7]))
            print('---\n\n')

            for l in lst:
                current = make_ordering_aux(current, l)

            # current = make_ordering_aux(current, remaining)
        return current

    return make_ordering_aux(current_list, my_coordinate_list)


if __name__ == "__main__":  # todo remove test below
    import random
    # random.seed(10239123)
    points = []
    coords = list(range(15000))
    random.shuffle(coords)
    for i in range(5000):
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