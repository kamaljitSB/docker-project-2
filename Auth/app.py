import connexion
from connexion import NoContent
from authentication import Authenticate

def login_user(username, password):
    "authenticate if user exist"
    user = Authenticate()
    result = user.check_credentials(username, password)
    print("this is the result", result)
    if result:
        return NoContent, 204
    else:
        return NoContent, 401

app = connexion.FlaskApp(__name__, specification_dir="")
app.add_api("openapi.yaml", strict_validation=True, validate_responses=True)
if __name__ == "__main__":
    app.run(port=8090)
