from gatekeeper_grpc import gatekeeper_pb2_grpc
from gatekeeper_grpc.config import LOGGER
from gatekeeper_grpc.gatekeeper_pb2 import BoardUpdateResponse
from gatekeeper_grpc.whiteboard import Whiteboard


def testMock():
    pass


class GatekeeperService(gatekeeper_pb2_grpc.GatekeeperServiceServicer):
    def updateBoard(self, request, context):
        for update in request.updates:
            LOGGER.info(f"set status of position: {update.position} to {update.status}")
            Whiteboard.set_status(update.position, update.status)
            response = BoardUpdateResponse()
            response.requestStatus = True
        return response
