# LibreOffice Remote Command Server

This project provides a server to remotely execute commands on LibreOffice using Python. The server listens for incoming connections, connects to LibreOffice, and executes the received commands.

## Prerequisites

- LibreOffice installed and running with the listening socket enabled (usually on port 2002).
- Python 3.x installed.
- `uno` package installed (part of LibreOffice Python bindings).

## Setup and Usage

1. **Ensure LibreOffice is running with socket listening enabled**:
   - Start LibreOffice with the command: `soffice --accept="socket,host=localhost,port=2002;urp;"`

2. **Install necessary Python packages**:
   - Ensure `uno` package is available and properly set up. It is usually included with LibreOffice installation.

3. **Run the Server**:
   - Execute the script: `python3 server.py`

4. **Client Commands**:
   - The server expects commands in a specific format to determine the LibreOffice component to open and the command to execute.
   - For example, to open Calc and execute a command: `calc some_command_here`
   - To open Writer and execute a command: `write some_command_here`

## Example

1. Start LibreOffice with socket listening:
   ```sh
   soffice --accept="socket,host=localhost,port=2002;urp;"
   ```

2. Run the Python server:
   ```sh
   python3 server.py
   ```

3. Connect to the server from a client (example using `telnet`):
   ```sh
   telnet localhost 9999
   ```

4. Send a command to the server:
   ```sh
   write document.Text.insertString(document.Text.End, "Hello, World!", 0)
   ```

## Notes

- This server script is for demonstration and educational purposes. It should be improved and secured before being used in a production environment.
- Proper error handling and validation should be added to ensure the server does not execute arbitrary or harmful commands.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.