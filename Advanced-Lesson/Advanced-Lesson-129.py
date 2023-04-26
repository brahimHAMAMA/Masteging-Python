import logging

logging.basicConfig(filename='my_app.log', filemode='a', format='%(name)s')

logging.critical('This Is Critical Msg')