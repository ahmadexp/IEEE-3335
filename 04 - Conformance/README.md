> Editor's note from Rodney C: This entire readme is a note for now. The intention is to describe what goes into a Conformance clause.

IEEE SA requires text like the following in a standard. This text cannot be edited by the Working Group... it is part of the IEEE SA template for a Standard like P3335. I'm providing a sample from 802.1 here because I don't know the latest IEEE SA version.

"
Requirements placed upon conformant implementations of this standard this standard are expressed using the following terminology:

1. **Shall** is used for mandatory requirements.
2. **May** is used to describe implementation or administrative choices (“may” means “is permitted to,”
and hence, “may” and “may not” mean precisely the same thing).
3. **Should** is used for recommended choices (the behaviors described by “should” and “should not” are
both permissible but not equally desirable choices).

"

IEEE SA usually prohibits use of "must", because it can be confused with "shall". IEEE P3335 text cannot use "must".

These three words are very important, because they tell an engineer how to implement the standard. Without these words, the document is nothing but recommendations (i.e., Recommended Practice).

There are roughly three methodologies for using these three words:

### Conformance Clause Only

Normative clauses (4 and up) and normative annexes avoid using the three words, using "is" and "are" to describe what an implementer does. There is a single Conformance clause that uses the three words by referencing the subsequent normative clauses. For example, the Conformance clause could state "An implementation of this standard shall implement only one of the following: a) clause 4, b) clause 6, c) subclause 8.2." IEEE 802.1 uses this methodology.

Advantages:
- The Conformance clause is the one-stop-shop to understand what is most important to an implementer.
- The Conformance clause can be a tree of requirements and options. For example, "If you implement high level option AAA, you shall implement subclause 4.5. If you implement high level option BBB, you may implement subclause 4.5."

Disadvantages:
- Standards authors will use "is" for something unrelated to conforamance. This can be very confusing.
- Standards authors will use the three words in normative text. This can be very confusing, especially when it contradicts the Conformance clause.

### Interspersed Without Conformance clause

Normative clauses (4 and up) and normative annexes use the three words. Words like "is" and "can" have no conformance implication. There is no Conformance clause, so the tree of requirements/options is reflected through organization of clauses. For example, subclause 6.8.3 might be titled "Feature foobar (optional)". IEEE 1588 uses this methodology.

Advantages:
- Avoids all disadvantages of Conformance Clause Only. Conformance is clear as you read the document.

Disadvantages:
- Sometimes more work for implementer to find all relevant shalls.
- Diffult for standards authors is create a complex tree of requirements/options.

### Interspersed With Conformance clause

Same as Interspersed Without Conformance clause, but add a Conformance clause to summarize the tree of of requirements/options. The Conformance clause is the high level summary, and subsequent text provides detailed conformance. For example, the Conformance clause can have "If you implement high level option AAA, you shall implement subclause 4.5. If you implement high level option BBB, you may implement subclause 4.5." Within subclause 4.5, "shall" means "if you support 4.5, you shall do this".

> Recommendation from Rodney C: Proceed with subsequent text using the Interspersed technique. Later in the P3335 project, we can consider whether we want a Conformance clause. My guess is that P3335 will have a tree, in which case the Conformance clause will be very useful.

> Recommendation from Rodney C: Avoid doing a PICS annex. A PICS is a repetition of all of the above into a table. The table is hierarchical, so it can cover the tree issue. Some people like to read tables instead of text for conformance, so a PICS exists in many IEEE standards for that reason. The huge disadvantage is that a PICS **will** (not maybe... will) get out of sync from the rest of the standard's conformance. That creates huge contradictions for an impelementer. Statements like "When there is a contradiction, ignore PICS" can help, but not much. IEEE 802.1Q suffers from this PICS problem.




