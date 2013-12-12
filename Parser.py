import HTMLParser

class Tag:
    '''
    tag representation
    self.tag - tag itself
    self.tags - inner html tags
    self.attrib = tag attributes
    '''
       
    def __init__(self, tag = '', attrib = [], outer_tag = None, data = None):
        self.attrib = attrib
        self.tag = tag
        self.outer_tag = outer_tag
        self.data = data
        self.inner_tag_counter = 0
        self.tags = []
        
        
    def Print(self):
        print "tag: ", self.tag," attributes:", self.attrib," inner tags count:", len(self.tags)

class BaseParser(HTMLParser.HTMLParser):
    '''
    base parser class
    self.page - html page address
    self.parser - html parser
    self.parse_res - page parsing result
    '''
    class ParserStates:
        head = 0
        starttag = 1
        data = 2
        endtag = 3
        startendtag = 4
    
    def __init__(self):
        self.state = BaseParser.ParserStates.head
        self.page = ''
        self.parse_res = []
        self.tag = Tag()
        self.curr_tag = self.tag
    
    def _state_machine(self, state, tag, attr):
        
        if self.state == BaseParser.ParserStates.head:
            new_tag = Tag(tag, attrs)
            self.curr_tag.tags.append(new_tag)
            
        elif self.state == BaseParser.ParserStates.starttag:
            pass
        
        elif self.state == BaseParser.ParserStates.startendtag:
            pass
        
        elif self.state == BaseParser.ParserStates.endtag:
            pass
        
        elif self.state == BaseParser.ParserStates.data:
            pass
        
    def handle_starttag(self, tag, attrs):
#         HTMLParser.HTMLParser.handle_starttag(self, tag, attrs)
        self._state_machine(BaseParser.ParserStates.starttag, tag, attr)
    
    def handle_endtag(self, tag, attr):
#         HTMLParser.HTMLParser.handle_endtag(self, tag)
        self._state_machine(BaseParser.ParserStates.endtag, tag, attr)
        
    def handle_startendtag(self, tag, attrs):
#         HTMLParser.HTMLParser.handle_startendtag(self, tag, attrs)
        self._state_machine(BaseParser.ParserStates.startendtag, tag, attr)
    
    def handle_data(self, data):
#         HTMLParser.HTMLParser.handle_data(self, data)
        self._state_machine(BaseParser.ParserStates.data, data, None)
    
    def Print(self):
        print self.state
        