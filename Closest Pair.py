import math
from math import ceil, floor, inf


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)



def shortest_d(input_x, input_y):

    if len(input_x) <= 3:
        s_dis = inf
        for i in range(len(input_x)-1):
            dis_tmp = distance(input_x[i], input_x[i+1])
            if dis_tmp < s_dis:
                s_dis = dis_tmp
        return round(s_dis,6)
    else:
        #Divide
        half_n = len(input_x)//2
        left_points = input_x[:half_n]
        right_points = input_x[half_n:]

        mid_x = input_x[half_n][0]       #Line
        
        Qy,Ry = [], []
        for point in input_y:
            if point[0] < mid_x:
                Qy.append(point)
            else:
                Ry.append(point)
        
        #Conquer
        l_s_t = shortest_d(left_points, Qy)
        r_s_t = shortest_d(right_points, Ry)

        #Combine
        delta = min(l_s_t, r_s_t)   
        # x_bar = left_points[-1][0]

        #Remove the data >delta from Line
        #candidates in delta region
        candidates = []
        for point in input_y:
            if abs(point[0] - mid_x) < delta:
                candidates.append(point)



        #1 + 7
        for i in range(len(candidates)-1):
            j = i + 1
            while j < min(len(candidates),  i + 7) and abs(candidates[i][1] - candidates[j][1]) < delta:
                dis_tmp = distance(candidates[i], candidates[j])
                if dis_tmp < delta:
                    delta = dis_tmp
                j += 1

        return round(delta,6)


def main():
    n_sets = int(input())
    if n_sets>= 0:
        for n in range(n_sets):
            n_points = int(input())
            points = []
            for i in range(n_points):
                point = [float(v) for v in input().split()]

                points.append(point)

            #Sort
            input_x = sorted(points , key=lambda k: k[0]) 
            input_y = sorted(points , key=lambda k: k[1]) 
            # input_x, input_y = first_sort(points)
            output = shortest_d(input_x, input_y)
            print('%6f' % (output))


main()



