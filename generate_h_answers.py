"""
Generate structured answers for H01-H06 evaluation scenarios.
Run: python generate_h_answers.py
Outputs: outputs/H01.md through H06.md
"""
import os
import anthropic
from knowledge.afs_knowledge import SYSTEM_PROMPT

SCENARIOS = {
    "H01": """Our existing NIR pilot follows API concentration in one powder formulation at the tablet press feed frame. We are introducing a different API and excipient blend and would like to reuse the calibration. A colleague suggests adding Raman so that the old calibration will remain valid. What should our first technical assessment and experiment be?""",
    "H02": """Our dairy process handles both a relatively clear whey stream and an opaque milk concentrate. We want a pilot for composition monitoring, using laboratory protein and fat results where those variables are relevant. We can compare different measurement interfaces before choosing the installation. What first measurement concepts and comparison experiment would make sense for these two streams?""",
    "H03": """We already have a fluorescence spectrometer and would like to use it to report glucose concentration and viable biomass directly during fermentation. Our only justification is that fluorescence can be very sensitive. We have not identified a fluorescent target, marker or reference relationship. What should the assistant tell us?""",
    "H04": """We want to investigate water content in a petroleum line using MIR ATR. The analyzer would be in another building. We already have a silica fiber cable from a visible or NIR measurement setup and would like to reuse it. The link length, routing and operating conditions have not yet been supplied. Can the assistant approve this concept?""",
    "H05": """We have a liquid process that occasionally goes off specification. We suspect contamination, but we cannot yet name the contaminant or the affected quality variable. We would like you to recommend the best spectroscopy method and exact sensor configuration immediately. What information and first experiment should come before that decision?""",
    "H06": """We read the supplied LED NIR kidney study and want to use the same concept to guide tumor boundary decisions during live surgery. Can we quote its findings as proof that the proposed sensor is ready for that use? We have no new in vivo data and no validation on our own setup. What assessment and next feasibility steps are appropriate?""",
}

os.makedirs("outputs", exist_ok=True)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))

for hid, scenario in SCENARIOS.items():
    print(f"Generating {hid}...")
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": scenario}],
    )
    answer = response.content[0].text
    out_path = f"outputs/{hid}.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# {hid} — AFS Spectroscopy Assessment\n\n")
        f.write(f"## Customer Enquiry\n\n{scenario}\n\n---\n\n")
        f.write(answer)
    print(f"  → {out_path}")

print("\nDone. All outputs saved to outputs/")
