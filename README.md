# FinGuru: AI Expense Copilot for Indian MSMEs

FinGuru is a production-style ML system that converts unstructured expense inputs (receipt photos + Hinglish voice notes) into auditable ledger entries with GST reasoning and confidence-gated human review.

It is intentionally designed as a constrained reasoning pipeline, not a free-form chatbot.

## Recruiter Snapshot (10-Second Read)

- Built an end-to-end AI finance workflow with FastAPI + React + AWS services.
- Implemented multimodal ingestion: receipt OCR and voice transcription.
- Added spec-driven classification with schema-constrained LLM outputs.
- Engineered confidence-based human-in-the-loop controls for safer automation.
- Exposed explainable outputs: category decision, GST logic, and confirmation triggers.

## Why This Project Matters

Small businesses often track expenses in ad-hoc ways, causing:

- poor bookkeeping quality,
- delayed GST visibility,
- high manual effort to reconcile receipts and voice notes.

FinGuru addresses this with a system that turns raw evidence into structured accounting entries while preserving explainability and control.

## Product Capabilities

- Receipt upload pipeline (image -> OCR -> structured expense entry)
- Voice pipeline for Hinglish expense logging (audio/text -> parsed entry)
- Explainability fields for each decision (rule applied + GST reasoning)
- Confidence thresholding with explicit confirmation flow
- Ledger APIs for retrieval, summary, category analytics, and corrections
- Advisor endpoint for higher-level spend insights

## Technical Architecture

```text
Frontend (React + Vite)
    |
    | REST /api
    v
Backend (FastAPI)
  - Routers: auth, receipts, voice, ledger, advisor
  - Services: reasoning, textract, transcribe, dynamodb, s3
    |
    +--> OCR / vision provider
    +--> LLM reasoning (OpenAI/OpenRouter)
    +--> AWS DynamoDB (ledger persistence)
    +--> AWS S3 (receipt/audio objects)
```

## ML and Reasoning Design

### 1. Spec-Driven Reasoning

Accounting and GST behavior is defined in YAML specs under backend/specs/accounting.yaml and consumed by the reasoning engine.

Benefits:

- business rules are inspectable and versionable,
- category logic is consistent across requests,
- policy updates do not require core pipeline rewrites.

### 2. Structured LLM Contract

When LLM reasoning is available, outputs are constrained by JSON schema (amount, category, confidence, rule_applied, gst_reasoning, explanation).

Benefits:

- deterministic response shape for downstream APIs,
- reduced parsing fragility,
- safer integrations with frontend and persistence layers.

### 3. Safety via Human-in-the-Loop

Entries below the configured confidence threshold are not blindly trusted and are flagged for confirmation.

Benefits:

- safer automation in finance workflows,
- clearer decision boundaries between AI and user control,
- lower risk of silent misclassification.

### 4. Graceful Fallback Behavior

If external LLM calls fail or quota is unavailable, the pipeline falls back to rule-based extraction/classification to preserve service continuity.

Benefits:

- resilient behavior under provider failures,
- lower operational brittleness,
- continued product usability.

## Engineering Quality Signals

- Clear modular backend: routers and services are separated by responsibility.
- Typed request/response contracts with Pydantic models.
- Config management through environment-driven settings.
- Consistent API prefixing and proxy integration with frontend.
- Runnable local stack for realistic end-to-end testing.

## Current Stack

- Backend: Python, FastAPI, Pydantic
- Frontend: React, TypeScript, Vite, Tailwind
- Storage/Infra: AWS DynamoDB, S3, Textract
- AI: OpenAI-compatible client (OpenAI/OpenRouter), Whisper-based transcription path
- Deployment artifacts: Procfile, render.yaml, vercel.json

## Repository Structure

```text
Finguru/
  backend/
    main.py
    config.py
    models/
    routers/
    services/
    specs/accounting.yaml
  frontend/
    src/
    package.json
    vite.config.ts
  README.md
  DEPLOYMENT.md
  SETUP_GUIDE.md
```

## API Surface (Representative)

- POST /api/auth/register
- POST /api/auth/login
- POST /api/receipts/upload
- POST /api/voice/upload
- POST /api/voice/upload-text
- GET /api/ledger/entries
- GET /api/ledger/summary
- GET /api/advisor/insights

## Local Run

### Backend

```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on port 3000 and proxies /api to backend port 8000.

## Suggested Resume Bullets (Use/Adapt)

- Built a multimodal AI expense intelligence platform for Indian MSMEs using FastAPI, React, and AWS services.
- Designed a spec-driven reasoning engine with schema-constrained LLM outputs and confidence-based human review to improve reliability in financial workflows.
- Implemented resilient fallback logic from LLM inference to rule-based classification, preserving availability under model/API failure conditions.
- Developed explainable GST categorization pipeline with auditable decision traces, supporting safer automation over black-box responses.

## Roadmap (High-Impact Next Steps)

- Add automated evaluation harness with precision/recall for amount and category extraction.
- Introduce integration tests for receipt and voice pipelines with golden fixtures.
- Add observability (latency, fallback rate, low-confidence rate, error classes).
- Implement role-based access and stronger auth/session hardening for production.
- Extend advisor layer with trend anomaly detection and cashflow forecasting.

## What Was Corrected From the Previous README

- Replaced unrelated content describing a different product and folder layout.
- Removed unverifiable claims not grounded in this repository.
- Aligned architecture, APIs, stack, and project structure with actual code.
- Reframed project narrative to emphasize impact, system depth, and engineering quality expected in strong ML portfolios.
