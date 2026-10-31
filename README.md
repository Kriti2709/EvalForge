# EvalForge

**Failure-Driven Evaluation and Autonomous Improvement Platform for LLM Applications**

## Overview

EvalForge is a developer-first platform designed to improve the reliability of Large Language Model (LLM) applications.

Rather than simply measuring AI application performance, EvalForge aims to identify why failures occur, reproduce them, propose evidence-backed improvements, and prevent recurring issues through automated regression testing.

## Core Features

- **Background Monitoring:** Lightweight instrumentation for collecting application evaluation traces.
- **Automated Evaluation:** Measure answer correctness, retrieval quality, grounding, latency and estimated cost.
- **Failure Diagnosis:** Identify likely causes of incorrect or unsupported responses.
- **Failure Replay:** Reproduce previously observed failures using saved inputs and configurations.
- **Regression Detection:** Identify performance deterioration and recurring failures.
- **AI-Assisted Improvements:** Generate proposed prompt and configuration changes.
- **Natural Language Control:** Allow developers to adjust proposed changes using prompts.
- **Change Management:** Review modifications, approve changes and restore previous configurations.

## Technology Stack

- Python
- FastAPI
- Streamlit
- SQLite
- SQLAlchemy
- scikit-learn
- Pydantic
- Pytest
- GitHub Actions
- Docker

## Project Status

Currently under active development.

The initial release focuses on Python-based RAG applications and reproducible evaluation workflows.

## Development Roadmap

1. Project architecture and initialization.
2. Benchmark dataset management.
3. RAG application integration.
4. Controlled failure simulation.
5. Evaluation engine.
6. Failure diagnosis.
7. Background monitoring.
8. Experiment storage.
9. Failure replay.
10. Regression detection.
11. Improvement proposal generation.
12. Natural-language change adjustment.
13. Dashboard and version control.
14. Testing and initial release.

## Project Goal

Make AI applications more reliable, measurable and easier to improve, while keeping the developer in control of consequential changes.