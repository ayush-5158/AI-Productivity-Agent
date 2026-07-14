from langchain.agents.middleware import wrap_tool_call
from langchain_core.messages import ToolMessage

@wrap_tool_call
def middleman(request,handler):
    """
    Ask for human approval before calling a tool
    """

    tool_name = request.tool_call['name']
    confirm = input(f"Agent is calling {tool_name}. (Y/N)")
    if confirm.lower()=='n':
        return ToolMessage(content="Tool call is denied by the user")
    
    return handler(request)