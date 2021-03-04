import numpy as np
import math
from numpy import linalg as LA
from sklearn.metrics.pairwise import cosine_similarity

# Tools for training
# 1) direction():

class Tools:
    dict_muscle = {'abd': 'HAB',
                   'add': 'HAD',
                   'iliopsoas': 'HFL',
                   'glut_max': 'GLU',
                   'hamstrings': 'HAM',
                   'rect_fem': 'RF',
                   'vasti': 'VAS',
                   'bifemsh': 'BFSH',
                   'gastroc': 'GAS',
                   'soleus': 'SOL',
                   'tib_ant': 'TA'}

    def active_one_muscle(self, name, leg, excitation):
        pos = 0
        activations = np.zeros(22)
        for MUS, mus in self.dict_muscle.items():
            if name == MUS or name == mus:
                if leg == "r":
                    activations[pos] = excitation
                elif leg == "l":
                    activations[pos + 11] = excitation
                else:
                    print("Wrong leg")
                    return
            pos += 1
        return activations

    def get_direction(self, toes_l, toes_r, mass_center_pos):
        l = np.asarray(toes_l)
        r = np.asarray(toes_r)
        mp = np.asarray((l + r) / 2)
        mass_center_pos = np.asarray(mass_center_pos)
        body_direction = mass_center_pos - mp
        return body_direction

    # get angles of the of Knee, Hip, Ankle
    def get_angle(self, joint, bone1, bone2):
        v1 = bone1 - joint
        v2 = bone2 - joint
        return np.arccos(np.inner(v1, v2)/(LA.norm(v1)*LA.norm(v2))).item(0)

    # get the angles of three joints on each leg:
    # return array of rhip, rknee, rankle, lhip, lknee, lankle
    def get_angles(self, state_desc):
        body_pos = state_desc["body_pos"]
        angles = []
        angles.append(body_pos["hip_r"])
        angles.append(body_pos["knee_r"])
        angles.append(body_pos["ankle_r"])
        angles.append(body_pos["hip_l"])
        angles.append(body_pos["knee_l"])
        angles.append(body_pos["ankle_l"])
        return angles

    def get_reward(self, direction, state_desc):
        ms = state_desc["misc"]["mass_center_pos"]
        des = np.array([0, 0, 1])
        err = des - ms
        reward = LA.norm(err)
        if reward == 0:
            return 0
        else:
            return 1/reward**2


    # def get_reward(self, direction, state_desc):
    #     pl = state_desc["body_pos"]["talus_l"]
    #     pr = state_desc["body_pos"]["talus_r"]
    #     ms = state_desc["misc"]["mass_center_pos"]
    #
    #     center_2_feet = np.asarray((np.asarray(pl) + np.asarray(pr)) / 2)
    #     if direction == "forward":
    #         center_2_feet[0] = 1
    #     if direction == "left":
    #         center_2_feet[2] = 1
    #     if direction == "right":
    #         center_2_feet[1] = 1
    #     direction_real = self.get_direction(pl, pr, ms)
    #
    #     direction_real = np.asarray([direction_real])
    #     direction_to_fall = np.asarray([center_2_feet])
    #     penalty = cosine_similarity(direction_real, direction_to_fall)[0][0]
    #     #penalty = np.pi - np.arccos(cosine)
    #     #penalty = np.arccos(penalty)
    #     return penalty

if __name__ == '__main__':
     tools = Tools()
    # #print(tools.active_one_muscle("rect_fem", "r", 1))
    # a = math.sqrt(3)
    # #print(tools.get_direction([-1, 0], [1, 0], [a, -1, 0]))
    # print(tools.get_angle(np.array([0,0,0]), np.array([0,1,0]), np.array([0,0,1])))
