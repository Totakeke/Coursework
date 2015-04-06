expected answer

"Python"
I do not	64
that he had	56
I am sure	56
as well as	48
could not be	40
by no means	40
I am not	38
that she had	36
one of the	36
would have been	34

"SSH Piping"
i do not        55
i am sure       50
she could not   40
as soon as      40
that he had     35
i dare say      27
i am not        26
it would be     25
in the world    25
it was not      24


hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input /datasets/test/pg1342.txt -output output/hs_word_count -mapper wc_mapper.py -reducer wc_reducer.py -file wc_mapper.py -file wc_reducer.py
cat part-00000 | sort -n -k4 -r | head

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input /datasets/en_wikipedia_dump/sample_data/chunk-1.xml -output output/wiki_sam_count -mapper wi_mapper.py -inputreader "StreamXmlRecordReader,begin=page,end=/page" -reducer wiki_reducer.py -file wi_mapper.py -file wiki_reducer.py
cat part-00000 | sort -n -k4 -r | head
hdfs dfs -rm -r output/wiki_sam_count


hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input /datasets/en_wikipedia_dump/sample_data/chunk-1.xml -output output/wiki_sam_count -mapper wc_mapper.py -reducer wc_reducer.py -file wc_mapper.py -file wc_reducer.py


hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input test.xml -output output/wiki_sam_count -mapper wi_mapper.py -inputreader "StreamXmlRecordReader,begin=page,end=/page" -file wi_mapper.py

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input /datasets/en_wikipedia_dump/sample_data/chunk-1.xml -output output/wiki_sam_count -mapper wiki_mapper.py -inputreader "StreamXmlRecordReader,begin=<page>,end=</page>" -file wiki_mapper.py

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -D mapreduce.map.memory.mb=4096 -input /datasets/en_wikipedia_dump/sample_data/ -output output/wiki_sam_count -mapper wiki_mapper.py -reducer wiki_reducer.py -file wiki_mapper.py -file wiki_reducer.py
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -D mapreduce.map.memory.mb=4096 -D mapreduce.job.reduces=8 -input /datasets/en_wikipedia_dump/xml_chunks/ -output output/wiki_count -mapper wiki_mapper.py -reducer wiki_reducer.py -file wiki_mapper.py -file wiki_reducer.py -inputreader "StreamXmlRecordReader,begin=<page>,end=</page>"

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input /datasets/en_wikipedia_dump/sample_data/ -output output/wiki_sam_count -mapper wi_mapper.py -reducer wiki_reducer.py -file wi_mapper.py -file wiki_reducer.py

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -D mapreduce.job.reduces=8 -input /datasets/en_wikipedia_dump/xml_chunks_small/ -output output/wiki_count2 -mapper wi_mapper.py -reducer wiki_reducer.py -file wi_mapper.py -file wiki_reducer.py


hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input output/wiki_sam_count -output output/wiki_top -mapper top_mapper.py -reducer top_mapper.py -file top_mapper.py -file top_mapper.py

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input /datasets/test/pg1342.txt -output output/pg_count -mapper wc_mapper.py -reducer wc_reducer.py -file wc_mapper.py -file wc_reducer.py
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -D mapreduce.job.reduces=1 -input output/pg_count -output output/top_3_gram -mapper wc_top.py -reducer wc_top.py -file wc_top.py -file wc_top.py

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input /datasets/en_wikipedia_dump/sample_data/ -output output/wiki_sam_count -mapper wiki_mapper.py -reducer wiki_reducer.py -file wiki_mapper.py -file wiki_reducer.py
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -D mapreduce.job.reduces=1 -input output/wiki_sam_count -output output/top_5_gram -mapper wiki_topmapper.py -reducer wiki_topreducer.py -file wiki_topmapper.py -file wiki_topreducer.py

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -D mapreduce.job.reduces=1 -input output/wiki_sam_count -output output/top_5_sam_gram -mapper wiki_topmapper.py -file wiki_topmapper.py 

pig -param input=test2.xml -param output=output/pig_test test.pig