import uno
import socket
import threading
import sys

document = None

def connect(component="swriter"):
    global document
    if document is None:
        local_context = uno.getComponentContext()
        resolver = local_context.ServiceManager.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", local_context)
        context = resolver.resolve(
            "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
        desktop = context.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop", context)
        document = desktop.loadComponentFromURL(f"private:factory/{component}", "_blank", 0, ())
    return document, context

def handle_command(request, document, context):
    try:
        exec(request)
        return "Command executed successfully.\n"
    except Exception as e:
        return f"Command execution failed: {e}\n"

def handle_client(client_socket):
    print("Trying to connect to LibreOffice...")
    try:
        request = client_socket.recv(4096).decode().strip()

        if request.startswith('calc '):
            component = "scalc"
        elif request.startswith('write '):
            component = "swriter"
        else:
            component = "swriter"

        document, context = connect(component)
        print("Connected to LibreOffice.")
    except Exception as e:
        response = f"Failed to connect: {e}\n"
        client_socket.send(response.encode())
        client_socket.close()
        return

    response = handle_command(request, document, context)
    client_socket.send(response.encode())
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen(5)
    print("Server started on port 9999.")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}.")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
