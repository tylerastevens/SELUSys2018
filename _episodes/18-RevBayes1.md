---
title: Bayesian Methods
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

First, we'll download [RevBayes] to our LONI work directories. 

```UNIX
git clone https://github.com/revbayes/revbayes.git
```

Now, change into the RevBayes build directory.

```UNIX
cd revbayes/projects/cmake
```

And execute the build script.

```UNIX
./build.sh
```


The PDF for today's tutorial is [here](https://github.com/revbayes/revbayes_tutorial/blob/master/tutorial_TeX/RB_MCMC_Archery_Tutorial/RB_MCMC_Archery_Tutorial.pdf)

While this downloads, we will discuss the crucial differences between Bayesian inference and maximum likelihood difference. Download this [software](http://tree.bio.ed.ac.uk/software/tracer/), for visualizing posterior samples. 

