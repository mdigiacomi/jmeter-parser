__author__ = 'mdigiacomi'
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class JMeterParser:
    def __init__(self):
        print('Initializing JMeter Parser')

    def parsejmeter(self):
        tree = ET.parse('jmeter-sample-format.jmx')
        root = tree.getroot()
        for child in root.iter('hashTree'):
            print(JMeterParser.prettify(child))

        return "Done"

    def prettify(elem):
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")


if __name__ == '__main__':
    jmeter = JMeterParser()
    print(jmeter.parsejmeter())