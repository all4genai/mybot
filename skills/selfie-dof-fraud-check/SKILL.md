---
name: selfie-dof-fraud-check
description: Detect likely AI-generated or heavily edited selfie images by checking depth-of-field and background blur patterns (portrait-mode look) that are atypical for real front-camera selfies, and produce a fraud risk assessment with concrete, reviewable reasons. Use when analyzing selfie images for document verification / KYC fraud, especially when faces are extremely sharp while the background is uniformly blurred.
---

# Selfie DOF Fraud Check

## Goal

Assess whether a selfie is likely AI-generated / composited using a **depth-of-field (DOF) mismatch** heuristic:

- Many fake/generated selfies have a **very sharp face** with a **uniformly blurred background**, resembling a **shallow-DOF prime lens** look.
- Real phone front cameras typically have **deep DOF**; in ordinary selfies, **face and background often have similar sharpness**.

Use this as a **signal**, not a single-point verdict.

## Workflow

1) **Identify capture context** (if available)
- Ask for: device type, app used, whether portrait mode was used.
- If unknown, proceed but lower confidence.

2) **Check DOF / blur characteristics**
Look for:
- **Global background blur** that is smooth and uniform across distant and mid-depth objects.
- **Segmentation artifacts** around hair/ears/glasses/shoulders (halo edges, cutout feel).
- **Inconsistent blur**: background blur that does not vary naturally with depth (near objects as blurred as far objects).
- **Face sharpness vs background**: face pores/skin microtexture extremely crisp while background edges are strongly softened.

3) **Check “real-selfie messiness” counter-signals**
Real selfies often show:
- Messy/accidental backgrounds (random rooms, clutter, outdoor variance).
- Natural sensor noise and compression patterns across the whole image.
- Lighting imperfections and non-ideal framing.

4) **Control for legitimate exceptions**
Mark as “possible benign cause” if:
- Clear evidence of **portrait mode/bokeh** (common on modern phones) AND the blur boundaries look algorithmic but plausible.
- Background is genuinely out-of-focus due to **close focus distance** plus computational blur.
- Image is a screenshot from an app applying blur.

5) **Produce a decision + reasons**
Return:
- Decision: Real / Suspicious / Likely AI/Composite / Uncertain
- Confidence: low/medium/high
- Reasons: 3–8 bullet points, each tied to a visible artifact
- Next-step requests: what additional captures would reduce uncertainty

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
