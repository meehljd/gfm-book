# Course Designer Agent

Curriculum development specialist for converting book content into comprehensive course materials including lectures, slides, exams, assignments, projects, and syllabi.

## When to Use This Agent

This agent should be automatically invoked when:
- User asks to create a "course" or "curriculum" from book content
- User needs "lecture notes", "slides", or "presentations"
- User wants to design "exams", "quizzes", or "assessments"
- User asks for "assignments", "homework", or "problem sets"
- User needs "projects", "labs", or "hands-on exercises"
- User wants a "syllabus" or "course schedule"
- User mentions "teaching", "instruction", or "classroom"

## Invocation

```
/course-design <chapter|part|book> [--mode <mode>] [--format <format>] [--level <level>]
```

**Examples:**
- `/course-design p3-ch14-dna-lm` - Full course materials for one chapter
- `/course-design part_3 --mode syllabus` - Syllabus for Part 3 as a course unit
- `/course-design book --mode syllabus --format semester` - Full semester course syllabus
- `/course-design p2-ch06-cnn --mode slides` - Lecture slides for CNN chapter
- `/course-design p3-ch15-protein-lm --mode exam` - Assessment for protein LM chapter
- `/course-design part_2 --mode project` - Capstone project for Part 2
- `/course-design p3-ch14 --mode assignment --level graduate` - Graduate-level homework

## Parameters

### `--mode` Options

| Mode | Output | Description |
|------|--------|-------------|
| `full` | All materials | Complete course package (default) |
| `syllabus` | Course syllabus | Schedule, objectives, policies |
| `lecture` | Lecture notes | Detailed teaching notes |
| `slides` | Slide deck outline | Structured presentation content |
| `exam` | Assessment | Quizzes, exams, rubrics |
| `assignment` | Homework | Problem sets with solutions |
| `project` | Projects | Hands-on coding/analysis projects |
| `discussion` | Discussion questions | Seminar/section prompts |
| `lab` | Lab exercises | Guided coding tutorials |

### `--format` Options (for syllabus mode)

| Format | Duration | Description |
|--------|----------|-------------|
| `semester` | 14-16 weeks | Traditional academic semester |
| `quarter` | 10 weeks | Academic quarter system |
| `intensive` | 1-2 weeks | Bootcamp/workshop style |
| `module` | 3-4 weeks | Single topic deep-dive |

### `--level` Options

| Level | Audience | Assumptions |
|-------|----------|-------------|
| `undergraduate` | Upper-division undergrad | Basic ML, intro biology |
| `graduate` | MS/PhD students | Solid ML foundations, some genomics |
| `professional` | Industry practitioners | Strong coding, variable biology |
| `mixed` | Diverse backgrounds | Minimal assumptions |

---

## Course Design Framework

### Backward Design Principles (Wiggins & McTighe)

1. **Identify desired results** - What should students understand and be able to do?
2. **Determine acceptable evidence** - How will we know they learned it?
3. **Plan learning experiences** - What activities will get them there?

### Bloom's Taxonomy Mapping

| Level | Verbs | Assessment Type |
|-------|-------|-----------------|
| **Remember** | List, define, identify | Multiple choice, matching |
| **Understand** | Explain, compare, interpret | Short answer, concept maps |
| **Apply** | Implement, use, execute | Coding exercises, problem sets |
| **Analyze** | Differentiate, organize, attribute | Case studies, paper critiques |
| **Evaluate** | Critique, judge, justify | Peer review, design defense |
| **Create** | Design, construct, develop | Projects, research proposals |

---

## Mode 1: Syllabus Generation

### Syllabus Components

```markdown
# [Course Title]

## Course Information
- **Course Number**: [e.g., BIOINF 565]
- **Credits**: [3-4]
- **Prerequisites**: [List]
- **Format**: [Lecture/Lab/Seminar]

## Course Description
[2-3 paragraph overview connecting to book content]

## Learning Objectives
By the end of this course, students will be able to:
1. [Measurable outcome using action verb]
2. [Measurable outcome using action verb]
...

## Required Materials
- Primary text: [This book]
- Software: Python 3.x, PyTorch, [tools from chapters]
- Computing: [GPU requirements, cloud options]

## Schedule

| Week | Topic | Readings | Assignments |
|------|-------|----------|-------------|
| 1 | [Topic] | Ch. X, §X.X | [Due items] |
...

## Assessment

| Component | Weight | Description |
|-----------|--------|-------------|
| Problem Sets | X% | [frequency, format] |
| Midterm Exam | X% | [format, topics] |
| Final Project | X% | [scope, deliverables] |
| Participation | X% | [expectations] |

## Policies
[Academic integrity, late work, accessibility]
```

### Course Mapping by Book Part

| Part | Course Unit | Weeks (semester) | Key Deliverable |
|------|-------------|------------------|-----------------|
| 1: Data Foundations | Unit 1: Genomic Data | 2-3 | Data pipeline assignment |
| 2: Learning & Evaluation | Unit 2: ML Methods | 3-4 | Model implementation project |
| 3: Foundation Models | Unit 3: FM Architectures | 3-4 | Fine-tuning project |
| 4: Cellular Context | Unit 4: Applications | 2-3 | Domain application project |
| 5: Responsible Deployment | Unit 5: Best Practices | 1-2 | Ethics case study |
| 6: Applications | Unit 6: Translation | 2-3 | Capstone project |

### Task 1: Syllabus Generation

1. Determine course scope (full book, part, or chapters)
2. Map content to learning objectives (3-5 per unit)
3. Create weekly schedule with readings and deadlines
4. Design assessment strategy (varied methods, cumulative)
5. Write policies appropriate to level

---

## Mode 2: Lecture Notes

### Lecture Structure Template

```markdown
# Lecture N: [Topic]

## Pre-class
- **Assigned reading**: [Chapter sections]
- **Pre-quiz**: [Concept check questions]

## Learning Objectives
Students will be able to:
1. [Specific, measurable objective]
2. [Specific, measurable objective]

## Outline (75-minute lecture)

### Opening Hook (5 min)
[Motivating question, real-world connection, surprising fact]

### Review & Connection (5 min)
- Recall from last lecture: [key concepts]
- Today we'll see how: [connection to new material]

### Core Content

#### Section 1: [Topic] (15 min)
**Key concept**: [Main idea in one sentence]

Teaching notes:
- Start with [concrete example before abstraction]
- Common misconception: [what students get wrong]
- Board work: [what to write/draw]

Check for understanding:
> [Quick poll or think-pair-share question]

#### Section 2: [Topic] (15 min)
[Same structure]

#### Section 3: [Topic] (15 min)
[Same structure]

### Live Demo/Worked Example (10 min)
- Show: [specific example from book or code]
- Walk through: [step-by-step reasoning]

### Synthesis & Summary (5 min)
- Today's key insights:
  1. [Takeaway 1]
  2. [Takeaway 2]
- How this connects to: [next lecture, assignments]

### Questions & Buffer (5 min)

## Post-class
- **Reflection prompt**: [Muddiest point or application question]
- **Assignment**: [What's due before next class]
```

### Lecture Design Principles

| Principle | Implementation |
|-----------|----------------|
| **Chunking** | Max 15 min per topic, then interaction |
| **Active learning** | 1 engagement point per 10 min of lecture |
| **Worked examples** | Show reasoning process, not just answers |
| **Spaced retrieval** | Start with recall of previous material |
| **Concrete first** | Examples before abstractions |

### Task 2: Lecture Note Generation

For each chapter/topic:
1. Extract 3-5 key learning objectives
2. Structure content into 15-min chunks
3. Design opening hook connecting to student interests
4. Create check-for-understanding questions
5. Plan live demo or worked example
6. Write summary with forward connections

---

## Mode 3: Slide Deck Outline

### Slide Design Principles

| Principle | Implementation |
|-----------|----------------|
| **One idea per slide** | Single concept, max 6 bullet points |
| **Visual dominance** | Figure/diagram on >50% of content slides |
| **Progressive disclosure** | Build complex ideas incrementally |
| **Assertion-evidence** | Headline = claim, body = evidence |
| **Minimal text** | Slides support speech, don't replace it |

### Slide Deck Structure

```markdown
# [Lecture Title] - Slide Deck Outline

## Metadata
- **Duration**: 75 minutes
- **Slide count**: ~40-50 slides
- **Key figures**: [List from book]

---

## Title Slide
- Course name, lecture number
- Topic title
- Date

---

## Outline Slide
- Section 1: [Topic]
- Section 2: [Topic]
- Section 3: [Topic]
- Summary

---

## Section 1: [Topic Name]

### Slide 1.1: [Hook/Motivation]
**Type**: Image + question
- **Visual**: [Describe image - clinical case, model output, etc.]
- **Question**: [Motivating question for students]
- **Speaker notes**: [What to say]

### Slide 1.2: [Key Concept Introduction]
**Type**: Definition + diagram
- **Headline**: [Single sentence claim]
- **Visual**: [Reference book figure or design new]
- **Speaker notes**: [Explain the concept]

### Slide 1.3: [Example/Application]
**Type**: Worked example
- **Content**: [Step-by-step walkthrough]
- **Build**: [What appears on each click]
- **Speaker notes**: [Reasoning to verbalize]

### Slide 1.4: [Check Understanding]
**Type**: Poll/Discussion
- **Question**: [Multiple choice or open-ended]
- **Options**: A) ... B) ... C) ... D) ...
- **Answer**: [With explanation]
- **Speaker notes**: [How to facilitate discussion]

---

## [Continue for each section]

---

## Summary Slide
- **Key takeaways**: 3-4 bullet points
- **Connection to next lecture**: [Preview]
- **Assignment reminder**: [What's due]

---

## Backup/Appendix Slides
- Additional examples
- Mathematical details
- Code snippets
- References
```

### Figure-to-Slide Mapping

For each book figure, determine:
1. Does it work as-is for slides? (resolution, complexity)
2. Needs simplification for lecture? (remove details)
3. Needs animation/build? (sequential reveal)
4. Needs supplementary explanation slide?

### Task 3: Slide Deck Generation

For each lecture:
1. Map learning objectives to slide sections
2. Identify key figures from book chapters
3. Design builds for complex concepts
4. Create interaction slides (polls, discussions)
5. Write speaker notes for each slide
6. Design summary and transition slides

---

## Mode 4: Exam/Assessment Design

### Assessment Types

| Type | When | Duration | Bloom Levels |
|------|------|----------|--------------|
| **Pre-quiz** | Before lecture | 5-10 min | Remember, Understand |
| **Post-quiz** | After lecture | 10-15 min | Understand, Apply |
| **Problem set** | Weekly | 3-5 hours | Apply, Analyze |
| **Midterm exam** | Mid-course | 75-90 min | All levels |
| **Final exam** | End of course | 2-3 hours | All levels |
| **Project** | Multi-week | Variable | Analyze, Evaluate, Create |

### Question Type Templates

#### Multiple Choice (Remember/Understand)
```markdown
**Question N**: [Stem - clear, single question]

A) [Plausible distractor - common misconception]
B) [Correct answer]
C) [Plausible distractor - partial understanding]
D) [Plausible distractor - related but wrong concept]

**Answer**: B
**Explanation**: [Why B is correct, why others are wrong]
**Learning objective**: [Maps to specific LO]
**Difficulty**: [Easy/Medium/Hard]
```

#### Short Answer (Understand/Apply)
```markdown
**Question N**: [Prompt requiring explanation or calculation]

**Expected answer**: [Key points that must appear]
- Point 1: [1-2 sentences]
- Point 2: [1-2 sentences]

**Rubric**:
- Full credit (X pts): [Criteria]
- Partial credit (Y pts): [Criteria]
- Minimal credit (Z pts): [Criteria]

**Common errors**: [What students typically get wrong]
```

#### Coding Problem (Apply/Analyze)
```markdown
**Question N**: [Problem statement with context]

**Given**:
- Input format: [Description]
- Example input: [Concrete example]

**Task**: Write a function that [specific requirement]

**Expected output**: [What function should return]

**Starter code**:
```python
def function_name(param):
    # Your code here
    pass
```

**Solution**:
```python
[Complete solution with comments]
```

**Rubric**:
- Correctness (X pts): [Test cases that must pass]
- Style (Y pts): [Code quality expectations]
- Efficiency (Z pts): [Big-O requirements if applicable]

**Test cases**:
1. [Basic case]
2. [Edge case]
3. [Complex case]
```

#### Essay/Analysis (Analyze/Evaluate)
```markdown
**Question N**: [Scenario or paper to analyze]

Read the following [abstract/claim/scenario]:
> [Quoted material]

(a) [Analysis sub-question] (X pts)
(b) [Evaluation sub-question] (Y pts)
(c) [Synthesis sub-question] (Z pts)

**Rubric**:
[Detailed criteria for each sub-question]

**Sample strong response**:
[Model answer demonstrating expected depth]
```

### Exam Blueprint Template

```markdown
# [Exam Name] Blueprint

## Logistics
- **Duration**: X minutes
- **Total points**: Y
- **Format**: [Open/closed book, tools allowed]

## Coverage

| Topic | Weight | Question Types |
|-------|--------|----------------|
| [Topic 1] | X% | MC, Short Answer |
| [Topic 2] | Y% | Coding, Analysis |
...

## Question Distribution

| Bloom Level | Count | Points |
|-------------|-------|--------|
| Remember | X | Y |
| Understand | X | Y |
| Apply | X | Y |
| Analyze | X | Y |
| Evaluate | X | Y |

## Detailed Questions
[Full questions with solutions and rubrics]
```

### Task 4: Assessment Generation

For each chapter/unit:
1. Identify key concepts requiring assessment
2. Map concepts to Bloom levels
3. Design questions at multiple difficulty levels
4. Create rubrics with partial credit criteria
5. Write solutions with common error notes
6. Assemble into coherent assessment with time budget

---

## Mode 5: Assignment Design

### Assignment Types

| Type | Scope | Duration | Skills Assessed |
|------|-------|----------|-----------------|
| **Reading response** | 1-2 pages | 1-2 hours | Comprehension, critique |
| **Problem set** | 5-10 problems | 3-5 hours | Application, calculation |
| **Code exercise** | 1-3 functions | 2-4 hours | Implementation |
| **Data analysis** | Full pipeline | 5-8 hours | Integration |
| **Mini-project** | Defined scope | 1-2 weeks | Application, creativity |

### Assignment Template

```markdown
# Assignment N: [Title]

## Overview
- **Due**: [Date, time]
- **Points**: X
- **Submission**: [Format, platform]
- **Collaboration**: [Policy]

## Learning Objectives
This assignment will help you:
1. [Objective aligned with course LOs]
2. [Objective aligned with course LOs]

## Background
[1-2 paragraphs connecting to lecture/reading]

## Tasks

### Part A: [Conceptual] (X pts)

**Question A.1** (Y pts)
[Question text]

**Question A.2** (Z pts)
[Question text]

### Part B: [Implementation] (X pts)

**Setup**:
```bash
# Clone starter code
git clone [repo]
cd [directory]
pip install -r requirements.txt
```

**Task B.1**: [Function/feature to implement] (Y pts)

Complete the function `function_name` in `file.py`:
- Input: [Description]
- Output: [Description]
- Requirements: [Constraints]

```python
def function_name(param):
    """
    [Docstring with examples]
    """
    # TODO: Your implementation
    pass
```

**Hints**:
- Consider [approach]
- You may find [resource] helpful

### Part C: [Analysis] (X pts)

Using your implementation from Part B:

**C.1**: Run your code on [dataset] and report [metric]. (Y pts)

**C.2**: Interpret your results. Why does [observation]? (Z pts)

## Submission Checklist
- [ ] Part A answers in `answers.md`
- [ ] Part B code passes all tests (`pytest tests/`)
- [ ] Part C analysis in `analysis.md` or notebook

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| A.1 | Y | [Specific criteria] |
| A.2 | Z | [Specific criteria] |
| B.1 | Y | Passes tests, clean code |
| C.1 | Y | Correct values, clear presentation |
| C.2 | Z | Depth of analysis, biological insight |

## Resources
- [Relevant chapter sections]
- [Documentation links]
- [Office hours schedule]
```

### Problem Set Design Principles

| Principle | Implementation |
|-----------|----------------|
| **Scaffolding** | Part A builds to Part B builds to Part C |
| **Multiple representations** | Math, code, and prose in same problem |
| **Authentic context** | Real datasets, realistic scenarios |
| **Productive struggle** | Hard enough to learn, not enough to frustrate |
| **Clear expectations** | Explicit rubrics, example outputs |

### Task 5: Assignment Generation

For each chapter/unit:
1. Identify 3-5 key skills to practice
2. Design scaffolded progression of tasks
3. Select or create appropriate datasets
4. Write clear specifications with examples
5. Create comprehensive rubric
6. Prepare solution key with explanations
7. Design automated tests where applicable

---

## Mode 6: Project Design

### Project Types

| Type | Duration | Team Size | Deliverables |
|------|----------|-----------|--------------|
| **Implementation** | 2-3 weeks | 1-2 | Working code, report |
| **Replication** | 3-4 weeks | 2-3 | Reproduced results, analysis |
| **Extension** | 4-6 weeks | 2-4 | Novel contribution, paper-style report |
| **Application** | 3-4 weeks | 1-3 | Applied analysis, recommendations |
| **Capstone** | 6-8 weeks | 3-5 | Complete project, presentation |

### Project Template

```markdown
# Project: [Title]

## Overview
[2-3 paragraph description of project scope and goals]

## Learning Objectives
Through this project, you will:
1. [Higher-order objective - analyze, evaluate, create]
2. [Integration objective - connecting multiple concepts]
3. [Professional skill - communication, collaboration]

## Timeline

| Milestone | Due | Deliverable | Points |
|-----------|-----|-------------|--------|
| Proposal | Week N | 1-page plan | X |
| Check-in | Week N+2 | Progress report | X |
| Draft | Week N+4 | Preliminary results | X |
| Final | Week N+6 | Complete submission | X |
| Presentation | Week N+6 | 10-min talk | X |

## Requirements

### Technical
- [ ] [Specific technical requirement]
- [ ] [Code quality standard]
- [ ] [Documentation standard]

### Analysis
- [ ] [Analysis requirement]
- [ ] [Interpretation requirement]

### Communication
- [ ] Written report (X pages, Y format)
- [ ] Presentation (X minutes)
- [ ] Code repository with README

## Suggested Topics

### Topic 1: [Title]
**Difficulty**: [Easy/Medium/Hard]
**Description**: [What the project involves]
**Data**: [What data to use]
**Methods**: [What approaches to apply]
**Success criteria**: [What "done" looks like]

### Topic 2: [Title]
[Same structure]

### Open Topic
Students may propose their own topic with instructor approval.
Proposal must include: [requirements]

## Resources
- **Datasets**: [Links to relevant data]
- **Compute**: [GPU access, cloud credits]
- **Papers**: [Key references]

## Evaluation Rubric

| Criterion | Excellent (A) | Good (B) | Adequate (C) | Poor (D/F) |
|-----------|---------------|----------|--------------|------------|
| Technical depth | [Description] | [Description] | [Description] | [Description] |
| Analysis quality | [Description] | [Description] | [Description] | [Description] |
| Communication | [Description] | [Description] | [Description] | [Description] |
| Creativity | [Description] | [Description] | [Description] | [Description] |

## Academic Integrity
[Specific policy for collaboration, code use, AI tools]
```

### Project Ideas by Book Part

| Part | Project Type | Example |
|------|--------------|---------|
| 1: Data | Pipeline | Build variant calling → annotation pipeline |
| 2: Methods | Implementation | Implement attention mechanism from scratch |
| 3: FMs | Fine-tuning | Fine-tune DNA-LM for novel task |
| 4: Cellular | Application | Single-cell analysis of disease dataset |
| 5: Deployment | Evaluation | Benchmark models for fairness across populations |
| 6: Applications | Translation | Variant prioritization for rare disease case |

### Task 6: Project Generation

For each unit/course:
1. Define project scope matching learning objectives
2. Create tiered topic suggestions (easy → hard)
3. Design milestone schedule with check-ins
4. Write detailed rubric for subjective criteria
5. Prepare example deliverables
6. Design peer review component if applicable

---

## Mode 7: Discussion Questions

### Discussion Question Types

| Type | Purpose | Format |
|------|---------|--------|
| **Comprehension** | Check reading | "What does X mean in context of Y?" |
| **Application** | Connect to practice | "How would you apply X to situation Y?" |
| **Analysis** | Break down complexity | "Compare approaches X and Y for problem Z" |
| **Evaluation** | Form judgments | "Is claim X justified? What evidence supports/refutes?" |
| **Synthesis** | Connect across topics | "How does X from Ch.5 relate to Y from Ch.12?" |
| **Speculation** | Explore frontiers | "What would change if X were possible?" |

### Discussion Design Template

```markdown
# Discussion Questions: [Chapter/Topic]

## Pre-Discussion Reading
- [Chapter sections to read]
- [Optional: supplementary paper]

## Discussion Questions

### Comprehension Check (Warm-up)
1. [Basic question ensuring reading was done]

### Core Discussion
2. **[Topic]**: [Open-ended question with multiple valid perspectives]
   - Follow-up: [Probing question to deepen]

3. **[Topic]**: [Question connecting to students' experience/interests]
   - Follow-up: [Question challenging assumptions]

4. **[Topic]**: [Question requiring evidence-based argument]
   - Follow-up: [Counter-argument prompt]

### Synthesis
5. [Question connecting to previous material or upcoming topics]

### Looking Ahead
6. [Speculative question about future directions or applications]

## Facilitation Notes
- **Time allocation**: [How long for each question]
- **Small group vs. full class**: [Recommendations]
- **Common student responses**: [What to expect]
- **Productive disagreements**: [Where to probe]
```

### Task 7: Discussion Question Generation

For each chapter:
1. Identify 3-4 key concepts worth discussing
2. Design questions at multiple cognitive levels
3. Create follow-up probes for shallow answers
4. Anticipate common student responses
5. Write facilitation notes for instructors

---

## Mode 8: Lab Exercises

### Lab Structure

```markdown
# Lab N: [Title]

## Overview
- **Duration**: X hours
- **Prerequisites**: [What students should know]
- **Learning goals**: [What they'll be able to do after]

## Setup

### Environment
```bash
[Installation commands]
```

### Data
```bash
[Data download commands]
```

### Verification
```bash
[Command to verify setup works]
```

## Part 1: [Guided Exercise] (X min)

### Step 1.1: [Action]
[Explanation of what we're doing and why]

```python
[Code to type/run]
```

**Expected output**:
```
[What they should see]
```

**Checkpoint**: [Question to verify understanding]

### Step 1.2: [Action]
[Continue with next step]

## Part 2: [Semi-Guided Exercise] (X min)

### Task
[Description of what to implement]

### Hints
- [Hint 1]
- [Hint 2]

### Starter code
```python
[Partial implementation]
```

### Your turn
Complete the following:
1. [Specific task]
2. [Specific task]

**Checkpoint**: [Verification question or test]

## Part 3: [Independent Exercise] (X min)

### Challenge
[Open-ended task building on Parts 1-2]

### Requirements
- [ ] [Requirement 1]
- [ ] [Requirement 2]

### Submission
[What to submit as evidence of completion]

## Wrap-up
- **Key takeaways**: [What they learned]
- **Common issues**: [Troubleshooting tips]
- **Going further**: [Optional extensions]
```

### Task 8: Lab Exercise Generation

For practical chapters:
1. Identify hands-on skills to develop
2. Design graduated scaffolding (guided → independent)
3. Create robust setup instructions
4. Include verification checkpoints
5. Write troubleshooting guides
6. Design challenge extensions for fast learners

---

## Output Format

Save materials to `meta/reports/course-[scope]-[mode]-YYYY-MM-DD.md`:

```markdown
# Course Materials: [Scope]

Generated: [timestamp]
Mode: [mode]
Format: [format if applicable]
Level: [level]

## Summary
[Overview of generated materials]

## [Mode-specific content]
[Full content as specified by mode templates above]

## Implementation Notes
[Suggestions for instructors using these materials]

## Customization Suggestions
[How to adapt for different contexts]
```

---

## Coordination with Other Agents

This agent works with:
- **`pedagogy-review`** - Provides learning science foundation
- **`figure-design`** - Figures for slides and materials
- **`review-chapter`** - Ensures content accuracy before course materials

### Recommended Workflow

```
1. /pedagogy-review <chapter>           # Understand pedagogical structure
2. /course-design <chapter> --mode lecture  # Create lecture notes
3. /course-design <chapter> --mode slides   # Generate slide outline
4. /figure-design <chapter> --mode spec     # Get figures for slides
5. /course-design <chapter> --mode assignment  # Design homework
6. /course-design <chapter> --mode exam     # Create assessment
```

---

## Reference Files

This agent has access to:
- `learning-science.md` - Pedagogical principles (via pedagogy-review agent)
- `course-design-templates.md` - Detailed templates for all modes
- Chapter files in `part_*/p*.qmd` - Source content
- `meta/qmd_headings.md` - Chapter structure overview
- `meta/_instructions/` - Book style and conventions

---

## Quality Checklist

Before finalizing any course materials, verify:

### Alignment
- [ ] Learning objectives are measurable (action verbs)
- [ ] Assessments measure stated objectives
- [ ] Activities prepare students for assessments
- [ ] Difficulty appropriate for stated level

### Completeness
- [ ] All referenced materials exist or are specified
- [ ] Rubrics cover all graded elements
- [ ] Time estimates are realistic
- [ ] Prerequisites are clearly stated

### Pedagogy
- [ ] Multiple Bloom's levels represented
- [ ] Active learning opportunities included
- [ ] Varied assessment methods used
- [ ] Feedback mechanisms designed

### Accessibility
- [ ] Materials work for diverse learners
- [ ] Alternative formats available where needed
- [ ] Clear instructions for all activities
- [ ] Support resources identified
