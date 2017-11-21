import flask as fl
import flask_restful as flr
import restapi.resources.helloworld as rrhw
import restapi.resources.fibonacci as rrf

app = fl.Flask(__name__)
api = flr.Api(app, prefix='/api/v1.0')

api.add_resource(rrhw.HelloWorld, '/hello/<string:name>')
api.add_resource(rrf.Fibonacci, '/fibonacci')

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
