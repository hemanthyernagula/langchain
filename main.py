from langchain.agents import create_tool_calling_agent, tool
from app.helpers.langchain_helper import phi3
from langchain.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

@tool
def add_numbers(a:int,b:int) -> int:
    """
    Add two numbers and return the result.
    
    Parameters:
    a (int): The first number to add.
    b (int): The second number to add.
    
    Returns:
    int: The sum of the two numbers.
    """
    print(f"adding {a}, {b} ")
    return a + b


tools = [add_numbers]

agent = create_tool_calling_agent(phi3, tools, prompt)

agent_executer = AgentExecuter(agent=agent, tools=tools, verbose=True)
agent_executer.invoke({"input": "what is the addition of 2 and 3"})




