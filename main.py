import cgi
from google.appengine.api import users
from webapp2 import RequestHandler, WSGIApplication


MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/sign" method="post">
      <div><textarea name="content" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Sign Guestbook"></div>
    </form>
  </body>
</html>
"""


class MainPage(RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)


class Guestbook(RequestHandler):
    def post(self):
        self.response.write('<html><body>You wrote:<pre>')
        self.response.write(cgi.escape(self.request.get('content')))
        self.response.write('</pre></body></html>')


app = WSGIApplication([('/', MainPage), ('/sign', Guestbook), ], debug=True)