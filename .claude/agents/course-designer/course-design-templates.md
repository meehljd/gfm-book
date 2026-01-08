# Course Design Templates

Detailed templates and examples for each course material type.

---

## Template 1: Full Semester Syllabus

### Example: BIOINF 565 - Genomic Foundation Models

```markdown
# BIOINF 565: Genomic Foundation Models
## Deep Learning for Biological Sequence Analysis

### Course Information
- **Semester**: Fall 2026
- **Credits**: 4 (3 lecture + 1 lab)
- **Meeting Time**: MWF 10:00-10:50 (lecture), Th 2:00-3:50 (lab)
- **Location**: [Building/Room]
- **Instructor**: [Name], [Email], [Office Hours]
- **TA**: [Name], [Email], [Office Hours]

### Course Description
This course provides a comprehensive introduction to foundation models for genomic data analysis. Students will learn the theoretical foundations of deep learning architectures (CNNs, transformers, state-space models) and their application to DNA, RNA, and protein sequences. Topics include sequence representation, pretraining strategies, model adaptation, variant effect prediction, and responsible deployment in clinical settings. Students will gain hands-on experience fine-tuning and applying genomic foundation models through weekly labs and a semester project.

### Prerequisites
- CS 229 (Machine Learning) or equivalent
- Basic biology/genetics (BIOL 101 or equivalent)
- Python programming proficiency
- Linear algebra and probability (recommended)

### Learning Objectives
By the end of this course, students will be able to:
1. **Explain** the design principles of foundation models for biological sequences
2. **Implement** sequence encoding, embedding, and tokenization strategies
3. **Compare** different model architectures (CNN, Transformer, SSM) for genomic tasks
4. **Fine-tune** pretrained models for specific downstream applications
5. **Evaluate** model performance using appropriate benchmarks and metrics
6. **Assess** limitations, biases, and responsible deployment considerations
7. **Apply** foundation models to real variant effect prediction problems

### Required Materials
**Primary Textbook**: Genomic Foundation Models (this book)

**Software Requirements**:
- Python 3.10+
- PyTorch 2.0+
- Hugging Face Transformers
- Jupyter notebooks
- Access to GPU compute (provided via course cluster)

**Recommended Reading**:
- Goodfellow et al., Deep Learning (2016) - Background
- Relevant papers assigned weekly

### Schedule

| Wk | Dates | Topic | Reading | Lab | Assignment |
|----|-------|-------|---------|-----|------------|
| 1 | 9/2-6 | Introduction: NGS & Variant Calling | Ch. 1 | Setup & Data | - |
| 2 | 9/9-13 | Genomic Datasets & Annotations | Ch. 2 | VCF Processing | PS1 out |
| 3 | 9/16-20 | GWAS & Polygenic Scores | Ch. 3 | GWAS Analysis | - |
| 4 | 9/23-27 | Classical Variant Effect Prediction | Ch. 4 | CADD/VEP | PS1 due, PS2 out |
| 5 | 9/30-10/4 | Sequence Representations | Ch. 5 | Tokenization | - |
| 6 | 10/7-11 | CNN Architectures for Genomics | Ch. 6 | DeepSEA Lab | PS2 due, PS3 out |
| 7 | 10/14-18 | Attention Mechanisms | Ch. 7 | Attention Viz | Project proposal due |
| 8 | 10/21-25 | **Midterm Exam** (10/23) | Ch. 1-7 | Review | PS3 due |
| 9 | 10/28-11/1 | Pretraining Strategies | Ch. 8 | MLM Training | PS4 out |
| 10 | 11/4-8 | Model Adaptation & Fine-tuning | Ch. 9-10 | Fine-tuning | - |
| 11 | 11/11-15 | Benchmarking & Evaluation | Ch. 11-12 | Benchmark Suite | PS4 due, PS5 out |
| 12 | 11/18-22 | DNA & Protein Language Models | Ch. 14-15 | PLM Embeddings | Project check-in |
| 13 | 11/25-29 | **Thanksgiving Break** | - | - | - |
| 14 | 12/2-6 | Regulatory & VEP Models | Ch. 16-17 | Enformer | PS5 due |
| 15 | 12/9-13 | Applications & Frontiers | Ch. 27-28 | Clinical VEP | Project due 12/13 |
| 16 | 12/16-20 | **Project Presentations** & **Final Exam** | - | - | - |

### Assessment

| Component | Weight | Description |
|-----------|--------|-------------|
| Problem Sets (5) | 25% | Weekly assignments, mix of written and coding |
| Midterm Exam | 20% | In-class, closed-book, Chapters 1-7 |
| Final Exam | 20% | Cumulative, emphasis on Chapters 8-17 |
| Labs | 15% | Weekly hands-on exercises, completion-based |
| Course Project | 20% | Team project applying FMs to genomic problem |

### Problem Sets
- Released Fridays, due following Friday 11:59 PM
- Two late days total for semester (no questions asked)
- Additional late submissions: 10% penalty per day
- Collaboration encouraged, but write-ups must be individual

### Project
- Teams of 2-3 students
- Proposal (Week 7): 1-page project plan
- Check-in (Week 12): Progress report and preliminary results
- Final submission (Week 15): Code, report (8-10 pages), and 10-min presentation

### Policies

**Academic Integrity**: All work must be your own. You may discuss concepts with classmates but must write your own solutions. Code must be original or properly attributed. Use of AI assistants (ChatGPT, Copilot) is permitted for debugging but not for generating solutions; document any AI use.

**Accessibility**: Students with disabilities should contact Disability Services to arrange accommodations. Please inform the instructor within the first two weeks.

**Attendance**: Lecture attendance expected but not graded. Lab attendance mandatory (one excused absence permitted).

**Communication**: Use Piazza for questions (instructors monitor daily). Email for personal matters only.
```

---

## Template 2: Lecture Notes

### Example: Lecture on Attention Mechanisms (Chapter 7)

```markdown
# Lecture 12: Attention Mechanisms in Genomics

## Pre-Class Materials
**Required Reading**: Chapter 7, Sections 7.1-7.3
**Pre-quiz** (due 9:00 AM): Canvas quiz on Q/K/V basics (5 min)

## Learning Objectives
By the end of this lecture, students will be able to:
1. Explain how self-attention computes relationships between sequence positions
2. Calculate attention weights given Q, K, V matrices
3. Describe how multi-head attention captures different relationship types
4. Compare attention patterns in genomic vs. natural language contexts

---

## Outline (75 minutes)

### Opening Hook (5 min)

**Slide**: Show attention heatmap from DNABERT on a promoter sequence

"Look at this visualization. The model has never been told about transcription factor binding sites, yet it's learned to attend to the TATA box and nearby regulatory elements. How does it know? That's what we'll understand today."

**Discussion prompt**: "What would you want a model to 'pay attention to' when analyzing a promoter sequence?"

---

### Review & Connection (5 min)

"Last lecture we saw how CNNs detect local patterns - motifs within their receptive field. But what if important relationships span hundreds or thousands of bases?"

**Quick recall**: "What limits how far a CNN can 'see'? [Receptive field size]"

"Today we'll see how attention removes this limitation entirely."

---

### Section 1: The Attention Intuition (15 min)

**Key concept**: Attention lets every position "look at" every other position, weighted by relevance.

#### Teaching sequence:

1. **Start with analogy** (3 min)
   - "Imagine you're reading a sentence and you encounter a pronoun 'it'. To understand 'it', you look back to find what it refers to - that's attention."
   - "In genomics: when you see a splice site, you might need to 'look at' distant regulatory elements to predict if it's used."

2. **Concrete example first** (5 min)
   - Board work: Simple 4-position DNA sequence
   - "Position 3 wants to know: 'who should I pay attention to?'"
   - Walk through intuitive scoring: "Position 1 has a similar context → high score"

3. **Formalize** (5 min)
   - Introduce Q, K, V with biological intuition
   - "Query = 'what am I looking for?'"
   - "Key = 'what do I have to offer?'"
   - "Value = 'what information should I pass along?'"

4. **Check understanding** (2 min)
   > Poll: "In the attention formula, what does the softmax ensure?"
   > A) Weights sum to 1  B) Weights are positive  C) Both A and B  D) Neither

---

### Section 2: Computing Self-Attention (15 min)

**Key concept**: Attention weights = softmax(QK^T / √d)

#### Teaching sequence:

1. **Worked example on board** (8 min)
   - 3-position sequence, d=4 embedding dimension
   - Show Q, K, V matrices (provide values)
   - Calculate QK^T step by step
   - Apply scaling and softmax
   - Multiply by V to get output

2. **Why the scaling factor?** (3 min)
   - "What happens as dimension grows?" → dot products grow, softmax saturates
   - "Dividing by √d keeps values in reasonable range"

3. **Complexity discussion** (2 min)
   - "What's the complexity of computing attention over length n?"
   - Build to O(n²) realization
   - "This is both attention's power AND its limitation"

4. **Check understanding** (2 min)
   > "If position i attends strongly to position j, what does that mean about their Q and K vectors?"
   > [They point in similar directions / high cosine similarity]

---

### Section 3: Multi-Head Attention (15 min)

**Key concept**: Multiple attention heads learn different types of relationships

#### Teaching sequence:

1. **Motivation** (3 min)
   - "One attention pattern isn't enough. You might want to attend to:
     - Nearby bases (local context)
     - Complementary strand (base pairing)
     - Upstream regulatory elements (long-range)"
   - "Different heads can specialize"

2. **Architecture** (5 min)
   - Show Figure 7.2 from book
   - Multiple parallel attention operations
   - Each head has its own Q, K, V projections
   - Concatenate and project outputs

3. **Genomic attention patterns** (5 min)
   - Show Figure 7.3: real learned patterns
   - "This head learned local context, this one learned base pairing"
   - "The model discovered biology from sequence alone"

4. **Check understanding** (2 min)
   > Discussion: "If you had 8 attention heads for genomic sequences, what different patterns might you hope they learn?"
   > [2-min pair discussion, then share-out]

---

### Live Demo: Visualizing Attention (10 min)

**Setup**: Jupyter notebook pre-loaded with DNABERT

```python
# Load model and tokenize a promoter sequence
from transformers import AutoModel, AutoTokenizer
model = AutoModel.from_pretrained("zhihan1996/DNABERT-6")
...

# Visualize attention from layer 6, head 3
# [Walk through code while running]
```

**Live exploration**:
- "Let's look at what head 3 in layer 6 attends to"
- "Notice how it focuses on [specific pattern]"
- "Now let's mutate a key position and see how attention changes"

**Key insight**: "The model's attention gives us interpretable views into what it thinks is important"

---

### Synthesis & Summary (5 min)

**Today's key insights**:
1. Attention lets every position consider every other position - no range limits
2. Q/K/V provides learnable relevance scoring
3. Multi-head attention captures diverse relationship types
4. Attention patterns reveal what models learn about sequence biology

**Connection to next lecture**:
"We've seen single attention layers. Next time: how to stack them into full transformers, and how to handle the O(n²) problem for genomic-scale sequences."

**Practical takeaway**:
"When you use a genomic foundation model, you can extract and visualize attention to understand its predictions."

---

### Questions & Buffer (5 min)

**Anticipated questions**:
- "How do we decide number of heads?" → Empirical, typically 8-16
- "Why not just use very large heads?" → Diversity matters more than size
- "How does this relate to kernel attention?" → Preview for efficient transformers lecture

---

## Post-Class

**Muddiest point** (due tonight): "What was the most confusing concept from today's lecture?"

**Assignment**: Problem Set 3, Questions 1-3 (attention calculations)

**Preparation for next lecture**: Read Chapter 7.4-7.6 on position encodings and full transformer blocks
```

---

## Template 3: Slide Deck Outline

### Example: DNA Language Models (Chapter 14)

```markdown
# DNA Language Models - Slide Deck

**Lecture**: 22 of 30
**Duration**: 75 minutes
**Slides**: ~45
**Key figures**: Fig 14.1 (timeline), Fig 14.2 (context revolution), Fig 14.3 (equivariance)

---

## Section 0: Opening (3 slides)

### Slide 1: Title
- BIOINF 565: Genomic Foundation Models
- Lecture 22: DNA Language Models
- [Date]

### Slide 2: Motivating Question
**Type**: Full-bleed image + question
- **Visual**: Side-by-side of text completion and DNA completion
- **Text**: "Can language modeling work on DNA?"
- **Speaker notes**: "GPT predicts the next word. What would it mean to predict the next nucleotide... or the next gene?"

### Slide 3: Today's Roadmap
- The DNA-LM revolution (what changed)
- Architecture innovations (how they work)
- What DNA-LMs learn (emergent capabilities)
- Current state and limitations (where we are)

---

## Section 1: The DNA-LM Revolution (10 slides)

### Slide 4: Before Foundation Models
**Type**: Timeline
- **Visual**: Fig 14.1 adapted - focus on 2016-2019 era
- **Text**: Task-specific models: DeepSEA, SpliceAI, etc.
- **Speaker notes**: "Each problem got its own model, trained from scratch on limited data"

### Slide 5: The Key Insight
**Type**: Quote + explanation
- **Quote**: "The genome is the 'language' of life"
- **Build**:
  1. Words → k-mers or nucleotides
  2. Grammar → sequence syntax and motifs
  3. Meaning → function encoded in sequence
- **Speaker notes**: "This analogy isn't perfect, but it's productive"

### Slide 6: What Changed in 2020-2023
**Type**: Three-column comparison
- **Pre-training data**: 1M → 1B+ sequences
- **Context length**: 1kb → 100kb+
- **Parameters**: 10M → 1B+
- **Speaker notes**: "Scale changed everything, just like in NLP"

### Slide 7: The Major Players
**Type**: Logo grid
- DNABERT family (Zhihan et al.)
- Nucleotide Transformer (InstaDeep)
- HyenaDNA (Nguyen et al.)
- Evo (Arc Institute)
- Caduceus (Schiff et al.)
- **Speaker notes**: Brief 1-sentence on each

### Slide 8: Long Context Revolution
**Type**: Figure
- **Visual**: Fig 14.2 - context length progression
- **Key point**: From promoters to whole genes to chromosomes
- **Speaker notes**: "The Hyena model can process 1M bp - that's an entire human chromosome"

### Slide 9: Why Long Context Matters (Biologically)
**Type**: Genome browser view
- **Visual**: Gene with distant enhancer
- **Annotations**: Gene body, enhancer 100kb away, CTCF sites
- **Speaker notes**: "Regulation happens at scales previous models couldn't see"

### Slide 10: Poll
**Type**: Interactive
- **Question**: "What's the hardest part of training on million-bp sequences?"
- A) Compute/memory
- B) Getting meaningful gradients
- C) Finding enough training data
- D) All of the above
- **Answer**: D, but we'll focus on A and how architectures solve it

---

## Section 2: Architecture Innovations (12 slides)

### Slide 11: The Quadratic Problem
**Type**: Graph
- **Visual**: Complexity plot - sequence length vs. memory/time
- **Highlight**: Standard attention is O(n²)
- **At 100kb**: "That's 10 billion attention scores - impossible"
- **Speaker notes**: "This is why we need new architectures"

### Slide 12: Solution 1: Efficient Attention
**Type**: Architecture diagram
- **Visual**: Sparse attention patterns
- **Examples**: Local windows, dilated, longformer-style
- **Trade-off**: Cheaper but loses some global context
- **Speaker notes**: "Nucleotide Transformer uses windowed attention"

### Slide 13: Solution 2: State Space Models
**Type**: Concept diagram
- **Visual**: Convolution-like but learnable
- **Key idea**: Linear scaling O(n)
- **Example**: HyenaDNA
- **Speaker notes**: "SSMs process sequence sequentially with fixed memory"

### Slide 14: HyenaDNA Architecture
**Type**: Architecture diagram
- **Visual**: Simplified Hyena operator block
- **Components**: Implicit convolutions, gating
- **Achievement**: 1M context, 300M parameters
- **Speaker notes**: Walk through data flow

### Slide 15: Solution 3: Mamba/S4 Evolution
**Type**: Architecture progression
- **Build**: S4 → Mamba → Evo
- **Key innovation**: Selective state spaces
- **Speaker notes**: "Mamba adds input-dependent dynamics"

### Slide 16: Evo Architecture
**Type**: Multi-panel figure
- **Visual**: Fig 14.4 adapted
- **Panel A**: Overall architecture
- **Panel B**: StripedHyena blocks
- **Panel C**: Training data (OpenGenome)
- **Speaker notes**: "Evo is currently the largest DNA-LM"

### Slide 17: A Unique Challenge: Reverse Complement
**Type**: DNA diagram
- **Visual**: Double helix with sequences labeled
- **Problem**: ACGT and ACGT-rc encode same biology
- **Question**: "How should models handle this?"
- **Speaker notes**: "This doesn't exist in NLP - DNA has strand symmetry"

### Slide 18: Caduceus: RC-Equivariance
**Type**: Figure
- **Visual**: Fig 14.3
- **Key idea**: Model gives same output regardless of strand
- **How**: Bidirectional Mamba with weight sharing
- **Speaker notes**: "This is an architectural inductive bias"

### Slide 19: Check Understanding
**Type**: Discussion
- **Question**: "Why can't we just augment training data with reverse complements?"
- **Pair**: 2 minutes discussion
- **Answer**: You can, but equivariance is more efficient and guaranteed

### Slide 20: Architecture Summary Table
**Type**: Comparison table
| Model | Architecture | Context | Parameters | RC-handling |
|-------|--------------|---------|------------|-------------|
| DNABERT-2 | Transformer | 4kb | 117M | Augmentation |
| NT | Transformer | 6kb | 2.5B | Augmentation |
| HyenaDNA | SSM | 1M | 300M | Augmentation |
| Evo | Hyena | 131k | 7B | Augmentation |
| Caduceus | BiMamba | 131k | 40M | Equivariant |

---

## Section 3: What DNA-LMs Learn (10 slides)

### Slide 21: Emergent Capabilities
**Type**: List with icons
- **Without supervision, DNA-LMs learn**:
  - Gene structure
  - Regulatory elements
  - Evolutionary conservation
  - Species-specific features
- **Speaker notes**: "These emerge from predicting the next nucleotide"

### Slide 22: Probing Experiments
**Type**: Figure
- **Visual**: Fig 14.5 - layer-wise probing
- **Concept**: Freeze model, train small classifier on embeddings
- **Insight**: Different layers capture different biology
- **Speaker notes**: "Early layers: local motifs. Later layers: functional elements"

### Slide 23: What Layer 3 Knows
**Type**: Sequence logo
- **Visual**: Motifs recovered from layer 3 attention
- **Examples**: TATA box, splice signals
- **Speaker notes**: "Model rediscovered known regulatory elements"

### Slide 24: What Layer 12 Knows
**Type**: Genomic tracks
- **Visual**: Correlation with epigenomic marks
- **Insight**: Higher layers integrate long-range context
- **Speaker notes**: "The model seems to understand chromatin state"

### Slide 25: Zero-Shot Capabilities
**Type**: Performance comparison
- **Task**: Variant effect prediction (no fine-tuning)
- **Comparison**: DNA-LM likelihood vs. CADD scores
- **Result**: Competitive performance with zero task-specific training
- **Speaker notes**: "The model already knows something about deleteriousness"

### Slide 26: Benchmark Performance
**Type**: Figure
- **Visual**: Fig 14.6 - benchmark results
- **Comparison**: Different models across tasks
- **Key finding**: Bigger isn't always better; architecture matters
- **Speaker notes**: Walk through specific comparisons

### Slide 27: Generative Capabilities
**Type**: Example
- **Visual**: Model-generated sequence vs. real
- **Application**: Generating regulatory elements
- **Caveat**: Generation ≠ guaranteed function
- **Speaker notes**: "Evo can generate plausible genes"

### Slide 28: Poll
**Type**: Interactive
- **Question**: "What would convince you a DNA-LM truly 'understands' genomics?"
- A) Good benchmark scores
- B) Useful embeddings for downstream tasks
- C) Generating functional sequences in the lab
- D) Something else (discuss)
- **Speaker notes**: "There's no right answer - this is active debate"

---

## Section 4: Limitations and Future (7 slides)

### Slide 29: Current Limitations
**Type**: Bulleted list
- Training data biases (human-centric)
- Evaluation gaps (benchmarks ≠ real utility)
- Computational requirements (inference cost)
- Interpretability challenges
- **Speaker notes**: "These aren't solved problems"

### Slide 30: The Data Distribution Problem
**Type**: Pie chart + globe
- **Training data**: Heavily human/model organism
- **Challenge**: Poor performance on underrepresented species
- **Implication**: "Universal" models aren't universal
- **Speaker notes**: Reference Chapter 11 on benchmarks

### Slide 31: Open Questions
**Type**: Question list
1. How much context is enough? (Is more always better?)
2. Should we use nucleotides, k-mers, or BPE tokens?
3. How to evaluate generative DNA models?
4. When will DNA-LMs surpass task-specific models?
- **Speaker notes**: "These are research frontiers"

### Slide 32: Looking Ahead
**Type**: Timeline (speculative)
- Near-term: Better benchmarks, clinical validation
- Medium-term: Multi-modal models (DNA + protein + expression)
- Long-term: Interpretable, controllable genome engineering
- **Speaker notes**: "This is moving fast"

---

## Section 5: Wrap-up (3 slides)

### Slide 33: Key Takeaways
**Type**: Numbered list
1. DNA-LMs apply language modeling to biological sequences
2. Long context requires architectural innovation (SSMs, efficient attention)
3. Reverse complement handling is a unique genomic challenge
4. Emergent capabilities are impressive but benchmarks have limitations
5. We're early - lots of open questions

### Slide 34: For Your Project
**Type**: Practical suggestions
- DNA-LM embeddings available via HuggingFace
- Consider: fine-tuning vs. probing vs. zero-shot
- Evo is powerful but compute-heavy; DNABERT-2 is accessible
- **Speaker notes**: "Happy to discuss project ideas in office hours"

### Slide 35: Next Lecture
- **Topic**: Protein Language Models (Chapter 15)
- **Reading**: Sections 15.1-15.4
- **Connection**: Same ideas, different alphabet and constraints

---

## Backup Slides (5 slides)

### Slide B1: Mathematical Details of Mamba
[Detailed equations for those who ask]

### Slide B2: Full HyenaDNA Architecture
[More detailed diagram]

### Slide B3: Training Curriculum
[How to train on long sequences progressively]

### Slide B4: Benchmark Details
[Full table from paper]

### Slide B5: Compute Requirements
[GPU hours, memory, estimated costs]
```

---

## Template 4: Problem Set

### Example: Problem Set 4 - Pretraining and Embeddings

```markdown
# Problem Set 4: Pretraining Strategies and Sequence Embeddings

**Course**: BIOINF 565 - Genomic Foundation Models
**Due**: Friday, November 8, 11:59 PM
**Total Points**: 100
**Estimated Time**: 5-6 hours

## Overview
This problem set covers pretraining objectives (Chapter 8), transfer learning (Chapter 9-10), and hands-on work with pretrained DNA language model embeddings.

## Submission Instructions
- Submit via Gradescope
- Written answers: PDF (LaTeX preferred, Word acceptable)
- Code: Submit `.py` files and Jupyter notebook
- Include your name and student ID on all documents

## Collaboration Policy
Discuss concepts with classmates, but write solutions independently. Document any collaboration in the header of your submission. AI assistants may be used for debugging only.

---

## Part A: Conceptual Questions (30 points)

### Question A.1 (10 points)
**Pretraining Objectives**

Consider two pretraining objectives for DNA sequences:
1. Masked Language Modeling (MLM): Predict masked nucleotides
2. Next Nucleotide Prediction (NNP): Predict the next nucleotide autoregressively

(a) [4 points] For each objective, explain what type of patterns the model learns. Give a specific biological example of something each objective would help the model learn.

(b) [3 points] One of these objectives produces bidirectional representations. Which one, and why does this matter for downstream tasks like variant effect prediction?

(c) [3 points] A colleague argues: "Since NNP is harder (no bidirectional context), it must produce better representations." Do you agree? Justify your answer.

---

### Question A.2 (10 points)
**Domain Alignment**

Figure 9.1 in the textbook shows the "domain alignment" challenge between pretraining and downstream tasks.

(a) [4 points] Explain the domain shift problem when using a DNA-LM pretrained on diverse species for a task focused on human regulatory regions.

(b) [3 points] Propose two strategies to mitigate this domain shift. For each, describe how it would be implemented and its trade-offs.

(c) [3 points] Under what circumstances would you expect domain shift to be minimal and fine-tuning to work well "out of the box"?

---

### Question A.3 (10 points)
**Masking Strategies**

Chapter 8.2 discusses different masking strategies for genomic MLM.

(a) [5 points] Compare single-nucleotide masking vs. span masking for a DNA-LM. What biological structures would each capture better?

(b) [5 points] Design a masking strategy specifically for learning splice site recognition. Describe:
   - What tokens to mask
   - What percentage to mask
   - Any curriculum or difficulty progression
   Justify your choices with reference to splice site biology.

---

## Part B: Implementation (40 points)

### Setup
```bash
# Clone the starter code
git clone https://github.com/bioinf565/ps4-starter.git
cd ps4-starter
pip install -r requirements.txt

# Download data
python download_data.py
```

### Question B.1 (15 points)
**Implementing Span Masking**

In `masking.py`, implement the `span_mask()` function that creates span-masked training examples.

```python
def span_mask(
    sequence: str,
    mask_prob: float = 0.15,
    max_span_length: int = 6
) -> Tuple[str, List[int], List[str]]:
    """
    Apply span masking to a DNA sequence.

    Args:
        sequence: DNA sequence string (e.g., "ACGTACGT...")
        mask_prob: Probability that each position starts a mask span
        max_span_length: Maximum length of each mask span

    Returns:
        masked_seq: Sequence with [MASK] tokens
        mask_positions: List of masked position indices
        mask_labels: Original nucleotides at masked positions

    Example:
        >>> span_mask("ACGTACGTAC", mask_prob=0.2, max_span_length=3)
        ('A[MASK][MASK]TACGTAC', [1, 2], ['C', 'G'])
    """
    # TODO: Your implementation here
    pass
```

**Requirements**:
- Span lengths should be sampled uniformly from [1, max_span_length]
- Spans should not overlap
- Edge cases: handle sequences shorter than max_span_length

**Tests**: Run `pytest tests/test_masking.py` to verify correctness.

**Grading**:
- Correct basic functionality: 8 points
- Handles edge cases: 4 points
- Code quality and comments: 3 points

---

### Question B.2 (25 points)
**Comparing Embedding Strategies**

Using the pretrained DNABERT-2 model, compare different strategies for obtaining sequence embeddings for a downstream classification task.

**Task**: Classify 1000-bp sequences as promoters vs. non-promoters.

**Data**: `data/promoter_dataset.csv` contains:
- 500 promoter sequences (label=1)
- 500 non-promoter sequences (label=0)

In `embeddings.py`, implement three embedding strategies:

```python
def get_cls_embedding(model, tokenizer, sequence: str) -> np.ndarray:
    """Return the [CLS] token embedding."""
    # TODO
    pass

def get_mean_embedding(model, tokenizer, sequence: str) -> np.ndarray:
    """Return mean of all token embeddings."""
    # TODO
    pass

def get_last_layer_mean(model, tokenizer, sequence: str, layer: int = -1) -> np.ndarray:
    """Return mean embedding from a specific layer."""
    # TODO
    pass
```

In `analysis.ipynb`:

(a) [10 points] Extract embeddings using all three strategies for all sequences. Train a simple classifier (logistic regression) on each embedding type and report:
- 5-fold cross-validation accuracy
- Training time
- Standard deviation across folds

Present results in a table.

(b) [8 points] Visualize embeddings using t-SNE or UMAP:
- Create one plot per embedding strategy
- Color points by label (promoter/non-promoter)
- Comment on the separation visible in each

(c) [7 points] Analysis questions (answer in your notebook):
1. Which embedding strategy performs best? Why do you think this is?
2. What do the visualization patterns tell you about what each embedding captures?
3. How would you expect these results to change with a harder classification task?

**Grading**:
- Correct implementations: 8 points
- Complete analysis: 10 points
- Quality of visualizations: 4 points
- Thoughtfulness of written analysis: 3 points

---

## Part C: Critical Analysis (30 points)

### Question C.1 (15 points)
**Paper Critique**

Read the following abstract from a (hypothetical) paper:

> "We introduce SuperGenome-LM, a 50-billion parameter DNA language model trained on 10 trillion base pairs. We show state-of-the-art performance on variant effect prediction, achieving 0.95 AUROC on ClinVar. Our model outperforms all existing methods, demonstrating that scale is all you need for genomic understanding."

(a) [5 points] Identify three methodological concerns with the evaluation described (hint: review Chapter 11 on benchmarks).

(b) [5 points] The authors used ClinVar as their test set. What specific issues might arise from this choice? How would you design a better evaluation?

(c) [5 points] The paper claims "scale is all you need." Based on what you've learned about DNA-LMs, what important factors beyond scale determine model quality?

---

### Question C.2 (15 points)
**Experimental Design**

You are designing a study to determine whether DNA-LM pretraining helps for predicting enhancer activity in a specific cell type (liver hepatocytes).

(a) [5 points] Design a controlled experiment comparing:
   - DNA-LM pretrained embeddings + fine-tuning
   - Training from scratch on your enhancer dataset

   Specify: model choices, training protocols, evaluation metrics, and what you would hold constant.

(b) [5 points] What confounders might make it difficult to draw conclusions? List at least three and explain how you would control for each.

(c) [5 points] Under what circumstances would you expect pretraining to help most? Least? Give biological and statistical reasoning.

---

## Submission Checklist

- [ ] Part A: Written answers in PDF (answers_A.pdf)
- [ ] Part B.1: masking.py with implementation
- [ ] Part B.2: embeddings.py with implementations
- [ ] Part B.2: analysis.ipynb with all outputs
- [ ] Part C: Written answers in PDF (answers_C.pdf)
- [ ] All code runs without errors
- [ ] Collaboration statement included

---

## Grading Rubric Summary

| Section | Points | Components |
|---------|--------|------------|
| A.1 | 10 | Conceptual understanding of pretraining |
| A.2 | 10 | Domain alignment reasoning |
| A.3 | 10 | Masking strategy design |
| B.1 | 15 | Span masking implementation |
| B.2 | 25 | Embedding comparison analysis |
| C.1 | 15 | Paper critique |
| C.2 | 15 | Experimental design |
| **Total** | **100** | |
```

---

## Template 5: Project Specification

### Example: Capstone Project Options

```markdown
# Course Project: Genomic Foundation Models in Practice

**Timeline**:
- Week 7: Proposal due (1 page)
- Week 12: Progress report due (2-3 pages)
- Week 15: Final submission (8-10 pages + code)
- Finals week: Presentation (10 min + 5 min Q&A)

**Team Size**: 2-3 students

---

## Project Options

### Option A: Fine-tuning for Variant Effect Prediction (Recommended)
**Difficulty**: Medium
**Skills**: PyTorch, HuggingFace, evaluation design

**Goal**: Fine-tune a pretrained DNA-LM for predicting the pathogenicity of missense variants.

**Dataset**: ClinVar pathogenic/benign variants + gnomAD common variants (provided)

**Requirements**:
1. Compare at least two pretrained models (e.g., DNABERT-2, Nucleotide Transformer)
2. Compare at least two fine-tuning strategies (e.g., full fine-tune, LoRA, linear probe)
3. Evaluate on held-out test set stratified by gene
4. Analyze performance by variant type, gene function, and population frequency

**Deliverables**:
- Fine-tuned models (uploaded to HuggingFace Hub)
- Evaluation report with statistical significance testing
- Analysis of what the models learned (attention visualization, embedding analysis)

**Success Criteria**:
- Models train successfully and achieve reasonable performance (>0.80 AUROC)
- Thoughtful comparison of approaches with clear conclusions
- Analysis goes beyond benchmark numbers

---

### Option B: DNA-LM Benchmark Suite
**Difficulty**: Medium-Hard
**Skills**: Software engineering, evaluation design, statistics

**Goal**: Create a comprehensive benchmark suite for evaluating DNA language models.

**Motivation**: Existing benchmarks are scattered and inconsistent. Build a unified framework.

**Requirements**:
1. Curate 5+ tasks spanning different biological questions:
   - Regulatory element prediction
   - Splice site prediction
   - Conservation prediction
   - Variant effect prediction
   - Species/tissue classification
2. Implement consistent evaluation protocols
3. Run at least 3 DNA-LMs through your benchmark
4. Analyze where models succeed and fail

**Deliverables**:
- Public benchmark suite with documentation
- Leaderboard with your baseline results
- Analysis paper discussing benchmark design choices

**Success Criteria**:
- Suite runs end-to-end on new models
- Clear documentation for community use
- Insightful analysis of model capabilities

---

### Option C: Long-Range Regulatory Modeling
**Difficulty**: Hard
**Skills**: Biology background, computational resources, experimental design

**Goal**: Investigate how well DNA-LMs capture long-range regulatory interactions.

**Biological Question**: Can DNA-LMs predict enhancer-promoter interactions?

**Requirements**:
1. Obtain Hi-C or similar 3D chromatin data for a cell type
2. Define positive pairs (interacting enhancer-promoter) and negatives
3. Test whether DNA-LM embeddings predict interactions
4. Compare against sequence-only baselines

**Deliverables**:
- Curated dataset of enhancer-promoter pairs
- Comprehensive comparison of models
- Analysis of what sequence features predict interaction

**Success Criteria**:
- Novel analysis not published elsewhere
- Clear biological insights
- Rigorous statistical methodology

---

### Option D: Generative Regulatory Elements
**Difficulty**: Hard
**Skills**: Generative modeling, wet-lab collaboration (optional)

**Goal**: Use DNA-LMs to generate novel regulatory sequences with desired properties.

**Approach**:
1. Train/fine-tune a generative DNA model
2. Condition generation on desired properties (cell-type specificity, strength)
3. Evaluate generated sequences computationally
4. (Bonus) Collaborate with wet lab to test top candidates

**Requirements**:
1. Generate sequences with controlled properties
2. Computational validation (motif analysis, in silico MPRA prediction)
3. Comparison against random/scrambled controls
4. Analysis of generation failure modes

**Deliverables**:
- Generative pipeline with documentation
- Generated sequence library with annotations
- Analysis report

**Success Criteria**:
- Generated sequences are distinguishable from random
- Clear methodology for controlling generation
- Honest assessment of limitations

---

### Option E: Open Project (Requires Approval)

Propose your own project applying genomic foundation models to a problem of interest.

**Proposal Requirements**:
- Clear research question
- Defined methodology
- Feasibility assessment (data, compute, time)
- Success criteria

**Submit proposal for approval by Week 6.**

---

## Evaluation Rubric

| Criterion | Excellent (A) | Good (B) | Adequate (C) | Poor (D/F) |
|-----------|---------------|----------|--------------|------------|
| **Technical Depth** (25%) | Novel methodology or significant implementation challenge solved elegantly | Solid implementation of standard methods with some extensions | Basic implementation with minimal extensions | Incomplete or incorrect implementation |
| **Rigor** (25%) | Comprehensive evaluation with appropriate controls and statistics | Good evaluation with minor gaps | Basic evaluation, some missing controls | Inadequate evaluation or flawed methodology |
| **Insight** (20%) | Meaningful new understanding of model capabilities or biology | Useful observations beyond benchmark numbers | Some analysis but limited depth | Only reports numbers without interpretation |
| **Communication** (15%) | Clear, well-organized report and presentation; figures aid understanding | Good writing and clear presentation | Understandable but some organization issues | Confusing, poorly organized |
| **Ambition & Creativity** (15%) | Tackles difficult problem or brings novel perspective | Solid work on substantial project | Meets minimum requirements | Minimal effort or too simple |

---

## Milestones

### Proposal (Week 7) - 5 points
One page covering:
- Team members
- Project option (A-E)
- Specific scope and goals
- Data sources
- Timeline with milestones
- Compute requirements

### Progress Report (Week 12) - 10 points
2-3 pages covering:
- Work completed so far
- Preliminary results (even if negative)
- Challenges encountered
- Revised timeline if needed
- Questions for instructors

### Final Submission (Week 15) - 70 points
- **Report** (8-10 pages, NeurIPS format): 50 points
  - Introduction and motivation
  - Methods
  - Results with figures and tables
  - Discussion and limitations
  - References
- **Code** (GitHub repository): 10 points
  - Reproducible with README
  - Clean code with comments
  - Requirements.txt or environment.yaml
- **Presentation** (10 min + Q&A): 10 points
  - Clear communication of project
  - Engaging visuals
  - Thoughtful Q&A responses

---

## Resources

**Compute**: Each team receives:
- 100 GPU hours on course cluster (A100)
- GCP credits available upon request

**Data**:
- Starter datasets on course server
- Links to public databases in course materials

**Support**:
- Office hours (prioritize project questions Weeks 10-15)
- Piazza project channel
- Peer feedback sessions in Week 13

**External Validation**:
- Top projects will be encouraged to submit to ML4Bio workshop
- Potential for co-authorship on course-related publications
```

---

## Template 6: Lab Exercise

### Example: Lab 8 - Fine-tuning DNA Language Models

```markdown
# Lab 8: Fine-tuning DNA Language Models

**Duration**: 2 hours
**Prerequisites**: Completed Labs 1-7, comfortable with PyTorch and HuggingFace
**Learning Goals**:
- Load and use pretrained DNA-LM from HuggingFace
- Implement fine-tuning for sequence classification
- Compare full fine-tuning vs. LoRA
- Visualize learned attention patterns

---

## Setup (10 min)

### Environment

```bash
# Activate course environment
conda activate bioinf565

# Verify GPU available
python -c "import torch; print(f'GPU: {torch.cuda.is_available()}')"

# Install additional requirements
pip install peft accelerate
```

### Data

```bash
# Download lab data
cd ~/labs/lab8
wget https://course-data.example.com/lab8_data.zip
unzip lab8_data.zip
```

**Dataset**: 2000 promoter/non-promoter sequences (1000 each)
- `train.csv`: 1600 sequences
- `val.csv`: 200 sequences
- `test.csv`: 200 sequences

### Verify Setup

```python
# Run this cell to verify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("zhihan1996/DNABERT-2-117M")
print("Setup complete!")
```

**Expected output**: "Setup complete!" with no errors

---

## Part 1: Loading Pretrained Model (20 min)

### Step 1.1: Explore the Model

```python
from transformers import AutoModel, AutoTokenizer, AutoConfig

model_name = "zhihan1996/DNABERT-2-117M"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

# Check tokenizer vocabulary
print(f"Vocab size: {tokenizer.vocab_size}")
print(f"Special tokens: {tokenizer.special_tokens_map}")

# Tokenize a sample sequence
sample_seq = "ATCGATCGATCGATCGATCG"
tokens = tokenizer(sample_seq, return_tensors="pt")
print(f"Input shape: {tokens['input_ids'].shape}")
print(f"Tokens: {tokenizer.convert_ids_to_tokens(tokens['input_ids'][0])}")
```

**Checkpoint**: What tokenization strategy does DNABERT-2 use? (k-mer vs BPE)

### Step 1.2: Load Model for Classification

```python
from transformers import AutoModelForSequenceClassification

# Load model with classification head
model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=2,  # Binary classification
    trust_remote_code=True
)

# Check model architecture
print(model)
print(f"\nTotal parameters: {sum(p.numel() for p in model.parameters()):,}")
print(f"Trainable parameters: {sum(p.numel() for p in model.parameters() if p.requires_grad):,}")
```

**Checkpoint**: How many parameters does the model have? How does this compare to models you've used before?

---

## Part 2: Preparing the Data (20 min)

### Step 2.1: Create Dataset Class

```python
import pandas as pd
from torch.utils.data import Dataset, DataLoader

class PromoterDataset(Dataset):
    def __init__(self, csv_path, tokenizer, max_length=512):
        self.data = pd.read_csv(csv_path)
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]

        # Tokenize sequence
        encoding = self.tokenizer(
            row['sequence'],
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        return {
            'input_ids': encoding['input_ids'].squeeze(),
            'attention_mask': encoding['attention_mask'].squeeze(),
            'labels': torch.tensor(row['label'])
        }

# Create datasets
train_dataset = PromoterDataset('data/train.csv', tokenizer)
val_dataset = PromoterDataset('data/val.csv', tokenizer)
test_dataset = PromoterDataset('data/test.csv', tokenizer)

print(f"Train: {len(train_dataset)}, Val: {len(val_dataset)}, Test: {len(test_dataset)}")
```

### Step 2.2: Create DataLoaders

```python
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=16)
test_loader = DataLoader(test_dataset, batch_size=16)

# Check a batch
batch = next(iter(train_loader))
print(f"Input shape: {batch['input_ids'].shape}")
print(f"Labels: {batch['labels']}")
```

**Checkpoint**: Why do we use `padding='max_length'`? What would happen if sequences had different lengths in a batch?

---

## Part 3: Full Fine-tuning (30 min)

### Step 3.1: Training Loop

```python
from transformers import AdamW, get_linear_schedule_with_warmup
from tqdm import tqdm
import numpy as np
from sklearn.metrics import accuracy_score, roc_auc_score

def train_epoch(model, loader, optimizer, scheduler, device):
    model.train()
    total_loss = 0

    for batch in tqdm(loader, desc="Training"):
        optimizer.zero_grad()

        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)

        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=labels
        )

        loss = outputs.loss
        total_loss += loss.item()

        loss.backward()
        optimizer.step()
        scheduler.step()

    return total_loss / len(loader)

def evaluate(model, loader, device):
    model.eval()
    all_preds = []
    all_labels = []
    all_probs = []

    with torch.no_grad():
        for batch in loader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels']

            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            probs = torch.softmax(outputs.logits, dim=1)[:, 1].cpu().numpy()
            preds = outputs.logits.argmax(dim=1).cpu().numpy()

            all_probs.extend(probs)
            all_preds.extend(preds)
            all_labels.extend(labels.numpy())

    return {
        'accuracy': accuracy_score(all_labels, all_preds),
        'auroc': roc_auc_score(all_labels, all_probs)
    }
```

### Step 3.2: Train the Model

```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Optimizer and scheduler
optimizer = AdamW(model.parameters(), lr=2e-5, weight_decay=0.01)
num_epochs = 3
num_training_steps = num_epochs * len(train_loader)
scheduler = get_linear_schedule_with_warmup(
    optimizer,
    num_warmup_steps=100,
    num_training_steps=num_training_steps
)

# Training loop
full_ft_results = []
for epoch in range(num_epochs):
    train_loss = train_epoch(model, train_loader, optimizer, scheduler, device)
    val_metrics = evaluate(model, val_loader, device)

    print(f"Epoch {epoch+1}: Loss={train_loss:.4f}, Val Acc={val_metrics['accuracy']:.4f}, Val AUROC={val_metrics['auroc']:.4f}")
    full_ft_results.append(val_metrics)

# Final test evaluation
test_metrics = evaluate(model, test_loader, device)
print(f"\nTest Results: Acc={test_metrics['accuracy']:.4f}, AUROC={test_metrics['auroc']:.4f}")
```

**Checkpoint**: How long did training take? What final accuracy did you achieve?

---

## Part 4: LoRA Fine-tuning (30 min)

### Step 4.1: Set Up LoRA

```python
from peft import LoraConfig, get_peft_model, TaskType

# Reload fresh model
model_lora = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=2,
    trust_remote_code=True
)

# Configure LoRA
lora_config = LoraConfig(
    task_type=TaskType.SEQ_CLS,
    r=8,  # Rank
    lora_alpha=32,
    lora_dropout=0.1,
    target_modules=["query", "value"]  # Which layers to adapt
)

# Apply LoRA
model_lora = get_peft_model(model_lora, lora_config)
model_lora.print_trainable_parameters()
```

**Checkpoint**: What percentage of parameters are now trainable? How does this compare to full fine-tuning?

### Step 4.2: Train with LoRA

```python
model_lora.to(device)

# Use higher learning rate for LoRA
optimizer_lora = AdamW(model_lora.parameters(), lr=1e-4, weight_decay=0.01)
scheduler_lora = get_linear_schedule_with_warmup(
    optimizer_lora,
    num_warmup_steps=100,
    num_training_steps=num_training_steps
)

# Train
lora_results = []
for epoch in range(num_epochs):
    train_loss = train_epoch(model_lora, train_loader, optimizer_lora, scheduler_lora, device)
    val_metrics = evaluate(model_lora, val_loader, device)

    print(f"Epoch {epoch+1}: Loss={train_loss:.4f}, Val Acc={val_metrics['accuracy']:.4f}, Val AUROC={val_metrics['auroc']:.4f}")
    lora_results.append(val_metrics)

# Test
test_metrics_lora = evaluate(model_lora, test_loader, device)
print(f"\nLoRA Test Results: Acc={test_metrics_lora['accuracy']:.4f}, AUROC={test_metrics_lora['auroc']:.4f}")
```

### Step 4.3: Compare Results

```python
import matplotlib.pyplot as plt

# Create comparison plot
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Accuracy over epochs
epochs = range(1, num_epochs + 1)
axes[0].plot(epochs, [r['accuracy'] for r in full_ft_results], 'b-o', label='Full Fine-tune')
axes[0].plot(epochs, [r['accuracy'] for r in lora_results], 'r-o', label='LoRA')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Validation Accuracy')
axes[0].legend()
axes[0].set_title('Training Progress')

# Final comparison
methods = ['Full FT', 'LoRA']
test_accs = [test_metrics['accuracy'], test_metrics_lora['accuracy']]
axes[1].bar(methods, test_accs)
axes[1].set_ylabel('Test Accuracy')
axes[1].set_title('Final Test Performance')
axes[1].set_ylim(0.5, 1.0)

plt.tight_layout()
plt.savefig('comparison.png')
plt.show()
```

**Discussion Question**: LoRA uses ~1% of the trainable parameters. Did it achieve similar performance? When might you prefer one approach over the other?

---

## Part 5: Attention Visualization (20 min)

### Step 5.1: Extract Attention Weights

```python
def get_attention_weights(model, tokenizer, sequence, device):
    """Extract attention weights from all layers and heads."""
    inputs = tokenizer(sequence, return_tensors='pt').to(device)

    with torch.no_grad():
        outputs = model.bert(
            inputs['input_ids'],
            attention_mask=inputs['attention_mask'],
            output_attentions=True
        )

    # Shape: (num_layers, num_heads, seq_len, seq_len)
    attention = torch.stack(outputs.attentions).squeeze(1)
    return attention.cpu().numpy(), tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])

# Get attention for a promoter sequence
test_seq = test_dataset[0]['sequence'] if hasattr(test_dataset[0], 'sequence') else "ATCGATCGATCGATCGATCG"
attention, tokens = get_attention_weights(model, tokenizer, test_seq[:200], device)
print(f"Attention shape: {attention.shape}")
```

### Step 5.2: Visualize Attention Patterns

```python
import seaborn as sns

def plot_attention(attention, tokens, layer, head, save_path=None):
    """Plot attention heatmap for a specific layer and head."""
    fig, ax = plt.subplots(figsize=(10, 8))

    attn = attention[layer, head, :len(tokens), :len(tokens)]

    sns.heatmap(
        attn,
        xticklabels=tokens,
        yticklabels=tokens,
        cmap='viridis',
        ax=ax
    )

    ax.set_title(f'Layer {layer}, Head {head}')
    ax.set_xlabel('Key Position')
    ax.set_ylabel('Query Position')

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

# Visualize different layers
plot_attention(attention, tokens[:30], layer=0, head=0, save_path='attention_L0H0.png')
plot_attention(attention, tokens[:30], layer=5, head=0, save_path='attention_L5H0.png')
plot_attention(attention, tokens[:30], layer=11, head=0, save_path='attention_L11H0.png')
```

**Your Turn**: Experiment with different layers and heads. Document 2-3 interesting patterns you observe.

---

## Wrap-up

### Key Takeaways
1. Pretrained DNA-LMs can be fine-tuned for downstream tasks with minimal code
2. LoRA provides an efficient alternative to full fine-tuning
3. Attention patterns reveal what the model "looks at" when making predictions

### Common Issues
- **CUDA out of memory**: Reduce batch size or sequence length
- **Model not loading**: Ensure `trust_remote_code=True`
- **Poor performance**: Check learning rate, try longer training

### Going Further
- Try other pretrained models (Nucleotide Transformer, HyenaDNA)
- Experiment with different LoRA ranks
- Apply to your project dataset

### Submission
Upload to Gradescope:
- `lab8_notebook.ipynb` with all cells executed
- `comparison.png`
- Attention visualizations (3 images)
- Brief answers to checkpoint and discussion questions
```

---

This templates file provides detailed examples that the course designer agent can reference and adapt when generating course materials.
