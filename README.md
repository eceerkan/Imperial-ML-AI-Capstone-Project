# Black-Box Optimisation (BBO) Capstone — Portfolio

**Eight unknown functions · 2–8 dimensions · 12 recorded weekly rounds · GP-based Bayesian optimisation**

## Project summary

Imagine trying to find the best settings for eight machines without knowing how they work. Every test reveals a score, but tests are limited. In this project, I used earlier test results to choose which settings to try next. I started by exploring different possibilities, then gradually focused on regions that performed well. A statistical model helped estimate which new settings might be promising and how uncertain those estimates were. Several functions improved considerably, especially Functions 4, 5 and 7. The final results show the value of learning from feedback, while also showing why a strong result is not proof of the absolute best possible setting.

## Objective and high-level method

Maximise eight synthetic hidden objective functions using one query per function each round. Combine **Gaussian Process regression**, ARD Matérn kernels, **Expected Improvement**, Sobol candidate sampling and local exploration; then manually review candidate values using prior results. Early exploration gave way to stronger local refinement. This is an iterative, low-evaluation-budget optimisation example, **not** a guaranteed global optimisation solution.

## Highlights from the data

| Function | Dimensions | Initial best | Best recorded by Week 12 | Best source |
|---|---:|---:|---:|---|
| 1 | 2 | 7.71088e-16 | 2.70804e-13 | week 6 |
| 2 | 2 | 0.611205 | 0.654767 | week 11 |
| 3 | 3 | -0.0348353 | -0.0322484 | week 11 |
| 4 | 4 | -4.02554 | 0.632921 | week 12 |
| 5 | 4 | 1088.86 | 8282.12 | week 8 |
| 6 | 5 | -0.714265 | -0.112233 | week 10 |
| 7 | 6 | 1.36497 | 2.43557 | week 8 |
| 8 | 8 | 9.59848 | 9.99084 | week 11 |

These are per-function **maximisation** scores, on different scales. Note: Function 5 reaches its highest **observed** output at all-four-inputs `0.995000`; it is not a proven global optimum.

## Repository map

```text
BBO_Capstone_Portfolio/
├── README.md
├── requirements.txt
├── data/
│   ├── initial_data/function_1...function_8/  # starter .npy arrays
│   └── processed/
│       ├── query_history.csv                   # 96 submitted evaluations
│       ├── all_observations.csv                # starter + all 12 rounds
│       └── summary.json                        # counts and best outcomes
├── notebooks/BBO_Weeks_1_to_12.ipynb           # executable walkthrough
├── src/optimisation.py                         # reference GP + EI implementation
├── docs/
│   ├── datasheet.md
│   ├── model_card.md
│   └── methodology.md
```

## Documentation and deliverables

- [Dataset datasheet](docs/datasheet.md) — motivation, collection, composition, gaps, appropriate use and maintenance.
- [Optimisation model card](docs/model_card.md) — techniques, performance, caveats and assumptions.
- [Methodology / data provenance](docs/methodology.md) — distinguishes starter data, recorded weekly outputs and reconstructed demonstration code.