from skmob import TrajDataFrame
from skmob.utils import constants
from skmob.measures import individual

import numpy as np
import pandas as pd


import math

class TestIndividualMetrics:
    def setup_method(self):
        latitude = constants.LATITUDE
        longitude = constants.LONGITUDE
        date_time = constants.DATETIME
        user_id = constants.UID

        lat_lons = np.array([[43.8430139, 10.5079940],
                             [43.5442700, 10.3261500],
                             [43.7085300, 10.4036000],
                             [43.7792500, 11.2462600],
                             [43.8430139, 10.5079940],
                             [43.7085300, 10.4036000],
                             [43.8430139, 10.5079940],
                             [43.5442700, 10.3261500],
                             [43.5442700, 10.3261500],
                             [43.7085300, 10.4036000],
                             [43.8430139, 10.5079940],
                             [43.7792500, 11.2462600],
                             [43.7085300, 10.4036000],
                             [43.5442700, 10.3261500],
                             [43.7792500, 11.2462600],
                             [43.7085300, 10.4036000],
                             [43.7792500, 11.2462600],
                             [43.8430139, 10.5079940],
                             [43.8430139, 10.5079940],
                             [43.5442700, 10.3261500]])

        traj = pd.DataFrame(lat_lons, columns=[latitude, longitude])

        traj[date_time] = pd.to_datetime([
            '20110203 8:34:04', '20110203 9:34:04', '20110203 10:34:04', '20110204 10:34:04',
            '20110203 8:34:04', '20110203 9:34:04', '20110204 10:34:04', '20110204 11:34:04',
            '20110203 8:34:04', '20110203 9:34:04', '20110204 10:34:04', '20110204 11:34:04',
            '20110204 10:34:04', '20110204 11:34:04', '20110204 12:34:04',
            '20110204 10:34:04', '20110204 11:34:04', '20110205 12:34:04',
            '20110204 10:34:04', '20110204 11:34:04'])

        traj[user_id] = [1 for _ in range(4)] + [2 for _ in range(4)] + \
                        [3 for _ in range(4)] + [4 for _ in range(3)] + \
                        [5 for _ in range(3)] + [6 for _ in range(2)]

        self.unique_users = [1,2,3,4,5,6]

        self.traj = traj.sort_values([user_id, date_time])
        self.trjdat = TrajDataFrame(traj, user_id=user_id)

    def test_radius_of_gyration(self):
        output = individual.radius_of_gyration(self.trjdat)

        assert (len(output) == 6)
        assert (isinstance(output, pd.core.frame.DataFrame))

        assert (math.isclose(output[output.uid==1]['radius_of_gyration'].values[0], 31.964885737))
        assert (math.isclose(output[output.uid == 2]['radius_of_gyration'].values[0], 14.988909726))
        assert (math.isclose(output[output.uid == 3]['radius_of_gyration'].values[0], 31.964885737))
        assert (math.isclose(output[output.uid == 4]['radius_of_gyration'].values[0], 35.241089869))
        assert (math.isclose(output[output.uid == 5]['radius_of_gyration'].values[0], 30.727237693))
        assert (math.isclose(output[output.uid == 6]['radius_of_gyration'].values[0], 18.146860183))

    def test_k_radius_of_gyration(self):
        output = individual.k_radius_of_gyration(self.trjdat)

        assert (len(output) == 6)
        assert (isinstance(output, pd.core.frame.DataFrame))

        assert (math.isclose(output[output.uid == 1]['2k_radius_of_gyration'].values[0], 18.14686018))
        assert (math.isclose(output[output.uid == 2]['2k_radius_of_gyration'].values[0], 8.0811433))
        assert (math.isclose(output[output.uid == 3]['2k_radius_of_gyration'].values[0], 9.64969996))
        assert (math.isclose(output[output.uid == 4]['2k_radius_of_gyration'].values[0], 9.64969996))
        assert (math.isclose(output[output.uid == 5]['2k_radius_of_gyration'].values[0], 34.07360735))
        assert (math.isclose(output[output.uid == 6]['2k_radius_of_gyration'].values[0], 18.14686018))

        output = individual.k_radius_of_gyration(self.trjdat, k=1)

        assert (len(output) == 6)
        assert (isinstance(output, pd.core.frame.DataFrame))

        assert (math.isclose(output[output.uid == 1]['1k_radius_of_gyration'].values[0], 0))
        assert (math.isclose(output[output.uid == 2]['1k_radius_of_gyration'].values[0], 0))
        assert (math.isclose(output[output.uid == 3]['1k_radius_of_gyration'].values[0], 0))
        assert (math.isclose(output[output.uid == 4]['1k_radius_of_gyration'].values[0], 0))
        assert (math.isclose(output[output.uid == 5]['1k_radius_of_gyration'].values[0], 0))
        assert (math.isclose(output[output.uid == 6]['1k_radius_of_gyration'].values[0], 0))

    def test_random_entropy(self):
        output = individual.random_entropy(self.trjdat)

        assert (len(output) == 6)
        assert (isinstance(output, pd.core.frame.DataFrame))

        assert (math.isclose(output[output.uid == 1]['random_entropy'].values[0], 2))
        assert (math.isclose(output[output.uid == 2]['random_entropy'].values[0], 1.5849625))
        assert (math.isclose(output[output.uid == 3]['random_entropy'].values[0], 2))
        assert (math.isclose(output[output.uid == 4]['random_entropy'].values[0], 1.5849625))
        assert (math.isclose(output[output.uid == 5]['random_entropy'].values[0], 1.5849625))
        assert (math.isclose(output[output.uid == 6]['random_entropy'].values[0], 1))

    def test_uncorrelated_entropy(self):
        output = individual.uncorrelated_entropy(self.trjdat)

        assert (len(output) == 6)
        assert (isinstance(output, pd.core.frame.DataFrame))

        assert (math.isclose(output[output.uid == 1]['uncorrelated_entropy'].values[0], 2))
        assert (math.isclose(output[output.uid == 2]['uncorrelated_entropy'].values[0], 1.5000000))
        assert (math.isclose(output[output.uid == 3]['uncorrelated_entropy'].values[0], 2))
        assert (math.isclose(output[output.uid == 4]['uncorrelated_entropy'].values[0], 1.5849625))
        assert (math.isclose(output[output.uid == 5]['uncorrelated_entropy'].values[0], 1.5849625))
        assert (math.isclose(output[output.uid == 6]['uncorrelated_entropy'].values[0], 1))

        output = individual.uncorrelated_entropy(self.trjdat, normalize=True)

        assert (len(output) == 6)
        assert (isinstance(output, pd.core.frame.DataFrame))

        assert (math.isclose(output[output.uid == 1]['norm_uncorrelated_entropy'].values[0], 1))
        assert (math.isclose(output[output.uid == 2]['norm_uncorrelated_entropy'].values[0], 0.94639463))
        assert (math.isclose(output[output.uid == 3]['norm_uncorrelated_entropy'].values[0], 1))
        assert (math.isclose(output[output.uid == 4]['norm_uncorrelated_entropy'].values[0], 1))
        assert (math.isclose(output[output.uid == 5]['norm_uncorrelated_entropy'].values[0], 1))
        assert (math.isclose(output[output.uid == 6]['norm_uncorrelated_entropy'].values[0], 1))

    def test_real_entropy(self):
        output = individual.real_entropy(self.trjdat)

        assert (len(output) == 6)
        assert (isinstance(output, pd.core.frame.DataFrame))

        assert (math.isclose(output[output.uid == 1]['real_entropy'].values[0], 1.60000000))
        assert (math.isclose(output[output.uid == 2]['real_entropy'].values[0], 1.14285714285))
        assert (math.isclose(output[output.uid == 3]['real_entropy'].values[0], 1.60000000))
        assert (math.isclose(output[output.uid == 4]['real_entropy'].values[0], 1.1887218755))
        assert (math.isclose(output[output.uid == 5]['real_entropy'].values[0], 1.1887218755))
        assert (math.isclose(output[output.uid == 6]['real_entropy'].values[0], 0.6666666666))


    def test_maximum_distance(self):
        output = individual.maximum_distance(self.trjdat)

        assert (len(output) == 6)
        assert (isinstance(output, pd.core.frame.DataFrame))

        assert (math.isclose(output[output.uid == 1]['maximum_distance'].values[0], 68.14698568))
        assert (math.isclose(output[output.uid == 2]['maximum_distance'].values[0], 36.29370121))
        assert (math.isclose(output[output.uid == 3]['maximum_distance'].values[0], 59.66188292))
        assert (math.isclose(output[output.uid == 4]['maximum_distance'].values[0], 78.4910639))
        assert (math.isclose(output[output.uid == 5]['maximum_distance'].values[0], 68.14698568))
        assert (math.isclose(output[output.uid == 6]['maximum_distance'].values[0], 36.29370121))

    def test_distance_straight_line(self):
        output = individual.distance_straight_line(self.trjdat)

        assert (len(output) == 6)
        assert (isinstance(output, pd.core.frame.DataFrame))

        assert (math.isclose(output[output.uid == 1]['distance_straight_line'].values[0], 123.74008488))
        assert (math.isclose(output[output.uid == 2]['distance_straight_line'].values[0], 70.57908362))
        assert (math.isclose(output[output.uid == 3]['distance_straight_line'].values[0], 96.10397212))
        assert (math.isclose(output[output.uid == 4]['distance_straight_line'].values[0], 97.79046189))
        assert (math.isclose(output[output.uid == 5]['distance_straight_line'].values[0], 127.8088686))
        assert (math.isclose(output[output.uid == 6]['distance_straight_line'].values[0], 36.29370121))

    def test_number_of_location(self):
        output = individual.number_of_locations(self.trjdat)

        assert (len(output) == 6)
        assert (isinstance(output, pd.core.frame.DataFrame))

        assert (output[output.uid == 1]['number_of_locations'].values[0] == 4)
        assert (output[output.uid == 2]['number_of_locations'].values[0] == 3)
        assert (output[output.uid == 3]['number_of_locations'].values[0] == 4)
        assert (output[output.uid == 4]['number_of_locations'].values[0] == 3)
        assert (output[output.uid == 5]['number_of_locations'].values[0] == 3)
        assert (output[output.uid == 6]['number_of_locations'].values[0] == 2)

    def test_home_location(self):
        output = individual.home_location(self.trjdat)

        assert (len(output) == 6)
        assert (isinstance(output, pd.core.frame.DataFrame))

        assert (output[output.uid == 1]['lat'].values[0] == 43.544270)
        assert (output[output.uid == 2]['lat'].values[0] == 43.8430139)
        assert (output[output.uid == 3]['lat'].values[0] == 43.544270)
        assert (output[output.uid == 4]['lat'].values[0] == 43.544270)
        assert (output[output.uid == 5]['lat'].values[0] == 43.708530)
        assert (output[output.uid == 6]['lat'].values[0] == 43.544270)

        assert (output[output.uid == 1]['lng'].values[0] == 10.326150)
        assert (output[output.uid == 2]['lng'].values[0] == 10.507994)
        assert (output[output.uid == 3]['lng'].values[0] == 10.326150)
        assert (output[output.uid == 4]['lng'].values[0] == 10.326150)
        assert (output[output.uid == 5]['lng'].values[0] == 10.403600)
        assert (output[output.uid == 6]['lng'].values[0] == 10.326150)

    def test_max_distance_from_home(self):
        output = individual.max_distance_from_home(self.trjdat)

        assert (len(output) == 6)
        assert (isinstance(output, pd.core.frame.DataFrame))

        assert (math.isclose(output[output.uid == 1]['max_distance_from_home'].values[0], 78.4910639))
        assert (math.isclose(output[output.uid == 2]['max_distance_from_home'].values[0], 36.29370121))
        assert (math.isclose(output[output.uid == 3]['max_distance_from_home'].values[0], 78.4910639))
        assert (math.isclose(output[output.uid == 4]['max_distance_from_home'].values[0], 78.4910639))
        assert (math.isclose(output[output.uid == 5]['max_distance_from_home'].values[0], 68.14698568))
        assert (math.isclose(output[output.uid == 6]['max_distance_from_home'].values[0], 36.29370121))

    def test_number_of_visits(self):
        output = individual.number_of_visits(self.trjdat)

        assert (len(output) == 6)
        assert (isinstance(output, pd.core.frame.DataFrame))

        assert (output[output.uid == 1]['number_of_visits'].values[0] == 4)
        assert (output[output.uid == 2]['number_of_visits'].values[0] == 4)
        assert (output[output.uid == 3]['number_of_visits'].values[0] == 4)
        assert (output[output.uid == 4]['number_of_visits'].values[0] == 3)
        assert (output[output.uid == 5]['number_of_visits'].values[0] == 3)
        assert (output[output.uid == 6]['number_of_visits'].values[0] == 2)