# Qualtrics × Prolific SurveyOps Automation

Prototype tooling for automating parts of a research workflow across **Qualtrics** and **Prolific**: creating surveys, generating participant-study drafts, exporting filter metadata, and supporting rubric-based LLM evaluation experiments.

This repository comes from my bachelor thesis work. The goal is to make repetitive survey/study setup more reproducible, auditable, and scriptable.

---

## What this project does

### Qualtrics automation
- Create surveys programmatically
- Add blocks and questions
- publish / activate survey flows

### Prolific automation
- Create study drafts linked to external Qualtrics surveys
- prepare launch-ready payloads
- support draft-first workflows before spending budget on live recruitment

### Sampling support
- Export available Prolific filters to JSON / CSV
- Generate example filter payloads for faster study setup

### Evaluation assets
- Store rubric / marker dictionaries used in structured evaluation workflows
- support LLM-assisted scoring and validation experiments

---

## Why this project matters

Survey and participant-study setup often involves repetitive UI work, manual copying, and fragile configuration steps. That is slow, hard to audit, and easy to get wrong.

This project shows how to turn that process into a semi-automated workflow with:
- API-driven setup
- reusable payload generation
- exportable artifacts
- safer draft-first execution

---

## Repository structure

```text
.
├── docs/
│   ├── prompts/            # prompt assets, workflow notes, and supporting docs
│   └── reference/          # papers, slides, and background materials
├── notebooks/              # notebook-first prototypes for survey/study workflows
├── outputs/                # generated artifacts, such as Prolific filter exports
├── report/                 # thesis PDF and source archive
├── scripts/                # Python utilities and workflow scripts
└── README.md

Main workflows
1) Qualtrics survey setup
Use the Qualtrics API to create and configure surveys programmatically rather than repeating UI steps by hand.
2) Qualtrics → Prolific handoff
Prepare an external-study flow where a Qualtrics survey is used as the participant-facing instrument and Prolific handles recruitment.
3) Prolific filter export and payload generation
Export available filtering metadata and generate reusable payloads for study targeting.
4) Rubric / evaluation support
Store and reuse structured assets for evaluation experiments involving LLM-generated ratings or rubric-driven prompts.

Quickstart
Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\Activate.ps1   # Windows PowerShell
Install dependencies
pip install requests jupyter
Optional, only for notebooks or scripts that call OpenAI:
pip install openai

Configuration
You will need credentials for the APIs you plan to use:
	•	Qualtrics
	◦	datacenter ID
	◦	API token
	•	Prolific
	◦	API token
	•	OpenAI (optional)
	◦	API key
Avoid hardcoding secrets in notebooks or scripts. Prefer environment variables or a local .env file that is excluded from version control.
Example variables:
export QUALTRICS_DATACENTER_ID="..."
export QUALTRICS_API_TOKEN="..."
export PROLIFIC_API_TOKEN="..."
export OPENAI_API_KEY="..."

How to run
Option A: Explore the workflow in notebooks
jupyter lab
Recommended notebooks:
	•	notebooks/qualtrics.ipynb — Qualtrics workflow
	•	notebooks/Qualtrics_w_Prolific.ipynb — end-to-end survey-to-study draft flow
	•	notebooks/ai_agents_flow_full_task.ipynb — prototype LLM-assisted workflow experiments
Option B: Run utility scripts
Some filenames may require quotes when run from the shell.
Export Prolific filters:
python "scripts/get_all_filters.py"
Create Prolific study drafts:
python "scripts/create_studies.py"
Run the exported end-to-end workflow script:
python scripts/qualtrics_w_prolific.py

Outputs
Generated artifacts are written to outputs/.
Examples include:
	•	outputs/prolific_filters.json
	•	outputs/prolific_filters.csv
These outputs make the workflow easier to inspect, reuse, and debug.

Safety and cost notes
Be careful with Prolific study publication.
Recommended workflow:
	1	create drafts first
	2	inspect payloads carefully
	3	verify workspace / account settings
	4	publish only when confident
This reduces the risk of accidentally triggering recruitment spend.

Thesis report
The report/ folder contains the thesis document and supporting archive:
	•	report/thesis.pdf
	•	report/thesis.zip

```
