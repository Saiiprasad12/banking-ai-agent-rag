from langchain.agents import Tool, initialize_agent
from langchain.llms import HuggingFacePipeline

def dummy_tool_func(input_text):
    return f"Banking process triggered: {input_text}"

tools = [Tool(name="TriggerBankingWorkflow", func=dummy_tool_func, description="Trigger banking workflows.")]

llm = HuggingFacePipeline.from_model_id(model_id="deepseek-ai/deepseek-coder-6.7b-instruct", task="text-generation")

agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)

def run_agent(query):
    return agent.run(query)
