<div align="center">

# AI Recruiting Intelligence Platform

### Evidence-Based Candidate Matching, Verification & Recruiter Submission

<p>
  An automation-first recruiting platform built with <strong>n8n Cloud</strong>,
  AI, structured data, document intelligence, verification workflows, and
  mandatory recruiter approval.
</p>

<p>
  <a href="#platform-overview">Platform</a> ·
  <a href="#core-capabilities">Capabilities</a> ·
  <a href="#recruitment-lifecycle">Lifecycle</a> ·
  <a href="#architecture">Architecture</a> ·
  <a href="#verification-engine">Verification</a> ·
  <a href="#ai-intelligence-layer">AI Layer</a> ·
  <a href="#data-model">Data Model</a> ·
  <a href="#setup">Setup</a>
</p>

<br>

<img src="https://img.shields.io/badge/n8n-Cloud-EA4B71?style=for-the-badge&logo=n8n&logoColor=white" alt="n8n Cloud">
<img src="https://img.shields.io/badge/AI-Intelligence-111827?style=for-the-badge&logo=openai&logoColor=white" alt="AI">
<img src="https://img.shields.io/badge/Supabase-Data%20Layer-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase">
<img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
<img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">

<br><br>

<img
src="https://capsule-render.vercel.app/api?type=waving&height=180&color=0:111827,100:4F46E5&section=header&text=AI%20Recruiting%20Intelligence&fontColor=FFFFFF&fontSize=38&fontAlignY=38&desc=Match%20better.%20Verify%20evidence.%20Submit%20with%20confidence.&descAlignY=62&descSize=16"
alt="AI Recruiting Intelligence"
width="100%">

>

</div>

---

## Platform Overview

The **AI Recruiting Intelligence Platform** is an automation-first recruiting system designed for staffing agencies, IT recruiters, RPO teams, contract staffing firms, and internal recruitment operations.

It turns unstructured hiring information into a controlled, evidence-backed recruitment process.

The platform is designed around one principle:

> **AI should accelerate recruiter work without becoming the final decision-maker.**

The system analyzes job descriptions, parses resumes, extracts evidence, evaluates candidate-to-job alignment, performs authorized professional-profile verification, verifies education and employment information, discovers public recruitment contacts, produces a recruiter-ready verification report, and waits for explicit human approval before submission.

### The Complete Operating Model

| Stage                | Purpose                                     | Primary Output                       |
| -------------------- | ------------------------------------------- | ------------------------------------ |
| Job Intake           | Capture role and client requirements        | Structured job record                |
| JD Intelligence      | Convert unstructured JD into requirements   | Mandatory and preferred requirements |
| Candidate Intake     | Capture candidate and resume                | Candidate record + source document   |
| Resume Intelligence  | Parse resume into structured facts          | Skills, education, experience        |
| Evidence Extraction  | Connect requirements to source evidence     | Requirement-level evidence           |
| Candidate Matching   | Evaluate candidate against the role         | Match assessment                     |
| Profile Verification | Compare authorized profile information      | Consistency assessment               |
| Company Verification | Validate employer identity                  | Company verification                 |
| Contact Discovery    | Find public/authorized recruitment contacts | Sourced HR/recruitment contact       |
| Verification Report  | Consolidate findings                        | Recruiter-ready report               |
| Recruiter Review     | Human decision checkpoint                   | Approved / Edited / Rejected         |
| Submission           | Prepare final candidate package             | Client-ready submission              |

---

# Core Capabilities

<div align="center">

<table>
<tr>
<td width="50%" valign="top">

### Job Intelligence

Structured job analysis from raw job descriptions.

* Mandatory requirements
* Preferred requirements
* Skills and technologies
* Education requirements
* Experience requirements
* Certifications
* Location constraints
* Employment type
* Domain requirements
* Evidence requirements
* Ambiguous requirement detection

</td>
<td width="50%" valign="top">

### Resume Intelligence

Transform resumes into structured candidate data.

* Identity extraction
* Skills
* Education
* Employment history
* Certifications
* Projects
* Languages
* Resume evidence
* Source-page references
* Missing-information detection

</td>
</tr>

<tr>
<td width="50%" valign="top">

### Evidence-Based Matching

Every important matching decision is connected to evidence.

* Requirement-by-requirement analysis
* Strong evidence
* Partial evidence
* No evidence
* Discrepancies
* Manual review states
* Deterministic date calculations
* Normalized skills
* Explainable match reasoning

</td>
<td width="50%" valign="top">

### Verification Intelligence

Verification is treated as a separate system layer.

* Education consistency
* Experience consistency
* Employment dates
* Company identity
* Profile comparison
* Public source discovery
* Recruitment contact discovery
* Source tracking
* Confidence and status

</td>
</tr>

<tr>
<td width="50%" valign="top">

### Recruiter Control

Human approval remains mandatory.

* Review queue
* Candidate comparison
* Edit before submission
* Approval
* Rejection
* Request review
* Manual overrides
* Audit history

</td>
<td width="50%" valign="top">

### Operational Reliability

Built for real automation rather than one-off AI prompts.

* Input validation
* JSON validation
* Retry handling
* Error branches
* API failure handling
* Rate-limit handling
* Audit logs
* Stable IDs
* Credential management
* Manual fallback states

</td>
</tr>
</table>

</div>

---

# Recruitment Lifecycle

<div align="center">

<table>
<tr>
<td align="center" width="14%">
<b>01</b><br><br>
Job<br>Intake
</td>
<td align="center" width="14%">
<b>02</b><br><br>
JD<br>Analysis
</td>
<td align="center" width="14%">
<b>03</b><br><br>
Candidate<br>Intake
</td>
<td align="center" width="14%">
<b>04</b><br><br>
Resume<br>Analysis
</td>
<td align="center" width="14%">
<b>05</b><br><br>
Evidence<br>Extraction
</td>
<td align="center" width="14%">
<b>06</b><br><br>
Candidate<br>Matching
</td>
<td align="center" width="14%">
<b>07</b><br><br>
Verification<br>Engine
</td>
</tr>
</table>

<br>

<table>
<tr>
<td align="center" width="20%">
<b>08</b><br><br>
Company<br>Verification
</td>
<td align="center" width="20%">
<b>09</b><br><br>
Contact<br>Discovery
</td>
<td align="center" width="20%">
<b>10</b><br><br>
Verification<br>Report
</td>
<td align="center" width="20%">
<b>11</b><br><br>
Recruiter<br>Review
</td>
<td align="center" width="20%">
<b>12</b><br><br>
Final<br>Submission
</td>
</tr>
</table>

</div>

### What Makes the Lifecycle Different

The platform does not reduce recruiting to a single AI score.

A candidate can be:

* a strong match with strong evidence
* a possible match requiring review
* a weak match
* a candidate with conflicting information
* a candidate whose information simply could not be verified

**Not verified does not mean false.**

That distinction is fundamental to the platform.

---

# Architecture

<div align="center">

<table>
<tr>
<td align="center" width="25%">

### Recruiter Interface

Job intake
Candidate intake
Review queue
Verification report
Approval

</td>

<td align="center" width="25%">

### n8n Cloud

Workflow orchestration
Validation
AI calls
Database operations
Integrations
Error handling

</td>

<td align="center" width="25%">

### Intelligence Layer

LLM extraction
Semantic reasoning
Embeddings
Evidence analysis
Normalization

</td>

<td align="center" width="25%">

### Data Layer

Supabase
PostgreSQL
Documents
Evidence
Audit logs

</td>
</tr>
</table>

<br>

<table>
<tr>
<td align="center" width="20%">
<img src="https://cdn.simpleicons.org/n8n/EA4B71" width="48" alt="n8n"><br>
<b>n8n Cloud</b><br>
<sub>Automation & orchestration</sub>
</td>

<td align="center" width="20%">
<img src="https://cdn.simpleicons.org/openai/111827" width="48" alt="OpenAI"><br>
<b>AI Provider</b><br>
<sub>Extraction & reasoning</sub>
</td>

<td align="center" width="20%">
<img src="https://cdn.simpleicons.org/supabase/3FCF8E" width="48" alt="Supabase"><br>
<b>Supabase</b><br>
<sub>Application data layer</sub>
</td>

<td align="center" width="20%">
<img src="https://cdn.simpleicons.org/postgresql/4169E1" width="48" alt="PostgreSQL"><br>
<b>PostgreSQL</b><br>
<sub>Structured persistence</sub>
</td>

<td align="center" width="20%">
<img src="https://cdn.simpleicons.org/github/181717" width="48" alt="GitHub"><br>
<b>GitHub</b><br>
<sub>Version control</sub>
</td>
</tr>
</table>

</div>

## Architecture Principles

| Principle       | Implementation                               |
| --------------- | -------------------------------------------- |
| Orchestration   | n8n Cloud                                    |
| AI              | Provider-independent LLM layer               |
| Structured Data | PostgreSQL / Supabase                        |
| Documents       | Original document + extracted representation |
| Matching        | Rules + normalization + semantic reasoning   |
| Verification    | Source-backed comparison                     |
| Decision Making | Recruiter-controlled                         |
| Reliability     | Validation + retries + error workflows       |
| Security        | Managed credentials + least-privilege access |
| Traceability    | Stable IDs + evidence + audit logs           |

---

# n8n Cloud Workflow Architecture

The project is intentionally divided into modular workflows rather than one giant automation.

<div align="center">

<table>
<tr>
<td align="center" width="33%">

<b>01 — Job Intelligence</b>

Job Intake
JD Analysis
Requirement Structuring

</td>

<td align="center" width="33%">

<b>02 — Candidate Intelligence</b>

Candidate Intake
Resume Analysis
Evidence Extraction
Candidate Matching

</td>

<td align="center" width="33%">

<b>03 — Verification</b>

Education
Experience
Company
Professional Profile
Contact Discovery

</td>
</tr>

<tr>
<td align="center">

<b>04 — Reporting</b>

Verification Report
Match Explanation
Discrepancies

</td>

<td align="center">

<b>05 — Human Review</b>

Recruiter Queue
Edit
Approve
Reject
Request Review

</td>

<td align="center">

<b>06 — Submission</b>

Final Candidate Package
Submission Record
Audit Log

</td>
</tr>
</table>

</div>

### Workflow Set

```text
01 - Job Intake
02 - JD Analysis
03 - Candidate Resume Intake
04 - Resume Analysis
05 - Evidence Extraction
06 - Candidate Matching
07 - Education Verification
08 - Experience Verification
09 - Company Verification
10 - HR Contact Discovery
11 - Verification Report
12 - Candidate Submission
13 - Recruiter Review
14 - Final Submission
15 - Error Handler
```

The workflow names above are implementation identifiers. The visual presentation intentionally uses structured modules rather than decorative arrow diagrams.

---

# Job Intelligence

## 01 — Job Intake

Recruiters can provide:

* Job title
* Company
* Job description
* Optional JD file
* Recruiter name
* Recruiter email
* Client/job reference

The workflow:

1. Validates the request.
2. Generates a stable job ID.
3. Stores the original job data.
4. Extracts document text when a file is provided.
5. Sends normalized content to JD Analysis.
6. Stores structured requirements.
7. Returns a job-processing result.

### Failure States

* Empty JD
* Unsupported document
* File extraction failure
* AI failure
* Invalid AI JSON
* Database failure

---

# 02 — JD Analysis

The AI layer converts the job description into structured requirements.

```json
{
  "job_title": "",
  "summary": "",
  "mandatory_requirements": [],
  "preferred_requirements": [],
  "education_requirements": [],
  "experience_requirements": [],
  "skills": [],
  "certifications": [],
  "location_requirements": [],
  "employment_type": "",
  "domain_requirements": [],
  "keywords": []
}
```

Every requirement should carry structured metadata such as:

```json
{
  "requirement_id": "",
  "name": "",
  "category": "",
  "mandatory": true,
  "minimum_years": null,
  "description": "",
  "evidence_needed": true,
  "requires_manual_review": false
}
```

The AI is not allowed to invent requirements that are absent from the source job description.

---

# Candidate Intelligence

## 03 — Candidate Resume Intake

Candidate intake supports:

* Candidate name
* Email
* Phone
* Professional profile URL
* Resume PDF
* Resume DOCX
* Resume TXT
* Job ID

The original resume remains preserved as the source document.

---

# 04 — Resume Analysis

Resume data is normalized into a structured candidate representation.

```json
{
  "candidate_id": "",
  "name": "",
  "email": "",
  "phone": "",
  "linkedin_url": "",
  "summary": "",
  "skills": [],
  "education": [],
  "experience": [],
  "certifications": [],
  "projects": [],
  "languages": []
}
```

### Education Representation

```json
{
  "institution": "",
  "degree": "",
  "field": "",
  "start_date": "",
  "end_date": "",
  "graduation_year": "",
  "evidence_text": ""
}
```

### Experience Representation

```json
{
  "company": "",
  "title": "",
  "start_date": "",
  "end_date": "",
  "employment_type": "",
  "description": "",
  "skills_used": [],
  "evidence_text": ""
}
```

Missing dates are left missing.

The system does not invent dates.

---

# 05 — Evidence Extraction

Evidence extraction is one of the core intelligence layers.

For every important requirement, the system attempts to identify source-backed evidence.

```json
{
  "requirement_id": "",
  "requirement": "",
  "evidence_text": "",
  "source": "",
  "page": null,
  "section": "",
  "strength": "strong",
  "confidence": 0.0
}
```

### Evidence States

| State             | Meaning                                         |
| ----------------- | ----------------------------------------------- |
| Strong Evidence   | Direct source evidence supports the requirement |
| Partial Evidence  | Related evidence exists but is incomplete       |
| No Evidence Found | No supporting evidence was identified           |
| Discrepancy       | Source information conflicts                    |
| Manual Review     | The system cannot safely determine the result   |

This prevents the common failure mode where an AI system produces a confident score without showing why.

---

# 06 — Candidate Matching

Candidate matching combines deterministic logic and AI reasoning.

### Deterministic Logic

Used for:

* Required skills
* Exact requirements
* Date calculations
* Experience duration
* Mandatory requirements
* Numeric constraints
* Eligibility rules

### AI Reasoning

Used for:

* Semantic skill relationships
* Requirement interpretation
* Contextual similarity
* Evidence explanation
* Related experience interpretation

### Matching Result

```json
{
  "requirement": "",
  "status": "strong_evidence",
  "evidence": [],
  "notes": ""
}
```

### Overall Classification

| Classification | Meaning                                          |
| -------------- | ------------------------------------------------ |
| Strong Match   | Most important requirements have strong evidence |
| Possible Match | Candidate may fit but requires review            |
| Weak Match     | Significant requirements are unsupported         |
| Manual Review  | Evidence is ambiguous or contradictory           |

If a scoring model is used, mandatory requirements must not be hidden by a high preferred-requirement score.

---

# Verification Engine

The verification engine is intentionally separated from candidate matching.

<div align="center">

<table>
<tr>
<td align="center" width="25%">

### Education

Degree
Institution
Field
Dates
Graduation Year

</td>

<td align="center" width="25%">

### Experience

Employer
Title
Start Date
End Date
Employment Sequence

</td>

<td align="center" width="25%">

### Company

Company Identity
Official Website
Public Sources
Normalization

</td>

<td align="center" width="25%">

### Contact

Recruitment
HR
Careers
Public Contact
Source

</td>
</tr>
</table>

</div>

---

# Professional Profile / LinkedIn Verification

The platform supports professional-profile verification only through **authorized or user-provided data sources**.

Supported patterns include:

* Authorized LinkedIn API access
* Candidate-provided professional profile information
* Recruiter-provided profile data
* Other authorized profile providers

The system must not depend on unauthorized LinkedIn scraping.

## Education Comparison

The platform compares:

* Institution
* Degree
* Field
* Start date
* End date
* Graduation year

## Experience Comparison

The platform compares:

* Company
* Job title
* Start date
* End date
* Employment sequence
* Overlapping periods
* Duration

### Verification Result

```json
{
  "status": "consistent",
  "resume_data": {},
  "profile_data": {},
  "differences": [],
  "evidence": []
}
```

Possible states:

* `consistent`
* `minor_discrepancy`
* `major_discrepancy`
* `not_verified`
* `manual_review`

### Important Rule

**Unavailable profile evidence is not evidence of deception.**

If profile data cannot be accessed, the system returns `not_verified` rather than inventing a conclusion.

---

# Company Verification

Company names are normalized before comparison.

Verification can use:

* Official company websites
* Public company information
* Authorized business/company APIs
* Recruiter-provided information

```json
{
  "company_name": "",
  "normalized_name": "",
  "official_website": "",
  "status": "verified",
  "sources": []
}
```

Supported statuses:

* `verified`
* `likely_match`
* `not_verified`
* `manual_review`

---

# HR & Recruitment Contact Discovery

The platform attempts to identify a public or authorized recruitment contact associated with the verified company.

Preferred sources:

1. Official company website
2. Careers page
3. Official contact page
4. Public recruitment email
5. Authorized company directory/API

The system never guesses email addresses.

```json
{
  "company": "",
  "contact_type": "recruitment",
  "email": "",
  "phone": "",
  "source": "",
  "verified": false
}
```

When no legitimate contact is found:

```json
{
  "company": "",
  "email": null,
  "status": "not_found"
}
```

---

# Verification Report

The verification report consolidates the complete candidate assessment.

## Report Sections

| Section                 | Content                            |
| ----------------------- | ---------------------------------- |
| Candidate Overview      | Identity and candidate summary     |
| Job Overview            | Role and client context            |
| Requirement Match       | Requirement-level evidence         |
| Education Verification  | Education comparison               |
| Experience Verification | Employment comparison              |
| Company Verification    | Employer validation                |
| Contact Discovery       | Public/authorized contact findings |
| Discrepancies           | Conflicting information            |
| Missing Evidence        | Items requiring additional proof   |
| Manual Review           | Human decisions required           |
| Recommendation          | Recruiter-oriented conclusion      |

The recommendation is a **decision-support output**, not an autonomous hiring decision.

---

# Recruiter Review

The recruiter remains the final decision-maker.

<div align="center">

<table>
<tr>
<td align="center" width="25%">

### APPROVE

Candidate is ready for the next stage.

</td>

<td align="center" width="25%">

### EDIT

Recruiter modifies the generated submission.

</td>

<td align="center" width="25%">

### REJECT

Candidate is not progressed.

</td>

<td align="center" width="25%">

### REQUEST REVIEW

Additional evidence or manual verification is required.

</td>
</tr>
</table>

</div>

No candidate should be automatically submitted to a client without an explicit approval step.

---

# Final Candidate Submission

After approval, the platform prepares a recruiter-editable candidate package containing only supported information.

The generated submission may include:

* Candidate summary
* Relevant skills
* Verified experience
* Relevant education
* Certifications
* Requirement alignment
* Evidence-backed highlights
* Verification notes
* Recruiter notes

The system must never invent:

* Qualifications
* Employment history
* Dates
* Certifications
* Achievements
* Skills
* Companies
* Contact information

---

# AI Intelligence Layer

The platform deliberately avoids treating one LLM as the entire system.

<div align="center">

<table>
<tr>
<td align="center" width="25%">

### LLM

Understanding
Extraction
Reasoning
Generation

</td>

<td align="center" width="25%">

### Embeddings

Semantic Similarity
Skill Relationships
Requirement Retrieval

</td>

<td align="center" width="25%">

### Deterministic Rules

Dates
Numbers
Mandatory Checks
Eligibility

</td>

<td align="center" width="25%">

### Evidence

Source Text
Pages
Sections
Verification Records

</td>
</tr>
</table>

</div>

## AI Output Validation

Every structured AI response should pass through a validation boundary.

| Result                    | Action                |
| ------------------------- | --------------------- |
| Valid JSON                | Continue              |
| Invalid JSON              | Repair / Retry        |
| Repeated Invalid Output   | Manual Review         |
| Missing Mandatory Field   | Reject Output         |
| External Provider Failure | Retry / Error Branch  |
| Empty Output              | Error / Manual Review |

---

# Data Model

The platform can be implemented on PostgreSQL through Supabase.

## Core Tables

```text
jobs
candidates
resumes
requirements
candidate_skills
candidate_education
candidate_experience
evidence
matches
verification_results
companies
company_contacts
submissions
audit_logs
```

## Candidate

```text
id
name
email
phone
linkedin_url
created_at
```

## Education

```text
id
candidate_id
institution
degree
field
start_year
end_year
source
```

## Experience

```text
id
candidate_id
company
job_title
start_date
end_date
source
```

## Evidence

```text
id
candidate_id
requirement
evidence_text
source
page_number
confidence
```

### Data Integrity Rule

Original source information should be preserved alongside normalized values.

Example:

```text
Original skill: "Node JS"
Normalized skill: "Node.js"
```

Normalization improves matching without destroying source fidelity.

---

# Status Model

A common status vocabulary keeps the system predictable.

| Status             | Meaning                                    |
| ------------------ | ------------------------------------------ |
| `strong_evidence`  | Strong source-backed support               |
| `partial_evidence` | Related but incomplete evidence            |
| `no_evidence`      | No supporting evidence found               |
| `discrepancy`      | Conflicting source information             |
| `not_verified`     | Verification source unavailable            |
| `manual_review`    | Human decision required                    |
| `verified`         | Source-backed verification succeeded       |
| `not_found`        | Requested public information was not found |

---

# Error Handling

Production automation needs explicit failure paths.

The central error workflow should handle:

* AI provider failure
* Invalid AI JSON
* API timeout
* Authentication failure
* Rate limits
* Document extraction failure
* Unsupported file
* Empty extracted text
* Database failure
* External service failure
* Missing required fields

### Reliability Rules

* Retry transient failures.
* Do not create infinite retry loops.
* Preserve failed execution context.
* Log the workflow and node.
* Store stable IDs.
* Route unresolved cases to manual review.
* Never silently convert failure into a positive verification result.

---

# Document Processing

Supported source formats:

| Format      | Processing             |
| ----------- | ---------------------- |
| PDF         | Text extraction        |
| DOCX        | Document extraction    |
| TXT         | Direct text processing |
| Scanned PDF | OCR when required      |

### Processing Model

```text
Upload
  |
  |-- File type validation
  |
  |-- Text extraction
  |
  |-- Empty-text validation
  |
  |-- OCR fallback when needed
  |
  |-- Structured analysis
```

The original source file remains available for audit and evidence review.

---

# Security & Responsible AI

Candidate information is sensitive and should be handled accordingly.

## Security Principles

* Store secrets in n8n credentials.
* Never place API keys inside prompts.
* Avoid hardcoded credentials.
* Use stable internal IDs.
* Minimize unnecessary candidate data.
* Apply least-privilege access.
* Preserve audit history.
* Validate external data before persistence.
* Restrict external communications to approved workflows.

## Responsible AI Principles

### AI Assists; Recruiters Decide.

The platform is not designed to autonomously:

* Hire candidates
* Reject candidates without human review
* Invent candidate qualifications
* Guess missing information
* Treat missing verification as proof of fraud
* Generate unsupported claims
* Send external candidate submissions without approval

---

# Testing Strategy

The platform should be tested at workflow and system level.

## Job Tests

* Valid JD
* Empty JD
* JD with ambiguous requirements
* JD with missing experience
* JD with unsupported file

## Resume Tests

* Clean PDF
* Scanned PDF
* DOCX
* Empty document
* Resume with missing dates
* Resume with conflicting dates

## Matching Tests

* Strong match
* Partial match
* Missing mandatory skill
* Related skill
* Insufficient experience
* Conflicting evidence

## Verification Tests

* Matching education
* Different degree
* Matching employment
* Different dates
* Missing profile data
* Company not found
* Public HR contact found
* No public contact found

## Reliability Tests

* AI timeout
* Invalid JSON
* API timeout
* Rate limit
* Database failure
* Duplicate candidate
* Duplicate job
* Failed document extraction

---

# Project Structure

```text
AI-Recruiting-Platform/
│
├── README.md
│
├── workflows/
│   ├── 01-job-intake.json
│   ├── 02-jd-analysis.json
│   ├── 03-candidate-resume-intake.json
│   ├── 04-resume-analysis.json
│   ├── 05-evidence-extraction.json
│   ├── 06-candidate-matching.json
│   ├── 07-education-verification.json
│   ├── 08-experience-verification.json
│   ├── 09-company-verification.json
│   ├── 10-hr-contact-discovery.json
│   ├── 11-verification-report.json
│   ├── 12-candidate-submission.json
│   ├── 13-recruiter-review.json
│   ├── 14-final-submission.json
│   └── 15-error-handler.json
│
├── prompts/
│   ├── jd-analysis.md
│   ├── resume-analysis.md
│   ├── evidence-extraction.md
│   ├── candidate-matching.md
│   ├── verification.md
│   └── submission.md
│
├── test-data/
│   ├── sample-job.json
│   ├── sample-candidate.json
│   └── sample-resume/
│
├── docs/
│   ├── architecture.md
│   ├── database.md
│   ├── integrations.md
│   └── deployment.md
│
└── assets/
    ├── branding/
    ├── screenshots/
    └── demo/
```

---

# Required Integrations

| Integration                   | Purpose                                 | Status                        |
| ----------------------------- | --------------------------------------- | ----------------------------- |
| n8n Cloud                     | Workflow orchestration                  | Core                          |
| PostgreSQL / Supabase         | Persistent data                         | Core                          |
| LLM Provider                  | Extraction and reasoning                | Required                      |
| Document Parser               | Resume/JD extraction                    | Required                      |
| Professional Profile Provider | Authorized verification                 | Optional / Approval Dependent |
| Company Data Provider         | Company verification                    | Optional                      |
| Public Search Source          | Public contact discovery                | Optional                      |
| Email Provider                | Approved recruiter/client communication | Optional                      |
| Object Storage                | Original resumes/documents              | Recommended                   |

### Placeholder Integrations

External integrations must be explicitly marked:

```text
PLACEHOLDER — CONFIGURE API
```

Each placeholder should document:

* Authentication
* Required credentials
* Required scopes
* Expected input
* Expected output
* Rate limits
* Failure behavior

The project does not invent API endpoints, credentials, scopes, or response fields.

---

# n8n Cloud Implementation

This project is designed for **n8n Cloud**.

n8n acts as the orchestration layer connecting:

* Forms
* AI models
* Databases
* Document processing
* External APIs
* Validation logic
* Approval workflows
* Notifications
* Error handling

The architecture keeps business logic modular so that workflows can be independently tested and maintained.

---

# Implementation Roadmap

<div align="center">

<table>
<tr>
<td align="center" width="20%"><b>Phase 01</b><br><br>Job + JD Intelligence</td>
<td align="center" width="20%"><b>Phase 02</b><br><br>Resume + Evidence</td>
<td align="center" width="20%"><b>Phase 03</b><br><br>Matching Engine</td>
<td align="center" width="20%"><b>Phase 04</b><br><br>Verification</td>
<td align="center" width="20%"><b>Phase 05</b><br><br>Recruiter Platform</td>
</tr>
</table>

</div>

### Phase 01

* Job intake
* JD extraction
* Requirement structuring
* PostgreSQL schema

### Phase 02

* Resume intake
* Document extraction
* Resume parsing
* Evidence extraction

### Phase 03

* Skill normalization
* Deterministic matching
* Semantic matching
* Evidence-backed explanations

### Phase 04

* Education verification
* Experience verification
* Company verification
* Contact discovery
* Verification reporting

### Phase 05

* Recruiter dashboard
* Review queue
* Candidate comparison
* Approval flow
* Client submission

---

# Product Vision

The long-term objective is not simply to build an AI resume parser.

The objective is to build a **recruiting intelligence layer** where recruiters can move from raw job requirements and candidate documents to a defensible, source-backed candidate submission with significantly less repetitive work.

The platform is designed to make recruiting:

**Faster**

Automate repetitive extraction, normalization, and comparison.

**More Explainable**

Show the evidence behind important conclusions.

**More Consistent**

Apply the same matching and verification rules across candidates.

**More Controllable**

Keep recruiters inside the decision loop.

**More Auditable**

Preserve sources, decisions, discrepancies, and workflow history.

---

# Why This Architecture

Many AI recruiting systems stop at:

```text
Resume → AI → Match Score
```

This platform goes further.

It separates:

```text
Understanding
Matching
Evidence
Verification
Decision
Submission
```

That separation makes the system easier to test, explain, audit, and improve.

---

# Design Principles

<div align="center">

<table>
<tr>
<td width="33%" valign="top">

### Evidence First

Important claims should have a source.

</td>

<td width="33%" valign="top">

### Deterministic Where Possible

Dates, numbers, and mandatory rules should not depend entirely on an LLM.

</td>

<td width="33%" valign="top">

### Human Controlled

Recruiters retain final decision authority.

</td>
</tr>

<tr>
<td width="33%" valign="top">

### Source Fidelity

Original candidate information is preserved.

</td>

<td width="33%" valign="top">

### Failure Is Explicit

Unknown and failed states are represented instead of hidden.

</td>

<td width="33%" valign="top">

### Modular Automation

Each major capability can be tested and replaced independently.

</td>
</tr>
</table>

</div>

---

# Demo / Screenshots

When implementation screenshots are available, place them in:

```text
assets/screenshots/
```

Recommended showcase sequence:

| Screenshot             | Purpose                     |
| ---------------------- | --------------------------- |
| `dashboard.png`        | Recruiter overview          |
| `jd-analysis.png`      | Structured job requirements |
| `candidate-match.png`  | Evidence-based matching     |
| `verification.png`     | Verification result         |
| `recruiter-review.png` | Human approval interface    |
| `submission.png`       | Final candidate package     |

For a polished repository, screenshots should show the actual implemented platform rather than conceptual mockups.

---

# Quick Start

## 1. Create the n8n Cloud Workspace

Create the required workflows in your n8n Cloud project.

## 2. Configure Credentials

Add provider credentials through n8n's credential system.

Do not place secrets directly inside workflow nodes or prompts.

## 3. Configure the Database

Create the PostgreSQL/Supabase schema.

## 4. Import Workflows

Import the workflow JSON files from:

```text
workflows/
```

## 5. Configure AI Provider

Add the selected LLM credential and connect it to the AI workflows.

## 6. Configure Document Extraction

Enable PDF/DOCX/TXT processing and OCR fallback where required.

## 7. Configure Verification Providers

Enable only authorized professional-profile, company, and public-source integrations.

## 8. Run Test Data

Use the sample records in:

```text
test-data/
```

## 9. Validate the Recruiter Review Stage

Verify that candidates cannot reach final submission without explicit recruiter approval.

---

# Example Verification Result

```json
{
  "candidate_id": "candidate_001",
  "job_id": "job_001",
  "overall_status": "manual_review",
  "match": {
    "classification": "possible_match",
    "mandatory_requirements_supported": 7,
    "mandatory_requirements_total": 8
  },
  "education_verification": {
    "status": "consistent"
  },
  "experience_verification": {
    "status": "minor_discrepancy"
  },
  "company_verification": {
    "status": "verified"
  },
  "contact_discovery": {
    "status": "found"
  },
  "manual_review_items": [
    "One mandatory requirement has only partial evidence.",
    "Employment date discrepancy requires recruiter review."
  ]
}
```

---

# Responsible Use Disclaimer

This platform is designed as a **recruiting decision-support and workflow automation system**.

It should not be used to make fully automated employment decisions.

Recruiters and authorized hiring professionals remain responsible for:

* Reviewing candidate information
* Confirming verification results
* Handling discrepancies
* Applying applicable employment laws and policies
* Obtaining required permissions for personal/profile data
* Making final recruitment decisions

Professional-profile and company verification must use authorized or publicly permitted data sources.

---

# Contributing

Contributions are welcome.

Recommended contribution areas:

* n8n workflow improvements
* Validation logic
* Document extraction
* Matching algorithms
* Evidence models
* Database improvements
* Testing
* Documentation
* Recruiter UX
* Integration adapters

Before contributing a new integration, document:

* Authentication
* Required permissions
* Input schema
* Output schema
* Error behavior
* Rate limits
* Data handling requirements

---

# License

Add your chosen project license here.

Example:

```text
MIT License
```

If the repository is intended for commercial/private deployment, replace this section with the project's actual license terms.

---

<div align="center">

## AI Recruiting Intelligence Platform

**Structured hiring intelligence for evidence-backed recruiting workflows.**

<br>

<img src="https://img.shields.io/badge/Built%20with-n8n%20Cloud-EA4B71?style=flat-square&logo=n8n&logoColor=white" alt="Built with n8n">
<img src="https://img.shields.io/badge/Data-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL">
<img src="https://img.shields.io/badge/Platform-Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white" alt="Supabase">

<br><br>

<sub>AI assists. Evidence supports. Recruiters decide.</sub>

</div>
