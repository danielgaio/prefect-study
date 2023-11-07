# What is prefect?
# Prefect is a new workflow management system, designed for modern infrastructure and powered by the open-source Prefect Core workflow engine. Users organize Tasks into Flows, and Prefect takes care of the rest.

# Things you can do with Prefect:
# 1 - Coordinating
# 2 - Scheduling
# 3 - Monitoring & Alerting

# Installation
# > pip install prefect

# Check version
# > prefect version

# Show dashboard
# > prefect server start

# Main concepts
# 1 - Task: a unit of work
# 2 - Flow: a collection of tasks
# 3 - Subflow: a flow that is used as a task within another flow
# 4 - FlowRunner: a class that runs a flow
# 5 - State: the result of running a task or flow
# 6 - TaskRunner: a class that runs a task
# 7 - Parameter: a value passed to a flow at runtime
# 8 - Schedule: a set of rules for when a flow should run
# 9 - Storage: a location where flow data is stored
# 10 - Backend: a location where flow runs are stored

# Deployment (an .yaml specification file)
# 1 - Build (specify the entry point, the file that contains the flow. After : specify the name of the flow to call):
# > prefect deployment build prefect_studies.py:say_hello -n say_hello_deployment
# 2 - Apply (push it to the server):
# > prefect deployment apply say_hello_deployment.yaml

# To execute flow runs from this deployment, start an agent that pulls work from the 'default' work queue:
# > prefect agent start -q 'default'

# This 'default' agent is just one agent that is on the default-work-pool. You can create your own agents and pools.


from hmac import new
from prefect import flow, task

@task
def create_message():
    msg = "Hello world from prefect!"
    return msg

@flow
def something_else():
    # this is a subflow
    result = 10
    return result   

@flow
def say_hello():
    sub_flow_message = something_else()
    task_message = create_message()
    new_message = task_message + " " + str(sub_flow_message)
    print(new_message)

if __name__ == "__main__":
    say_hello()