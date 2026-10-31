# Documented-workflow comparison and bounded methodological advantage
**CCEV / Nursery Fee Clarity — public research memorandum**  
**Checked:** 31 October 2026  
**Status:** Source-backed documented-method comparison; **not** experimentally established superior accuracy, unique invention, or Innovator Founder endorsement.

## Research question
For a parent who has *an original nursery fee schedule* but **does not yet have a trusted, fully itemised quote**, can a source-first evidence-verification workflow resolve a booking-specific cost (or justify why a price cannot be given) with less manual inference than the **documented procedures** of existing tools?

We compare advertised inputs, transformations, outputs and dependencies. We **do not** infer that undocumented competitor functions are absent. We do not need privileged knowledge of their software internals, but descriptions alone cannot prove their actual case-level reliability.

## Seven relevant competitors: directly documented workflows
| Provider | Confirmed public inputs and method | Publicly described result | Genuine overlap / bounded implication |
|---|---|---|---|
| [Clever Mum: Nursery cost comparison](https://clevermum.co.uk/tools/childcare-planner/) | Parents enter a provider's **written weekly quote after funded hours**, weekly extras, weeks charged, joining fees and deposits; the tool computes (weekly care + extras) × weeks + joining fees; unknown remains unknown. | Compare up to three first-year budgets; refundable deposits separately; visit checklist. | Demonstrates well-designed quote-based comparisons; it starts **after the parent/provider identifies the applicable charges**, unlike our proposed source-first interpretation. Does not show every unadvertised capability. |
| [Clear Nursery Fees: Invoice Checker](https://clearnurseryfees.co.uk/invoice-checker) and [calculator](https://clearnurseryfees.co.uk/calculator) | Enters or scans **invoice line items**, compares paid hours, funded hours and fees with entitlement and published LA rates; calculator models government help and a supplied private nursery rate. | Identifies potential invoice inconsistencies and estimated costs. | **Significant overlap** in evidence-checking and add-ons, with automated invoice scanning. Our potential distinction is **pre-invoice interpretation of original provider tariff terms**; it is NOT fair to call Clear Nursery Fees a mere four-function calculator. |
| [NurseryWise](https://nurserywise.co.uk/) | Nursery-search tool presents provider fees where published, **the sentence the fee came from and a source link**; also helps compare nurseries. | Fee-source provenance attached to nursery listings. | **Direct overlap in source citation**. Citing a source is **not** itself our novelty. The proposed additional step is composing multiple provider-specific clauses for a requested booking and withholding a whole unsupported cost. Its absence from the published description is not proof the competitor cannot do it. |
| [Local Nursery Fees: How we work](https://localnurseryfees.co.uk/how-we-work) and [quote checker](https://localnurseryfees.co.uk/check-a-nursery-quote) | Combines official registers, published tariffs and LA funding rates; periodically checks prices; compares a supplied quote against published local/full-day fees; explicitly says when unknown. | Dated published rates, local comparisons and quote guidance. | **Overlap in published source collection, verification and explicit unknowns**. Target contrast: **conditional booking-specific tariff-rule composition**, not source transparency alone. Respect published restrictions on bulk reuse; only cite/link their public descriptions. |
| [Toddle](https://toddlekids.com/) | Nursery search/shortlist and cost estimator based on selected ages, days, hours, reported or average prices, meals and funding assumptions. | Comparison of settings, fees, availability and monthly estimates; explain term-time vs stretched funding. | Overlap in nursery choice and cost estimation. Proposed distinction is verifying the specific **original nursery contract/fee conditions** for a scenario. |
| [Famly: Invoicing Profiles](https://help.famly.co/en/articles/4912323-invoicing-profiles) and [New Invoicing](https://help.famly.co/en/articles/12441806-a-new-invoicing-experience) | Nursery-authorised users configure attendance schedules, fee profiles, grants, extras, annualisation and invoice rules; new invoicing can add extras automatically. | Detailed and configurable parent invoices and funding application. | **Major overlapping complex calculation and conditional funding features.** Distinction is independent parent-side examination of original public terms **without the nursery first configuring an authorised billing system**; no suggestion Famly lacks robust finance logic. |
| [Nursery in a Box: Funding, Invoicing & Payments](https://www.nurseryinabox.com/funding-invoicing-payments) | Nursery records bookings, sessions, allocated funding, extras and discounts; previews and produces itemised invoices. | Draft-reviewed invoices, funded-hour allocations and parent-visible charge breakdowns. | **Major overlap** in conditional billing and invoice verification. Potential distinction: consumer-accessible pre-contract source-to-scenario checking independently of a nursery-managed account. |

### Provenance and interpretation discipline
- All links above point to supplier-operated public product/help pages reviewed on 31 October 2026. Published descriptions are **evidence of advertised workflow**, not source code, proprietary internal implementation or proof of the full feature inventory.
- Apparent absence of a step in documentation = "**not evidenced in reviewed public workflow**", **not** "does not exist".
- Supplier pages can change. Retain URL, check date and a short factual claim; do not bulk-copy copyrighted content.
- This is a **bounded comparison**, not a matched real-time customer experiment. No third-party live case responses were obtained.

## Candidate CCEV method
Let the original provider document be D and the parent's proposed booking be x. A reliable source-to-decision pipeline ought to:
1. Identify versioned source D and page/span provenance.
2. Extract candidate rules R with exact supporting spans (age bands, session duration, tariff period, booking minimums, extras, discounts, term weeks, funding where supported).
3. Verify every decision-critical rule: source containment, correct temporal/version scope, age/session eligibility, consistent unit and billing basis, cross-rule precedence and arithmetic.
4. Build an auditable dependency graph: **booking x → applicable source rule set → justified line items → deterministic total**.
5. Withhold the total, cite the blocking rule and request a precise clarification if the necessary source evidence is absent or ambiguous. Do not convert "unknown" to zero, assume funded-hours eligibility, or infer a discount's applicability from the discount's amount.

For eligible scenarios, a simplified gross contractual amount is
\[
C = \sum_{i=1}^{n} q_i(x)\,p_i(D) + \sum_{j=1}^{m} e_j(x,D) - \sum_{k=1}^{r} d_k(x,D)
\]
**only if** each applicable fee, required extra, permitted discount and period basis has verified evidence; public provider documents alone are not proof of a family's statutory funded-hours eligibility.

### Worked methodological counterexample: minimum booking
Assume a **fictional** nursery publishes "full day £72" and "minimum two days each week"; a parent wants one day.
- A calculator supplied the interpreted rate £72 can multiply it by one, but £72 would be an **unsupported bookable one-day price** if it does not also check the booking minimum.
- A source-first rule verifier reads and enforces the minimum and reports the one-day booking cannot be priced as requested. It should ask whether a different arrangement is offered.
- This shows a **logical advantage of a correctly implemented rule-aware method over rate-only multiplication in this specifically defined case**; it does **not** prove any named competitor necessarily makes that error or that our deployed implementation succeeds on real examples.

## Why this can be meaningful but is not a finished superiority finding
**Potential benefit:** parent need not pre-interpret all conditional tariffs; outputs are independently evidence-linked and bounded by source constraints. This could reduce manual cost interpretation and discourage unsupported amounts.

**Substantial overlap:** NurseryWise already displays fee source sentences; Local Nursery Fees verifies published rates and unknowns; Clear Nursery Fees validates invoice details; Famly and Nursery in a Box encode conditional funding and extras. We cannot claim "no competitor uses sources", "no other product verifies fees", or "this method cannot be copied".

**Current live evidence:** 5/7 unfamiliar nursery documents captured. 15/21 cases executed: 12 numerical-reference cases, **4 exact provisional matches and 8 refusals**, with no recorded incorrect numeric quotations. Three expected-refusal cases were withheld, but refusal reasons need scrutiny. Six cases unexecuted. Frozen reference arithmetic has source-based corroboration with qualifications; this is not external human signoff. **Do not** characterise this as reliable superiority: numerical coverage was 33.3% on executable numeric cases.

## Falsifiable superiority and replication claims
| Claim | Falsifier / required proof |
|---|---|
| Source rules remove parent-side pre-interpretation | In observed parent studies, participants still need to extract rate/discount/billing context manually to finish. Measure tasks, input burden, correct understanding, completion and time. |
| Stronger evidential justification | Decision-critical outputs do not point to exact source spans, fail to encode their scope, or incorrectly refuse/quote. |
| Booking-specific rule composition is useful | Real users cannot resolve meaningful choices that their existing workflow handles, or judge the output less useful. |
| Reliable automation | Fresh blind cohort still produces excess false abstentions or materially wrong quotes; the first cohort's 4/12 already raises this issue. |
| Reasonable barrier to straightforward replication | A capable competitor can reproduce the key end-to-end error bounds and case handling cheaply using ordinary OCR + prompts + simple calculator without additional difficult engineering, benchmark assets or data advantages. |

### Gate discipline
- **Documented method-level contrast:** supported as a *qualified structural proposition* against specific documented workflows.
- **Proven overall competitive superiority:** NOT ESTABLISHED.
- **Reliability for unrestricted real family quotes:** NOT ESTABLISHED.
- **Replication barrier:** NOT ESTABLISHED.
- **Customer evidence:** Collect a privacy-conscious research sample. An unverified public GitHub issue count is *not* equivalent to independently confirmed unique parent participants.

## Immediate evidence collection
1. Publish a website "How the methods differ" section explaining the precise comparison and overlaps.
2. Invite people to explore **fictional only** booking scenarios and answer structured questions: booking status, main obstacle, perceived clarity and practical value.
3. Provide two safe paths: local feedback copy (works without sign-in) or optional public GitHub issue (requires a GitHub account, public identity/answer; **no personal data or nursery documents**).
4. Record study provenance and qualitative observations separately from GitHub issue counts, and avoid calling interest a purchase, retained use or actual product accuracy.

## Launch constraints
This public repository intentionally contains only static assets. Render has **one active free PostgreSQL database already assigned to another project**; Render offers only one active free Postgres instance per workspace, and free Render Key Value does not persist reliably. We do not put childcare research data in another venture's datastore, publish a personal email address, or enable a paid backend without approval. See [Render free tier restrictions](https://render.com/docs/free).

Endorsement requires a **credible competitive distinction, implementable advantage, viability and scalability**, not merely an attractive architecture description. This comparison is a traceable component of that case, not a substitute for it.
