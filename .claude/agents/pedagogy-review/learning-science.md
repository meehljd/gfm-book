# Learning Science Principles Reference

Evidence-based principles from cognitive psychology and educational research for optimizing textbook pedagogy.

---

## 1. Cognitive Load Management

**Research basis:** Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science*, 12(2), 257-285.

**Core insight:** Working memory has limited capacity (~4 items). Learning fails when cognitive load exceeds capacity.

### Three Types of Load

| Load Type | Definition | Goal |
|-----------|------------|------|
| **Intrinsic** | Complexity inherent to the material | Cannot reduce; manage through sequencing |
| **Extraneous** | Unnecessary complexity from poor presentation | Minimize ruthlessly |
| **Germane** | Productive effort building mental schemas | Maximize through active processing |

### Checks

- [ ] Complex concepts broken into chunks (max 3-4 new concepts before consolidation)
- [ ] Worked examples precede abstract principles
- [ ] Diagrams integrated with text (contiguity principle)
- [ ] No split attention (forcing readers to integrate distant information)
- [ ] Redundant information eliminated
- [ ] Technical jargon introduced gradually, not front-loaded
- [ ] Essential information highlighted without overwhelming

### Red Flags

- Introducing >4 new terms in a single paragraph
- Figure on different page than explaining text
- Same information in text and figure caption (redundancy)
- Jargon-heavy opening paragraphs

---

## 2. Retrieval Practice & Testing Effect

**Research basis:** Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249-255.

**Core insight:** Actively retrieving information from memory strengthens memory more than re-reading. Testing is not just assessment; it is a powerful learning event.

### Implementation Patterns

| Pattern | Example |
|---------|---------|
| **Prediction prompt** | "Before reading on, how would you approach X?" |
| **Comparison prompt** | "How does this differ from Y in Section Z?" |
| **Self-test** | "Can you explain why X leads to Y?" |
| **Knowledge check** | "What are the three key components of X?" |

### Checks

- [ ] Embedded knowledge checks within chapter (not just at end)
- [ ] Section openings that prompt recall of prerequisites
- [ ] "Stop and think" moments before revealing answers
- [ ] Prediction prompts before explanations
- [ ] Comparison tasks connecting to earlier material

### Red Flags

- All content presented passively (read-only)
- Questions only at chapter end
- Answers given immediately without pause for thought

---

## 3. Interleaving

**Research basis:** Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science*, 35(6), 481-498.

**Core insight:** Mixing related topics during learning improves discrimination between concepts and enhances transfer. Blocked practice (exhausting one topic before moving to next) feels easier but produces worse long-term learning.

### Implementation Patterns

| Pattern | Example |
|---------|---------|
| **Explicit comparison** | "Unlike k-mer tokenization, BPE learns vocabulary from data" |
| **Return with new lens** | Revisit attention mechanism after introducing long-range dependencies |
| **Cross-domain example** | Show same principle in DNA and protein contexts |
| **Alternation** | Present CNN approach, then attention approach, then compare |

### Checks

- [ ] Related concepts compared/contrasted explicitly
- [ ] Same principle shown in multiple contexts
- [ ] Return to earlier concepts with new perspective (spiral curriculum)
- [ ] "Compare this to..." prompts
- [ ] Alternation between approaches rather than exhaustive blocking

### Red Flags

- Entire chapter on approach A, then separate chapter on approach B with no comparison
- Concepts introduced and never revisited
- No explicit contrast between similar methods

---

## 4. Spacing & Distributed Practice

**Research basis:** Cepeda, N. J., et al. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354-380.

**Core insight:** Information revisited across time is retained better than massed practice. Forgetting and re-learning strengthens memory traces.

### Implementation Patterns

| Pattern | Example |
|---------|---------|
| **Forward hook** | "We'll see why this matters when we discuss transfer learning" |
| **Backward connection** | "Recall from Chapter 5 that tokenization determines resolution" |
| **Terminology reactivation** | Re-use and briefly re-explain key terms when they reappear |
| **Cumulative examples** | Examples that build on earlier material |

### Checks

- [ ] Key concepts referenced in later sections
- [ ] Forward hooks to create anticipation
- [ ] Backward connections to reactivate memory
- [ ] Terminology reactivated, not assumed remembered
- [ ] Cumulative complexity building on foundations

### Red Flags

- Concept introduced once and never mentioned again ("orphaned concepts")
- Assumptions that reader remembers material from 10+ pages earlier
- No forward references to motivate current material

---

## 5. Elaborative Interrogation

**Research basis:** Pressley, M., et al. (1987). Elaborative interrogation facilitates acquisition of confusing facts. *Journal of Educational Psychology*, 79(3), 268-278.

**Core insight:** Asking "why" and "how" questions during learning deepens processing and creates richer memory traces.

### Implementation Patterns

| Pattern | Example |
|---------|---------|
| **Explicit mechanism** | "The reason single-nucleotide resolution matters is..." |
| **Causal chain** | "This leads to X, which in turn causes Y, because..." |
| **Rationale provision** | "We use cross-entropy loss rather than MSE because..." |
| **Design justification** | "The authors chose this architecture because..." |

### Checks

- [ ] "Why" explanations accompany descriptions of "what"
- [ ] Mechanism explanations are explicit, not assumed
- [ ] Causal reasoning made clear
- [ ] Design choices justified, not just stated
- [ ] "The reason X happens is..." patterns present

### Red Flags

- Describing what a method does without explaining why it works
- Stating facts without mechanistic grounding
- "This is done by X" without "because Y"

---

## 6. Concrete Examples & Case-Based Learning

**Research basis:** Chi, M. T. H., et al. (1989). Self-explanations: How students study and use examples. *Cognitive Science*, 13(2), 145-182.

**Core insight:** Abstract concepts need grounding in specific instances. Examples should precede or accompany generalizations, not just follow them.

### Implementation Patterns

| Pattern | Example |
|---------|---------|
| **Clinical case** | "A patient with *DMD* variant presents with..." |
| **Worked scenario** | Step-by-step application of concept |
| **Concrete numbers** | "Processing 1 million variants requires..." |
| **Multiple instances** | Show concept in 2-3 different contexts |

### Checks

- [ ] Each major concept has at least one concrete example
- [ ] Examples precede or accompany generalizations
- [ ] Biological/clinical cases ground technical concepts
- [ ] Numbers and scales provided (not just "large" or "many")
- [ ] Worked-through scenarios showing concepts in action
- [ ] Multiple examples showing range of application

### Red Flags

- Abstract explanations without concrete grounding
- "Many applications" without naming specific ones
- Examples only after extensive theory
- Single example for complex concept

---

## 7. Dual Coding & Multimedia Learning

**Research basis:** Mayer, R. E. (2009). *Multimedia Learning* (2nd ed.). Cambridge University Press.

**Core insight:** Verbal and visual information processed in separate channels. Coordinated presentation in both channels enhances learning.

### Mayer's Principles

| Principle | Meaning |
|-----------|---------|
| **Contiguity** | Place text near corresponding graphics |
| **Signaling** | Use cues to highlight essential information |
| **Redundancy** | Don't duplicate identical information in text and narration |
| **Coherence** | Exclude extraneous material |
| **Segmenting** | Present in learner-paced segments |

### Checks

- [ ] Key concepts have both textual and visual representation
- [ ] Figures referenced in surrounding text
- [ ] Figure captions are explanatory, not just labels
- [ ] Visual metaphors for abstract concepts
- [ ] Spatial organization reflects conceptual relationships
- [ ] No gratuitous visuals that don't aid understanding

### Red Flags

- Figures distant from relevant text
- Captions that just label ("Figure 1: The model")
- Complex concepts with text-only explanation
- Decorative images without pedagogical value

---

## 8. Prior Knowledge Activation

**Research basis:** Ausubel, D. P. (1968). *Educational Psychology: A Cognitive View*. Holt, Rinehart & Winston.

**Core insight:** New information is learned by anchoring to existing knowledge structures. Meaningful learning requires connecting new material to what learner already knows.

### Implementation Patterns

| Pattern | Example |
|---------|---------|
| **Advance organizer** | Chapter preview, concept map at start |
| **Explicit prerequisite** | "This builds on the tokenization concepts from Chapter 5" |
| **Analogy** | "Like word embeddings in NLP, genomic embeddings..." |
| **Misconception correction** | "You might expect X, but actually Y because..." |

### Checks

- [ ] Advance organizers present (chapter previews, roadmaps)
- [ ] Explicit connections to assumed prerequisite knowledge
- [ ] Analogies to familiar domains (NLP→genomics)
- [ ] Misconception identification and correction
- [ ] Bridges from intuitive understanding to technical detail

### Red Flags

- Jumping into technical detail without context
- Assuming reader knows domain-specific background
- No analogies to familiar concepts
- Prerequisites unstated

---

## 9. Metacognitive Scaffolds

**Research basis:** Flavell, J. H. (1979). Metacognition and cognitive monitoring. *American Psychologist*, 34(10), 906-911.

**Core insight:** Learners benefit from thinking about their own learning. Scaffolds help learners monitor comprehension and identify gaps.

### Implementation Patterns

| Pattern | Example |
|---------|---------|
| **Learning objectives** | "After this section, you should be able to..." |
| **Summary structure** | Key points consolidated at section end |
| **Difficulty warning** | "This section is mathematically dense..." |
| **Self-check prompt** | "Can you explain X without looking back?" |

### Checks

- [ ] Learning objectives stated or implied at chapter/section start
- [ ] Summary structures help consolidation
- [ ] Difficulty warnings for challenging sections
- [ ] "Key insight" or "Core idea" callouts
- [ ] Self-test prompts for comprehension monitoring

### Red Flags

- No indication of what reader should learn
- Abrupt transitions between difficulty levels
- No consolidation points
- Reader cannot self-assess understanding

---

## 10. Desirable Difficulties

**Research basis:** Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing*.

**Core insight:** Some difficulties during learning enhance long-term retention and transfer. Making learning too easy can impair it.

### Implementation Patterns

| Pattern | Example |
|---------|---------|
| **Prediction before reveal** | "What do you think happens when...?" (then explain) |
| **Generation** | Reader must produce answer before seeing it |
| **Varied conditions** | Same concept in different contexts |
| **Spaced practice** | Revisit with delay, requiring effort to recall |

### Checks

- [ ] Questions posed before answers given
- [ ] Opportunities to predict before revealing
- [ ] Not everything immediately explained (productive gaps)
- [ ] Comparison tasks requiring active discrimination
- [ ] Progressive disclosure rather than all-at-once

### Red Flags

- Everything explained immediately with no pause
- No opportunity for reader to think before answer given
- Overly scaffolded content that requires no effort
- Hand-holding through every step

---

## 11. Hooks & Narrative Structure

**Research basis:** Willingham, D. T. (2009). *Why Don't Students Like School?* Jossey-Bass.

**Core insight:** The mind is drawn to stories and curious about gaps in knowledge. Narrative structure and curiosity gaps maintain attention and motivation.

### Implementation Patterns

| Pattern | Example |
|---------|---------|
| **Curiosity gap** | Raise question, delay answer |
| **Stakes** | Why should reader care? Real consequences |
| **Story structure** | Problem → attempt → resolution |
| **Emotional connection** | Patient cases, discovery narratives |

### Checks

- [ ] Opening creates curiosity gap (question raised, not immediately answered)
- [ ] Stakes established early (why should I care?)
- [ ] Narrative thread through technical content
- [ ] Tension/resolution structure within sections
- [ ] Emotional connection (patient cases, discovery stories)

### Red Flags

- Dry, encyclopedic presentation
- No clear "why should I care?"
- Questions answered immediately after being raised
- Pure information transfer without engagement

---

## 12. Transfer & Application

**Research basis:** Perkins, D. N., & Salomon, G. (1992). Transfer of learning. *International Encyclopedia of Education* (2nd ed.).

**Core insight:** Knowledge should apply beyond the learning context. Explicit attention to transfer conditions helps learners generalize appropriately.

### Implementation Patterns

| Pattern | Example |
|---------|---------|
| **Multiple contexts** | Same principle in DNA, RNA, protein |
| **Boundary conditions** | "This approach works when X, but fails when Y" |
| **Application scenario** | "In a clinical setting, you would..." |
| **Generalization** | "The broader principle here is..." |

### Checks

- [ ] Same principle shown in multiple contexts (near transfer)
- [ ] Explicit discussion of when approach works/doesn't work
- [ ] Application scenarios beyond training examples
- [ ] Connection to real-world decision making
- [ ] Generalization boundaries made explicit

### Red Flags

- Concepts presented only in single context
- No discussion of limitations or boundary conditions
- Abstract principles without application guidance
- No guidance on when to use/not use approach

---

## Quick Reference: Principle Application

| When You See... | Apply Principle... |
|-----------------|-------------------|
| Dense technical paragraph | Cognitive Load: chunk, add examples |
| Long explanation with no questions | Retrieval Practice: add prompts |
| Sequential topics never compared | Interleaving: add comparisons |
| Concept mentioned once, never again | Spacing: add reactivation |
| "What" without "why" | Elaboration: add mechanism |
| Abstract concept without grounding | Examples: add concrete case |
| Complex idea, text only | Dual Coding: add visual |
| New topic with no bridge | Prior Knowledge: add analogy |
| No clear learning goals | Metacognition: add objectives |
| Everything explained immediately | Desirable Difficulty: add prediction |
| Dry opening | Hooks: add curiosity gap |
| Single context only | Transfer: add multiple applications |
