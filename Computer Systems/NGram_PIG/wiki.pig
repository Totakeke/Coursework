REGISTER '/usr/local/pig/lib/piggybank.jar'
REGISTER 'pythonUDF.py' using jython as myfuncs;

DEFINE XPath org.apache.pig.piggybank.evaluation.xml.XPath();

A = load '$input' using org.apache.pig.piggybank.storage.XMLLoader('page') as (x:chararray);
-- Using XPath to extract xml text
B = FOREACH A GENERATE XPath(x, 'page/revision/text') as (text:chararray), XPath(x,'page/title') as (title:chararray), XPath(x, 'page/id') as (pid:long);
C = FILTER B by (text is not null);
-- Using UDF to generate ngrams
D = FOREACH C GENERATE (pid, title) AS key, myfuncs.nGramsGenerate(TRIM(text),5) AS ngram;
-- Flattening the bag of ngram into individual ones
E = FOREACH D GENERATE flatten(ngram), key;
-- Grouping by ngram and then counting, ordering, and extracting only the top 5 highest count ngram
F = GROUP E BY ngram;
G = FOREACH F GENERATE group, COUNT(E) AS total;
H = ORDER G BY total DESC;
I = LIMIT H 5;

-- Formatting the grouped list to have only necessary and distinct pages
M = FOREACH F GENERATE group, E.key AS list;
N = FOREACH M {
	keys = DISTINCT list.key;
	GENERATE group, keys; 
	}

-- Joining the top 5 count ngram in I and formatted information in N
X = JOIN I BY group, N BY group;
-- Further formatting the data to leave only the required information
Y = FOREACH X GENERATE I::group, I::total, keys;

STORE Y INTO '$output' USING PigStorage (',');