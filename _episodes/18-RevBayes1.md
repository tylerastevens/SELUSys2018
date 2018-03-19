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

##Briefly, let's finish RAxML

I have placed a Phylip formatted in the classroom repo. Move into the classroom repo, do a git pull, and observe which file has been added. In your copy, make a new folder called “raxmllab” and add this file to its data directory (which you’ll also have to create).

Enter this directory, and load raxml

```
module load raxml
```
And execute a tree search

```
raxmlHPC-PTHREADS-SSE3 -m GTRGAMMA -s Data/primates.phy -n sample -p 869877
```

You can also run a bootstrap in RAxML:

```
raxmlHPC-PTHREADS-SSE3 -m GTRGAMMA -s Data/primates.phy -n bootrun -p 9734057 -­b 89723947 -# 100
```

RAxML does not automatically map the bootstraps to the tree, so we have to do that by hand:

```
raxmlHPC -m GTRCAT -p 12345 -f b -t RAxML_bestTree.sample -z RAxML_bootstrap.bootrun -n mapped
```

You can now visualize the tree in IcyTree or FigTree.

### Moving on to RevBayes


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

In your work directory, create a RevBayesLab0 directory. Change into it.

