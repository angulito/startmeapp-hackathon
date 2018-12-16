import numpy as np
import pandas as pd

from math import sin, cos, sqrt, atan2, radians
import math

def distance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

class AIBici():
    BICYCLE_RATIO = 0.7

    def __init__(self):
        self.parking = pd.read_csv('datasets/aparcabicis.csv', encoding = "ISO-8859-1", delimiter=';')
        self.pollution = pd.read_csv('datasets/datos_calidad.csv', encoding = "ISO-8859-1")
        self.accidents = pd.read_csv('datasets/AccidentesBicicletas_2018.csv', encoding = "ISO-8859-1")

    def nearest_parking(self, loc):
        best_distance = math.inf
        for index, row in self.parking.iterrows():
            dist = distance(*loc, row['LATITUD'], row['LONGITUD'])

            if dist < best_distance:
                best_distance = dist
                best_parking = row['IDENTIFICADOR_MINT']
                best_loc = (row['LATITUD'], row['LONGITUD'])

        return {'distance': best_distance, 'id': best_parking, 'location': best_loc}

    def bicycle_time(self, results):
        dist_a = results.get('parking_start').get('distance')
        dist_b = results.get('parking_end').get('distance')
        time = self.BICYCLE_RATIO*results.get('parking_distance') + dist_a + dist_b
        return time

    def bicycle_a_to_b(self, a, b):
        p_a = self.nearest_parking(a)
        p_b = self.nearest_parking(b)

        dist_pa_pb = distance(*p_a.get('location'), *p_b.get('location'))

        results = {}
        results['parking_start'] = p_a
        results['parking_end'] = p_b
        results['parking_distance'] = dist_pa_pb
        results['time_expected'] = self.bicycle_time(results)

        return results

    def walking_a_to_b(self, a, b):
        results = {}
        dist = distance(*a, *b)
        results['distance'] = dist
        results['time_expected'] = dist
        return results

    def from_address(self, address):
        MATADERO_LOC = (40.392457, -3.698432)
        EL_PAIS_LOC = (40.43723, -3.623797)
        if address == 'matadero':
            return MATADERO_LOC
        else:
            return EL_PAIS_LOC
