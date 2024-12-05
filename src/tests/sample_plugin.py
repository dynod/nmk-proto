import logging
import sys

from google.protobuf.compiler import plugin_pb2


def handle(request: plugin_pb2.CodeGeneratorRequest, response: plugin_pb2.CodeGeneratorResponse):
    # Iterate on files
    for pfile in request.proto_file:
        logging.info(f"Handling custom code generation for {pfile.name}")


def main():
    # Prepare a response
    response = plugin_pb2.CodeGeneratorResponse()

    # Handle code generation
    handle(plugin_pb2.CodeGeneratorRequest.FromString(sys.stdin.buffer.read()), response)

    # Push generated stuff to stdout
    sys.stdout.buffer.write(response.SerializeToString())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
