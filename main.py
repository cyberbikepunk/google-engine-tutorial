from google.appengine.api import users

from webapp2 import WSGIApplication, RequestHandler


class MainPage(RequestHandler):

    def get(self):
        # Checks for active Google account session
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
            self.response.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))


app = WSGIApplication([('/', MainPage), ], debug=True)

