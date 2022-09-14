from Types import DataType
from DataReader import DataReader
import xml.etree.ElementTree as ET


class XMLDataReader(DataReader):

    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()

        for student in root:
            self.students[student.attrib["name"]] = \
                [(subject.attrib["name"], int(subject.text))
                 for subject in student]

        return self.students
