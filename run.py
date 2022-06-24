from extensions import app
from app.controller.service_controller import api
import logging

logging.basicConfig(level=logging.DEBUG)

app.logger.setLevel(logging.INFO)


# register the api
app.register_blueprint(api)

if __name__ == '__main__':
    ''' run application '''
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=True)