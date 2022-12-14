# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import command_pb2 as v2ray_dot_com_dot_core_dot_app_dot_stats_dot_command_dot_command__pb2


class StatsServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetStats = channel.unary_unary(
        '/v2ray.core.app.stats.command.StatsService/GetStats',
        request_serializer=v2ray_dot_com_dot_core_dot_app_dot_stats_dot_command_dot_command__pb2.GetStatsRequest.SerializeToString,
        response_deserializer=v2ray_dot_com_dot_core_dot_app_dot_stats_dot_command_dot_command__pb2.GetStatsResponse.FromString,
        )
    self.QueryStats = channel.unary_unary(
        '/v2ray.core.app.stats.command.StatsService/QueryStats',
        request_serializer=v2ray_dot_com_dot_core_dot_app_dot_stats_dot_command_dot_command__pb2.QueryStatsRequest.SerializeToString,
        response_deserializer=v2ray_dot_com_dot_core_dot_app_dot_stats_dot_command_dot_command__pb2.QueryStatsResponse.FromString,
        )


class StatsServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetStats(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def QueryStats(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StatsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetStats': grpc.unary_unary_rpc_method_handler(
          servicer.GetStats,
          request_deserializer=v2ray_dot_com_dot_core_dot_app_dot_stats_dot_command_dot_command__pb2.GetStatsRequest.FromString,
          response_serializer=v2ray_dot_com_dot_core_dot_app_dot_stats_dot_command_dot_command__pb2.GetStatsResponse.SerializeToString,
      ),
      'QueryStats': grpc.unary_unary_rpc_method_handler(
          servicer.QueryStats,
          request_deserializer=v2ray_dot_com_dot_core_dot_app_dot_stats_dot_command_dot_command__pb2.QueryStatsRequest.FromString,
          response_serializer=v2ray_dot_com_dot_core_dot_app_dot_stats_dot_command_dot_command__pb2.QueryStatsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'v2ray.core.app.stats.command.StatsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
