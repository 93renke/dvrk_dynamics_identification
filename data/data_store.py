from robot_model_data import RobotModel

import cloudpickle as pickle
import os.path
#import pickleshare as pickle

class DataStore:
    def __init__(self, model_folder, trajectory_folder, optimal_trajectory_folder, model_name, robot_model=[]):

        # Names
        self._model_folder = model_folder
        self._trajectory_folder = trajectory_folder
        self._optimal_trajectory_folder = optimal_trajectory_folder
        self._model_name = model_name
        self._model_file = self._model_folder + self._model_name + '.pkl'

        # Data
        self.robot_model = robot_model

    def save_data(self):
        with open(self._model_file, 'wr') as f:
            pickle.dump(self.robot_model, f)

    def load_data(self):
        if os.path.exists(self._model_file):
            self.robot_model = pickle.load(open(self._model_file, 'rb'))
        return self.robot_model

    def __serialize_robot_data(self):
        x = 0
