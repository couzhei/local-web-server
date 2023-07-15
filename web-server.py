import socket

# The code sets the host IP address (127.0.0.1) and port number
# (7656) for the server.
HOST = "127.0.0.1"
PORT = 7656

# This is the RESPONSE variable contains the HTTP response that
# will be sent to the client.
RESPONSE = b"""\
HTTP/1.1 200 OK
Content-type: text/html
Content-length: 15

<h1>Hello!</h1>""".replace(
    b"\n", b"\r\n"
)

# By default, socket.socket creates TCP sockets.
# By using it in a with statement, the socket will
# be automatically closed when the block is exited.
with socket.socket() as server_sock:
    # This tells the kernel to reuse sockets that are in `TIME_WAIT` state.
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # sets the socket options to allow reusing addresses in the TIME_WAIT state.

    # This tells the socket what address to bind to.
    server_sock.bind((HOST, PORT))

    # 0 is the number of pending connections the socket may have before
    # new connections are refused.  Since this server is going to process
    # one connection at a time, we want to refuse any additional connections.
    server_sock.listen(0)
    print(f"Listening on {HOST}:{PORT}...")

    # n order to actually process incoming connections we need to call the
    # accept method on our socket. Doing so will block the process until a
    # client connects to our server.
    # client_sock, client_addr = server_sock.accept()
    # print(f"New connection from {client_addr}.")

    # Once we have a socket connection to the client, we can start to communicate
    # with it. Using the sendall method, let’s send the connecting client an
    # example response:
    # with client_sock:
    #     client_sock.sendall(RESPONSE)

    # If you run the code now and then visit http://127.0.0.1:9000 in your
    # favourite browser, it should render the string “Hello!”

    # Unfortunately, the server will exit after it sends the response so
    # refreshing the page will fail. Let’s fix that:

    # Note: In the above commented code, the server is set to handle a
    # single connection at a time. To see the response in a web browser,
    # you can uncomment the relevant lines and comment out the remaining lines.

    while True:
        # This loop is used to continuously accept incoming
        # connections.
        client_sock, client_addr = server_sock.accept()
        print(f"New connection from {client_addr}.")
        with client_sock:
            client_sock.sendall(RESPONSE)
