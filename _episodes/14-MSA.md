---
title: Multiple Sequence Alignment
teaching: 30
exercises: 0
questions:
- "How do I assign homology in molecular data sets?"
objectives:
- "Explain how multiple sequence alignment works."
- "Explain how guide-tree approaches perform multiple sequence alignment."
- "Explain how multiple genes can be efficiently indivdually aligned." 
---

##Overview of multiple sequence alignment

As you have discussed in class, building a phylogeny is dependent on homology.
If we are using character data, typically an expert has assigned homology based on their knowledge of the fossil record, developmental sequence and other sources of information.  

When we are working with molecular data, this is not possible. The goal of multiple sequence alignment (MSA) is to introduce gaps such that each residue in a _column_ will be homologous. At the end of this process, we have a data matrix in which the residues in each column are hypothesized to be descended from a residue in a common ancestor.

This typically takes the form of several possible moves:  
1. Rewarding matches.  
* Add to alignment score  
2. Penalize opening gaps.  
* Decrement score. Typically 5 points to open.   
3. Penalize rare substitutions, but not slight differences.  
* Decrement score.  
4. Penalize extending gaps.  

The alignment that maximizes the total score is considered to be the best. There are multiple ways of achieving an alignment. We will cover three of them today.  

Exercise One & Two on board

We often use what are called _scoring matrices_ to obtain the score of individual substitutions. We will talk about many types of substitution matrices. One that is commonly used in alignment is BLOSUM 62, which is based on empirically-calculated likelihoods of seeing different types of substitutions. 

![Blosum](../fig/blosum62.png)

Exercise 3 and 4 on board.  

As we can see, involving true biological knowledge to score alignments can improve alignment scores, sometimes dramatically!

The three exercises we will do today will focus on different strategies that may be deployed to find the optimal alignment. 

##Progressive MSA

Pairwise Multiple Sequence Alignment does exactly what we discussed above, for all your sequences. Typically, this is performed by first performing a pairwise MSA, as we did above, between the two sequences with the least differences. Then, sequences are added in the order of least differences. Progressive alignments score different alignment possibilities based on the alignment and user-specified scoring matrices, such as BLOSUM 62, or others. Clustal is an example of progressive alignment, but is known to be fairly innaccurate. Below, we use T-COFFEE to get an alignment. 

First, we will download and compile T_Coffee

```
git clone git@github.com:cbcrg/tcoffee.git tcoffee
cd tcoffee
cd compile
make t_coffee
```
We haven't played with any software yet in this class, so I'll now have you create a single location for all your software to live. Change directories into your home. Create a directory called 'bin'. Move the t-coffee executeable into it.

Now, move into the SELUSys repository. Enter the data directory, and the MSALab directory. We'll now run t_coffee on its default settings (a BLOSUM62 matrix with no gap penalty):

```
t_coffee data/sh3.fasta
```
Now, we'll try a gap-opening penalty:

```
t_coffee data/sh3.fasta -matrix blosum62mt -gapopen 5 -outfile=gapopen5
```

And one with a gap-extending penalty: 
```
t_coffee data/sh3.fasta -matrix blosum62mt -gapopen 5 gapextend 5 outfile gapopen5
```

Try one or two more additional alignments, such as increasing the gap open or extension. 

Now, transfer your .aln files to your personal machine using the scp command. Use http://msa.biojs.net/ to view them.

##Iterative Approaches to MSA
##Coestimation of MSA and Phylogeny


##References:
* T-Coffee Manual: http://tcoffee.readthedocs.io/en/latest/