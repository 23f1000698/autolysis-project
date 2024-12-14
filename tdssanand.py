import gzip
import re
from datetime import datetime

# Function to check if a given date is a Thursday
def is_thursday(date_str):
    date_obj = datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S')
    return date_obj.weekday() == 3  # Thursday

# Function to check if the time is between 07:00 and 09:00
def is_between_7_and_9(date_str):
    time_obj = datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S')
    return time_obj.hour == 7 or (time_obj.hour == 8 and time_obj.minute == 0)

# Pattern to match the log entry format
log_pattern = re.compile(
    r'(?P<ip>[\d\.]+) - - \[(?P<time>[^\]]+)] "(?P<request>[^"]+)" (?P<status>\d{3}) (?P<size>\d+) "(?P<referer>[^"]*)" "(?P<user_agent>[^"]*)" (?P<vhost>[\S]+) (?P<server>[\S]+)'
)

# Initialize the counter
successful_get_requests = 0

# Open and read the GZipped log file
with gzip.open('C:\Users\katur\Downloads\s-anand.net-May-2024.gz', 'rt') as f:
    for line in f:
        match = log_pattern.match(line)
        if match:
            # Extract fields
            time_str = match.group('time')
            request = match.group('request')
            status = int(match.group('status'))
            
            # Parse time and check if it's Thursday and between 7:00 and 9:00
            if is_thursday(time_str) and is_between_7_and_9(time_str):
                # Split request into method, URL, and protocol
                method, url, _ = request.split()
                
                # Check if method is GET, URL starts with /tamil/, and status is successful
                if method == 'GET' and url.startswith('/tamil/') and 200 <= status < 300:
                    successful_get_requests += 1

# Output the result
print("Number of successful GET requests under /tamil/ on Thursdays from 7:00 to 9:00:", successful_get_requests)
