from datetime import datetime
import time
import math
import json

def get_data(step):
    id_val = 'prop.fuel'
    x = int(str(datetime.now().timestamp()).replace('.', ''))
    y = math.sin(step*math.pi/180)

    data =  {
        'timestamp': x,
        'value': y,
        'id': id_val
    }

    return json.dumps(data)

