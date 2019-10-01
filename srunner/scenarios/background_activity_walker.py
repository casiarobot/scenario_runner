#!/usr/bin/env python

#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

"""
Scenario spawning elements to make the town dynamic and interesting
"""

import py_trees

from srunner.scenariomanager.atomic_scenario_behavior import *
from srunner.scenarios.basic_scenario import *


BACKGROUND_ACTIVITY_SCENARIOS = ["BackgroundActivityWalkers"]


class BackgroundActivityWalkers(BasicScenario):

    """
    Implementation of a dummy scenario
    """

    category = "BackgroundActivityWalkers"

    def __init__(self, world, ego_vehicle, config, randomize=False, debug_mode=False, timeout=35 * 60):
        """
        Setup all relevant parameters and create scenario
        """
        self.config = config
        self.debug = debug_mode

        self.timeout = timeout  # Timeout of scenario in seconds

        super(BackgroundActivityWalkers, self).__init__("BackgroundActivityWalkers",
                                                 ego_vehicle,
                                                 config,
                                                 world,
                                                 debug_mode,
                                                 terminate_on_failure=True,
                                                 criteria_enable=True)

    def _initialize_actors(self, config):
        for actor in config.other_actors:
            new_actors = CarlaActorPool.request_new_batch_actors_walkers(actor.model,
                                                                         actor.amount,
                                                                         actor.transform)
            if new_actors is None:
                raise Exception("Error: Unable to add actor {} at {}".format(actor.model, actor.transform))

            for _actor in new_actors:
                self.other_actors.append(_actor)



    def _create_test_criteria(self):
        """
        A list of all test criteria will be created that is later used
        in parallel behavior tree.
        """
        pass

    def __del__(self):
        """
        Remove all actors upon deletion
        """
        self.remove_all_actors()
