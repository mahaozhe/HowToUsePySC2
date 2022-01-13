# Using StarCraft II as Learning Environment

`PySC2` is DeepMind's Python component of the StarCraft II Learning Environment (SC2LE).

## Installation

**It's strongly recommended to use virtual environments to manage packages.**

You may need to run `pip install --upgrade pip` before all the following steps.

### Install on Windows

* Get `PySC2`
    
    ```
    pip install pysc2
    ```
    **Not recommended unless you need:** download from source, please refer to: <https://github.com/deepmind/pysc2#from-source>

* Get *StarCraft II* game
    
    - Download from Blizzard official network: <https://starcraft2.com/>.
    - You can firstly install the Battle.net Agent/Desktop and install the StarCraft II game in the game launcher: <https://www.blizzard.com/en-us/apps/battle.net/desktop>
    - If you customized the install-location, you might need to set the `SC2PATH` environment variable with your new location.

* Get maps
    
    Create a folder named `Maps` in the game root folder. Then download the maps and mini-maps and extract them into `Maps`. You can start from the mini-games. For example, after you extract the maps in the folder, the path should be like this: `GameFolder/Maps/Melee/XXX.SC2Map`. 
    
    - All map packs: <https://github.com/Blizzard/s2client-proto#downloads>
    - Mini-games: <https://github.com/deepmind/pysc2/releases/download/v1.2/mini_games.zip>
    - Melee maps: <http://blzdistsc2-a.akamaihd.net/MapPacks/Melee.zip>
    
    The password to extract the packages is **iagreetotheeula**

### Install on Linux

* Install `PySC2`: `pip install pysc2`
* Install StarCraft II game:
    - Download the linux package: <https://github.com/Blizzard/s2client-proto/blob/master/README.md#linux-packages>
        * Can using the command: `wget http://blzdistsc2-a.akamaihd.net/Linux/SC2.4.10.zip`
    - Unzip the file at the home path: `unzip -o SC.X.X.zip`
        * The password is **iagreetotheeula**
    - It seems that the maps are already included in the `[StarCraftII]/Maps/` folder, if you need to install the replays, you need to download and unzip them into the `[StarCraftII]/Replays/` folder manually.


## Run Some Built-in Examples

* Run the built-in agent example: `python -m pysc2.bin.agent --map Simple64`
* Run your own agent: `python -m pysc2.bin.agent --map CollectMineralShards --agent pysc2.agents.scripted_agent.CollectMineralShards`
    - Will have more detailed instructions to write and run our self-defined agents later.
* Run two agents against each other `python -m pysc2.bin.agent --map Simple64 --agent2 pysc2.agents.random_agent.RandomAgent`
* Play the games as a human: `python -m pysc2.bin.play --map Simple64`
* List the maps: `python -m pysc2.bin.map_list`
* Watch the replay: `python -m pysc2.bin.play --replay <path-to-replay>`
    - Running an agent and playing as a human save a replay by default. You can watch that replay by running the above command.

## Official Doc of PySC2 and Useful Links

* Before we start, it's very **important** to read the official document from `PySC2`: <https://github.com/deepmind/pysc2/blob/master/docs/environment.md>
    - You can briefly know about (but you may still be very confused with): the structure of `pysc2`, the observations and actions provided by `pysc2`, the environment for reinforcement learning, and so on.
* Introductions to the mini-games (read it when you need): <https://github.com/deepmind/pysc2/blob/master/docs/mini_games.md>

## Start to Use PySC2

* Approach 1: only customize the agent, and run the agent by running the above commands.
    - In this approach, your agent gets observation from the environment and returns actions to interact with it.
    - You need to run the agent using the built-in module `pysc2.bib.agent`
    - It's hard to realize a learning agent.
    - It's a good way to start to know about the environment.
    - [Detailed instructions](./Docs/Using_PySC2_Approach_1.md) and [example codes](./Approach_1.py).

* Approach 2: customize both the environment and the agent, run your codes independently without any built-in modules.
    - More flexible.
    - Can define our logics in your agent, like learning and doing inference.
    - Can run the codes directly without any built-in modules.
    - Can debug easily.
    - [Detailed instructions](./Docs/Using_PySC2_Approach_2.md) and [example codes](./Approach_2.py).

## Main Reference

* PySC2 introduction and documents by DeepMind: <https://github.com/deepmind/pysc2>