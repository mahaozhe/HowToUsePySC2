# Approach 1: Define Your Own Agent

## How to Use Custom-Defined Agents?

Run the command:

```
python -m pysc2.bin.agent --map <Map> --agent <Agent>
```

Assuming that your own agent class named `MyAgentClassName` is defined in `MyAgentFile.py` in a directory `[PATH]`, then when you run command in the `[PATH]` directory, you can identify the agent by:

```
python -m pysc2.bin.agent --map <Map> --agent MyAgentFile.MyAgentClassName
```

## How to Design My Own Agent and Make It Interact with PySC2?

Any custom designed agent should derive from the `BaseAgent` class (in `pysc2.agents.base_agent`) and override the `step(self, obs)` function, where the argument `obs` is the observations.

A basic template for a self-defined agent can be found [here](./../Approach_1.py).

## How to Get Observations and Rewards from The Environment?

The observations (as well as the rewards) taken from environment are all included in the parameter `obs` of the `step` function, such as the feature maps, valid actions, rewards and so on. 

for example:
* state, viz. different types of feature maps: `obs.observation["screen"][feature_map_name]`
* valid actions: `obs.observation["available_actions"]` or `obs.observation.available_actions`
* rewards: `obs.reward`

## How to Send Actions to Interact with The Environment?

In the `step` function, return the action (packed up as a `FunctionCall` instance).

