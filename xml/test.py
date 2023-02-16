import xml.etree.ElementTree as ET

# Define the data object
data = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
}

# Parse the XML schema file
xmlschema_doc = ET.parse("xml\example.xsd")
xmlschema = ET.XMLSchema(xmlschema_doc)

# Create the root element of the XML file
root = ET.Element("person")

# Add the child elements to the root element
name = ET.SubElement(root, "name")
name.text = data["name"]
age = ET.SubElement(root, "age")
age.text = str(data["age"])
email = ET.SubElement(root, "email")
email.text = data["email"]

# Validate the XML file against the XML schema
if xmlschema.validate(root):
    # Write the XML file to disk
    ET.ElementTree(root).write("example.xml", encoding="utf-8", xml_declaration=True)
else:
    print("XML validation failed.")
