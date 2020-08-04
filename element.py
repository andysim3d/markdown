class Element(object):
    """Super class for any objects"""
    def __init__(self, content):
        self._content = content # text content
        self._children = []
        self._parent = None

    def render(self):
        """render self as html format"""
        return self._render()

    def content(self):
        return self._content

    def children(self):
        return self._children

    def inner_text(self):
        "inner text or nested elements as string format"
        return str(self._content)

    def _render(self):
        pass

    def nested(self):
        """Could this element hold other elements inside, True for yes.
        """
        return False
