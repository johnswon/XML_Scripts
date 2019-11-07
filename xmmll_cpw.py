import xml.etree.ElementTree as xml


tree = xml.parse('file')

XML = tree.getroot().findall('FILELIST')
wr = open('file2', 'wb')

for ele in XML:
    filetext = ele.find('FILE').text
    if filetext.split(".")[-1].upper() == "APPROVED":
        wr.write(ele.find('FILE').text + '\n')
wr.close()
