# AI Research Team – Multi-Agent System Using CrewAI

An AI-powered multi-agent research system built with **CrewAI** using a **hierarchical process**. A Manager Agent coordinates three specialized agents—Research, Analysis, and Writing—to turn a user-provided topic into a structured research report.

## Agents

| Agent | Responsibility |
|---|---|
| Manager Agent | Delegates tasks, coordinates the workflow, and oversees the final result. |
| Research Agent | Collects relevant information about the topic using the language model's existing knowledge. |
| Analysis Agent | Examines the findings and identifies key insights, patterns, advantages, and limitations. |
| Writing Agent | Produces a structured research report in Markdown format. |

## Workflow

1. The user enters a research topic.
2. The Manager Agent coordinates the work and delegates tasks.
3. The Research Agent prepares research findings.
4. The Analysis Agent evaluates the findings and identifies insights.
5. The Writing Agent prepares the final report.
6. The report is saved as `report.md`.

## Technologies

- Python
- CrewAI
- Ollama
- Qwen 2.5 3B
- python-dotenv

## Requirements

- Python installed on your computer.
- Ollama installed and running.
- The `qwen2.5:3b` model downloaded in Ollama.

Download the model if needed:

```bash
ollama pull qwen2.5:3b
```

Start Ollama if it is not already running:

```bash
ollama serve
```

If Ollama is already running, do not start a second server. You can check it with:

```bash
curl http://localhost:11434/api/tags
```

## Installation

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Install the Python dependencies:

```bash
pip install -r requirements.txt
```

4. Make sure Ollama is running and `qwen2.5:3b` is available.
5. Run the project:

```bash
python main.py
```

When prompted, enter a research topic. The final report will be generated as `report.md`.

## Configuration

The project connects to Ollama at:

```text
http://localhost:11434
```

The model is configured in the Python file as:

```python
LLM(
    model="ollama/qwen2.5:3b",
    base_url="http://localhost:11434",
    temperature=0.3
)
```

## Output

The generated `report.md` contains sections such as:

- Introduction
- Research Findings
- Analysis
- Key Insights
- Conclusion

See [`sample_output.md`](sample_output.md) for an illustrative example.

## Important Note

This version does **not** use an internet search tool. The Research Agent relies on the model's existing knowledge and the information provided in the task. It does not independently retrieve or verify live web sources. For current research, connect a search tool or provide source material.

## Project Structure

```text
AI-Research-Team/
├── main.py
├── requirements.txt
├── README.md
├── sample_output.md
└── report.md        # Generated when the program runs
```

## License

Add a license file if you intend to distribute or reuse this project publicly.
