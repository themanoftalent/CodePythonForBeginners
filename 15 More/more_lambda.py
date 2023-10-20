points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
          #'dict' object has no attribute 'sort' so we use a list



points.sort(key=lambda i: i['x'])
print(points)
