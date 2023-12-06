import time
from typing import Callable
import logging
import ecs_logging

from fastapi import Response, Request
from fastapi.routing import APIRoute
from starlette.background import BackgroundTask


log = logging.getLogger(__file__)


def log_response(res: Response, req: Request, start_time: float):
    port_frmtd = f':{req.client.port}' if req.client.port else ''
    url = str(req.url)
    log.info(
        f'Request from {req.client.host}{port_frmtd} to {url} handled',
        extra={
            'request': {
                'client': {
                    'host': req.client.host,
                    'port': req.client.port,
                },
                'url': url,
                'method': req.method,
                'cookies': req.cookies,
                'params': {
                    'query': req.query_params,
                    'path': req.path_params,
                },
                'headers': req.headers,
            },
            'response': {
                'body': res.body,
                'status_code': res.status_code,
                'headers': res.headers,
                'charset': res.charset,
                'media_type': res.media_type,
                'duration': time.time() - start_time,
            }
        }
    )


class LoggingRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def logging_route_handler(request: Request) -> Response:
            response = await original_route_handler(request)
            response.background = BackgroundTask(
                log_response, response, request, time.time())
            return response

        return logging_route_handler


def init_logger(log_level=logging.DEBUG, log_path='microblog-api.log'):
    logger = logging.getLogger('root')
    logger.setLevel(log_level)

    handlers = [
        logging.StreamHandler(),
        logging.FileHandler(log_path)
    ]

    for handler in handlers:
        handler.setFormatter(ecs_logging.StdlibFormatter())
        logger.addHandler(handler)

    return logger
