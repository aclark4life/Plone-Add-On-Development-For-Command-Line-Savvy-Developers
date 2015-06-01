# This is hello/world/hello.py
from zope.publisher.browser import BrowserPage as View


class Hello(View):
    """
    View class and methods. Access by opening /<VIEW>{/<METHOD>} e.g. /hello{/world}
    """

    def world(self):
        return("Hello, World!")
