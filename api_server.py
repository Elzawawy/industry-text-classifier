from flask import Flask,render_template
from flask_restful import Api, Resource, reqparse
import requests
from joblib import dump, load
#Defining App !
app = Flask(__name__)
api = Api(app)

# Only one Endpoint to API supported: {GET}
class Model(Resource):
    # Endpoint to Get a Campaign already created in my datastore.
    def get(self, job_title):
        model = load('model.joblib')
        pred_industry = model.predict([job_title])
        return pred_industry[0], 200

# Adding routes to the Application and Endpoints to App.
api.add_resource(Model, "/model/api/<string:job_title>")
# Run this baby server !
app.run()