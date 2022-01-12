import os

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import View

from generator.constants.html import HTML_BASE, H1, H2, P, A

# Program to generate html and download html file

class GeneratorView(View):
    template = 'generator/index.html'
    html_file = 'main.html'
    
    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        file_path = self.get_file_path()
        html_content = self.generate_html_content()
        html_file = self.generate_html_file(file_path, html_content)

        response = HttpResponse(html_file)
        # Set the HTTP header to indicate is gonna be downloaded
        response['Content-Disposition'] = "attachment; filename=%s" % self.html_file
        return response

    def get_file_path(self):
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/files/' + self.html_file

    def generate_html_content(self):
        title       = self.request.POST.get("page_title", "Page title")
        h1          = H1.format(self.request.POST.get("main_title", "Title"))
        header_p    = P.format(self.request.POST.get("header_paragraph", "Paragraph."))
        h2          = H2.format(self.request.POST.get("section_title", "Section Title"))
        section_p   = P.format(self.request.POST.get("section_paragraph", "Paragraph."))
        link        = A.format(self.request.POST.get("link", "Some link"))

        return HTML_BASE.format(
            title=title,
            h1=h1,
            header_paragraph=header_p,
            h2=h2,
            section_paragraph=section_p,
            a=link,
        )

    def generate_html_file(self, file_path, html_content):
        f = open(file_path, "w+")
        f.write(html_content)
        f.close()
        f = open(file_path, "rb")
        content = f.read()
        f.close
        return content
