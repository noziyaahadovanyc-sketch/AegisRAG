import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain.tools import tool

# 1. SETUP & MODEL CONFIGURATION
# In production, keys are loaded via environment variables (.env)
os.environ["OPENAI_API_KEY"] = "your-openai-api-key-here"
llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

# 2. HYBRID SEARCH TOOL GENERATION
@tool("Hybrid Document Search Tool")
def hybrid_search_tool(query: str) -> str:
    """
    Executes a high-precision hybrid vector and semantic search 
    across the internal corporate documentation database (PDFs, financial reports).
    """
    # Vector DB connection (Pinecone/Milvus) goes here. 
    # Returning structured mock context for workflow demonstration:
    mock_database = (
        "RETRIEVED KNOWLEDGE BASE CONTEXT:\n"
        "According to the Q4 financial report, AegisCorp's net profit reached $4.2 billion, "
        "marking a 12% year-over-year growth. The primary growth driver was the mass deployment "
        "of autonomous Enterprise-grade AI Agents across Fortune 500 clients."
    )
    return mock_database

# 3. CORE AI AGENTS DEFINITION
researcher_agent = Agent(
    role="Senior Research Analyst",
    goal="Extract and filter precise facts from the documentation database without guessing.",
    backstory="""You are an expert at deep-diving into unstructured enterprise data. 
    You use precise search queries, ignore noise, and gather only verified facts. 
    You never assume things that are not explicitly stated in the context.""",
    tools=[hybrid_search_tool],
    llm=llm,
    verbose=True
)

auditor_agent = Agent(
    role="Lead Quality Assurance and Compliance Auditor",
    goal="Verify that the final response is strictly factual and entirely free of hallucinations.",
    backstory="""You are a paranoid security and truth compliance officer. 
    Your job is to compare the researcher's output against the raw retrieved data. 
    If you detect even a single word of speculation, extrapolation, or hallucination, 
    you reject the answer and demand a rewrite. You ensure 100% faithfulness.""",
    tools=[],
    llm=llm,
    verbose=True
)

# 4. PIPELINE TASKS DEFINITION
user_question = "What was AegisCorp's net profit in Q4 and what specifically drove the growth?"

task_retrieve = Task(
    description=f"Analyze the user query: '{user_question}'. Use the Hybrid Document Search Tool to find all relevant metrics and reasons.",
    expected_output="A structured list of facts, numbers, and direct quotes from the document context.",
    agent=researcher_agent
)

task_audit = Task(
    description="""Review the facts gathered by the researcher. Compare them with the source database capability. 
    Draft a professional, executive-ready response for the client. 
    STRICT COMPLIANCE RULE: If the answer cannot be fully proven by the context, state that the information is unavailable.""",
    expected_output="The final audited response, 100% accurate, ready to be delivered to the Enterprise client.",
    agent=auditor_agent
)

# 5. ORCHESTRATION & KICKOFF
aegis_crew = Crew(
    agents=[researcher_agent, auditor_agent],
    tasks=[task_retrieve, task_audit],
    process=Process.sequential,
    verbose=True
)

if _name_ == "_main_":
    print("--- LAUNCHING AEGISRAG MULTI-AGENT ARCHITECTURE ---")
    final_output = aegis_crew.kickoff()
    print("\n================ FINAL SYSTEM ANSWER ================")
    print(final_output)
