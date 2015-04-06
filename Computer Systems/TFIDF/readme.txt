Name: Justin Law
UNI: jhl2184

Part 1
spark-submit --master yarn-client p1_tf_idf.py /datasets/hw3/p1_dataset/

Part 2
- 0.3 is the threshold argument
spark-submit --master yarn-client p2_cc.py /datasets/hw3/p2_dataset/ 0.3

Part 3
- 10 is the iterations argument
spark-submit --master yarn-client p3_pagerank.py /datasets/hw3/p3_dataset/page_files/ 10

Extra credit
- pythonUDF.py needs to be in the same directory as wiki.pig
- Works on a very small test.xml file. 
- Seems to some arbitary memory limit preventing the code from successfully executing.
- Most logic is present except the formatting at the end, the output is the top 5 most commmon ngram along with the pages and their ids
pig -param input=/user/jhl2184/test.xml -param output=output/pigwiki wiki.pig
