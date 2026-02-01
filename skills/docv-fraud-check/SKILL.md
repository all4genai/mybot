---
name: docv-fraud-check
description: Document verification (DocV) fraud review playbook for likely AI-generated IDs and deepfake/AI-generated selfies. Use when assessing KYC/DocV images for fraud risk and producing a decision with concrete, reviewable reasons, including checks for selfie deepfakes, mismatched ID vs selfie, and shallow depth-of-field / background blur artifacts.
---

# DocV Fraud Check

## Scope

This skill guides fraud review for **document verification** cases, especially:
- AI-generated or edited **ID images**
- AI-generated / deepfake **selfies**
- **ID ↔ selfie mismatch** checks

## Selfie deepfake check (includes DOF / background-blur heuristic)

A strong heuristic for generated/composited selfies is a **DOF mismatch**:
- Fake/generated selfies often show a **very sharp face** with a **uniformly blurred background**, resembling a shallow-DOF prime lens.
- Real phone front cameras usually have **deep DOF**; face and background sharpness are often closer.

Treat as a **signal**, not a single-point verdict.

## Workflow (quick)

1) **Gather context** (if available)
- Document type/jurisdiction; capture channel (WhatsApp/app upload); whether portrait mode was used.

2) **Selfie deepfake checks**
- **DOF / background blur**
  - Uniform, strong background blur with an extremely sharp face
  - Blur that does not vary naturally with depth
  - Segmentation artifacts around hair/ears/glasses/shoulders (halo/cutout)
- **Lighting/physics consistency**
  - Light direction vs shadows; eye catchlights; specular highlights
- **Texture realism**
  - Over-smoothing, synthetic skin microtexture, repeated/regular wrinkle patterns
- **Real-selfie counter-signals**
  - Whole-image noise/compression consistency; messy background; imperfect framing
- **Benign exceptions**
  - Portrait mode/bokeh, app filters, screenshots (reduce confidence; request original)

3) **ID image checks** (high-level)
- Text legibility without "AI gibberish"; font edge consistency
- Security features / hologram plausibility (limited under compression)
- Signs of compositing (cut edges, mismatched noise, warped text, repeated patterns)
- **Document fake signature check**
  - Flag signatures that look like a **printed cursive font** rather than ink strokes
  - Look for overly consistent line thickness, perfectly smooth bezier-like curves, uniform spacing, and repeated glyph shapes
  - Check for lack of natural pen-lift artifacts: variable pressure, micro tremor, stroke overlap/starts/ends, and irregular baseline
  - Watch for "signature" rendered at the same sharpness/anti-aliasing as surrounding printed text (suggesting it was typeset)

4) **ID ↔ selfie match checks**
- Face geometry + stable features: brow ridge, nose shape, ear shape, moles/scars (if visible)
- Age plausibility, hairline, facial hair, glasses, etc.
- **Headshot–selfie generation pair check**
  - Flag pairs where the ID headshot and the selfie look *too similar* in pose, expression, gaze, framing, hairstyle, and lighting
  - In real life, ID headshots are often taken at a different time than the selfie; expect more variance (age cues, haircut/facial hair changes, different camera distance/angle)
  - Watch for subtle “same-template” cues: near-identical face angle, eyebrow lift, smile shape, eye catchlights, and background style despite being two supposedly separate captures
  - Note: some applicants may upload a recent ID, so treat this as a signal and combine with other artifacts
- **Name, age, and face consistency check**
  - Compare claimed demographics (name, DOB/age, sex marker if present) against the apparent face in the ID headshot and selfie
  - Flag obvious mismatches (e.g., masculine-coded name with a clearly feminine-presenting face, or vice versa)
  - Flag large age mismatches vs DOB (e.g., DOB implies ~50 but face appears much younger/older) beyond what normal variance would explain
  - Treat as a *review* signal: names are not perfectly gendered across cultures, and appearance varies; combine with other evidence rather than auto-decline

5) **Output decision + reasons**
- Decision: Real / Suspicious / Likely AI/Composite / Uncertain
- Confidence: low/medium/high
- Reasons: 3–10 bullets tied to visible artifacts
- Next steps: what additional capture reduces uncertainty (video liveness, hand-hold ID selfie, original upload)

## Output template

- **Decision**: <Likely real / Suspicious / Likely AI or composite / Uncertain>
- **Confidence**: <low / medium / high>
- **Reasons (reviewable)**:
  - <DOF / background blur signal #1>
  - <Edge / segmentation artifact #1>
  - <Consistency (noise / lighting / text) #1>
- **Possible benign explanations** (if applicable):
  - <Portrait mode / app filter / screenshot / etc.>
- **Next evidence to request**:
  - 10s liveness selfie video (turn head / blink / read a number)
  - Hand-hold ID selfie (include angle changes to reveal hologram/texture)
  - Original upload (avoid chat compression)

## Notes

- This heuristic is strongest when the image claims to be a plain selfie but visually matches a studio/prime-lens shallow DOF look.
- Always consider WhatsApp or platform compression; ask for original upload when possible.
