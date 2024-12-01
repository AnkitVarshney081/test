from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld1-handler')


class HelloWorld1(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        # todo implement business logic
        return 200
    

HANDLER = HelloWorld1()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
