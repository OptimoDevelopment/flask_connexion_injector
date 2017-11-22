import flask_restful as flr
import flask_restful.reqparse as rp

class Fibonacci(flr.Resource):
    def post(self):
        parser = rp.RequestParser()
        parser.add_argument("index", type=int, help="Index of the number in Fibonacci sequence.")
        args = parser.parse_args()

        return {"index": args["index"], "value": list(self.get_fib_value(args["index"]))}

    def get_fib_value(self, index):
        a, b = 0, 1
        while index:
            yield a
            a, b = b, a + b
            index -= 1
