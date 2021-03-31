""" pdfXBlock main Python class"""

import pkg_resources
from django.template import Context, Template

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment

class pdfJsXblock(XBlock):

    '''
    Icon of the XBlock. Values : [other (default), video, problem]
    '''
    icon_class = "other"

    '''
    To reduce API call white author is editing the lab on studio
    '''
    has_author_view = True
    '''
    Fields
    '''
    display_name = String(display_name="Display Name",
        default="PDF_JS",
        scope=Scope.settings,
        help="This name appears in the horizontal navigation at the top of the page.")

    url = String(display_name="PDF URL",
        default="https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/web/compressed.tracemonkey-pldi-09.pdf",
        scope=Scope.content,
        help="The URL for your PDF.")

    '''
    Util functions
    '''
    def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__, resource_path)
        return unicode(resource_content)

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))

    '''
    Main functions
    '''
    def student_view(self, context=None):

        """
        The primary view of the XBlock, shown to students
        when viewing courses.
        """
        context = {
            'display_name': self.display_name,
            'url': self.url,
        }
        html = self.render_template('static/html/pdf_view.html', context)

        frag = Fragment(html)
        frag.add_css(self.load_resource("static/css/pdf.css"))
        frag.add_javascript(self.load_resource("static/js/pdf.js"))
        frag.add_javascript(self.load_resource("static/js/pdf_view.js"))
        frag.initialize_js('pdfXBlockInitView', context.get('url'))
        return frag

    def author_view(self, context=None):
     
        context = {
            'display_name': self.display_name,
            'url': self.url,
        }
        html = self.render_template('static/html/pdf_view.html', context)

        frag = Fragment(html)
        frag.add_css(self.load_resource("static/css/pdf.css"))
        frag.add_javascript(self.load_resource("static/js/pdf.js"))
        frag.add_javascript(self.load_resource("static/js/author_view.js"))
        frag.initialize_js('pdfXBlockAuthorView', context.get('url'))
        return frag

    def studio_view(self, context=None):

        """
        The secondary view of the XBlock, shown to teachers
        when editing the XBlock.
        """

        context = {
            'display_name': self.display_name,
            'url': self.url,
        }
        html = self.render_template('static/html/pdf_edit.html', context)

        frag = Fragment(html)
        frag.add_javascript(self.load_resource("static/js/pdf_edit.js"))
        frag.initialize_js('pdfXBlockInitEdit')
        return frag

    @XBlock.json_handler
    def save_pdf(self, data, suffix=''):
        """
        The saving handler.
        """
        self.display_name = data['display_name']
        self.url = data['url']
        
        return {
            'result': 'success',
        }
