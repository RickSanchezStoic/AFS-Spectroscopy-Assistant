# H01–H06 Pre-Generated Outputs

These files contain the structured assessments for the six evaluation scenarios supplied by Art Fiber Systems for the National AI Hackathon 2026.

## Provenance

| File | Scenario | Decision Status |
|------|----------|----------------|
| H01.md | NIR calibration reuse after API/excipient change | Provisional assessment |
| H02.md | Composition monitoring across two dairy streams | Provisional assessment |
| H03.md | Fluorescence for glucose and viable biomass | Insufficient information |
| H04.md | Silica fiber reuse for MIR ATR petroleum | Cannot approve |
| H05.md | Off-specification liquid, unknown contaminant | Insufficient information |
| H06.md | LED kidney study cited as surgical readiness proof | Outside supported scope |

**Model used:** claude-opus-4-5 via `generate_h_answers.py`  
**Generated:** October 2026  
**Editing:** None — outputs are verbatim model responses to the scenario text.

## Reproducing

```bash
# Set ANTHROPIC_API_KEY in .env, then:
python generate_h_answers.py
```

The outputs committed here were produced in a single uninterrupted run. The assistant may give slightly different wording on a re-run (LLM non-determinism) but the decision status and structure are stable.
