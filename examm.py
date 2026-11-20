
from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv

load_dotenv()

# LLM configuration using Ollama
llm = LLM(
    model="ollama/qwen2.5:3b",
    base_url="http://localhost:11434",
    temperature=0.3
)

# 1. Research Agent
research_agent = Agent(
    role="Research Specialist",
    goal="Collect relevant information about the given topic.",
    backstory="""
    You are an expert researcher.
    You collect important facts, information
    and knowledge about different topics.
    """,
    llm=llm,
    verbose=True
)

# 2. Analysis Agent
analysis_agent = Agent(
    role="Research Analyst",
    goal="Analyze research findings and identify key insights.",
    backstory="""
    You are an experienced research analyst.
    You analyze information, identify patterns,
    advantages, disadvantages and conclusions.
    """,
    llm=llm,
    verbose=True
)

# 3. Writing Agent
writing_agent = Agent(
    role="Research Report Writer",
    goal="Prepare a well-structured research report.",
    backstory="""
    You are a professional report writer.
    You convert research findings into
    clear and organized research reports.
    """,
    llm=llm,
    verbose=True
)

# 4. Manager Agent
manager_agent = Agent(
    role="Research Team Manager",
    goal="Manage agents and coordinate the research workflow.",
    backstory="""
    You are an experienced AI project manager.
    You delegate tasks to the Research Agent,
    Analysis Agent and Writing Agent.
    You coordinate the complete workflow
    and ensure the final report is complete.
    """,
    llm=llm,
    allow_delegation=True,
    verbose=True
)

# 5. Research Task
research_task = Task(
    description="""
    Research the topic: {topic}
    Collect important information, facts and details.
    """,
    expected_output="A detailed document containing research findings."
)

# 6. Analysis Task
analysis_task = Task(
    description="""
    Analyze the research findings.
    Identify key insights, patterns,
    advantages, disadvantages and conclusions.
    """,
    expected_output="A detailed analysis with key insights."
)

# 7. Writing Task
writing_task = Task(
    description="""
    Prepare a structured research report containing:
    1. Introduction
    2. Research Findings
    3. Analysis
    4. Key Insights
    5. Conclusion
    """,
    expected_output="A complete and well-structured research report.",
    output_file="report.md"
)

# 8. Create Hierarchical Crew
research_crew = Crew(
    agents=[
        research_agent,
        analysis_agent,
        writing_agent
    ],
    tasks=[
        research_task,
        analysis_task,
        writing_task
    ],
    manager_agent=manager_agent,
    process=Process.hierarchical,
    verbose=True
)

# 9. Execute the Crew
topic = input("Enter your research topic: ")

result = research_crew.kickoff(
    inputs={"topic": topic}
)

print("\n===== FINAL RESEARCH REPORT =====\n")
print(result)

print("\nReport saved as report.md")
