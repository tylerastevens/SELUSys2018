---
title: Likelihood HW
teaching: 180
exercises: 0
questions:
- "How does a estimating a tree under likelihood differ from scoring one under parsimony?"
- "How does the output of a maximum likelihood tree search differ from that of a parsimony tree search?"
- "Can we compare trees and models? How?"
objectives:
- "Explain what different models are telling us about evolution."  
- "How does a heuristic search differ under likelihood?"
- "Perform ML analyses using PAUP on LONI" 
---


## Model Comparison Homework

1. In our initial model comparisons, we compared K80, F81 and JC. K80 was the best, but ultimately, that branch of the nested diagram did not produce the best model. What does this tell you about the strengths and weaknesses of hierachical model testing?

2. Fill in the model table:

| Model | nst | basefr | Invariant sites? | Gamma Distributed rate heterogeneity | Score | LR |
|-------|-------|----|------|-------| -------|-----|
| Name of model | nst=      |  basefr=  | yes/no | gamma = | L= | 2\*(lnL1-lnL2) = | 
| Name of model   | nst=   | basefr= | yes/no | gamma = | L= | 2\*(lnL1-lnL2) = |
| Name of model   | nst=  | basefr=  | yes/no | gamma = | L= | 2\*(lnL1-lnL2) = |

2b. Which model was ultimately preferred out of your set of candidate models? 

3. In the RAxML call, change the name of the run, and the random number seed. Add the -N flag, and a number of your choosing, to get multiple replicates. Do you get the same score every time?

4. Use the treecompare script to compare if you got the same topology for each tree. 