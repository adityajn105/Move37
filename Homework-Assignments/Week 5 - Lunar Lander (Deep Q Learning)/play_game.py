import numpy as np
import gym
import torch
import torch.nn as nn
import argparse
import collections
import os

class DQN(nn.Module):
    def __init__(self, in_features, n_actions):
        super(DQN,self).__init__()
        self.neuralnet = nn.Sequential(
            nn.Linear(in_features,256),
            nn.ReLU(),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Linear(128,64),
            nn.ReLU(),
            nn.Linear(64,n_actions)
        )
        
    def forward(self,x):
        return self.neuralnet(x)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model", required=True, help="Model file to load")
    parser.add_argument("-r", "--record", help="Directory to store video recording")
    
    env = gym.make('LunarLander-v2')
    args = parser.parse_args()

    if args.record:
    	if not os.path.exists(os.path.join('.',args.record)):
    		os.makedirs(os.path.join('.',args.record))
    	env = gym.wrappers.Monitor(env, args.record)
 
    net = DQN(env.observation_space.shape[0], env.action_space.n)
    net.load_state_dict(torch.load(args.model, map_location=lambda storage, loc: storage))

    state = env.reset()
    total_reward = 0.0
    c = collections.Counter()

    while True:
        env.render()
        
        state_v = torch.tensor(np.array([state], copy=False))
        
        q_vals = net(state_v).data.numpy()[0]

        action = np.argmax(q_vals)
        
        c[action] += 1
        
        state, reward, done, _ = env.step(action)
        
        total_reward += reward
        if done:
            break
    print("Total reward: %.2f" % total_reward)
    print("Action counts:", c)
    if args.record:
        env.env.close()
