class Element(object):
    """Super class for any objects"""
    def __init__(self, content):
        self._content = content  # text content
        self._children = []
        self._parent = None

    def render(self):
        """render self as html format"""
        return self._render()

    def content(self):
        return self._content

    def children(self):
        return self._children

    def add_child(self, child):
        self._children.append(child)

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def _render(self):
        pass

    def nested(self):
        """Could this element hold other elements inside, True for yes.
        """
        return True
