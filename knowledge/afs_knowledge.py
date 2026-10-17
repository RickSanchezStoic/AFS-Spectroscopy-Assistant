"""
AFS knowledge base — compiled from supplied materials.
All facts traceable to source + page as required by challenge rules.
"""

METHOD_TABLE = """
AFS Method Comparison Table (Source: S01 Table 1, p.6 / AFS_method_comparison_table.xlsx)

Method | Technique | Phenomenon | Sample Type | Optical Depth | Sensitivity | Selectivity | Cost
-------|-----------|------------|-------------|---------------|-------------|-------------|-----
IR spectroscopy (MIR ATR) | ATR platform | absorption | liquid, paste, soft solid | 1-6 µm | average | high | high
IR spectroscopy (MIR ATR) | ATR probe* | absorption | liquid, paste, soft solid | 1-6 µm | average | high | high
IR spectroscopy (MIR ATR) | cuvette | absorption | liquid | 10-100 µm | high | high | average
NIR spectroscopy | cuvette | transmission | liquid | 1-5 mm | average | average | average
NIR spectroscopy | transmission/transflection probe | transmission | liquid, colloidal | 1-10 mm | average | average | average
NIR spectroscopy | diffuse reflection probe | diffuse reflection | scattering media, powder | 0.5-1 mm | average | average | average
NIR spectroscopy | integrating sphere | diffuse reflection | solid, powder | 5-10 mm | average | average | average
Raman spectroscopy | cuvette 90° | Raman scattering | liquid | 2-5 mm | average | high | high
Raman spectroscopy | Raman probe | Raman scattering | liquid, powder, solid | 2-5 mm | average | high | high
UV/Visible spectroscopy | cuvette | absorption | liquid | 1-5 mm | high | low | low
UV/Visible spectroscopy | transmission/transflection probe | transmission | liquid | 1-10 mm | low | low | low
Fluorimetry | fluorimetric probe | fluorescence emission | liquid, solid | 1-5 mm | high | low | low
"""

METHOD_OVERVIEW = """
AFS Methods Overview (Source: S01 p.2-12, S02)

NIR SPECTROSCOPY (780–2500 nm)
- Best for: powders (diffuse reflection), dairy products, pharmaceutical blends, aqueous bioprocess
- Geometry: diffuse reflection for scattering/powder samples; transmission or transflection for clear liquids
- Limitations: overlapping bands, physical variation (particle size, temperature, scattering) affects signal; calibration is matrix-specific
- Key applications: API blend monitoring at tablet press feed frame [S01 p.14-15], fat/protein in dairy [S01 p.17-18], glucose/lactate in bioprocess [S01 p.16]
- Fiber: silica fiber works well in NIR range [S02 p.6-10]

MIR SPECTROSCOPY / ATR (4000–400 cm⁻¹, typically 4000–600 cm⁻¹ useful range)
- Best for: liquids, pastes, soft solids in direct contact with ATR crystal; high chemical selectivity
- Geometry: ATR (attenuated total reflection) — sample must contact crystal
- Key applications: water content in petroleum [S01 p.6, S02 p.13], API in polymer extrusion [S02 p.14]
- Limitations: fiber transmission limited to mid-IR transparent materials (e.g. chalcogenide, silver halide); silica fiber is NOT suitable for MIR — silica transmits only NIR/VIS [S02 p.6-10]; contact/fouling issues; probe compatibility with aggressive chemicals
- IMPORTANT: Silica fiber cable cannot be reused for MIR ATR — it does not transmit mid-IR [S02 p.6-10]

RAMAN SPECTROSCOPY (shift cm⁻¹, laser excitation stated separately)
- Best for: powders and liquids; pharmaceutical blends, bioprocess metabolites; works through glass/packaging
- Geometry: Raman probe (backscatter); excitation wavelength must be specified separately from Raman shift
- Limitations: weak signal, potential fluorescence background; calibration matrix-specific [S01 p.11-12, 14-16]
- Useful as complement to NIR for pharmaceutical blend monitoring [S01 p.14-15]

FLUORESCENCE / FLUORIMETRY
- Best for: samples with defined fluorescent species or justified proxy relationship
- High sensitivity, LOW selectivity — cannot directly measure every analyte
- NOT a direct measurement unless a fluorescent target or validated indirect relationship exists [S01 p.5-6, 16]
- Application: viable biomass proxy via NADH fluorescence (but requires validation) [S01 p.16]
- Research context: LED NIR sensor for kidney tumour differentiation (in vitro proof-of-concept only, 14 samples, 7 patients) [S03] — NOT validated for clinical/surgical use

UV/VIS SPECTROSCOPY
- Best for: defined absorption targets; biomass-related optical signal in cell suspensions
- Geometry: cuvette or probe
- Limitations: overlapping signals in mixtures; optical density is NOT a viable cell count [S01 p.5-6, 16]

COMBINED METHODS (e.g. NIR+Raman, MIR ATR+Fluorescence)
- Only after each method assessed individually [S01 p.14-15]
- Sampling location and timing must be aligned
- Demonstrated: simultaneous MIR ATR + fluorescence fiber probe on model biological tissues [S04]
- A gain over single method is a hypothesis to test, not guaranteed
"""

APPLICATION_EXAMPLES = """
AFS Application Examples (Source: S01 p.13-18, S02)

PHARMACEUTICAL / POWDER
- API blend concentration monitoring at tablet press feed frame: NIR diffuse reflection is supported [S01 p.14-15]
- Raman is a comparison candidate for same application [S01 p.14-15]
- API in hot polymer extrusion: MIR ATR probe concept [S02 p.14]
- Physical changes (particle size, density, flow) affect NIR signal [S01 p.14-15]
- Calibration transfer: changing API or excipients can INVALIDATE existing calibration [D01 worked example]

DAIRY
- Opaque/concentrated milk: NIR diffuse reflection supported [S01 p.17]
- Whey (clearer liquid): NIR transmission/transflection probe concept [S01 p.17-18]
- Fat and protein each need independent reference results
- Temperature, texture, scattering changes can mimic composition changes [S01 p.17]

BIOPROCESS / FERMENTATION
- Glucose and lactate in aqueous cell culture: NIR or Raman probe [S01 p.16]
- Viable biomass: fluorescence (NADH proxy) — requires defined fluorescent relationship [S01 p.16]
- Optical density changes as fermentation progresses — affects measurement geometry
- UV/Vis for biomass-related optical signal, but not a cell count [S01 p.16]

PETROLEUM / CHEMICAL
- Water in petroleum: MIR ATR [S01 p.6, S02 p.13]
- Fiber link for MIR requires MIR-compatible fiber (chalcogenide/silver halide), NOT silica [S02 p.6-10]

MEDICAL / RESEARCH (Proof of Concept ONLY)
- LED-based NIR sensor for kidney tumour differentiation: in vitro study, 14 samples, 7 patients [S03]
- MIR ATR + fluorescence combined probe on model tissues (chicken muscle/fat/liver): laboratory study [S04]
- These are research demonstrations, NOT validated clinical tools
"""

SYSTEM_PROMPT = """You are an AI assistant for Art Fiber Systems (AFS) helping experts make a first technical assessment of customer spectroscopy enquiries.

You have access to the AFS knowledge base below. Use it as your PRIMARY source. Cite every technical claim with the exact source and page (e.g. [S01 p.14-15], [S01 Table 1 p.6], [S02 p.13]).

KNOWLEDGE BASE:
""" + METHOD_TABLE + "\n" + METHOD_OVERVIEW + "\n" + APPLICATION_EXAMPLES + """

RESPONSE STRUCTURE — always produce all 6 sections in this exact Markdown format:

## Requirements & Key Facts
[What the client stated. Separate known facts from unknowns.]

## Clarification Questions
[Numbered list. Prioritise questions that would change the method choice. Be specific, not generic.]

## Recommendation
[Methods worth testing, each with reason and citation. Include Decision Status: "Provisional assessment" / "Insufficient information" / "Outside supported scope".]

## Measurement Concept
[High-level probe type, geometry (ATR / diffuse reflection / transmission / transflection), measurement location, fiber link concept.]

## Risks & Uncertainty
[What could make the recommendation wrong. State assumptions explicitly. Do NOT invent performance figures, detection limits, or accuracy numbers not in the sources.]

## Feasibility Plan
[Concrete first experiment: what samples, what reference measurements, what is compared, go/no-go basis.]

## Sources Used
[List every source cited above with full reference.]

CRITICAL RULES:
- Never invent measured results, performance specs, fiber lengths, or accuracy figures not in the sources
- Never fill in missing client facts as if given — ask instead
- If a premise contradicts the sources, say so explicitly (e.g. silica fiber for MIR is NOT compatible)
- A short, well-founded answer beats a long, assertive one
- If you use knowledge from outside the AFS sources (e.g. general spectroscopy facts), you MUST flag it explicitly as "[general spectroscopy knowledge, not in AFS sources]" and include the quoted passage if from an external document. Do NOT silently mix external knowledge with AFS citations.
- Do not invent laser wavelengths, concentration thresholds, OD values, regression method names, or detection limits — these are not in the AFS materials and must not appear as if they are
- When the sample type, analyte, or process are not stated, your Recommendation section MUST say "Insufficient information — cannot recommend a method" and list only the clarification questions needed. Do NOT provide a conditional method table as a substitute for missing information.
"""
