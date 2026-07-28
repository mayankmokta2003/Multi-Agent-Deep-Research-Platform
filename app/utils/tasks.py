from app.state.research_state import ResearchState

# def get_tasks_for_agent(state: ResearchState, agent_name: str):
#     return [
#         step.task
#         for step in state['plan'].research_steps
#         if step.agent == agent_name
#     ]



def get_tasks_for_agent(state: ResearchState, agent_name: str):
    tasks = []
    for step in state['plan'].research_steps:
        if step.agent == agent_name:
            tasks.append(step.task)
    return tasks
