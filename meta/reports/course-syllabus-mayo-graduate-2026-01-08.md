# BIOM 7650: Genomic Foundation Models for Translational Research

## AI Methods for Variant Interpretation and Precision Medicine

---

## Course Information

| | |
|---|---|
| **Credits** | 3 (2 lecture + 1 lab) |
| **Semester** | Fall 2026 |
| **Meeting Times** | Lecture: Tu/Th 1:00-1:50 PM; Lab: Fri 2:00-3:50 PM |
| **Location** | Stabile Building, Room 2-42 / Computational Lab |
| **Prerequisites** | Graduate standing in biomedical sciences; basic familiarity with Python helpful but not required |
| **AI Minor** | Counts toward Mayo AI Minor elective requirement |

### Instructors

| Role | Name | Email | Office Hours |
|------|------|-------|--------------|
| Instructor | [Name] | [email] | Thu 2-3 PM or by appointment |
| Co-Instructor | [Name] | [email] | Wed 10-11 AM |
| TA | [Name] | [email] | Fri 4-5 PM (Lab help) |

---

## Course Description

This course introduces clinician-scientists and biomedical researchers to foundation models—large-scale AI systems pretrained on biological sequences—and their applications in variant interpretation, disease risk prediction, and precision medicine. Unlike traditional ML courses, we assume strong biological intuition and focus on building computational literacy in service of translational research questions.

Students will learn to critically evaluate AI methods for genomic analysis, understand when and how to apply pretrained models to their research, and gain hands-on experience with tools used in clinical genomics pipelines. The course emphasizes interpretation and clinical deployment considerations rather than model development from scratch.

**Target Audience**: M.D.-Ph.D. students, biomedical Ph.D. students, clinical fellows, and researchers seeking to integrate AI methods into genomics research. Students should be comfortable with basic genetics/genomics concepts but need not have prior programming or machine learning experience.

---

## Learning Objectives

By the end of this course, students will be able to:

### Conceptual Understanding
1. **Explain** how foundation models learn patterns from biological sequences without explicit labels
2. **Compare** different AI architectures (CNNs, transformers, state-space models) and their trade-offs for genomic applications
3. **Evaluate** the evidence supporting AI-based variant effect predictions in clinical contexts
4. **Identify** limitations, biases, and failure modes of genomic AI tools

### Practical Skills
5. **Use** pretrained genomic models via Python APIs and web interfaces
6. **Interpret** model outputs including variant scores, confidence estimates, and attention patterns
7. **Design** appropriate validation strategies for AI tools in research workflows
8. **Critically appraise** papers using genomic foundation models

### Clinical Translation
9. **Assess** when AI predictions are appropriate for clinical decision support
10. **Navigate** regulatory and ethical considerations for AI in genomic medicine
11. **Communicate** AI-derived insights to clinical colleagues and patients

---

## Course Philosophy

### What This Course Is
- A bridge from your biological expertise to AI fluency
- Focused on using and evaluating models, not building them from scratch
- Grounded in clinical and translational applications
- Heavy on interpretation and critical thinking

### What This Course Is Not
- A computer science course (we won't derive backpropagation)
- A statistics course (though we'll discuss key concepts)
- A software engineering course (code will be scaffolded)
- A comprehensive ML survey (we focus on genomics applications)

### Pedagogical Approach
- **Biology first**: Every AI concept connected to familiar biological examples
- **Scaffolded coding**: Labs provide substantial starter code; you fill in key pieces
- **Clinical cases**: Real variant interpretation scenarios throughout
- **Peer learning**: You'll teach each other—clinical insights are as valuable as computational ones

---

## Required Materials

### Textbook
**Genomic Foundation Models** (this book) - Available free online

### Software (all free, installed in lab computers)
- Python 3.10+ via Anaconda
- Google Colab (GPU access for labs)
- Hugging Face account (for model access)
- ClinVar/gnomAD web interfaces

### Recommended Background Reading
For those wanting to strengthen fundamentals before the course:
- *Python for Biologists* by Martin Jones (Chapters 1-4)
- 3Blue1Brown "Neural Networks" YouTube series (4 videos, ~1 hour total)
- StatQuest "Machine Learning" playlist (first 5 videos)

---

## Schedule Overview

| Unit | Weeks | Theme | Key Question |
|------|-------|-------|--------------|
| **0** | 1 | Foundations | What do I need to know to learn AI? |
| **1** | 2-4 | Genomic Data & Classical Methods | How have we predicted variant effects without AI? |
| **2** | 5-8 | Deep Learning Fundamentals | How do neural networks learn from sequences? |
| **3** | 9-12 | Foundation Models | What can large pretrained models do? |
| **4** | 13-15 | Clinical Translation | How do we responsibly use AI in the clinic? |
| **5** | 16 | Synthesis | Where is the field going? |

---

## Detailed Schedule

### Unit 0: Computational Foundations (Week 1)

#### Week 1: Getting Started

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | Course overview; Why AI for genomics? | Preface, Ch. 1.1 | Introductions; clinical scenarios discussion |
| Thu | Python crash course for biologists | [Online tutorial] | Live coding demo |
| Fri Lab | **Lab 0**: Setting up your environment | - | Install software, run first notebook |

**Learning Goals**:
- Articulate why AI methods matter for your research
- Navigate Jupyter notebooks and run provided code
- Access course materials and submit assignments

**No prior programming required** - Lab 0 starts from scratch

---

### Unit 1: Genomic Data & Classical Methods (Weeks 2-4)

*Leverage your biological knowledge to understand the problem space before introducing AI*

#### Week 2: The Variant Interpretation Problem

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | From sequencing to variants: the data pipeline | Ch. 1.1-1.3 | Case: Interpreting a WES report |
| Thu | Variant types and their clinical significance | Ch. 1.4-1.5 | ClinVar exploration exercise |
| Fri Lab | **Lab 1**: Exploring VCF files and ClinVar | - | Hands-on with real variant data |

**Clinical Connection**: You've seen VUS reports—now understand where they come from

#### Week 3: Genomic Datasets and Population Genetics

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | Reference genomes and population databases | Ch. 2.1-2.3 | gnomAD walkthrough |
| Thu | Ancestry, representation, and bias | Ch. 2.4-2.5 | Discussion: Whose genomes train our models? |
| Fri Lab | **Lab 2**: Population frequency analysis | - | Filtering variants by frequency |

**Clinical Connection**: Why does ancestry matter for variant interpretation?

#### Week 4: Classical Variant Effect Prediction

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | Conservation scores: GERP, PhyloP, SIFT, PolyPhen | Ch. 4.1-4.3 | Hands-on: Scoring variants |
| Thu | Ensemble methods: CADD, REVEL; ACMG/AMP guidelines | Ch. 4.4-4.6 | Case: Applying ACMG criteria |
| Fri Lab | **Lab 3**: Building a variant prioritization pipeline | - | End-to-end annotation workflow |

**Clinical Connection**: These are the tools in your current clinical pipelines

**Assignment 1 Due**: Variant interpretation case report (clinical reasoning + computational annotation)

---

### Unit 2: Deep Learning Fundamentals (Weeks 5-8)

*Build intuition for how neural networks learn, without requiring calculus*

#### Week 5: What is Machine Learning?

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | Supervised learning: the core idea | Ch. 5.1-5.2 | Interactive: Training a simple classifier |
| Thu | Features, embeddings, and representations | Ch. 5.3-5.4 | Visualizing sequence embeddings |
| Fri Lab | **Lab 4**: Training your first classifier | - | Logistic regression on variant features |

**Key Insight**: ML finds patterns in data—we'll see how this extends to sequences

#### Week 6: Neural Networks for Sequences

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | From features to learned representations | Ch. 6.1-6.2 | Intuition building: What do layers do? |
| Thu | Convolutional networks: learning motifs | Ch. 6.3-6.4 | Visualizing learned DNA motifs |
| Fri Lab | **Lab 5**: DeepSEA walkthrough | - | Predicting chromatin marks |

**Biological Intuition**: CNNs are like position weight matrices that learn themselves

#### Week 7: Attention and Transformers

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | The attention mechanism: letting positions "talk" | Ch. 7.1-7.3 | Step-by-step attention calculation |
| Thu | Transformers: attention at scale | Ch. 7.4-7.6 | Visualizing attention patterns |
| Fri Lab | **Lab 6**: Attention visualization in genomic models | - | What does the model "look at"? |

**Key Insight**: Attention captures long-range dependencies—like enhancer-promoter interactions

#### Week 8: Training and Evaluation

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | How models learn: loss functions and optimization | Ch. 8.1-8.3 | Interactive training visualization |
| Thu | Evaluation: metrics, overfitting, and generalization | Ch. 11.1-11.4 | Case: When benchmarks mislead |
| Fri Lab | **Lab 7**: Training and evaluating a splice predictor | - | End-to-end model development |

**Midterm Exam**: Take-home, open-book (covers Units 0-2)

---

### Unit 3: Foundation Models (Weeks 9-12)

*The core content: understanding and using pretrained genomic models*

#### Week 9: The Foundation Model Paradigm

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | Pretraining: learning from unlabeled sequences | Ch. 8.4-8.6, Ch. 13.1-13.2 | Discussion: What can be learned without labels? |
| Thu | Transfer learning: from pretraining to your task | Ch. 9, Ch. 10.1-10.2 | When does transfer work? |
| Fri Lab | **Lab 8**: Using pretrained embeddings | - | Extract embeddings, train classifier |

**Key Insight**: Foundation models learn "genomic grammar" that transfers to many tasks

#### Week 10: DNA Language Models

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | DNABERT, Nucleotide Transformer, HyenaDNA | Ch. 14.1-14.4 | Model comparison exercise |
| Thu | What do DNA-LMs learn? Probing experiments | Ch. 14.5-14.6 | Paper discussion |
| Fri Lab | **Lab 9**: Fine-tuning DNABERT for promoter prediction | - | Hands-on fine-tuning |

**Clinical Connection**: These models power next-generation variant predictors

#### Week 11: Protein Language Models

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | ESM-2: learning protein structure from sequence | Ch. 15.1-15.3 | AlphaFold vs ESMFold comparison |
| Thu | Variant effect prediction with protein LMs | Ch. 15.4-15.5 | Scoring missense variants |
| Fri Lab | **Lab 10**: Predicting variant effects with ESM | - | Zero-shot variant scoring |

**Clinical Connection**: Protein LMs inform missense interpretation in the clinic

#### Week 12: Variant Effect Prediction with Foundation Models

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | AlphaMissense and modern VEP tools | Ch. 17.1-17.3 | Benchmarking VEP tools |
| Thu | Regulatory variant prediction: Enformer and beyond | Ch. 16, Ch. 17.4-17.5 | Non-coding variant interpretation |
| Fri Lab | **Lab 11**: Building a foundation model VEP pipeline | - | Multi-model variant scoring |

**Assignment 2 Due**: Foundation model comparison report (benchmark a model on your variants of interest)

---

### Unit 4: Clinical Translation (Weeks 13-15)

*The unique considerations for deploying AI in clinical genomics*

#### Week 13: Uncertainty and Calibration

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | Why uncertainty matters: the VUS problem | Ch. 23.1-23.3 | Case: Communicating uncertainty |
| Thu | Calibration: when 90% confident should mean 90% correct | Ch. 23.4-23.6 | Calibration analysis exercise |
| Fri Lab | **Lab 12**: Evaluating prediction confidence | - | Calibration curves and selective prediction |

**Clinical Connection**: How confident should you be in an AI prediction?

#### Week 14: Bias, Fairness, and Interpretability

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | Population bias in genomic AI | Ch. 11.5, Ch. 12 | Discussion: AI equity in precision medicine |
| Thu | Interpretability: understanding model decisions | Ch. 24.1-24.4 | Attention visualization, in-silico mutagenesis |
| Fri Lab | **Lab 13**: Interpreting model predictions | - | Why did the model predict pathogenic? |

**Clinical Connection**: Can you explain an AI prediction to a patient?

#### Week 15: Regulatory and Ethical Considerations

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | FDA regulation of AI/ML in diagnostics | Ch. 26.1-26.3 | Case: SaMD regulatory pathway |
| Thu | Ethical frameworks for genomic AI | Ch. 26.4-26.5 | Panel discussion: AI governance |
| Fri Lab | **Project work session** | - | Final project completion |

**Guest Lecture** (Thu): FDA reviewer or industry regulatory expert (TBC)

---

### Unit 5: Synthesis (Week 16)

#### Week 16: Future Directions and Project Presentations

| Day | Topic | Reading | Activities |
|-----|-------|---------|------------|
| Tue | The frontier: multi-modal models, agentic systems | Ch. 31 | Discussion: Where is genomic AI going? |
| Thu | **Project Presentations** (Part 1) | - | 10-min presentations |
| Fri | **Project Presentations** (Part 2) | - | 10-min presentations |

**Final Exam**: Take-home, comprehensive (due end of finals week)

---

## Assessment

| Component | Weight | Description |
|-----------|--------|-------------|
| Lab Completion | 20% | Weekly labs, completion-based (13 labs, drop lowest) |
| Assignments | 25% | Two written assignments with computational components |
| Midterm Exam | 15% | Take-home, open-book, Units 0-2 |
| Final Exam | 15% | Take-home, comprehensive |
| Final Project | 25% | Applied project with presentation |

### Grading Scale

| Grade | Percentage | Description |
|-------|------------|-------------|
| A | 90-100% | Exceptional mastery |
| B | 80-89% | Solid understanding |
| C | 70-79% | Adequate, room for growth |
| F | <70% | Insufficient |

Mayo Graduate School does not use +/- grades.

---

## Assignments

### Assignment 1: Variant Interpretation Case Report (Week 4)
**Weight**: 12.5%

You will receive a clinical case with a set of variants identified by WES. Your task:
1. Annotate variants using classical tools (gnomAD, ClinVar, CADD)
2. Apply ACMG/AMP criteria to classify variants
3. Write a 3-page clinical interpretation report
4. Reflect on limitations of current methods

**Scaffolding provided**: Template report, annotation pipeline code

### Assignment 2: Foundation Model Comparison (Week 12)
**Weight**: 12.5%

Compare at least two foundation model-based VEP tools on a variant set relevant to your research:
1. Select variants (from your research or provided dataset)
2. Run multiple VEP tools (AlphaMissense, ESM, CADD, etc.)
3. Compare predictions and analyze disagreements
4. Write a 4-page analysis with recommendations

**Scaffolding provided**: Variant sets, API code, analysis template

---

## Final Project

### Overview
Apply foundation models to a question relevant to your research or clinical interests. Projects should demonstrate ability to use pretrained models, interpret results, and critically evaluate limitations.

### Timeline
- **Week 9**: Submit 1-page proposal
- **Week 12**: Progress check-in (in lab)
- **Week 15**: Final submission (report + code)
- **Week 16**: Presentation (10 min + 5 min Q&A)

### Suggested Project Types

#### Type A: Clinical Variant Set Analysis
Apply VEP tools to a disease-relevant variant set:
- Variants from a disease cohort you're studying
- Gene panel variants for a specific condition
- Reanalysis of "unsolved" cases

#### Type B: Method Benchmarking
Systematic evaluation of AI tools for a specific application:
- Compare VEP tools on a specific gene family
- Evaluate ancestry bias in prediction tools
- Assess calibration of confidence scores

#### Type C: Tool Development
Build a user-friendly interface or pipeline (with significant scaffolding):
- Streamlit app for variant interpretation
- Automated report generation pipeline
- Integration of multiple tools

#### Type D: Critical Review
Systematic analysis of a published study using genomic AI:
- Reproduce key results
- Identify limitations not discussed
- Propose improvements

### Evaluation Rubric

| Criterion | Weight | Excellent | Adequate | Insufficient |
|-----------|--------|-----------|----------|--------------|
| Biological/Clinical Relevance | 25% | Clear translational significance | Some relevance | Unclear motivation |
| Technical Execution | 25% | Correct, complete analysis | Minor issues | Major errors |
| Critical Thinking | 25% | Insightful limitations discussion | Basic awareness | Naive acceptance |
| Communication | 25% | Clear, well-organized | Understandable | Confusing |

---

## Lab Structure

Labs are designed for students with limited programming experience. Each lab includes:

### Components
1. **Pre-lab reading** (15 min): Conceptual preparation
2. **Guided walkthrough** (45 min): Step-by-step with explanations
3. **Your turn exercises** (30 min): Fill-in-the-blank coding
4. **Challenge problems** (optional): For those who want more

### Support
- TA available throughout lab sessions
- Peer programming encouraged
- Drop-in office hours Friday 4-5 PM
- Piazza for asynchronous questions

### Completion Criteria
Labs are graded completion-based. To receive credit:
- Attend lab session (or complete makeup within 1 week)
- Complete all required exercises
- Submit notebook with outputs

---

## Policies

### Attendance
- **Lecture**: Expected but not graded; recordings available
- **Lab**: Mandatory; one excused absence allowed; makeup within 1 week

### Late Work
- **Labs**: Due by end of Friday of the following week (no penalty)
- **Assignments**: 10% per day late, maximum 3 days
- **Exams**: No extensions except for documented emergencies
- **Project**: No late submissions (presentation scheduled)

### Collaboration
- **Labs**: Encouraged; work together, learn from peers
- **Assignments**: Discuss concepts, but write independently
- **Exams**: Individual work only
- **Project**: Teams of 1-2 allowed

### AI Tool Use
You may use AI assistants (ChatGPT, GitHub Copilot) with the following requirements:
1. **Document all AI use** in a statement with your submission
2. AI may help with: debugging code, explaining concepts, brainstorming
3. AI may NOT: write your analysis, generate your conclusions, complete assignments
4. **You are responsible** for correctness of all submitted work

Undocumented AI use that generates substantial portions of an assignment constitutes academic misconduct.

### Academic Integrity
Mayo Graduate School academic integrity policies apply. Violations will be reported to the Academic Standards Committee.

### Accessibility
Students requiring accommodations should contact the Office of Student Affairs. Accommodations will be arranged confidentially.

---

## Resources

### Computing
- Lab computers with GPU access available
- Google Colab provides free GPU for notebooks
- Mayo HPC available for larger projects (request access)

### Help
- **Piazza**: Monitored daily by TAs and instructors
- **Office Hours**: See schedule above
- **Peer Tutoring**: Connect with classmates via Piazza

### Background Resources
If you're struggling, these resources can help:

**Python Basics**:
- Codecademy Python course (free tier)
- *Python for Biologists* textbook

**Machine Learning Concepts**:
- 3Blue1Brown YouTube: Neural Networks series
- StatQuest YouTube: ML playlist
- Google's ML Crash Course

**Genomics Refresher**:
- NHGRI Genomics Education resources
- ClinGen learning materials

---

## Frequently Asked Questions

**Q: I've never programmed before. Can I succeed in this course?**
A: Yes! The course is designed for this. Labs provide substantial scaffolding, and we focus on using and understanding models rather than building them from scratch. Plan to spend extra time in the first few weeks getting comfortable with Python.

**Q: I'm already comfortable with Python/ML. Will this be too basic?**
A: The early weeks may be review, but the foundation model content (weeks 9-15) will be new to most students. Consider the early labs as an opportunity to help classmates while solidifying your own understanding.

**Q: How much time should I expect to spend?**
A: Plan for 8-10 hours/week total:
- Lectures: 2 hours
- Lab: 2 hours
- Reading: 1-2 hours
- Assignments/studying: 3-4 hours

**Q: Can I use my own research data for assignments/projects?**
A: Absolutely—this is encouraged! Using your own data makes the course directly relevant to your work. Talk to the instructor about data handling if you have PHI considerations.

**Q: Do I need my own computer?**
A: You can complete all work on lab computers or Google Colab. A personal laptop is convenient but not required.

**Q: How does this course relate to the AI Minor?**
A: This course counts as an elective for the Mayo AI Minor. It pairs well with the minor's core courses in AI fundamentals.

---

## Schedule At-a-Glance

| Week | Dates | Topic | Due |
|------|-------|-------|-----|
| 1 | Aug 26-30 | Course intro, Python basics | - |
| 2 | Sep 2-6 | Variant interpretation problem | - |
| 3 | Sep 9-13 | Genomic datasets, populations | - |
| 4 | Sep 16-20 | Classical VEP | **Assignment 1** |
| 5 | Sep 23-27 | Machine learning basics | - |
| 6 | Sep 30-Oct 4 | Neural networks for sequences | - |
| 7 | Oct 7-11 | Attention and transformers | - |
| 8 | Oct 14-18 | Training and evaluation | **Midterm** |
| 9 | Oct 21-25 | Foundation model paradigm | Project proposal |
| 10 | Oct 28-Nov 1 | DNA language models | - |
| 11 | Nov 4-8 | Protein language models | - |
| 12 | Nov 11-15 | VEP with foundation models | **Assignment 2** |
| 13 | Nov 18-22 | Uncertainty and calibration | - |
| 14 | Nov 25-29 | *Thanksgiving - No class Thu/Fri* | - |
| 15 | Dec 2-6 | Bias, fairness, regulation | **Project due** |
| 16 | Dec 9-13 | Presentations, synthesis | **Presentations** |
| Finals | Dec 16-20 | - | **Final exam** |

---

## Version History

| Date | Changes |
|------|---------|
| 2026-01-08 | Initial syllabus created |

---

*This syllabus is subject to change. Students will be notified of any modifications via email.*
