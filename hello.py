from datetime import datetime
import time
import math
import json
from exam import get_data
# def get_data(step):
#     id_val = 'prop.fuel'
#     x = int(str(datetime.now().timestamp()).replace('.', ''))
#     y = math.sin(step*math.pi/180)
#
#     data = {
#         'timestamp': x,
#         'value': y,
#         'id': id_val
#     }
#
#     return data

if __name__ == '__main__':
    print(get_data(5))
    print('hello')