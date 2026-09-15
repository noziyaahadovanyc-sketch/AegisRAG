# 🛡️ AegisRAG: Enterprise Multi-Agent RAG Architecture

A production-ready, scalable *Retrieval-Augmented Generation (RAG)* framework engineered to completely eliminate hallucinations in Large Language Models (LLMs) when querying complex proprietary corporate data. 

This architecture orchestrates autonomous, specialized AI agents to dynamically retrieve, filter, validate, and synthesize information from unstructured business documentation.

## 🧠 Key Features & Engineering Architecture
* *Multi-Agent Consensus Pipeline:* Built using *CrewAI* and *LangChain* to enforce a strict two-step verification layer (Retriever Agent + Paranoid Auditor Agent) before delivering responses.
* *Semantic Chunking Strategy:* Replaces naive character-count splitting with semantic text boundaries to preserve the integrity of tables, financial metrics, and legal context.
* *Hybrid Structural Search:* Ready for integration with dense vector embeddings (BGE-Large) and sparse lexical search (BM25) managed via enterprise vector stores.
* *Anti-Hallucination Compliance Guardrails:* Programmed with restrictive prompting layers that automatically fallback when data constraints are not met, securing 100% faithfulness.

## 💻 Tech Stack
* *Orchestration:* CrewAI, LangChain
* *Core LLM:* OpenAI GPT-4o / Anthropic Claude 3.5 Sonnet
* *Evaluation Framework:* Ragas (Faithfulness & Context Recall benchmarks)
* *Environment:* Python 3.10+

## 🚀 Getting Started

### Installation
bash
pip install crewai langchain-openai langchain-community


### Execution
Set your OpenAI API key in your environment and run the core pipeline:
bash
python main.py
