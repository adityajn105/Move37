## Week 2 : Dynamic Programming for Value Iteration Algorithm
1. Simple Bellman equation is valid only for only deterministic environment.
2. Suppose in our game, mario agent is drunk and floor is slippery, so our mario agent has some probability < 1 for following our commands. This is a stochastic environment where our agent has some probability of following right path.
3. For this stochastic environment we will modify our Bellman Equation as follows
	* ``` V[s] = max[a]{ sum[s',r] { p(s',r|s,a)[r + gamma * V[s']] } } ```
4. We will follow following algorithm:
	1. Initialize a table V of value estimates for each square with all zeroes
	2. Loop over every state S
		1. From state s loop over every possible action a
			1. Get a list of all (prob,reward,s') transition tuples from state s, action a
			2. expected_reward = sum of all possible reward multiplied by their probs
			3. expected_value = lookup V[s'] for each possible s' multipliedby probability, sum
			4. action_value = expected_reward + GAMMA * expected_value
		2. set V[s] to the best acttion_value found
	3. repeat step 2-8 until largest change in V[s] is below over threshold

## Week 2 : Policy Iterations and Value Iterations
1. Policy Iterations includes: policy evaluation + policy improvement and the two are expected iteratively until policy converges.
2. Value iterations includes: finding optimal value function + one policy extraction. There is no repeat of the two because once the value function is optimal, then the policy out of it should also be optimal.
3. Finding optimal value function can also be seen as combination of policy improvement (due to max) and truncated policy evaluation.
4. The algorithm for policy evaluation and finding optimal value function are highly similar except for a max operation.
5. Similarly, the key steps to policy imporvement and policy extraction are identical except the former involves a stability check.