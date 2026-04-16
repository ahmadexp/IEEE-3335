> **Editor's Note (Rodney C., P3335 Working Group):** 
> This document currently serves as a structural guideline for defining what will eventually go into the Conformance clause of the P3335 standard. We want to align the working group on drafting normative requirements.

# 4. Conformance Guidelines & Methodology

## 4.1 IEEE-SA Terminology Standards
IEEE-SA strictly regulates the terminology used to express requirements within a standard. The following boilerplate text is provided by the IEEE-SA template and cannot be edited by the Working Group. 

Requirements placed upon conformant implementations of this standard are expressed using the following specific keywords:

1. **Shall:** Used exclusively to indicate **mandatory requirements** (must-have features to claim conformance).
2. **May:** Used exclusively to describe **implementation or administrative choices** ("may" means "is permitted to"). *Note that "may" and "may not" mean precisely the same thing in this context.*
3. **Should:** Used exclusively for **recommended choices**. The behaviors described by "should" and "should not" are both permissible, but one is clearly more desirable than the other.

### 4.1.1 Prohibited and Deprecated Terminology
* **Must:** IEEE-SA strictly prohibits the use of "must" to describe requirements because it is frequently confused with "shall". The P3335 text **cannot** use "must." (If an unavoidable physical limitation exists, "must" may sometimes be justified, but it is generally deprecated in modern drafting).
* **Will / Can:** These words are used only for statements of fact or capability, completely devoid of conformance implications.

These three core keywords (*shall, should, may*) are critical. They instruct an engineer exactly how to implement the standard. Without the strategic use of these words, the document functions merely as a "Recommended Practice" rather than a true Standard.

---

## 4.2 Structural Methodologies for Conformance
Within IEEE standards, there are three primary methodologies for organizing and expressing these requirements.

### 4.2.1 Methodology A: Conformance Clause Only
In this approach, normative clauses (Clause 4 and up) and normative annexes avoid using the three keywords entirely, instead using descriptive verbs like "is" and "are" to explain what an implementer does. A single, dedicated Conformance Clause at the beginning uses the keywords by referencing the subsequent normative clauses (e.g., *"An implementation of this standard shall implement only one of the following: a) Clause 4, b) Clause 6, c) Subclause 8.2"*). 
* **Example:** IEEE 802.1

**Advantages:**
* The Conformance Clause serves as a "one-stop shop" to quickly understand the core requirements.
* It easily supports a hierarchical tree of requirements and options (e.g., *"If you implement high-level option A, you shall implement subclause 4.5"*).

**Disadvantages:**
* Standards authors frequently slip and use "is" for concepts unrelated to conformance, which causes ambiguity.
* Authors inevitably accidentally use the three keywords within the normative text anyway, creating contradictions with the central Conformance Clause.

### 4.2.2 Methodology B: Interspersed Without Conformance Clause
In this approach, the normative clauses and annexes directly use the three keywords (*shall, should, may*). Words like "is" and "can" are reserved solely for factual statements with no conformance implication. There is no central Conformance Clause; instead, the requirement tree is reflected purely through the structural organization of the document (e.g., Subclause 6.8.3 might be explicitly titled *"Feature foobar (Optional)"*).
* **Example:** IEEE 1588

**Advantages:**
* Avoids the ambiguities and accidental contradictions of Methodology A.
* Conformance is immediately clear as the implementer reads through the technical text.

**Disadvantages:**
* Places a heavier burden on the implementer to hunt through the entire document to find all relevant "shalls."
* It is significantly more difficult for authors to document a complex, mutually exclusive tree of dependencies.

### 4.2.3 Methodology C: Interspersed With Conformance Clause
This is a hybrid approach. It uses the dispersed keywords of Methodology B but adds a high-level Conformance Clause to summarize the major requirement trees. 

The Conformance Clause provides the high-level roadmap (e.g., *"If you implement high-level option A, you shall implement subclause 4.5"*). Within subclause 4.5 itself, the text will state things like, *"The port shall transmit..."* which implicitly means *"If you support 4.5, you shall do this."*

---

## 4.3 P3335 Working Group Recommendations

### 4.3.1 Recommended Drafting Methodology
> **Recommendation (Rodney C.):** Proceed with drafting the subsequent text using the **Interspersed Technique** (Methodology B). 

As the P3335 project matures, the Working Group can evaluate whether a high-level Conformance Clause (upgrading to Methodology C) is necessary. Because P3335 is likely to develop a complex feature tree, a summarizing Conformance Clause will likely prove highly beneficial in later drafts.

### 4.3.2 Protocol Implementation Conformance Statement (PICS)
> **Recommendation (Rodney C.):** Strongly avoid creating a PICS annex.

A PICS typically takes all the dispersed requirements and repeats them in a massive hierarchical table. Some engineers prefer reading tables to text for compliance checking, which is why PICS annexes are included in many IEEE standards. 

**The critical disadvantage:** A PICS *will* inevitably fall out of sync with the main text of the standard during drafting and iterative revisions. This creates massive contradictions for implementers. Adding disclaimers like *"When there is a contradiction, ignore the PICS"* is often insufficient. *(Note: IEEE 802.1Q heavily suffers from this exact PICS desynchronization problem).*
