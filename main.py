from Board import Board
from Agent import Agent
from Objects import Objects
import random as rd


def main():
    env = Board(10, 10)
    nb_agents = 10
    nb_objects = 20
    k_take = 0.3
    k_put = 0.3
    step = 1
    mem_size = 10
    agents = [Agent(env, str(i), mem_size, step, k_take, k_put) for i in range(nb_agents)]
    objects = [Objects((['A', 'B'])[i % 2]) for i in range(nb_objects)]
    env.init_squares(objects, agents)

    env.print()
    for i in range(100000):
        agent = rd.choice(agents)
        agent.move()
        agent.percepts()
        agent.chose_action()
        #agent.print()
    print("==============")
    env.print()
    pass


if __name__ == "__main__":
    main()


