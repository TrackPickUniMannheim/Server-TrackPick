import random
import string

import cherrypy


class Generator(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, 8))
		



if __name__ == '__main__':
    cherrypy.quickstart(Generator())