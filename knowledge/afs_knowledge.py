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
AFS Application Examples (Source: S01 p.13-18, S02, D01-D08 development scenarios)

PHARMACEUTICAL / POWDER [S01 p.14-15]
- API blend concentration monitoring at tablet press feed frame: NIR diffuse reflection is supported [S01 p.14-15]
- Raman is a comparison candidate: 785 nm excitation wavelength stated for pharma blend application [S01 p.15]
- NIR detects hydrogen bonds and asymmetric polar groups; Raman detects molecular backbone and symmetrical non-polar groups — they are complementary [S01 p.15]
- NIR+Raman combined: low-level data fusion (spectra merged into one matrix), then PLS regression; can predict API potency or coating thickness with higher accuracy than single method [S01 p.15]
- Multispectral NIRaman combined probe fits inside tablet press feed frame [S01 p.15, Fig.6]
- API in hot polymer extrusion: MIR ATR probe concept [S02 p.14]; interface may foul; offline assays available
- Physical changes (particle size, density, flow) affect NIR signal [S01 p.14-15]
- Calibration transfer: changing API or excipients can INVALIDATE existing calibration [S01 p.10]

DAIRY [S01 p.17-18]
- Opaque/concentrated products (yogurt, butter, whole milk concentrates): NIR Reflection (diffuse reflection probe, flush-mounted) [S01 p.17-18]
- Clear/semi-transparent liquids (skim milk, whey, permeate): NIR Transmission preferred; path length 1-10 mm [S01 p.18]
- Transflection probe: can work for both low-fat and high-fat products as a combined solution [S01 p.18]
- Whey (clearer liquid, D03): NIR transmission/transflection probe concept; BUT turbidity may change — probe geometry must handle this variation [S01 p.17-18]
- NIR Reflection sensitive to surface characteristics and fat globule size; scattering correction (MSC, SNV) needed before PLS regression [S01 p.17]
- Fat and protein each need independent reference results
- Temperature, texture, scattering changes can mimic composition changes [S01 p.17]
- Advanced labs also use Fluorescence, Raman, and MIR ATR for higher molecular specificity in dairy [S01 p.18]

BIOPROCESS / FERMENTATION [S01 p.16-17]
- Glucose and lactate in aqueous cell culture (D04): NIR or Raman probe; Raman well-suited for aqueous environments (low water absorbance); medium and cell population change during the run
- Raman detects: glucose, lactate, glutamine, acetate, TCD/VCD (Fig.7 spectral map) [S01 p.17]
- Fluorescence detects: NAD(P)H, proteins, vitamins, ethanol/metabolic changes, cell mass — down to nM-uM range [S01 p.16-17]
- NIR/MIR detects: glucose, lactate, ammonium, pH, biomass, fructose, acetic acid, ethanol [S01 p.17]
- UV/Vis tracks cell suspension turbidity (correlates with cell density) as low-cost real-time biomass signal, but optical density is NOT a viable cell count [S01 p.16]
- For high optical density (turbid/opaque) media: UV-ATR probe needed instead of transmission [S01 p.16]
- Biomass/growth monitoring during yeast fermentation (D05): "biomass signal" and "metabolic signal" must be defined separately before selecting method; broth optical density increases during run
- Viable biomass via fluorescence: requires defined fluorescent target (e.g. NADH) or validated proxy [S01 p.16]

PETROLEUM / CHEMICAL
- Water in petroleum (D06): MIR ATR [S01 p.6, S02 p.13]; fiber link for MIR requires MIR-compatible fiber (chalcogenide/silver halide), NOT silica [S02 p.6]; analyzer may be outside process area — fiber length and safety requirements matter
- Water measurement at remote location: a fiber link from probe to analyzer outside process area is the typical AFS approach [S02 p.13]

PHARMACEUTICAL / EXTRUSION (D07)
- Hot polymer melt with API: MIR ATR probe or NIR probe; interface may foul (material build-up) [S02 p.14]; offline assays provide reference; probe must tolerate heat and chemical environment
- High temperature and potential fouling are key clarification questions before probe selection

MEDICAL / RESEARCH (Proof of Concept ONLY)
S03 - LED NIR kidney tumour sensor [S03]:
- Compact sensor: 4 LEDs at NIR wavelengths + 1 photodiode (NOT a full spectrometer)
- 14 in vitro samples from 7 patients; two sensor prototypes (Series A and B) tested
- PCA and PLS-DA confirmed general applicability to tumour/healthy tissue discrimination
- Paper's own conclusion: "proof-of-concept", "first estimate of real-life applicability", further studies needed
- Key limitation: HIGH measurement variance in cancer tissue samples; false negatives unacceptable in oncology
- NOT validated for clinical/surgical use; NOT applicable to process control [S03]

S04 - Combined MIR ATR + Fluorescence probe on model tissues [S04]:
- Probe design: ZrO2 ATR crystal (truncated cone), CIR fibers for MIR, silica fibers for fluorescence — single probe head
- Samples: chicken breast, fat, liver — 3 samples per tissue type, 5 measurement points each (45x118 IR + 45x705 fluorescence matrices)
- IR alone: better for fat discrimination (ester carbonyl C=O peak at ~1740 cm-1)
- Fluorescence alone: better for liver discrimination (porphyrin peak at 613 nm)
- Combined: cleanly separates all three tissue types — demonstrates synergistic gain [S04 p.4]
- Key limitation stated explicitly: sequential measurements from two separate probes CANNOT guarantee same measurement spot in heterogeneous tissue — combined single probe solves this [S04 p.2]
- These are laboratory demonstrations, NOT validated clinical tools [S04]
"""

AFS_BUSINESS_CONTEXT = """
AFS Commercial Pathway (Source: S05)

AFS operates a 3-step guided pathway for customers:

1. MULTI-METHOD LAB TEST
   Run the customer's process sample through AFS's Multi-Spectral Fiber System covering 0.3-16 um.
   Test multiple spectral methods simultaneously (NIR, MIR ATR, Raman, Fluorescence, UV-Vis).
   Do NOT commit to a single method before this step.

2. SELECTION OF KEY SPECTRAL FEATURES
   Use multivariate data analysis and data fusion (chemometrics) to identify which spectral
   features and which method combination actually discriminate the target variable.
   AI-driven chemometric model development to control molecular changes in-line.

3. TAILORED SOLUTION — one of two outcomes:
   a) Custom MSF-System: budget-matched set of fiber spectrometers for the specific process
   b) Spectral Fiber Sensors (SFS): customised for specific process, remote cloud control

AFS product coverage: 0.3-16 um spectral range [S05]
Target industries: Pharma, Chemicals, Food [S05]

IMPLICATION FOR FEASIBILITY PLANS:
The correct AFS feasibility plan is NOT "pick NIR and validate it."
It is: test multiple methods on representative samples first, use chemometrics to find what works,
THEN design the in-line system. This is AFS's actual commercial process.
"""

DEVELOPMENT_SCENARIOS = """
AFS Development Scenarios D03-D08 (from AFS_Examples_and_Reference.docx)
Use these as templates for recognising scenario types in customer enquiries.

D03 - Clear whey stream (turbidity may change)
Facts: whey stream; protein concentration requested; initially relatively clear; turbidity may change; laboratory reference available.
Key issue: probe geometry must handle both clear and turbid states — do not assume liquid stays clear.
Useful sources: S01 p.5, 10, 17, 18

D04 - Glucose and lactate in aqueous bioprocess
Facts: cell culture; glucose and lactate requested; medium and cells change during the run; lab reference measurements exist.
Key issue: changing matrix means calibration may need to account for medium composition drift during run.
Useful sources: S01 p.5, 10, 11, 16

D05 - Biomass monitoring during yeast fermentation
Facts: yeast fermentation; growth and metabolic changes mentioned; optical density increases; target variables NOT yet defined.
Key issue: "biomass signal" and "metabolic signal" are not the same — define targets before selecting method; broth becomes more optically dense.
Useful sources: S01 p.5, 16

D06 - Water content in petroleum stream
Facts: petroleum stream; water content requested; lab measurement exists; analyzer outside process area.
Key issue: MIR ATR needs MIR-compatible fiber (not silica); remote analyzer needs appropriate fiber link [S02 p.6, 13].
Useful sources: S01 p.6, 9, 10; S02 p.6, 13

D07 - API concentration in hot polymer extrusion
Facts: hot polymer melt; API composition changes requested; offline assays available; interface may foul.
Key issue: hot interface and fouling are critical — probe must tolerate temperature and material build-up [S02 p.14].
Useful sources: S01 p.5, 6, 10; S02 p.14

D08 - Heterogeneous model tissues (lab classification)
Facts: lab model tissues (chicken muscle/fat/liver); heterogeneous; compare MIR ATR and fluorescence; no clinical use.
Key issue: sequential measurements from different probes may NOT sample the same location in heterogeneous material — this is a stated limitation of the study design [S04].
Useful sources: S01 p.5, 6, 8-10; S04 p.1, 3, 4
"""

FIBER_FAMILIES = """
Fiber Families (Source: S02 p.6 - transcribed for reference; always check original figure)
Unit reminder: wavelength in µm = 10 000 / wavenumber in cm-1 (4000 cm-1 = 2.5 µm)

Fiber Type | Approximate Transmission Range | Notes
-----------|---------------------------------|------
Standard and Al/Cu-coated UV-Vis silica fibers | 190-1200 nm (UV to near-NIR only) | Low-OH silica; robust 100-300m cables for industrial process control [S02 p.7]
Standard and Al/Cu-coated Vis-NIR silica fibers | 350-2400 nm (visible to NIR) | Al/Cu-coated: high temp resistance, hermetically sealed, polymer-fluorescence-free for Raman/fluorescence [S02 p.7]
Chalcogenide As-S IR fibers (CIR) | 1.1-6.5 µm (covers MIR range) | For MIR ATR applications [S02 p.9]
Polycrystalline infrared fibers (PIR / AgHal) | 3-17 µm (deep MIR) | Very flexible, non-brittle, non-toxic; HIGH NA>0.3 gives better coupling with FTIR spectrometers than HWG; preferred for ATR probes [S02 p.9, 10]
Hollow glass waveguides (HWG) | 2-18 µm (deep MIR) | Low NA>0.1 causes poor coupling with FTIR; PIR fibers preferred for ATR probe applications [S02 p.10]
Indium fluoride fibers | 0.3-5.5 µm | [S02 p.6]
Zirconium fluoride fibers | 0.3-4.5 µm | [S02 p.6]

KEY RULES [S02 p.6-10]:
- Silica fiber (UV-Vis or Vis-NIR) stops at ~1200-2400 nm. Cannot carry MIR ATR signals.
- MIR ATR requires CIR, PIR, HWG, or fluoride fibers.
- PIR fibers are preferred over HWG for ATR probes with FTIR spectrometers (higher NA = better coupling).
- PIR fiber transmission range 3-16 µm matches the molecular fingerprint region and black body radiation at 0-100 deg C [S02 p.8].
- Al/Cu-coated silica cables: polymer-jacket-free = no fluorescence interference for Raman and fluorescence spectroscopy [S02 p.7].

S02 p.7 key facts:
- Robust 100-300m silica cables with low OH-content (<0.1 ppm OH) enable remote industrial process control
- Al/Cu-coated fibers: high temperature resistance, increased durability, high strength, hermetically sealed

S02 p.13 - Water in petroleum application:
- ATR probe tip: ZrO2 (zirconia), diamond, etc., sealed in PEEK shaft, protected by PEEK tubing
- Can be used in microwave furnaces
- MIR ATR spectrum shows water peaks clearly distinguishable from 0.1% to 2.0% water content in oil
- Water O-H stretching region (~3300-3600 cm-1) and combination band (~2300 cm-1) visible in oil matrix

S02 p.14 - Polymer extrusion application:
- NIR reflection AND MIR ATR both applied in-line for hot polymer extrusion
- API control with PIR-fiber FTIR spectroscopy in pharma industry
- Diamond cone ATR probe coupled to iC10 FTIR (MTAC) used to get spectra of API in hot polymer melt
- NIR probe mounted at extruder barrel/die for feed-forward control (waste gate switch: good product vs waste)
- Both NIR and MIR ATR are viable options for hot melt extrusion; MIR gives higher chemical selectivity
"""

METHOD_OVERVIEW_FULL = """
AFS Method Overview Table (from AFS_Examples_and_Reference.docx, section 5)
This is a starting point compiled from the sources. Not a product specification.

Method | Nominal Range | Typical Samples/Geometry | Main Limitations | Read
-------|--------------|--------------------------|------------------|-----
NIR | 780-2500 nm | Powders/dairy - diffuse reflection for scattering; transmission/transflection for clear liquids | Overlapping bands, physical variation; calibration matrix-specific | S01 p.5, 10, 14-15, 17-18
MIR (ATR) | 4000-400 cm-1 | Liquids/pastes/soft solids in contact with ATR crystal; water in petroleum, API in polymer extrusion | Usable range limited by fiber and crystal; contact, fouling, compatibility | S01 p.6, 9-10; S02 p.6, 13-14
Raman | Raman shift (cm-1) + laser excitation (nm) stated separately | Powders and liquids: pharma blends, bioprocess metabolites | Weak signal, fluorescence background; calibration matrix-specific | S01 p.11-12, 14-16
Fluorescence | Depends on fluorescent species | Only for defined fluorescent species or justified indicator | High sensitivity, low selectivity; not a direct measurement of every analyte | S01 p.5, 6, 16; S04
UV-Vis | Depends on target | Defined absorption; biomass-related optical signal in cell suspensions | Overlapping signals in mixtures; OD is not a viable cell count | S01 p.5-6, 16
Combinations | Only ranges confirmed for actual components | NIR+Raman, MIR ATR+fluorescence; compare with best single method | Sampling location and timing must align; a gain is a hypothesis to test | S01 p.7-9, 14-15; S04
"""

SYSTEM_PROMPT = """You are an AI assistant for Art Fiber Systems (AFS) helping experts make a first technical assessment of customer spectroscopy enquiries.

You have access to the AFS knowledge base below. Use it as your PRIMARY source. Cite every technical claim with the exact source and page (e.g. [S01 p.14-15], [S01 Table 1 p.6], [S02 p.13]).

KNOWLEDGE BASE:
""" + METHOD_TABLE + "\n" + METHOD_OVERVIEW + "\n" + METHOD_OVERVIEW_FULL + "\n" + FIBER_FAMILIES + "\n" + APPLICATION_EXAMPLES + "\n" + DEVELOPMENT_SCENARIOS + "\n" + AFS_BUSINESS_CONTEXT + """

RESPONSE STRUCTURE — always produce all 7 sections in this exact Markdown format:

## Requirements & Key Facts
List what the client stated as separate bullet points. Then explicitly list key unknowns.
Keep client facts and your assumptions visibly separate.

## Clarification Questions
Numbered list. Ask only questions that would change the method choice or the feasibility plan.
Be specific — name the variable, the range, the constraint. Avoid generic questions.

## Recommendation
**Decision Status:** one of:
- "Provisional assessment" — enough information to propose a testable direction with explicit assumptions
- "Insufficient information" — cannot recommend until key questions answered; list only what is needed
- "Cannot approve — [specific reason]" — enquiry contradicts the sources (e.g. wrong fiber type, out of scope)
- "Outside supported scope" — requested proof level beyond what AFS materials demonstrate

For each recommended method: state reason, cite source, state what assumption underlies the recommendation.
If the premise contradicts the sources, say so and explain why.

## Measurement Concept
High-level probe type and geometry (ATR / diffuse reflection / transmission / transflection).
Fiber link concept — state which fiber family is needed and why [S02 p.6].
Measurement location.
Note: do NOT specify probe model codes, exact lengths, or component ratings — these require AFS confirmation.

## Risks & Uncertainty
Bullet list of what could make the recommendation wrong.
State every assumption explicitly.
Do NOT invent performance figures, detection limits, accuracy, or response times not in the sources.
If a variable changes during the process (temperature, composition, optical density), name it as a risk.

## Feasibility Plan
A concrete first experiment following this structure:
1. **Samples:** what representative samples are needed (range of the target variable, physical variation)
2. **Reference measurements:** which independent analytical method provides reference values, and why it is independent
3. **Measurements to compare:** which spectroscopy options to test and how (geometry, probe type)
4. **Sequence:** single-method models first, then combinations if justified
5. **Go/no-go basis:** what numerical acceptance criterion, agreed with the client, decides success — do NOT invent the criterion, but state that one must be agreed before the experiment
6. **Minimum samples:** state that the required sample count depends on matrix complexity and analyte range; do not invent a number, but note that a pilot with too few samples cannot validate a calibration
State what the experiment would demonstrate and what it would NOT demonstrate.

## Sources Used
List every source cited above with full reference. Format: [S01] = AFS_Multispectral_Laboratory.pdf, [S02] = AFS_Process_Control_Slides.pdf, [S03] = LED_Kidney_Study_2017.pdf, [S04] = Combi_MIR_Fluorescence_2021.pdf.

CRITICAL RULES:
- Never invent measured results, performance specs, fiber lengths, or accuracy figures not in the sources
- Never fill in missing client facts as if given — ask instead
- If a premise contradicts the sources, say so explicitly (e.g. silica fiber for MIR is NOT compatible [S02 p.6])
- A short, well-founded answer beats a long, assertive one
- If you use knowledge from outside the AFS sources, flag it explicitly as "[general spectroscopy knowledge, not in AFS sources]"
- Do not invent laser wavelengths, concentration thresholds, OD values, regression method names, or detection limits
- When the sample type, analyte, or process are not stated, Decision Status MUST be "Insufficient information"
- Laser excitation wavelength for Raman must be stated SEPARATELY from Raman shift — never conflate them
- Unit reminder: wavelength in µm = 10 000 / wavenumber in cm-1 (4000 cm-1 = 2.5 µm) [S02 p.6]
- Sequential measurements from two different probes may NOT sample the same location in heterogeneous samples [S04]
- A published application example is a reason to TEST a method, not proof it will work for a new customer
- Research papers (S03, S04) demonstrate proof-of-concept only — never cite them as clinical or process validation
"""
