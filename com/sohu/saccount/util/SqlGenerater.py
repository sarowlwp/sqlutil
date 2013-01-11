'''
Created on 2013-1-9

@author: wenpingliu
'''
import ConfigParser 

config = ConfigParser.ConfigParser()
db_name_prefix = str()
table_name_prefix = str()
db_num = int()
db_table_num = int()
result_type = "console"

def cover_to_int(str):
    """
    cover int util
    """
    if str is None:
        return 0
    if str is '':
        return 0
    return int(str)

def format_sql(sql):
    if str(sql).find("#table") is -1:
        return sql
    else:
        return sql.replace("#table","{0}")
    
def print_sql_list(sqllist,result_type="console"):
    #print result_type
    #print str("file")
    if str(result_type) == str("file"):
        sql_file = open("result.sql","w")
        for sql in sqllist:
            sql_file.writelines(sql + "\n")
        sql_file.close()
        print "SQL Generate end,file name:" + "result.sql"
    else:
        print "######################################### SQL RESULT #######################################"
        for sql in sqllist:
            print sql
        print "############################################################################################"

#########################load config############################################

config.read("db.conf")
print "###################################################"
print "\t\tSQL GENERATER V 1.0"
print "\t\tUsage:follow the tip."
print "###################################################"
print "1.Configuration Type:"
configlist = config.sections()
result_type = config.get("system","result_type")
del configlist[configlist.index("system")]

if len(configlist) > 0:
    #print "There are some configurations for DB here, do you want load one of them ? "
    for db_config in configlist:  
        print str(configlist.index(db_config)) + ".\t" + db_config
load_config_num = raw_input("2.Choose one from above or input below and type enter:\n")

if load_config_num is '':
    db_name_prefix = raw_input("Please input dbname_prefix:")
    table_name_prefix = raw_input("Please input the tablename_prefix:")
    db_num = cover_to_int(raw_input("Please input db number:"))
    db_table_num = cover_to_int(raw_input("Please input table number:"))
else:
    #print configlist[0]
    load_config = configlist[int(load_config_num)]
    db_name_prefix = config.get(load_config,"db_name_prefix")
    table_name_prefix = config.get(load_config,"table_name_prefix")
    db_num = cover_to_int(config.get(load_config,"db_num"))
    db_table_num = cover_to_int(config.get(load_config,"db_table_num"))
################################################################################
print "############################## CONFIG ########################################"
print "Database name prefix:\t\t[" + db_name_prefix+"]"
print "Table name prefix:\t\t[" + table_name_prefix+"]"
print "Hash Database number:\t\t[" + str(db_num)+"]"
print "Hash Table number:\t\t[" + str(db_table_num)+"]"
print "Generate Result Type:\t\t[" + str(result_type)+"]\n"

#"ALTER TABLE `#table`  ALTER `nick` DROP DEFAULT,  ALTER `username` DROP DEFAULT;"
print "3.Type the sql_template:"
print "SQL EXAMPLE : \n"
print "Original Sql : ALTER TABLE `saccount.accessinfo`  ALTER `nick` DROP DEFAULT,  ALTER `username` DROP DEFAULT;"
print "Transfered Sql : ALTER TABLE `#table`  ALTER `nick` DROP DEFAULT,  ALTER `username` DROP DEFAULT;"
unformat_sql = raw_input("Please input the unformated sql !!!and replace the target table_name with '#table':\n")
sqllist = list()
unformat_sql = format_sql(unformat_sql)


for dbindex in range(0,db_num):
    current_db_name = db_name_prefix + str(dbindex)
    sqllist.append("use `"+current_db_name+"`;") 
    for tableindex in range(0,db_table_num):
                current_table_name = table_name_prefix+str((tableindex + dbindex*db_table_num));
                table_name = current_db_name +"`.`" + current_table_name;
                sql = unformat_sql.format(table_name)
                sqllist.append(sql) 

print_sql_list(sqllist,result_type)
has_next = raw_input("Press anykey to continue,type 'exit' to quit.:\n")
