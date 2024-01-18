import subprocess
import os
import sys

html_directory = 'ui'
flask_server_file = 'backend/server.py'

html_file_path = os.path.join(html_directory, 'index.html')

# Open HTML file in the default web browser on macOS
if sys.platform == 'darwin':
    subprocess.run(['open', html_file_path])
else:
    # For non-macOS systems, use webbrowser.open
    import webbrowser
    webbrowser.open(html_file_path, new=2)

# Run Flask server
flask_command = f'python3 {flask_server_file}'
subprocess.run(flask_command, shell=True)