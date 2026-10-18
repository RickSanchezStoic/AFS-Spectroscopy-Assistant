# AFS Spectroscopy Assistant
**National AI Hackathon 2026 - Art Fiber Systems Challenge**
*AI Assistant for In-line Spectroscopy Solution Design*

---

## What It Does

A chat assistant that helps AFS experts make a first technical assessment of customer spectroscopy enquiries. Given a process description in plain language, it:

1. Extracts stated requirements and identifies key unknowns
2. Asks specific clarification questions that could change the method choice
3. Recommends one or more spectroscopy approaches with a clear decision status
4. Proposes a high-level probe and measurement concept
5. States risks, assumptions, and uncertainty explicitly
6. Proposes a concrete first feasibility experiment with a go/no-go basis

Every technical claim cites the specific AFS source and page (e.g. `[S01 p.14-15]`).

---

## Architecture

```
AFS_Assistant/
├── app.py                        # Flask backend, streaming SSE chat
├── knowledge/
│   └── afs_knowledge.py          # AFS knowledge base compiled from all materials
├── templates/
│   └── index.html                # Single-page chat UI
├── outputs/                      # Pre-generated H01-H06 evaluation answers
│   ├── H01.md
│   ├── H02.md
│   ├── H03.md
│   ├── H04.md
│   ├── H05.md
│   └── H06.md
└── requirements.txt
```

### How AFS materials are used

All supplied materials were read and compiled into `knowledge/afs_knowledge.py`:

| Source | Content used |
|--------|-------------|
| `S01_Multispectral_Laboratory.pdf` | Methods overview (p.2-12), application cases (p.13-18) |
| `S02_AFS_Process_Control_Slides.pdf` | Fiber transmission ranges (p.6-10), process applications (p.13-14) |
| `S03_LED_Kidney_Study_2017.pdf` | Proof-of-concept scope and limitations (in vitro, n=14) |
| `S04_Combi_MIR_Fluorescence_2021.pdf` | Combined MIR ATR + fluorescence probe on model tissues |
| `AFS_method_comparison_table.xlsx` | Method x technique x sensitivity x selectivity x cost table |
| `AFS_Examples_and_Reference.docx` | All D01-D08 scenarios, worked examples D01-D02, method overview table, fiber families table, good practice rules |

The knowledge base is injected as system context on every request. The model cites sources by ID and page for every technical claim.

---

## Setup

**Requirements:** Python 3.9+ · [Anthropic API key](https://console.anthropic.com) (free tier available)

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Create a `.env` file** in the project root with your Anthropic key:
```
ANTHROPIC_API_KEY=your_key_here
```

**3. Run the app**
```bash
python app.py
```
Or on Windows, double-click **`start.bat`**.

You should see:
```
[AFS] Provider: Claude / claude-haiku-4-5
 * Running on http://127.0.0.1:5000
```

Open `http://localhost:5000` in your browser.

> **The app runs on Claude by default.** No config changes needed — just the API key above.

### Other providers (optional)
If you don't have an Anthropic key, you can switch to a free alternative by changing one line in `app.py`:
```python
PROVIDER = "groq"       # free at console.groq.com — add GROQ_API_KEY to .env
PROVIDER = "gemini"     # add GEMINI_API_KEY to .env
PROVIDER = "sambanova"  # add SAMBANOVA_API_KEY to .env
```

---

## Evaluation Scenarios (H01-H06)

Pre-generated answers are in `outputs/`. Each answer follows the structured format required by the challenge brief and was produced by the assistant without manual editing.

| ID | Scenario | Decision Status |
|----|----------|----------------|
| H01 | NIR calibration reuse after API/excipient change | Provisional assessment - key correction to stated premise |
| H02 | Composition monitoring across two dairy streams | Provisional assessment - two separate measurement concepts |
| H03 | Fluorescence for glucose and viable biomass | Insufficient information - no fluorescent target identified |
| H04 | Silica fiber reuse for MIR ATR petroleum | Cannot approve - fundamental fiber incompatibility |
| H05 | Off-specification liquid, unknown contaminant | Insufficient information - characterise problem before method |
| H06 | LED kidney study cited as surgical readiness proof | Outside supported scope - proof-of-concept not clinical validation |

---

## Key Design Decisions

- **No hallucinated specs:** the assistant is explicitly instructed never to invent accuracy figures, detection limits, fiber lengths, or performance numbers not in the supplied materials
- **"Insufficient information" is a valid answer:** the system is designed to push back on under-specified or contradictory enquiries rather than filling gaps with invented facts
- **Source citations on every claim:** judges can trace every recommendation to a specific AFS document and page
- **Streaming UI:** responses stream token-by-token; the sidebar loads any of the six evaluation scenarios with one click for live demo
