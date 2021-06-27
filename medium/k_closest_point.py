import math

import pandas as pd


def kClosest(points, k):
    center = [0, 0]
    df = pd.DataFrame(points, columns=['x', 'y'])
    df['x_2'] = df['x'].pow(2)
    df['y_2'] = df['y'].pow(2)
    df['x_plus_y'] = df['x_2'] + df['y_2']
    df['distance'] = df['x_plus_y'].pow(0.5)
    df = df.sort_values(['distance'])
    df = df[['x', 'y']].head(k)
    return df.values.tolist()
    # print(df)


def kClosest_basic(points, k):
    for i in range(len(points)):
        dis = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
        points[i].append(dis)
    points = sorted(points, key=lambda x: x[2])
    res = [[x[0], x[1]] for x in points]
    return (res[:k])


if __name__ == '__main__':
    print(kClosest_basic(points=[[1, 3], [-2, 2]], k=1))
