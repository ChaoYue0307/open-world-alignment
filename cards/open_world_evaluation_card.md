# Open-World Evaluation Card

Use this card when a system makes an ASI-relevant or beyond-human capability claim: a claim where consequential outputs exceed unaided human ability to reliably generate, rank, verify, or forecast.

The card separates human-facing scores from broader evidence about task success, hard constraints, evaluator weakness, absent stakeholders, and deployment-time revision.

## System

- **System name:**
- **System description:**
- **Version or deployment setting:**
- **Card owner:**
- **Date:**

## 1. Claim Type

- What beyond-human or ASI-relevant capability is being claimed?
- Is the claim scoped to a domain, task family, population, benchmark, deployment setting, or institution?
- Where does unaided human supervision become weak?
- What would the system not be allowed to claim based on the current evidence?

## 2. Target World State

- What real-world outcome is the system intended to improve?
- What evidence would show that this outcome improved?
- What evidence would show that the system failed?
- Which parts of the target state are delayed, hidden, or hard to observe?

## 3. Human-Signal Role

- Which labels, preferences, ratings, benchmarks, judge models, expert reviews, or user feedback channels are used?
- Are they training signals, evaluation signals, deployment gates, interpretation aids, or monitoring signals?
- What can these signals verify?
- What can these signals not verify unaided?
- Could a system receive high human approval while failing the target world state?

## 4. Verifier Stack

- Which hard verifiers test whether outputs are actually correct or useful?
- Which soft verifiers provide advisory or qualitative evidence?
- Which external tools, simulators, test harnesses, theorem provers, audits, or monitors are used?
- Which human review channels interpret or challenge verifier outcomes?
- Why are the verifiers not merely correlated versions of the same proxy?
- How are verifier-gaming risks tested?

## 5. Hard Constraints

- Which safety, legal, privacy, rights, resource, ecological, or policy constraints cannot be traded away?
- How are these constraints operationalized?
- Which constraints are hard gates rather than soft preferences?
- Can aggregate performance override any constraint?
- Who can approve an exception, if any?

## 6. Evaluator Frontier

- Where do humans become weak supervisors for this system?
- What tools do humans need to inspect, reproduce, or challenge outputs?
- When should the system abstain, defer, escalate, or invoke stronger verification?
- What happens when verifiers disagree?
- What happens when coverage is weak or inputs are unfamiliar?

## 7. Absent Stakeholders

- Which affected non-users are outside the direct rating loop?
- Which downstream users, institutions, future populations, or ecosystems bear consequences?
- How are these stakeholders represented in mandate formation, evaluation, monitoring, or rollback?
- What harms or externalities would current human-facing metrics miss?

## 8. Monitoring and Rollback

- Which post-deployment signals are monitored?
- Which signals trigger redesign, suspension, rollback, or withdrawal?
- Who has authority to act on monitoring evidence?
- How often is the verifier stack reviewed?
- What evidence would require revising the original capability claim?
