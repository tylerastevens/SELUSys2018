## Alignment Homework

### Some of these questions do not have a right answer.

Fill out this worksheet (it can be opened in a plain text editor, like TextEdit [Mac] or TextWrangler [Mac] or Notepad [Windows]. Commit and push it to your copy of the course repo. I will pull your copies Friday at 5, and try to have comments for you by next class period, when we will discuss them. 

Feel free to work in groups, and discuss the assignments as needed. However, I do expect you to turn in your own copy, with answers in your own words.

1. Some algorithms treat a gap as a single penalty value, regardless of how large the gap is. Others assess a gap opening penalty, then a smaller gap extension penalty. When (i.e. what kind of biological scenarios) might you think it might be better to use one algorithm over the other?

It would be more appropriate to use an algorithm with a gap extension penalty when comparing species that have been determined to be likely closely related based off information gathered from other data, such as morphological or ecological data.  The species should not differ to the extent that a significant gap extension should be necessary to create the best alignment between sequences, so if a large gap is needed it should be penalized appropriately, as this could be an indication that the two species are less closely related than considered previously.  On the other hand, if two species are known to be very distantly related and the biologist is simply trying to establish a more broad sense of relationships between species then large gaps may be expected and necessary to complete a satisfactory alignment so the algorithm for this assessment should not include a gap extension penalty.  

2. Breaking problems into subproblems is a common way to attack a tough problem. In the case of iterative alignments, we break the tree into smaller pieces. Are there biological questions for which you expect this would not be helpful?

I think iterative alignments would be helpful in any biological inquiry.  The iterative methods avoid the potential error associated with progressive methods and create results that are likely more accurate than results achieved from a progressive method alignment.  The iterative methods should be preferred due to the methods’ ability to repeat the process of reincorporating data back into previous sequences to achieve better alignment, an ability not possessed by progressive methods.  Progressive method may be acceptable if you’re looking at very small portions of similar sequences, but an iterative method would still be considered the best method.  



3. From the iterative alignment section: Which aslignment (pasta_script1, pasta_script2, pasta_script3) do you think is the "best"? By what criteria did you arrive at this decision? 
