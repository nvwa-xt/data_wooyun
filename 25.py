import web
import sys
  
urls = ("/Service/hello","hello")
app = web.application(urls,globals())
  
class hello:
    def GET(self):
        return 'Hello,world!';
if __name__=="__main__":
    app.run()
