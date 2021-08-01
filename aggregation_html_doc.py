class Tag(object):

    def __init__(self, name, contents) -> None:
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self) -> str:
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)
    
    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self) -> None:
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''   # DOCTYPE doesn't have an end tag


class Head(Tag):

    def __init__(self, title=None) -> None:
        super().__init__('head', '')
        if title:
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)


class Body(Tag):

    def __init__(self) -> None:
        super().__init__('body', '')    # Body contents will be built up separately
        self._body_contents = []
    
    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)
        

class HTMLDoc(object):

    def __init__(self, doc_type, head, body) -> None:
        self._doc_type = doc_type
        self._head = head
        self._body = body
        
    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)
    
    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == "__main__":
    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances "
                        "of objects to build other object.")
    new_body.add_tag('p', "The composed object doesn't actually own the object that it is composed of "
                        "- if it's destroyed, those objects continue to exist.")

    new_doc_type = DocType()
    new_header = Head('Aggregation Document')
    my_page = HTMLDoc(new_doc_type, new_header, new_body)

    with open("test3.html", 'w') as test_doc:
        my_page.display(file=test_doc)
