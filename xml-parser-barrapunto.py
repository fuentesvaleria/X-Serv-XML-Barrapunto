
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys

# usado de base xml-parser-jokes.py
def normalize_whitespace(text):
    "Remove redundant whitespace from a string"
    return string.join(string.split(text), ' ')
    
class myContentHandler(ContentHandler):

    def __init__ (self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
    
    def startElement (self, name, attrs):
    	if name == 'item':
    		self.inItem = True
    	elif self.inItem:
    		if name == 'title':
    			self.inContent = True
    		elif name == 'link':
    			self.inContent = True
            
    def endElement (self, name):
    	if name == 'item':
    		self.inItem = False
    	elif self.inItem:
        	if name == 'title':
        		line = "Title: " + self.theContent + "."
        		print (line.encode('utf-8'))
        		self.inContent = False
        		self.theContent = ""
        	elif name == 'link':
        		print (" Link: " + self.theContent + ".")
        		self.inContent = False
        		self.theContent = ""

    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars
            
# --- Main prog

if len(sys.argv)<2:
    print ("Usage: python xml-parser-barrapunto.py <document>")
    print ()
    print (" <document>: file name of the document to parse")
    sys.exit(1)
    
# Load parser and driver

theParser = make_parser()
theHandler = myContentHandler()
theParser.setContentHandler(theHandler)

# Ready, set, go!

xmlFile = open(sys.argv[1],"r")
theParser.parse(xmlFile)

print ("Parse complete")