# Simple-Python-Port-Scanner
A port scanner I made using Python

# Description
This script is a simple port scanner that scans ports from 1 to 1023 on a given target (IP address or hostname). It checks if each port is open and logs the results to both the console and a log.txt file. It also tracks the time the scan starts and finishes, and it reports its elapsed duration.

# Explaining the Code

1. Importing modules
   
   - The ``` sys ``` module allows for system interactions. It gives us access to command line args and allows us to exit the script.
   The ``` socket ``` module is used for network communication. This script uses it to check if a port on the target server is open.
   - The ``` datetime ``` module works with dates and times. I used it here to capture the scan start time and to calculate the elapsed time.

2. Defining the Target
   The if-else statement defines our target. The target name/IP is entered as an argument when the script is run in the terminal. For example: ``` python PortScanner.py example.com ```

   - ``` if len(sys.argv) == 2 ```  checks if one argument was input. The second argument is the target hostname/IP.
   - ``` socket.gethostbyname(sys.argv[1]) ``` converts a hostname like ``` example.com ``` into an IPV4 address. the ``` gethostbyname ``` function takes the provided hostname as input and provides the IPv4 address
  
3. Capturing Scan Start Time
    - ``` start_time = datetime.now() ``` This captures the current date and time when the scan starts. This also gets used later on for calculating the elapsed time.

 4. Creating and Writing to the Log File
      - ``` open('log.txt', 'w') ``` opens a file named log.txt ``` w ``` meaning in write mode.
      -  ``` log_file.write("=" * 45 + "\n") log_file.write(f"Scan Target: {target}\n") log_file.write(f"Starting scan: {str(start_time)}\n") log_file.write("=" * 45 + "\n") ``` This block writes text to the log file. This adds the target IP, start time, and I added a line of = for better formatting

5. Port Scanning
   - ``` for port in range(1, 1023) ``` This for loop loops through numbers 1 to 1023 and checks if these ports are open.
   - ``` socket.socket(socket.AF_INET, socket.SOCK_STREAM) ``` This creates a socket using IPv4 and TCP
   - ``` socket.socket(socket.AF_INET, socket.SOCK_STREAM) ``` This creates a 1 second timeout in between connection attempts
   - ``` s.connect_ex((target, port)) ``` This connects to the specific port on the target IP. A successful connection returns 0, meaning an open port, and an error means a failed connection.
  - ``` s.close(): ``` After each connection attempt, this closes the socket to free up resources.

6. Capturing the End Time and Logging the Scan
   - ``` end_time = datetime.now(): ``` This captures the end time of the scan.

   - ``` elapsed_time = end_time - start_time: ``` This calculates the time difference between the start and end time, which gives us the elapsed time.

   - ``` elapsed_seconds = elapsed_time.total_seconds(): ``` This converts the elapsed time to seconds.
  
   - ``` scan_complete_message = f"\nScan completed at {end_time.strftime('%Y-%m-%d %H:%M:%S')} | Duration: {elapsed_seconds:.2f} seconds\n" log_file.write(scan_complete_message) print(scan_complete_message, end='') ``` This block converts the end time string and formats the elapsed time. Then writes to the log file and prints out to the console

7. The Rest
   The rest of the code is exception handling for invalid hostnames or other errors, and user keyboard interruption to allow the user to stop the script and exit. 
    
   

   
