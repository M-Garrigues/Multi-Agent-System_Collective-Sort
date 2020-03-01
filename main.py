from Board import Board
from Agent import Agent
from Objects import Objects
import random as rd


def main():
    env = Board(15, 15)
    nb_agents = 10
    nb_objects = 60
    k_take = 0.51
    k_put = 0.41
    step = 2
    mem_size = 10
    agents = [Agent(env, str(i), mem_size, step, k_take, k_put) for i in range(nb_agents)]
    objects = [Objects((['A', 'B'])[i % 2]) for i in range(nb_objects)]
    env.init_squares(objects, agents)

    print("Proba take           proba put")
    for fa in range(1,9):
        fa = fa/8.0
        print(1-(fa / (k_take + fa)) ** 2, "", 1-(k_put / (k_put + fa)) ** 2)

    env.print()
    for i in range(50000):
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


