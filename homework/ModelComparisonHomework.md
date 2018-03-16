## Model Comparison Homework

1. In our initial model comparisons, we compared K80, F81 and JC. K80 was the best, but ultimately, that branch of the nested diagram did not produce the best model. What does this tell you about the strengths and weaknesses of hierarchical model testing?\

The strength of hierarchical model testing is the efficiency.  By not comparing every variation of models possible through each step of the hierarchy, model comparison is completed at a faster rate.  However, the cost of this efficiency could result in the selection of an inferior model.  Only nested models are compared so this could prevent the best model from being selected if it is not within the nested branch of models.  Also, the quality of the initial estimate of relationships contained in your data set will impact the results for the remainder of the model comparison process. 

2. Fill in the model table:

| Model | nst | basefr | Invariant sites? | Gamma Distributed rate heterogeneity | Score | LR |
|-------|-------|----|------|-------| -------|-----|
| SYM            | nst=6 | basefr=eq  | no | gamma = no | L= 6424.20 | 2\*(6424.20-6144.54) = 559.32 |
| K80+gamma      | nst=2 | basefr=eq  | no | gamma = yes| L= 5971.83 | 2\*(6424.20-5971.83) = 904.74 |
| K80+invariants | nst=2 | basefr=eq  | yes| gamma = no | L= 5982.71 | 2\*(6424.20-5982.71) = 882.98 |

2b. Which model was ultimately preferred out of your set of candidate models? 
The K80+gamma model was the preferred model.

3. In the RAxML call, change the name of the run, and the random number seed. Add the -N flag, and a number of your choosing, to get multiple replicates. Do you get the same score every time?

4. Use the treecompare script to compare if you got the same topology for each tree. 