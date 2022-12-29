from typing import Dict
from xml.etree import cElementTree as ElementTree

from xml_converter.exceptions import BadFormatFileException


def convert_to_dict(xml_file) -> Dict:

    try:
        tree = ElementTree.parse(xml_file)
        root = tree.getroot()
        
        dict = xml_to_dict(root, [])
        
        result = {root.tag: dict}

        return result

    except Exception:
        raise BadFormatFileException("bad format file")

def xml_to_dict(xml, result: list):
    for child in xml:

        reg = {child.tag: child.text}

        if len(child) == 0:
            result.append(reg)
        else:
            result.append({child.tag: xml_to_dict(child, [])})
    
    return result if result else ""
