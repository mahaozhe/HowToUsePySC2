"""
A template for approach 1.

The agent randomly selects actions.

Use the `pysc2.bin.agent` module to run `MyAgent` when your commands are in the current path:
    python -m pysc2.bin.agent --map <MAP_NAME> --agent pysc2EnvTemplate.MyAgent
"""

# to be compatible with python 2.x
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

# import the BaseAgent class which we should derive from
from pysc2.agents import base_agent
# import actions
from pysc2.lib import actions
# import features
from pysc2.lib import features


# define our own agent
class MyAgent(base_agent.BaseAgent):

    def step(self, obs):
        super(MyAgent, self).step(obs)

        # -------------------#
        # RL algorithm here~ #
        # -------------------#

        # get available actions
        function_id = np.random.choice(obs.observation.available_actions)
        # randomly select one action and its argument
        args = [[np.random.randint(0, size) for size in arg.sizes]
                for arg in self.action_spec.functions[function_id].args]
        # pack up the actions as a `FunctionCall`
        function_call = actions.FunctionCall(function_id, args)

        # return the actions a.k.a. the function_call
        return function_call
