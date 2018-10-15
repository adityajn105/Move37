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
