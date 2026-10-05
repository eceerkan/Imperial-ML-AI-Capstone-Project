# BBO Capstone Project - Dataset Datasheet

## Motivation

This dataset was created as part of my Black-Box Optimisation (BBO) capstone project.

The objective of the project is to maximise eight unknown functions using a limited number of evaluations. Each function accepts a numerical input vector and returns a numerical output.

The dataset supports experimentation with optimisation under uncertainty. Since the mathematical forms of the functions are unknown, previous input and output observations are used to decide which points should be tested next.

---

## Composition

The dataset contains the initial observations provided for each of the eight functions, together with the additional queries and outputs collected during the project.

The eight functions range from 2 to 8 dimensions. Each observation contains:

- An input vector
- A numerical output
- The function number
- The round in which the query was submitted

The amount of data is relatively small because only one new query per function can be submitted during each round.

A major gap in the dataset is that the search spaces are only sparsely sampled. This is especially important for the higher-dimensional functions where the available observations represent only a very small part of the complete search space.

---

## Collection Process

The initial data was provided as part of the capstone project.

Additional observations were collected over multiple weekly rounds. For each round, I manually reviewed previous inputs and outputs before selecting one new query for each function.

During the earlier rounds I focused more on exploration because there was limited information about the functions.

As more results became available, I moved towards exploitation and local refinement around successful regions.

I also used Gaussian Process modelling and Bayesian optimisation concepts such as Expected Improvement to identify promising areas. Proposed queries were manually reviewed before being submitted.

---

## Preprocessing and Uses

Input values were kept within the permitted range and formatted to six decimal places.

I generally avoided exact zero values when creating new queries.

The outputs were compared based on their numerical values because the objective for every function was maximisation.

For modelling, outputs could also be standardised to make the different numerical scales easier to handle. Function 5 required additional consideration because its output values became significantly larger than those of the other functions.

### Intended Uses

The dataset is intended for:

- Black-box optimisation experiments
- Bayesian optimisation
- Gaussian Process modelling
- Comparing exploration and exploitation strategies
- Educational analysis of sequential decision making

### Inappropriate Uses

The dataset should not be treated as evidence that this optimisation strategy will perform equally well on real-world systems.

It should not be directly applied to safety-critical areas such as medical treatment or autonomous systems without further testing and validation.

---

## Distribution and Maintenance

The dataset is stored in my public GitHub repository.

The dataset is intended for educational use as part of the BBO capstone project and should be used according to the course requirements and any applicable repository terms.

I am responsible for maintaining the dataset and updating the repository when new results or documentation are added.

---

## Known Limitations

The main limitations of the dataset are:

- Small number of observations
- Sparse coverage of the search space
- Increasing concentration around successful regions
- Limited exploration in later rounds
- Greater uncertainty for higher-dimensional functions

These limitations mean that the best observed outputs cannot be assumed to represent the true global maximum of each function.
