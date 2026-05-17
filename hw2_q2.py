from enum import Enum
from collections import namedtuple
from itertools import batched

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def compare_agents(agent1: Agent, agent2: Agent):
    (
        """"" receives two agents as arguements, and return a tuple with the two agents, in their new state.
    """
        ""
    )
    if (
        agent1[1] == Condition.DEAD
        or agent2[1] == Condition.DEAD
        or agent1[1] == Condition.HEALTHY
        or agent2[1] == Condition.HEALTHY
        or (agent1[1] == Condition.CURE and agent2[1] == Condition.CURE)
    ):
        return (agent1, agent2)
    if agent1[1] == Condition.CURE:
        i = agent2[1]
        agent2_new = Agent(agent2[0], Condition(i.value - 1))
        return (agent1, agent2_new)
    if agent2[1] == Condition.CURE:
        i = agent1[1]
        agent1_new = Agent(agent1[0], Condition(i.value - 1))
        return (agent1_new, agent2)
    else:
        i_1 = agent1[1].value
        i_2 = agent2[1].value
        agent1_new = Agent(agent1[0], Condition(i_1 + 1))
        agent2_new = Agent(agent2[0], Condition(i_2 + 1))
        return (agent1_new, agent2_new)


def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent type, containing a 'name' field and a 'category' field, with 'category' being of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result of the meeting.
    """
    list_of_agents = []
    to_add = []
    for agent in agent_listing:
        if agent.category != Condition.HEALTHY and agent.category != Condition.DEAD:
            list_of_agents.append(agent)
        else:
            to_add.append(agent)
    list_new = list(batched(list_of_agents, n=2))
    to_return = []
    for tup in list_new:
        if len(tup) == 2:
            agent1, agent2 = compare_agents(tup[0], tup[1])
            to_return.append(agent1)
            to_return.append(agent2)
        elif len(tup) == 1:
            to_return.append(tup[0])
    to_return += to_add
    return to_return
