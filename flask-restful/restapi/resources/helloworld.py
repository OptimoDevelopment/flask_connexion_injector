import flask_restful as flr

class HelloWorld(flr.Resource):
    def get(self, name):
        return {'hello': name}
