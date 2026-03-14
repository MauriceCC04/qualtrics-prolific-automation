# Qualtrics × Prolific SurveyOps Automation

Prototype tooling for automating parts of a research workflow across **Qualtrics** and **Prolific**: creating surveys, generating participant-study drafts, exporting filter metadata, and supporting rubric-based evaluation workflows.

This repository comes from my bachelor thesis work. The main goal is to make repetitive survey and participant-study setup more reproducible, auditable, and scriptable.

---

## What this project does

### Qualtrics automation
- create surveys programmatically
- add blocks and questions
- support repeatable survey setup without relying entirely on manual UI work

### Prolific automation
- create study drafts linked to external Qualtrics surveys
- prepare launch-ready payloads
- support a safer draft-first workflow before publishing paid studies

### Sampling support
- export available Prolific filters
- generate reusable filter payload examples for study targeting

### Evaluation support
- store rubric and marker assets used in structured evaluation workflows
- support experiments involving rubric-based or LLM-assisted scoring

---

## Why this project matters

Survey and participant-study setup often involves repetitive UI work, manual copying, and fragile configuration steps. That process is slow, hard to audit, and easy to get wrong.

This project turns parts of that workflow into reusable scripts and notebook-based prototypes, making it easier to:
- standardize setup steps
- inspect generated artifacts
- reuse filtering logic
- reduce avoidable mistakes before launching a study

---

## Repository structure

```text
.
├── docs/
│   ├── prompts/
│   └── reference/
├── notebooks/
│   ├── Qualtrics_w_Prolific.ipynb
│   ├── ai_agents_flow_full_task.ipynb
│   ├── qualtrics.ipynb
│   └── test.ipynb
├── outputs/
│   └── prolific_filters.json
├── report/
├── scripts/
│   ├── create_studies.py
│   ├── definitions.py
│   ├── filter_examples.py
│   ├── get_all_filters.py
│   ├── marker_subrubrics.py
│   ├── markers.py
│   └── qualtrics_w_prolific.py
└── README.md
````

---

## Main workflows

### 1. Qualtrics survey setup

Use the Qualtrics API to create and configure surveys programmatically rather than repeating the same UI steps by hand.

### 2. Qualtrics → Prolific handoff

Prepare an external-study flow where Qualtrics is used as the participant-facing survey and Prolific handles recruitment.

### 3. Prolific filter export and payload generation

Export available filtering metadata and generate reusable payloads for study targeting.

### 4. Rubric and evaluation support

Store and reuse structured assets for evaluation experiments involving rubric-driven prompts or LLM-assisted scoring.

---

## Quickstart

### Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\Activate.ps1   # Windows PowerShell
```

### Install dependencies

```bash
pip install requests jupyter
```

Optional, only for notebooks or scripts that call OpenAI:

```bash
pip install openai
```

---

## Configuration

You will need credentials for the APIs you plan to use.

### Qualtrics

* datacenter ID
* API token

### Prolific

* API token

### OpenAI (optional)

* API key

Avoid hardcoding secrets in notebooks or scripts. Prefer environment variables or a local `.env` file excluded from version control.

### Example environment variables

```bash
export QUALTRICS_DATACENTER_ID="..."
export QUALTRICS_API_TOKEN="..."
export PROLIFIC_API_TOKEN="..."
export OPENAI_API_KEY="..."
```

---

## How to run

### Option A: Explore the workflow in notebooks

```bash
jupyter lab
```

Recommended notebooks:

* `notebooks/qualtrics.ipynb` — Qualtrics workflow prototype
* `notebooks/Qualtrics_w_Prolific.ipynb` — end-to-end survey-to-study draft flow
* `notebooks/ai_agents_flow_full_task.ipynb` — prototype LLM-assisted workflow experiments

### Option B: Run utility scripts

#### Export Prolific filters

```bash
python scripts/get_all_filters.py
```

#### Create Prolific study drafts

```bash
python scripts/create_studies.py
```

#### Run the end-to-end workflow script

```bash
python scripts/qualtrics_w_prolific.py
```

---

## Outputs

Generated artifacts are written to `outputs/`.

Example:

* `outputs/prolific_filters.json`

These outputs make the workflow easier to inspect, reuse, and debug.

---

## Safety and cost notes

Be careful with Prolific study publication.

Recommended workflow:

1. create drafts first
2. inspect payloads carefully
3. verify account and workspace settings
4. publish only when confident

This reduces the risk of accidental recruitment spend.

---

## Thesis context

This repository was developed as part of my bachelor thesis work on workflow automation and evaluation support for survey-based research operations.

The `report/` folder contains the thesis-related material and supporting files.

---

## Summary

This repo is best understood as a **workflow automation / research tooling project**, not a polished Python package. Its value is in showing how survey setup, study creation, filtering, and evaluation support can be scripted and made more reproducible across Qualtrics and Prolific.
