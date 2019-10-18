import configparser
from ast import literal_eval
import os


def Runcmd(cmd):
    return_code = os.system(cmd)
    return return_code


#*********************************************************************
#Main function
#
#*********************************************************************
    def main():
        conf = "C:\\Users\\nkandasamy\\PycharmProjects\\MyProject\\conf\\logmon.conf"
        config = configparser.ConfigParser()
        config.read(conf)
        condition = (config['MATCH_CONDITIONS'])
        queue_file = config['LOG']['QUEUE_FILE']
        whole_line = config['LOG']['Entire_line_key']

        main_conditions = {}
        only_conditions = {} -
        #  default_conditions = {val: key for (key, val) in condition.items()}
        #  print (default_conditions.keys())
        for key in condition.keys():
            condition1 = literal_eval(condition[key])
            main_conditions[key] = condition1
            only_conditions[condition1['condition']] = key

    queue_file = config['LOG']['QUEUE_FILE']

    queue_data = open(queue_file, 'r').readlines()

    queue_obj = open(queue_file, 'w')

    for line in queue_data:
        queue_data_split = line.split(' : ')
        split_match = literal_eval(queue_data_split[1])
        print (split_match)

    #    print (main_conditions[queue_data_split[0]]['trigger'])
#        new = main_conditions[queue_data_split[0]]['trigger'].replace('$var',split_match[int(main_conditions[queue_data_split[0]]['$var'])])

        only_conduition_variables = main_conditions[queue_data_split[0]].copy()
      #  print(main_conditions[queue_data_split[0]])
        del (only_conduition_variables['condition'])
        del (only_conduition_variables['trigger'])
      #  print (only_conduition_variables)
      #  print(main_conditions[queue_data_split[0]])
        for key in (only_conduition_variables.keys()):
            main_conditions[queue_data_split[0]]['trigger'] = main_conditions[queue_data_split[0]]['trigger'].replace(key, split_match[(main_conditions[queue_data_split[0]][key])])
        #    print (main_conditions[queue_data_split[0]]['trigger'])
        print (main_conditions[queue_data_split[0]]['trigger'])
     #   print(main_conditions[queue_data_split[0]]['trigger'].replace(key, split_match[int(main_conditions[queue_data_split[0]][key])]))



        if whole_line in  main_conditions[queue_data_split[0]]['trigger']:
            main_conditions[queue_data_split[0]]['trigger'] = main_conditions[queue_data_split[0]]['trigger'].replace(whole_line, queue_data_split[2])

        if (config['LOG']['Trigger_Type'] == "run_command"):
            if(0 == 0):
                queue_obj.write(line)
    queue_obj.close()

main()