import json


def move(offset_point, initial_points):
    results = []
    for point in initial_points:
        if isinstance(point, str):
            parsed = json.loads(point)
            parsed['x'] += offset_point['x']
            parsed['y'] += offset_point['y']
            results.append(parsed)
        else:
            point['x'] += offset_point['x']
            point['y'] += offset_point['y']
            results.append(point)


polyline = [
  {'x': 0, 'y': 0},
  {'x': 10, 'y': 10},
  '{"x": 20, "y": 20}',
  {'x': 30, 'y': 30},
]

print(move(offset_point=[{'x': 10, 'y': -5}], initial_points=polyline))
