from langchain.tools import tool
import uuid

@tool
def uuid_generator():
    """
    Generate and return a uuid .
    """
    return str(uuid.uuid4())

