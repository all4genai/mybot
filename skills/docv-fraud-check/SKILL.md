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

4) **ID ↔ selfie match checks**
- Face geometry + stable features: brow ridge, nose shape, ear shape, moles/scars (if visible)
- Age plausibility, hairline, facial hair, glasses, etc.

5) **Output decision + reasons**
- Decision: Real / Suspicious / Likely AI/Composite / Uncertain
- Confidence: low/medium/high
- Reasons: 3–10 bullets tied to visible artifacts
- Next steps: what additional capture reduces uncertainty (video liveness, hand-hold ID selfie, original upload)

## Output template

- **结论**：<更像真实 / 疑似合成 / 高度疑似合成 / 不确定>
- **置信度**：<低/中/高>
- **理由（可复核）**：
  - <DOF/背景虚化特征 1>
  - <边缘/分割伪影 1>
  - <一致性/噪声/光照 1>
- **可能的良性解释**（如适用）：
  - <人像模式/应用滤镜/截图等>
- **建议补充材料**：
  - 10秒活体自拍视频（转头/眨眼/读数字）
  - 手持证件自拍（带角度变化）
  - 原图（非聊天压缩）

## Notes

- This heuristic is strongest when the image claims to be a plain selfie but visually matches a studio/prime-lens shallow DOF look.
- Always consider WhatsApp or platform compression; ask for original upload when possible.
