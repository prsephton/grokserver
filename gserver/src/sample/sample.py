import grok
from sample import resource

class Sample(grok.Application, grok.Container):
    title = "Sample App"
    description = "A sample application"

class Index(grok.View):

    def update(self):
        resource.style.need()
