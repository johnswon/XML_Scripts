import xml.etree.ElementTree as xml


tree = xml.parse('xml.par')

XML = tree.getroot().find('Content').findall('JOB')

wr = open('xml2.par', 'wb')

for ele in XML:
    wr.write(ele.find('DOCUMENT_TYPE').text + '\n')
wr.close()
