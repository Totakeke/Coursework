Author: Justin Law
Topic: McKinsey Digital Labs Intern Application Exercise

To find items purchased together, a part of the process used to perform association analysis is used to find item sets that appear more often than a specified minimum support level. The support level is the frequency of the item sets appearing in all the transaction. 

Tools:
Python - Pandas, Itertools, and Matplotlib packages

Through examining the data set, there is a wide gulf between a small group of 11 items that appear more than 20% in all the transactions and the rest. This implies that the analysis should be much more straightforward as only a small group of items have significant impact on the results.  

The main findings are:
At a 20% minimum support level, item sets of size 3 are the largest and the sets are (item_2, item_7, item_29), and (item_3,item_5,item_22) with 21.76% and 21.67% support level respectively. At a 10% minimum support level, item set of size 4 are the largest and there is only one set which is (item_1, item_9, item_35, item_39) at a support level of 16.31%. Larger item set sizes can be also found at much lower minimum support levels, i.e. 0.1%, but these levels should be too low to matter. 

To run the script through the command line:
Type "python <source_file> <path_of_input_data_file> <min_support_level>" in the command line. For example, type " python MDL.py data.csv 0.2" to analyze data.csv at a 20% support level.

The analysis can be conducted at different minimum support levels easily by changing the minimum support level. The itemsets and support variables include all the analysis results. The assocAnalysis function will keep checking for larger item sets until it is unable to find any more item sets that exceed the minimum support level or it hits max_set size with a default of size 10. 
