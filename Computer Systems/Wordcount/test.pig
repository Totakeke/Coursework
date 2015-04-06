REGISTER '/usr/local/pig/lib/piggybank.jar'
REGISTER 'pythonUDF.py' using jython as myfuncs;

DEFINE XPath org.apache.pig.piggybank.evaluation.xml.XPath();

A = load '/datasets/en_wikipedia_dump/sample_data/chunk-29.xml' using org.apache.pig.piggybank.storage.XMLLoader('page') as (x:chararray);
B = FOREACH A GENERATE XPath(x, 'page/revision/text') as (text:chararray), XPath(x,'page/title') as (title:chararray), XPath(x, 'page/id') as (pid:long);
C = FILTER B by (text is not null);
D = FOREACH C GENERATE myfuncs.nGramsGenerate(TRIM(text),5), title, pid;
E = LIMIT D 5;

dump E;

-- couldn't quite figure out how to take tuples (ngrams) out of bags and the count them




B = FOREACH A GENERATE XPath(x, 'page/revision/text'), XPath(x,'page/title'), XPath(x, 'page/id');

REGISTER 'pythonUDF.py' using jython as myfuncs;

A = load '/datasets/test/pg1342.txt' AS (words:chararray);
B = filter A by (words is not null);
C = foreach B GENERATE myfuncs.nGramsGenerate(TRIM(words), 3);

dump C;




A = load '/datasets/en_wikipedia_dump/sample_data/chunk-29.xml' using org.apache.pig.piggybank.storage.XMLLoader('title') as (x:chararray);



-- A = LOAD '$input' using org.apache.pig.piggybank.storage.StreamingXMLLoader('page');
-- B =  A;

-- A =  LOAD '$input' using org.apache.pig.piggybank.storage.XMLLoader('xml') as (x:chararray);

-- B = FOREACH A GENERATE XPath(x, 'page/title');

-- B = foreach A GENERATE FLATTEN(REGEX_EXTRACT_ALL(x,'<title>(.*)</title>'));

B = LIMIT A 1;
dump B;
-- store B into '$output';

B = REGEX_EXTRACT_ALL("<title>piggy</title>",'<title>(.*)</title>')

A = load 'catalog.xml' using org.apache.pig.piggybank.storage.XMLLoader('page') as (x:chararray);
B = foreach A GENERATE FLATTEN(REGEX_EXTRACT_ALL(x,'<page>\\s*<title>(.*)</title>\\s*<id>(.*)</id>\\s*</page>')) AS (title:chararray, id:chararray);

B = foreach A GENERATE FLATTEN(REGEX_EXTRACT_ALL(x,'<page>\\s*<title>(.*)</title>\\s*</page>'));
B = FOREACH A GENERATE XPath(x, 'BOOK/YEAR');



A = load '/datasets/test/pg1342.txt AS (words:chararray);';

DEFINE tokenize org.archive.bacon.Tokenize(); 
DEFINE ngram org.archive.bacon.NGram(); 

A