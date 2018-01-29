import xml.etree.ElementTree as ET  #模块重命名

tree = ET.parse('xml')
root = tree.getroot()

'''
操作XML
'''
# for child in root:
#     print(child.tag,child.attrib)  #tag去标签,attrib取属性,text取文本
#     for i in child:
#         pass
#         print(i.tag,i.text,i.attrib)
'''
修改XML
'''
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set("updated",'yes')
# tree.write("xml.xml")
'''
删除XML
'''
# for country in root.findall('country'):
#     rank = int(country.find("rank").text)
#     if rank > 50 :
#         root.remove(country)
# tree.write("xml.xml")
'''
创建XML
'''
# new_xml = ET.Element("namelist")
# name = ET.SubElement(new_xml,'name',attrib={'enrolled':'yes'})
# name.text = rq
# et = ET.ElementTree(new_xml) #生成文档对象
# et.write('test.xml',encoding='utf-8',xml_declaration=True)
# ET.dump(new_xml)# 打印生成的格式