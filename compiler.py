import os
import webapp2
import jinja2

from google.appengine.ext import ndb

#initializing work environment: the file, and the jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
template_loader = jinja2.FileSystemLoader(template_dir)
template_env = jinja2.Environment(loader = template_loader, autoescape = True)

# page making handler
class Handler(webapp2.RequestHandler):
    """contains the basic methods for rendering the templates into html pages"""
    def write(self, *arguments, **key_word_dictionary):
        """makes a html page out of the inputs"""
        self.response.out.write(*arguments, **key_word_dictionary)

    def render_str(self, template, **parameters):
        """makes a string out of the inputs"""
        t = template_env.get_template(template)
        return t.render(parameters)

    def render(self, template, **key_word_dictionary):
        """takes template to fill it in with the keywords"""
        self.write(self.render_str(template, **key_word_dictionary))

class HomePage(Handler):
    def get(self):
        """make homepage page up"""
        self.render("index.html")


#creation of pages
app = webapp2.WSGIApplication([('/', HomePage),
                              ],
                              debug = True)