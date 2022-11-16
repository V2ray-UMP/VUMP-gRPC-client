# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import config_pb2 as v2ray_dot_com_dot_core_dot_app_dot_log_dot_command_dot_config__pb2


class LoggerServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RestartLogger = channel.unary_unary(
        '/v2ray.core.app.log.command.LoggerService/RestartLogger',
        request_serializer=v2ray_dot_com_dot_core_dot_app_dot_log_dot_command_dot_config__pb2.RestartLoggerRequest.SerializeToString,
        response_deserializer=v2ray_dot_com_dot_core_dot_app_dot_log_dot_command_dot_config__pb2.RestartLoggerResponse.FromString,
        )


class LoggerServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RestartLogger(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LoggerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RestartLogger': grpc.unary_unary_rpc_method_handler(
          servicer.RestartLogger,
          request_deserializer=v2ray_dot_com_dot_core_dot_app_dot_log_dot_command_dot_config__pb2.RestartLoggerRequest.FromString,
          response_serializer=v2ray_dot_com_dot_core_dot_app_dot_log_dot_command_dot_config__pb2.RestartLoggerResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'v2ray.core.app.log.command.LoggerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))