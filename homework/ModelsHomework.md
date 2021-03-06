##Models Homework

1. From section "What is parsimony doing anyway?": How is the parsimony score impacted if you set a different number of characters to the custom model? For this answer, give the ctype command that you used to set up the model, and the number of parsimony steps in the best tree uncovered.

Parsimony score decreases as more characters are added to the custom model.

ctype my_ctype:1-2
Score (parsimony steps) of best tree with 2 characters set to the custom model = 67

ctype my_ctype:1-3
Score (parsimony steps) of best tree with 5 characters set to the custom model = 62


2. From section "Transitions and Transversions". Try the same analysis, except with a 3-1 weighting on transitions to transversions. For this answer, paste below your transition matrix and provide the parsimony score. Also note if there were any major differences in the consensus tree built from the 2-1 transition-transversion model and the consensus tree built from 3-1 transition-transversion model.

usertype 3_1 stepmatrix=4

	a  c  g  t
[a]	.  3  1  3
[c]	3  .  3  1
[g]	1  3  .  3
[t]	3  1  3  .

Parsimony = 1905

There were no changes in the topology of the two consensus trees.

3. So far, we looked at models that vary in two paramters, base frequencies and transition/transversion bias. Which parameter made a bigger difference? Does this make sense to you? Why or why not?

The parameter that made the biggest difference was base frequencies.  This makes sense because there can be a significant amount of heterogeneity among nucleotide frequencies.  
  


## Commit and push to your copy of the repository by Friday at 5 pm.