from langgraph.graph import StateGraph
from langgraph.graph.utils import visualize_graph
from workflow.chatbot_workflow import chatbot_workflow

def visualize_workflow():
    workflow = chatbot_workflow()
    graph = StateGraph(workflow)
    return visualize_graph(graph)

if __name__ == "__main__":
    visualize_workflow()
