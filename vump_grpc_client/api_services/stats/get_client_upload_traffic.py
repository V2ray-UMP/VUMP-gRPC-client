import grpc
from vump_grpc_client.v2ray_api.app.stats.command import command_pb2
from .._base import BaseService


class GetClientUploadTraffic(BaseService):
    def get_client_upload_traffic(self, email, reset=False):
        try:
            return self.stats_stub.GetStats(
                command_pb2.GetStatsRequest(
                    name=f"user>>>{email}>>>traffic>>>uplink", reset=reset
                )
            ).stat.value
        except grpc.RpcError:
            return 0
