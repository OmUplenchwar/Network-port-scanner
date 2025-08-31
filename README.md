🔍 Network Port Scanner
  📌 Project Overview

   The Network Port Scanner is a Python-based tool that scans a machine’s localhost (127.0.0.1) to detect open ports. 
   It demonstrates how socket programming works and highlights the importance of monitoring active ports for security purposes.

  ⚙️ Technologies & Tools Used
  
  Python – Programming language used to implement the scanner.
  Socket Library – Handles networking and port connection checks.
  Command Prompt (Windows) – Used to execute and run the project.

 🛠️ Workflow

  User runs the Python script.
  The scanner iterates through a range of ports (1–1024).
  For each port, it tries to establish a connection using sockets.
  If a connection is successful → Port is OPEN.
  If not → Port is CLOSED (ignored).
  Results are displayed on the console.

🔐 Security Features

Scans only localhost (127.0.0.1) → Safe & non-intrusive.
Does not perform aggressive scanning (only basic connect).
Helps identify unnecessary open ports to reduce risks.

📂 Folder Structure
network-port-scanner/
│── port_scanner.py      # Main Python script
│── README.md            # Project documentation
│── Report.docx          # Detailed project report

📊 Observations

Detected open ports on localhost (e.g., 135, used by Windows RPC).
Validated that different machines may expose different sets of open ports.

📦 Deliverables

port_scanner.py → Source code.
README.md → Project documentation.
Report.docx → Report with workflow, features, and results.

🎯 Learning Outcomes

Gained hands-on experience with Python socket programming.
Understood networking basics and the concept of open/closed ports.
Learned the importance of monitoring ports for system security.

✅ Conclusion
This project successfully implemented a Network Port Scanner using Python.
It helped in understanding how open ports can be identified and why securing them is critical for preventing unauthorized access.
