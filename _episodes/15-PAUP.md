---
title: PAUP and Parsimony
teaching: 180
exercises: 0
questions:
- "How do I use PAUP to build a parsimony tree?"
objectives:
- "Explain how parsimony works."
- "Explain two statistical tests of clade support."
- "Perform parsimony analyses using PAUP on LONI" 
---

## Maximum Parsimony Analysis Using PAUP

**Note to self:** Discuss homeworks. 

Today, we will use  PAUP* (Phylogenetic Analysis Using Parsimony [*and other methods]) to estimate a phylogeny using the maximum parsimony optimality criterion. We will also practice performing bootstrap and jackknife quantification of uncertainty. In the process, we will also see some of the basics of how phylogenetic software will read data and understand models.

**A Note on Software Installs on LONI**: After we're done with a piece of software, if you can't see yourself using it again, feel free to delete it. I will make a note otherwise if I need you to retain it for future use. 

## Download PAUP and Data

Log in to LONI, and remain in your home directory. We will load PAUP via a provided module.

```UNIX
module load paup
```

Now, move into your work directory. Go into the class repository and pull my changes (I have added several data files). 

Exit the class repository. Make a folder for today's lab called "PaupLab". Make Data, Results, and Scripts subdirectories inside of it. Enter the Data directory. Copy the data from class repository. The following is a fill in the blank - figure out how you get from your data directory to the classroom data dir. 

```UNIX
cp _____/SELUSys2018/data/PAUPlab/primate-mtDNA.nex .
``` 

Now, we will start an interactive session, since we'll be performing some sort of intense computations:

```UNIX
qsub -I -V -A loni_selu_sys -q single -l nodes=1:ppn=1,walltime=3:00:00
```

## PAUP 

Paup is one of the older phylogenetics software packages available, and Dave Swofford has put considerable effort into ensuring that the main mechanisms and models are correct. Many of us who do other software development use PAUP as a check on our own calculations.

PAUP reads in data in the Nexus format. Go ahead and use nano to open the primate dataset. 

Next, we will open PAUP:

```UNIX
paup
```

You should get something like the below:

```UNIX
P A U P *
Portable version 4.0b10 for Unix
Sat Feb 17 16:04:16 2018

      -----------------------------NOTICE-----------------------------
        This is a beta-test version.  Please report any crashes,
        apparent calculation errors, or other anomalous results.
        There are no restrictions on publication of results obtained
        with this version, but you should check the WWW site
        frequently for bug announcements and/or updated versions.  
        See the README file on the distribution media for details.
      ----------------------------------------------------------------

paup>

```

Next, we will load in the data file, using the execute command. Execute is kind of PAUP's catch-all for loading in data.

```UNIX
execute Data/primate-mtDNA.nex
```

Let's have a look at the screen output. What information does it tell us?

Some other useful commands are:

```
cstatus
tstatus
showmatrix
showdist
log file="mylogfile"
```

Try each command. What is it telling you? If any of them are still unclear, you can add a question mark after the command to get more info.

First, we will compute a parsimony tree using the command all trees:

```UNIX
alltrees;
```

This will take a moment. Let's talk about parsimony, and the alltrees command. What is that command doing? What is parsimony doing? [go to board exercise]

Look at the best tree with the command showtree:

```unix
showtree;
```

Are we surprised by the length of the tree, given the number of characters?

Next, we will try heuristic searching:

```unix
hsearch
```

Note that a heuristic is being applied. What is a heuristic? 

Did it make a difference to the score of the best tree? Why?

Let's try some data that are too large for an exhaustive search:

```
execute Data/BardenClean.nex
```

This is some of my research data. Try to execute alltrees now. What does this message mean? Now try the heuristic search.

What is the score of the best tree you found _________. How many best trees were there? ________ Try one of the alternative swap measures (either NNI or SPR). 

```
hsearch swap= ______
```

What was the score of your best tree? When would you expect the swap algorithm to matter strongly?

## The Bootstrap 

We will now bootstrap our data. The bootstrap analysis generates a number of matrices (in our case, 100) from the original data matrix. Every taxon is represented in every matrix. Columns, however, are drawn, with replacement up until the original size of the matrix is obtained (i.e., the matrices are resampled with replacement). This process randomizes which characters are in the matrix, and measures repeatability. Typically more than 100 bootstraps will be run, and will generate support values for a node that run from 0-100. 


Reload the primate data. Now, begin a bootstrap run: 

```UNIX
bootstrap nreps=100 search=heuristic /addseq=random;
```

Save the tree:

```UNIX
savetrees from=1 to=1 savebootp=nodelabels file=output/bootstrap.tre;
```

## The Jackknife


The jackknife is similar to the bootstrap, but is performed without replacement. Therefore, each dataset is smaller.

Why would this be useful?

```unix 
savetrees from=1 to=1 savebootp=nodelabels file=output/jackknife.tre;
```



