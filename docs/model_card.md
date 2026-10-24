# BBO Capstone Project - Optimisation Model Card

## Overview

**Name:** BBO Bayesian Optimisation Approach  
**Type:** Sequential Black-Box Optimisation  
**Version:** Capstone - Round 10  

This approach combines previous observations, Gaussian Process surrogate modelling, Bayesian optimisation concepts and manual review to select new query points for eight unknown functions.

---

## Intended Use

The approach is intended for optimising unknown numerical functions when evaluations are limited or expensive.

It is particularly useful when:

- Only a small number of observations are available
- The underlying function is unknown
- Relationships between inputs and outputs may be nonlinear
- Exploration and exploitation need to be balanced
- Uncertainty is important when selecting new observations

The approach should not be used without additional validation for high-risk applications such as medical treatment, autonomous safety systems or other situations where incorrect optimisation decisions could cause harm.

---

## Approach Details

My optimisation strategy evolved across the ten rounds.

### Early Rounds

During the early rounds, I focused more heavily on exploration because there was limited information about the unknown functions.

I compared the initial observations and attempted to identify areas of the search space that could potentially produce stronger outputs.

### Middle Rounds

As more observations became available, I started using the historical results more directly.

Gaussian Process models were useful because they can represent nonlinear relationships while also providing uncertainty estimates.

I used Bayesian optimisation concepts, particularly Expected Improvement, to help identify promising candidate points.

However, I manually reviewed the proposed values before submitting the final queries.

### Later Rounds

During the later rounds, my approach became more function-specific.

When a function repeatedly improved within a particular region, I focused more heavily on exploitation and made smaller changes around successful points.

When results became worse or inconsistent, I either moved back towards stronger historical observations or allowed more exploration.

For example, Function 5 increasingly favoured high input values. Functions 6 and 7 required more gradual local refinement.

By Weeks 9 and 10, my strategy was much more targeted than it had been during the first rounds.

---

## Performance

The main performance metric was the **highest observed output** because all eight functions are maximisation problems.

Each new output was compared against the previous best result for that function.

Several functions showed clear improvements during the project.

Examples include:

- Function 2 reached approximately `0.6493`
- Function 5 reached approximately `8282.12`
- Function 7 reached above `2.4`
- Function 8 produced results close to `10`

Functions 1 and 3 showed smaller improvements and appeared to already be close to strong regions based on the available observations.

Because the true maximum of each black-box function is unknown, I cannot calculate the exact optimality gap.

Therefore, performance represents the **best observed result** rather than proof that the global maximum has been found.

---

## Assumptions

One important assumption is that points close to strong previous observations are more likely to produce similarly strong outputs.

This assumption supports local refinement and exploitation.

However, it may not always be correct. A function could contain several separate peaks, meaning a much better region could exist somewhere that has not been explored.

I also assume that previous observations provide useful information for selecting future queries.

---

## Limitations

A major limitation is the small number of evaluations available.

Only one new query per function can be submitted during each round. This makes it difficult to explore the complete search space, particularly for functions with six, seven or eight dimensions.

The approach may also suffer from sampling bias.

As the project progressed, more queries were concentrated around successful regions. This improves exploitation but means that large parts of the search space remain unexplored.

Gaussian Process models can also be sensitive to kernel choices and hyperparameters.

The approach therefore cannot guarantee that the best observed point represents the true global optimum.

---

## Ethical Considerations

Transparency is important because optimisation results can appear more certain than they actually are.

Recording the complete query history, outputs, assumptions and changes in strategy makes it easier for another researcher to understand how decisions were made.

For reproducibility, the project should provide:

- Complete input and output history
- Jupyter Notebook or optimisation code
- Preprocessing steps
- Query selection strategy
- Model configuration
- Explanation of manual decisions

If this approach was adapted to a real-world application, additional testing would be required to consider safety, fairness, domain constraints and the consequences of incorrect optimisation decisions.
