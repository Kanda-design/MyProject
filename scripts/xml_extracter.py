# Python code to illustrate parsing of XML files
# importing the required modules


import xml.etree.ElementTree as ET

def main():
    # load rss from web to update existing xml file


    # parse xml file
    xmlfile = 'C:\\Users\\nkandasamy\\Documents\\test11.xml'


'''    tree = ET.parse(xmlfile)
    stuff = tree.findall('policy_groups/group')
    for a in stuff:
        print ("\nGroup : " + a.find('name').text + "\n")
        stuff1 = a.findall('group/policy')
        for b in stuff1:
            print (b.find("name").text )


    
    root = tree.getroot()
    for child in root:
     #   if(child.tag == "policy_group"):
         for elem in child:
             if (elem.tag == "group"):
                 for child1 in elem:
                    print (child1.tag("name") + ":" + child1.text("name"))
'''


'''
    root = tree.getroot()
    print(root)
    # store news items in a csv file



#    for name in root.iter('name'):
#        print (name.text)


    for child in root:
      #  print(child.tag)
        if (child.tag == "policy_groups"):
            for elem in child.iter():
                if (elem.tag == "group"):
                    for elem1 in elem.iter("group"):
                        print (elem1.tag + "\t" + elem1.text)
                #if (elem.tag == "policy"):
                #print(elem.text)
'''

if __name__ == "__main__":
    # calling main function
    main()
