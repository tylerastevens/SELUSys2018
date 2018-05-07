---
title: Stepping Stone Homework
teaching: 180
exercises: 0
questions:
- "How can we compute a partitioned topology on LONI?"
---

## DivTime HW1
1. Which partition schemes do you think are most likely, biologically?
Gene and codon partition schemes are most likely the more biologically accurate partition schemes due to the variance in evolutionary patterns of individual genes.  It is unlikely that multiple genes’ evolutionary processes are similar, so a uniform partition scheme that groups all of the genes together with no partitions would probably not be the most accurate partition scheme.

2. Use Stepping stone and path sampling to determine which is the best partitioning scheme. Below, paste the marginal likelihood values and explain which partitioning scheme you think is best justified for these data.

Partitioning Scheme	Stepping Stone ML		Path Sampling ML
Uniform			-21401.48			-21398.67
Gene			-21399.46			-21398.79
Gene & Codon		-20529.43			-20530.60

Based on the marginal likelihood scores from stepping stone and path sampling, the gene and codon partitioning scheme would be the best choice for this data.

## Submit the homework by the course finals time