import dendropy
from dendropy.calculate import treecompare
import sys

tree1 = dendropy.Tree.get(src=sys.argv[1], schema="newick")
tree2 = dendropy.Tree.get(src=sys.argv[1], schema="newick")
print(treecompare.symmetric_difference(tree1, tree2))
