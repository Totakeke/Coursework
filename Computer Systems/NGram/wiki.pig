REGISTER '/usr/local/pig/lib/piggybank.jar'
REGISTER 'pythonUDF.py' using jython as myfuncs;

DEFINE XPath org.apache.pig.piggybank.evaluation.xml.XPath();

A = load '$input' using org.apache.pig.piggybank.storage.XMLLoader('page') as (x:chararray);
B = FOREACH A GENERATE XPath(x, 'page/revision/text') as (text:chararray), XPath(x,'page/title') as (title:chararray), XPath(x, 'page/id') as (pid:long);
C = FILTER B by (text is not null);
D = FOREACH C GENERATE myfuncs.nGramsGenerate(TRIM(text),5), title, pid;
E = LIMIT D 5;

DUMP E;
-- store E into '$output';