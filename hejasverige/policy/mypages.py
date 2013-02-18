from five import grok
from hejasverige.policy.interfaces import IMyPagesFolder


class MyPages(grok.View):
    grok.context(IMyPagesFolder)
    grok.name('my-pages')
    grok.require('zope2.View')

    def render(self):
        contextURL = self.context.absolute_url() + '/my-account'
        self.request.response.redirect(contextURL)
