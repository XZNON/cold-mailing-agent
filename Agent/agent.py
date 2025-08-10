from langchain.agents import AgentExecutor,create_tool_calling_agent
from config.initiation import model
from langchain.prompts import ChatPromptTemplate
from tools.sendMail import send_mail,readExcel
from langchain import hub

#initiate the tools
tools = [
    readExcel,
    send_mail
]

# System + user messages
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an automation agent that:
    1. Calls readExcel to get recipient data.
    2. Loops over all rows and calls send_mail for each.
    3. You dont need to write the mails send_mail function alredy does that.
    3. Continues even if one fails.
    4. Defaults job_role to 'Software developer' if missing."""),
    ("user", "{input}"),
    ("assistant", "{agent_scratchpad}")
])

agent = create_tool_calling_agent(model,tools,prompt)

agent_executor  = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose= True
) 

agent_executor.invoke({"input":"Send the emails from the excel file"})