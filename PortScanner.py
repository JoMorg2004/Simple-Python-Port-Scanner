# Importing modules
import sys
import socket
from datetime import datetime

# Defining the target
if len(sys.argv) == 2:
    # Hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Please enter target hostname or IP")
    sys.exit()

# Capture the start time
start_time = datetime.now()

# Open log file in write mode
with open('log.txt', 'w') as log_file:
    # Write the header information to the log file
    log_file.write("=" * 45 + "\n")
    log_file.write(f"Scan Target: {target}\n")
    log_file.write(f"Starting scan: {str(start_time)}\n")
    log_file.write("=" * 45 + "\n")

    # Running scan
    try:
        # Scans specified ports.
        for port in range(1, 1023):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # Result of scan
            result = s.connect_ex((target, port))
            if result == 0:
                # Log to file and print to console
                log_message = f"Port number {port} is open\n"
                log_file.write(log_message)
                print(log_message, end='')  # Optional: still prints to console
            s.close()

        # Capture the end time and calculate elapsed time
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        elapsed_seconds = elapsed_time.total_seconds()

        # Log scan completion with time and duration
        scan_complete_message = f"\nScan completed at {end_time.strftime('%Y-%m-%d %H:%M:%S')} | Duration: {elapsed_seconds:.2f} seconds\n"
        log_file.write(scan_complete_message)
        print(scan_complete_message, end='')  

    except KeyboardInterrupt:
        log_file.write("\nScan halted by user.\n")
        print("\nScan halted by user.")
        sys.exit()

    except socket.gaierror:
        log_file.write("Hostname could not be resolved.\n")
        print("Hostname could not be resolved.")
        sys.exit()

    except Exception as e:
        log_file.write(f"An error occurred: {e}\n")
        print(f"An error occurred: {e}")
        sys.exit()
