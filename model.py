import random
from mesa import Model, Agent
from mesa.time import RandomActivation

from mesa.datacollection import DataCollector
import numpy as np


class SchellingAgent(Agent):

    def __init__(self, unique_id, model, unit_price, production_cost):
        super().__init__(unique_id, model)
        self.unit_price = unit_price
        self.production_cost = production_cost
        self.total_gross_margin = 0
        self.unit_sold_rount = 0

    def step(self):
        self.unit_price = max(np.mean(
            [agent.unit_price for agent in self.model.schedule.agents if agent.unique_id != self.unique_id]),
            self.production_cost) * (100+random.randint(0,10)-5)/100.0
        print("[%d] %f" % (self.unique_id, self.unit_price))


class Schelling(Model):
    '''
    Model class for the Schelling segregation model.
    '''

    def __init__(self, agent_count=3):
        '''
        '''

        self.schedule = RandomActivation(self)
        self.market_price = 100



        for i in range(0, agent_count):
            agent = SchellingAgent(i, self, random.randint(95, 100), random.randint(85, 95))
            self.schedule.add(agent)
            setattr(self, "market_price_%d" % i, 100)



        self.datacollector = DataCollector(
            {"market_price_%d" % i: "market_price_%d" % i for i in range(0, agent_count)}
        )

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        '''
        Run one step of the model. If All agents are happy, halt the model.
        '''
        self.schedule.step()

        for k, agent in enumerate(self.schedule.agents):
            setattr(self, "market_price_%d" % k, agent.unit_price)
        self.datacollector.collect(self)

