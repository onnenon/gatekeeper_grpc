from concurrent import futures

import grpc

from gatekeeper_grpc import gatekeeper_pb2_grpc
from gatekeeper_grpc.config import BANNER, LOGGER, SERVER_ADDRESS
from gatekeeper_grpc.services import GatekeeperService


def main():
    server = grpc.server(futures.ThreadPoolExecutor())

    gatekeeper_pb2_grpc.add_GatekeeperServicer_to_server(GatekeeperService(), server)
    server.add_insecure_port(SERVER_ADDRESS)

    LOGGER.info(BANNER)

    try:
        server.start()
        server.wait_for_termination()
    except Exception as e:
        LOGGER.error(e.message)


if __name__ == "__main__":
    main()
