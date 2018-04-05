---
title: Bayesian Methods HW2
teaching: 180
exercises: 0
questions:
- "How does a estimating a solution using a Bayesian method differ from likelihood?"
- "How does the output of a Bayesian tree search differ from that of likelihood or parsimony?"
objectives:
- "Explain what different models are telling us about evolution."  
- "How does a heuristic search differ under likelihood?"
- "Perform ML analyses using PAUP on LONI" 
---

## RevBayes Homework Two

1. In the slide move, try 5 different ranges for the slide move. Which one produces the best ESS? 

The modified delta values that created window ranges that were too narrow or too broad produced lower ESS values.  The delta values closest to 1 provided the highest ESS values.

Delta  	ESS
.01	718
.1	759
1	901
10	732
100	701

2. In the scale move, try 5 different ranges for the scale move. Which one produces the best ESS?

The modified lambda values that are too large or too small produced lower ESS values.  The lambda values closest to 1 provided the highest ESS values. 

Lambda	ESS 
.01	843
.1	866
1	901
10	901
100	879

3. How does using both moves change the ESS? Why does this make (or not make) sense?

When using the slide move, window ranges created from modified delta values that are too broad or narrow lowers the ESS value.  This makes sense because the proposed values of mu can be very different from the current mu value if the delta value is large.  Also, if the delta value is small, the window range of proposed mu values is also small.  

When using the scale move, lower ESS values also resulted from using lambda values that were too large or too small.  This make sense because if lambda is a large or small value, then the resulting mu prime will be very different from the current mu value. 

4. What happens if you double one of the moves? For example, if you have a scale move that means the mu prime will be far from the mu, _and_ one that implies the mu prime should be really different? 

If lambda is doubled, then the ESS drops dramatically.  If delta is doubled, ESS is decreased, but the decrease is not as significant.

Delta	Lambda	ESS
10	10	748
20	10	525
10	20	293 

##Try to have this done by the end of the work week, but if it's done by the end of spring break, that's OK, too.