from dataclasses import dataclass
from unittest import TestCase
from unittest.mock import MagicMock, patch

from gatekeeper_grpc.services import GatekeeperService
from gatekeeper_grpc.whiteboard import Whiteboard


@dataclass
class Update:
    position: int
    status: int


class ServiceTests(TestCase):
    @patch.object(Whiteboard, "set_status")
    def test_updateBoard(self, set_status_mock):
        service = GatekeeperService()
        request = MagicMock()
        request.updates = [
            Update(1, 4),
            Update(5, 3),
        ]

        service.updateBoard(request, None)

        self.assertEquals(set_status_mock.call_count, 2)
