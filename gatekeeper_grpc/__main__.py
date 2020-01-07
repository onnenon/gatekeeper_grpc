from concurrent import futures

import grpc

from gatekeeper_grpc import gatekeeper_pb2, gatekeeper_pb2_grpc
from gatekeeper_grpc.config import SERVER_ADDRESS
from gatekeeper_grpc.whiteboard import set_status


class GatekeeperServicer(gatekeeper_pb2_grpc.GatekeeperServicer):
    def updateBoard(self, request, context):
        for update in request:
            set_status()


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gatekeeper_pb2_grpc.add_GatekeeperServicer_to_server(GatekeeperServicer(), server)
    server.add_insecure_port(SERVER_ADDRESS)
    print("*************** Start Gatekeeper GRPC Server ***************")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
