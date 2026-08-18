# **The Worldly Chatbot: Dual-Channel Personality Assessment**

**Status:** Concept summary — working document  
 **Date:** April 2026

---

## **The Core Idea**

A conversational AI that regularly checks in with users to assess personality states and support movement toward trait goals. It runs two measurement channels simultaneously in every conversation:

**Channel 1 — Language-based trait extraction.** The chatbot extracts personality signal from the user's natural language: word choice, emotional valence, sentence structure, conversational style. This is what the existing NLP-personality literature does (Fan et al. 2023, Oltmanns et al. 2025). It works. Convergent validity with questionnaires runs r \= .3–.5. But it is fundamentally self-report through a different channel — it captures how the person *presents*, not how they *process*.

**Channel 2 — Behavioral measurement through embedded SJTs.** The chatbot delivers situational judgment items drawn from the BRILLIANCE SJT battery (Social Calibration × Threat Discrimination × CRT), embedded in the natural flow of conversation rather than presented as a test. The chatbot can make a social bid and observe whether the user detects it. It can present a threat-ambiguous scenario and observe whether the user discriminates signal from noise. It can embed a cognitive lure and observe whether the user overrides the heuristic default. This measures *algorithmic capacity* — what the person can actually do when the autonomous system misfires — not what they say about themselves.

**The novel contribution is running both channels at once and testing where they diverge.**

BRILLIANCE predicts specific, theoretically motivated divergence patterns. The clearest: a user whose language signals high Extraversion (approach-oriented, positive emotion words, high social-process word use) but who fails bid-detection items is showing the E2/E3 dissociation — affiliative warmth without social-calibration skill. That pattern is invisible to any single-channel instrument. It's also clinically and practically useful: the intervention for "wants connection but misreads signals" is different from the intervention for "reads signals but avoids connection."

---

## **What the Chatbot Does Differently from Existing Approaches**

**Activates the autonomous system.** Written SJT items have an ecological validity problem: reading is deliberative, so the person is already in System 2 by the time they see the options. A chatbot that's been talking with someone for ten minutes can embed the lure in conversational flow, activating autonomous processing the way real social situations do.

**Follows up on selections.** Current SJTs give you a choice and an error direction. A chatbot can ask *why* — and the rationale separates algorithmic capacity from reflective disposition (Stanovich's key distinction). Picking the wrong answer because you didn't see the signal is a detection failure (algorithmic). Picking the wrong answer because you saw the signal but felt rude overriding it is an override failure (reflective). The current instrument can't distinguish these. A chatbot can.

**Generates adaptive item variants.** The difficulty-family architecture (e.g., E-3 → E-3c, graded by bid explicitness) is an IRT item bank. The chatbot starts mid-difficulty and moves up or down based on responses — standard CAT logic. But it can also generate context-matched variants dynamically, adjusting scenarios to the user's actual life context (work domain, relationship type, cultural setting). This solves the ecological validity concern without sacrificing psychometric structure.

**Captures latency and confidence.** The five-component scoring framework includes confidence and latency predictions. A chatbot naturally captures response time and can probe confidence without it feeling like a test.

**Protects item security.** CRT items are already compromised by exposure. If the chatbot generates novel variants from the underlying generative grammar (Cialdini's influence principles for E-items, de Becker's pre-incident indicators for N-items, Kahneman's heuristic catalog for I-items), the *structure* is the instrument, not the specific items. Much more defensible against exposure effects.

---

## **State Tracking Over Time**

If the chatbot assesses someone regularly (weekly, biweekly), it generates a time series of personality states, not just a one-shot trait estimate. Fleeson's whole trait theory predicts the average across sessions converges on the trait. But the variance around that average — state variability — is itself an individual difference worth tracking.

BRILLIANCE gives this a mechanistic interpretation: state variability \= attractor instability \= how easily the workspace shifts between configurations. High state variability on the SJT channel (algorithmic capacity fluctuates session to session) may index workspace fragility — the system can reach the high-performance attractor but doesn't stay there reliably. That's a different clinical picture from someone whose performance is stably low (the attractor is stable but in the wrong basin) or stably high (robust workspace access).

The two channels should show different temporal dynamics. Language-based trait estimates (Channel 1\) should be relatively stable session to session — people's conversational style doesn't swing much week to week. SJT performance (Channel 2\) should be more state-sensitive — algorithmic capacity is affected by sleep, stress, cognitive load, mood. If this dissociation holds empirically, it means Channel 1 tracks the trait and Channel 2 tracks the state, and you need both.

---

## **Traps as Chatbot Guardrails**

The Brilliant Traps taxonomy serves two functions in the chatbot:

**User-facing (Scrubs traps).** The chatbot recognizes when the user is falling into a personality-relevant failure mode and gently redirects:

* *Fatalist* — treats personality as verdict ("I'm just not a people person"). Chatbot reframes toward capacity and state, not fixed identity.  
* *Pragmatist* — treats personality as a project to optimize ("just tell me what to do"). Chatbot maintains that understanding precedes intervention.  
* *Escapist* — blames environment, denies stable patterns ("it's just my job / relationship / city"). Chatbot holds the cross-situational signal.  
* *Situationist* — denies traits entirely ("I'm different in every context"). Chatbot presents the density distribution evidence.

**System-level (White Coat traps).** Guard against the chatbot reinstalling the very errors BRILLIANCE is designed to correct:

* *Homuncular Fallacy* — LLMs are structurally agentive. The chatbot will naturally say "you need to take control of your attention." System prompt audits outputs for language that implies a homunculus directing traffic.  
* *False Dichotomy* — mainstream personality psychology separates cognition from affect. The chatbot needs active guardrails against reinstalling this split when it gives feedback.  
* *Flat Mind* — the chatbot only sees text (the read-head). Two users with identical response patterns may have different underlying configurations and need different interventions. The chatbot must hold uncertainty about depth.  
* *Module Fallacy* — "your Conscientiousness score is X" installs modularity. The chatbot must translate between user-accessible language and architecturally accurate framing without collapsing into either extreme.

---

## **Open Questions**

1. **Convergent validity design.** What's the right study to establish that Channel 2 (SJT) measures something Channel 1 (language extraction) doesn't? Need a sample where both channels run simultaneously, plus external criteria that one channel should predict better than the other.

2. **Item generation at scale.** Can LLMs generate valid SJT variants from the Cialdini/de Becker/Kahneman generative grammars? Need expert scoring of generated items to validate the generation pipeline before deployment.

3. **State sensitivity calibration.** How much session-to-session variance in SJT performance is real state fluctuation vs. measurement noise? Need test-retest data at multiple intervals.

4. **Trap detection accuracy.** Can the chatbot reliably distinguish the four Scrubs traps from each other and from non-trap conversation? Need labeled training examples.

5. **The coaching problem.** Assessment and intervention are different things. The chatbot can measure where someone is. Helping them move toward where they want to be requires a theory of change that the SJT battery doesn't provide. The Architecture doc's two-regime model (reversible dynamics vs. structural degradation) is relevant here — the chatbot needs to know which regime the person is in before recommending interventions.

