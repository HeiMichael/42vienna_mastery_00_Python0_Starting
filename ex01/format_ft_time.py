from time import time
from datetime import datetime#, timezone

seconds = int(time())
print(f"Seconds since January 1, 1970: {seconds} or {seconds:.3e} in scientific notation")

#seconds_alt = int(datetime.now(timezone.utc).timestamp())
#print(f"Seconds since January 1, 1970: {seconds_alt} or {seconds_alt:.3e} in scientific notation")

today = datetime.now()
print(today.strftime("%b %d %Y"))