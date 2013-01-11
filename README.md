sqlutil
=======

Introduction:

a simple util to generate sql for hash database


Usage:

python SqlGenerater.py



Example:


\###################################################

SQL GENERATER V 1.0
Usage:follow the tip.
	
\###################################################

1.Configuration Type:

0.	saccount_.access_info_


2.Choose one from above or input below and type enter:


----------------------------------------------------------------------------------------------------------------


\############################# CONFIG ########################################

Database name prefix:		[saccount_]

Table name prefix:		[access_info_]

Hash Database number:		[4]

Hash Table number:		[25]

Generate Result Type:		[console]


-----------------------------------------------------------------------------------------------------------------


3.Type the sql_template:

SQL EXAMPLE : 

Original Sql : ALTER TABLE `saccount.accessinfo`  ALTER `nick` DROP DEFAULT,  ALTER `username` DROP DEFAULT

Transfered Sql : ALTER TABLE `#table`  ALTER `nick` DROP DEFAULT,  ALTER `username` DROP DEFAULT

Please input the unformated sql !!!and replace the target table_name with '#table':





