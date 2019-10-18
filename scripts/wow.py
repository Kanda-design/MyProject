import json
import configparser
import re
import time
import pickle
import os
from ast import literal_eval


start = time.time()
print (start)

#********************************************************************
#Function               : readfile()
#Input                  : filename
#Description    : Read content from the file
#********************************************************************

def readfile(file):
    txtFile = open(file, 'r')
    #txtFile.read()
    #txtFile.close()
    return txtFile

#********************************************************************
#Function               : ReadWriteFile()
#Input                  : filename
#Description    : Read content from the file
#********************************************************************

def WriteFile(file):
    txtFile = open(file, 'w')
    #txtFile.read()
    #txtFile.close()
    return txtFile

#********************************************************************
#Function               : WriteAsDict()
#Input                  : file,data
#Description            : write content to the file
#********************************************************************

def WriteAs(file,data):
    with open(file, 'wb') as handle:
        pickle.dump(data, handle)
        handle.close()
    return 0

#********************************************************************
#Function               : WriteAsDict()
#Input                  : file,data
#Description            : write content to the file
#********************************************************************

def ReadAs(file):
    with open(file, 'rb') as handle:
        data = pickle.loads(handle.read())
        handle.close()
    return data


#********************************************************************
#Function               : OpenAsAppend()
#Input                  : filename
#Description            : Open the file with append method
#********************************************************************

def OpenAsAppend(file):
    picklistFile = open(file, 'a')
    return picklistFile

#********************************************************************
#Function               : WriteContent()
#Input                  : fileobj and line
#Description            : append the line to the file
#********************************************************************

def WriteContent(fileobj,line):
    fileobj.write(line.rstrip() + "\n")
    return 0

#********************************************************************
#Function               : CloseFile()
#Input                  : fileobj
#Description            : Close the file
#********************************************************************

def CloseFile(fileobj):
    fileobj.close()
    return 0



#********************************************************************
#Function               : make_hash()
#Input                  : FileName and content
#Description            : Convert the input list content into the
#                         dictonary
#********************************************************************

def make_hash(file_name, content):
    picklistObj = dict()
    picklistObj['File Name']  = file_name
    picklistObj['items'] = list()
    i=0
    for line in content:
        picklistItemObj = dict()
        picklistItemObj['value'] = str(i)
        picklistItemObj['text'] = line.strip()
        picklistObj['items'].append(picklistItemObj)
        i = i + 1
    return picklistObj



#********************************************************************
#Function               : compress()
#Input                  : FileName and content
#Description            : Load the list into dict. list content stores in key
#                         and vaule will be incremental number
#********************************************************************

def compress(file_name, content):
    rev_multidict = {}
    i=1
    for line in content:
        #Removing the empty lines
        if line not in ['\n', '\r\n']:
            rev_multidict.setdefault(line, set()).add(str(i))
            i = i + 1
    #print(rev_multidict)
    return rev_multidict


#********************************************************************
#Function               : split_dict()
#Input                  : FileName,content,pattern,count
#Description            : split the content and store it in dictonary
#********************************************************************

def split_dict(content, pattern, count):
    custom_dict = {}
 #   print (pattern,count)
    for line in content:
        line_list = line.split(pattern,count)
       # print (line_list)
        key = line_list.pop(-1)
        key = key.rstrip()
        custom_dict[key] = line_list
    return custom_dict



#********************************************************************
#Function               : split_dict_compress()
#Input                  : FileName,content,pattern,count
#Description            : split the list content and store it in dictonary
#********************************************************************

def split_dict_compress(file_name, content, pattern, count):
    custom_dict = {}
    i=1
    for line in content:
        line_list = line.split(pattern,count)
        key = line_list.pop(-1)
        custom_dict.setdefault(key, set()).add(str(i))
        i = i + 1
    return custom_dict



#********************************************************************
#Function               : split_dict_compress_match()
#Input                  : FileName,content,pattern,count,content_match
#Description            : split the content and store it in dictonary
#********************************************************************

def split_dict_compress_match(line_content, conditions,default_conditions,fileobj):
    triggers = dict()
    for condition in conditions:
        match = re.search(condition,line_content)
    #    print ("output : " + match)
        if match:
            WriteContent(fileobj,default_conditions[condition] + " : " + str(list(match.groups())) + " : " + line_content)
          #  print ("cominggg")
       #     WriteContent(fileobj,out)
            conditions[condition] += 1
            break
    triggers[condition]=line_content

    return triggers




#********************************************************************
#Function               : dict_json()
#Input                  : dict
#Description            : Convert the input dictonary content into the json
#********************************************************************

def dict_json(dict_content):
    picklistJson = json.dumps(dict_content, indent=4)

    return picklistJson


def CheckStat(stat_file,log_file_obj,log_file,read_type):

    if not read_type == "last_read_position":
        return readfile(log_file)

    if not os.path.exists(stat_file):
        return readfile(log_file)


    if (os.path.getsize(stat_file) == 0):
        return readfile(log_file)
    else:
        stat_obj = readfile(stat_file)
        file_create_time = os.path.getctime(log_file)
  #  print (stat_obj.read())
        content = stat_obj.read()
        dict_content = literal_eval(content)

        if dict_content[log_file].get(file_create_time):
        #    print ("state content")
        #    print(dict_content[log_file].get(file_create_time))
            log_file_obj.seek(dict_content[log_file].get(file_create_time))
            log_data = log_file_obj.readline()
            #for line in log_data:
        #    print ("conent file 1: "+log_data)
        else:
            log_data = log_file_obj.read()
    CloseFile(stat_obj)
    return log_data


def UpdateStat(stat_file,log_file,log_file_obj):
    position = (log_file_obj.tell())
    file_create_time = os.path.getctime(log_file)
 #   os.ftruncate(stat_file)
    if os._exists(stat_file):
        os.remove(stat_file)
    stat_obj = WriteFile(stat_file)
    stat_content = {log_file : {file_create_time : position }}

    #stat_obj = stat_obj.truncate()
    WriteContent(stat_obj,str(stat_content))
    CloseFile(stat_obj)


#*********************************************************************
#Main function
#
#*********************************************************************
def main():
    conf="C:\\Users\\nkandasamy\\PycharmProjects\\MyProject\\conf\\logmon.conf"
    Triggers = dict()
    config = configparser.ConfigParser()

#reading configuration file

    config.read(conf)
    file=config['LOG']['FILENAME']
    pattern = config['LOG']['pattern']
    count = config['LOG']['count']
    if 'EMPTY' in pattern:
        pattern = ' '
    conditions = config['MATCH_CONDITIONS']
    queue_file = config['LOG']['QUEUE_FILE']
    stat_file = config['LOG']['STAT_FILE']
    read_type = config['LOG']['LOG_READ_TYPE']
    reordered_cond_path = config['LOG']['REORDERED_CONDITION_PATH']


    file_obj = readfile(file)
    CheckStat(stat_file,file_obj,file,read_type)


#copying to conditions dict to another dict

    main_conditions = {}
    default_conditions = {}
#    temp_keys = conditions.keys() - conditions_hit_counts.keys()
 #  default_conditions = {val: 0 for (key, val) in conditions.items()}
#    print (default_conditions)

    for key in conditions.keys():
        condition1 = literal_eval(conditions[key])
        main_conditions[key] = condition1
        default_conditions[condition1['condition']] = key

    if os.path.isfile(reordered_cond_path) and os.path.getsize(reordered_cond_path) > 0:
        conditions_hit_counts = ReadAs(reordered_cond_path)
    #    print(type(conditions_hit_counts))
    #    print(conditions_hit_counts)
#        print(conditions_hit_counts['naveen'])

#checking the reordered_condition dict with default condition dict

        cond_diff = default_conditions.keys() - conditions_hit_counts.keys()
        for cond in cond_diff:
            conditions_hit_counts[cond] = 0

        cond_diff = conditions_hit_counts.keys() - default_conditions.keys()
        for cond in cond_diff:
            del conditions_hit_counts[cond]

    else:
        conditions_hit_counts=default_conditions

  #  print (conditions_hit_counts)

#    file_data=readfile(file)
    out_obj = OpenAsAppend(queue_file)
  #  CompressLines=split_dict_compress(file,file_data,str(pattern),int(count))
    CompressLines=split_dict(file_obj,str(pattern),int(count))
    cnt = len(CompressLines.keys())
    for key in CompressLines:
        if key not in ['\n', '\r\n']:
            Triggers = split_dict_compress_match(str(key),conditions_hit_counts,default_conditions,out_obj)
 #   file_data.close()
    #    print (Triggers)
   #jsonout=dict_json(out)
    print ("Number of check lines : " + str(cnt))
    CloseFile(out_obj)


    UpdateStat(stat_file,file,file_obj)

#    print("File position")



#178036
    CloseFile(file_obj)
# sort the dict with respect to hit count
 #   print(conditions_hit_counts)

    conditions_hit_counts1 = dict(sorted(conditions_hit_counts.items(),key= lambda kv: (kv[1], kv[0]),reverse=True))
   # conditions_hit_counts = sorted(conditions_hit_counts.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

  #  reordered_condition_obj = readwritefile(reordered_cond_path)
    WriteAs(reordered_cond_path,conditions_hit_counts1)

  #  print (conditions_hit_counts1)


   # WriteContent(reordered_condition_obj,conditions_hit_counts)
#    CloseFile(reordered_condition_obj)
 #   print (conditions_hit_counts['.*'])

  #  print("File created time : ")
  #  print (os.path.getctime(file))



#***************************
#Calling main function
#***************************
main()
end = time.time()
print (end)