# Python Introduction Course

This repository contains beginner-friendly Python lessons and the runnable
examples used during class.

## Course map

| Day | Topic | Main material |
| --- | --- | --- |
| Day 1 | Python basics and classes | [`Day1/`](Day1/) |
| Week 1 Review | Control flow, loops, and input | [review lesson](Week1_Review/README.md) |
| Day 2 | Core data structures | [`data_structures.py`](Day2/data_structures.py) |
| Day 3 | Text, JSON, CSV, and image files | [Day 3 lesson](Day3/README.md) |
| Day 4 | Git, GitHub CLI, and collaboration | [Day 4 lesson](Day4/README.md) |

## Setup

Create or activate a virtual environment, then install the lesson dependency:

```bash
python -m pip install -r requirements.txt
```

Run the Day 3 file examples:

```bash
python Day3/file_structure_and_handling.py
```

Run the Day 4 sample program and its tests:

```bash
python Day4/team_greeting.py
python -m unittest discover -s Day4 -p "test_*.py" -v
```

Day 3 writes its output files to `Day3/output/`. The Day 4 lesson uses this
directory to demonstrate why and how a `.gitignore` file is created.
