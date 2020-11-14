class Element(object):
    """Super class for any objects"""
    def __init__(self, content, children=None):
        self._content = content  # text content
        if children is None:
            self._children = []
        else:
            self._children = children
        self._parent = None

    def render(self):
        """render self as html format"""
        return self._render()

    def content(self):
        return self._content

    @property
    def children(self):
        return self._children

    def add_child(self, child, index=None):
        if not index or index > len(self._children):
            self._children.append(child)
        else:
            self._children.insert(index, child)

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def _render(self):
        pass

    def render_html(self):
        return '<html>{}</html>'

    def nested(self):
        """Could this element hold other elements inside, True for yes.
        """
        return True

    def __eq__(self, value):
        return isinstance(value, type(self)) and \
            value.content() == self.content() and \
                value.children == self.children
