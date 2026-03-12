# Benchmarking LLM Evaluative Performance:
Development of a Pipeline for Automatic Validation — Qualtrics × Prolific SurveyOps (Bachelor Thesis Prototype)

Research prototype for **programmatically building surveys** (Qualtrics) and **launching participant studies** (Prolific), with optional **LLM-assisted** helpers for rubric/prompting workflows.

This repo is intentionally *not* a polished library — it’s the organized code + artifacts behind a bachelor thesis project.

## What this project does

- **Qualtrics API automation**
  - Create a survey, add blocks/questions, publish/activate
- **Prolific API automation**
  - Create study drafts (and optionally publish) pointing to an external Qualtrics link
- **Sampling support tooling**
  - Export all available Prolific filters to JSON/CSV
  - Generate example filter payloads for faster study setup
- **Rubric assets**
  - “Markers” + sub-rubrics used for structured evaluation / scoring

> ⚠️ Safety note: publishing Prolific studies can spend money. Start with drafts and double-check account/workspace settings.

---

## Repo structure

```text
.
├── notebooks/            # Notebook-first prototypes (Qualtrics + Prolific flows)
├── scripts/              # Python utilities + rubric dictionaries
├── outputs/              # Generated artifacts (e.g., Prolific filter exports)
├── report/               # Thesis PDF (+ source zip)
└── docs/
    ├── prompts/          # Prompts/guidelines + supporting workflow files
    └── reference/        # Papers/slides/notes used during thesis work
````

---

## Quickstart

### 1) Create an environment

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\Activate.ps1  # Windows PowerShell
```

### 2) Install minimal dependencies

```bash
pip install requests jupyter
```

Optional (only if you use notebooks/scripts that call OpenAI):

```bash
pip install openai
```

---

## Configuration (credentials)

Several notebooks/scripts include placeholders like:

* `API_TOKEN = ""`
* `DATACENTER_ID = ""`

You will need credentials for:

* **Qualtrics**: datacenter ID + API token (`X-API-TOKEN`)
* **Prolific**: API token
* **OpenAI** (optional): API key (only for LLM-assisted experiments)

**Do not commit secrets.** Prefer environment variables or a local `.env` file (and add it to `.gitignore`).

---

## How to run

### Option A — Run notebooks (recommended for understanding the workflow)

```bash
jupyter lab
```

Then open:

* `notebooks/qualtrics.ipynb` — Qualtrics API workflow (connect → create → add content)
* `notebooks/Qualtrics_w_Prolific.ipynb` — End-to-end: Qualtrics survey → Prolific study draft
* `notebooks/ai_agents_flow_full_task.ipynb` — LLM-assisted chaining experiments (prototype)

### Option B — Run scripts (utility-style)

> Some filenames contain spaces — use quotes when running them.

Export Prolific filters to JSON/CSV and generate example payloads:

```bash
python "scripts/get_all_filters.py"
```

Create a Prolific study draft (and optionally publish):

```bash
python "scripts/create_studies.py"
```

End-to-end Qualtrics → Prolific flow (exported from notebook):

```bash
python scripts/qualtrics_w_prolific.py
```

---

## Outputs

Generated artifacts are stored in `outputs/`, e.g.:

* `outputs/prolific_filters.json`
* `outputs/prolific_filters.csv`

---

## Thesis report

* `report/Thesis.pdf` — the final thesis document
* `report/thesis.zip` — thesis source archive

---

## Notes / limitations (prototype honesty)

* This is a **research prototype** (not production-ready).
* Some scripts are **exported notebooks** and may reuse variable names / require manual edits.
* Publishing Prolific studies can trigger recruitment and costs — use drafts until you’re confident.
