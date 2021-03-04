from osim.env import L2M2019Env
from utils import Tools
import json
import chart_studio.plotly  as py
import plotly.graph_objs as go

import plotly.graph_objects as go

# Create random data with numpy
import numpy as np

# print(env.get_observation_dict())

# def init():
#     env = L2M2019Env(visualize=True)
#     observation = env.reset(project=True, seed=None, init_pose=None, obs_as_dict=True)
#     tools = Tools()
#     # state_desc = env.get_state_desc()
#     # body_pos = state_desc.get('body_pos')
#     # print(body_pos)
#
#     for i in range(200):
#         observation, reward, done, info = env.step(tools.active_one_muscle("iliopsoas", "r", 1))
#
#         if i == 20:
#             state_desc = env.get_state_desc()
#             print(type(state_desc["body_pos"]["toes_r"][0:2]))
#             print(state_desc["body_pos"]["talus_l"][0:2])
#             print(state_desc["body_pos"]["talus_r"][0:2])
#             print(state_desc["misc"]["mass_center_pos"])
#             print(state_desc["body_pos_rot"])
#             input("Press Enter to continue...")
#             print(reward)


if __name__ == '__main__':
    #init()
    # with open("C:\\Users\\YunfeiZHAO\\Desktop\\1.json", 'r') as f:
    #     content = f.read()
    #     print(content)
    #     parsed = json.loads(content)
    #     jp = json.dump(parsed, indent=4, sort_keys=True)
    #     print(jp)

    env = L2M2019Env(visualize=True)
    observation = env.reset(project=True, seed=None, init_pose=None, obs_as_dict=True)
    tools = Tools()
    state_desc = env.get_state_desc()
    print(tools.get_reward(state_desc))


