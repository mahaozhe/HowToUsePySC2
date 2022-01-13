# Approach 2: Control Your Own Environment and Agent

The environment of PySC2 is defined in `pysc2.env.sc2_env`, while the actions and observations are defined in `pysc2.lib.features`. The class of `PySC2` environment is `SC2Env`, which Inherits from `pysc2.env.environment.Base`. **You can use the `SC2Env` just like any other *OpenAI Gym* environments.**

A basic template to instantiate the environment and an agent, and run the codes to make the agent interact with the environment can be found [here](./../Approach_2.py).

## To Instantiate An Environment

Import the `SC2Env` from `pysc2.env.sc2_env` and instantiate it by `env = SC2Env([parameters])`.

The definition of the class and all its parameters can be found [here](https://github.com/deepmind/pysc2/blob/master/pysc2/env/sc2_env.py#L121).

Some important arguments:

* `map_name`: the name of the map.
    - You can find the namelist in `pysc2.bin.map_list` or by running `python -m pysc2.bin.map_list`
    - Or you can find them under the `pysc2/maps/` folder, like the script `pysc2/maps/melee.py` lists all the maps of *Melee*:
    ```
    melee_maps = ["Flat32", "Flat48", "Flat64", "Flat96", "Flat128", "Simple64", "Simple96", "Simple128",]
    ```
* `players`：a list, containing one or two instances of `pysc2.env.sc2_env.Agent` or `pysc2.env.sc2_env.Bot`, some maps only allow one agent.
    - Note: the `Agent` and `Bot` is different from the `pysc2.agents.base_agent` we mentioned before, here is an example for these two classes:
    ```python
    class Agent(collections.namedtuple("Agent", ["race", "name"])):
        """Define an Agent. It can have a single race or a list of races."""
	
        def __new__(cls, race, name=None):
            return super(Agent, cls).__new__(cls, to_list(race), name or "<unknown>")
	
	
    class Bot(collections.namedtuple("Bot", ["race", "difficulty", "build"])):
        """Define a Bot. It can have a single or list of races or builds."""
	
        def __new__(cls, race, difficulty, build=None):
            return super(Bot, cls).__new__(cls, to_list(race), difficulty, to_list(build or BotBuild.random))
    ```
* `agent_interface_format`: to define the format of observation and action, like the resolution of the feature maps. It takes an instance of `pysc2.lib.features.AgentInterfaceFormat` or an instance of `pysc2.env.sc2_env.AgentInterfaceFormat`.
    - The number of `AgentInterfaceFormat` should be the same as the length of the list for the above `player` argument, with the same order.
    - Please refer to [the definition](https://github.com/deepmind/pysc2/blob/master/pysc2/lib/features.py#L470) of `AgentInterfaceFormat` for more details.
* `step_mul`: an int to identify after how many steps to take one observation and apply one action. (not the real number of frames). 1 second equals to 16 steps, which means if we set 16 here, we will get the observations every 1 second.
* `game_steps_per_episode`: how many steps of one episode. For example, if we set `200*16` here, it means one episode will last for 200 seconds.
* `save_replay_episodes`: how many episodes to save one replay.
* `replay_dir`: the location to save replays.

## Define A Function to Interact with The Environment

To define a function to interact with the environment, you can refer to the `run_loop` function in [pysc2/env/run_loop.py](https://github.com/deepmind/pysc2/blob/master/pysc2/env/run_loop.py#L23)

Here is also a good reference to instantiate an `SC2Env` and an `Agent`, and use the above `run_loop` function to test them in [pysc2/tests/easy_scripted_test.py](https://github.com/deepmind/pysc2/blob/master/pysc2/tests/easy_scripted_test.py).

## Run the Program

To actually run the codes above, we need the `run` function in `absl.app` package. The function takes in our running function as a parameter, like this:

```python
from pysc2.env import run_loop, sc2_env
from pysc2.agents import random_agent
from absl import app


def main(args):
    agent = random_agent.RandomAgent()

    with sc2_env.SC2Env(map_name="MoveToBeacon", 
	                players=[sc2_env.Agent(sc2_env.Race.terran)],
			agent_interface_format=sc2_env.AgentInterfaceFormat(feature_dimensions=sc2_env.Dimensions(screen=84, minimap=64)), 
			step_mul=16,
			game_steps_per_episode=200 * 16, 
			visualize=True) as env:
	run_loop.run_loop([agent], env, 200)


if __name__ == "__main__":
    app.run(main)
```

**Notes**: When we define the `main` function, it must have at lest one argument, like `args` here. You may not use it, but you have to define it.
