import xml.etree.ElementTree as et
import datetime
start = datetime.datetime.now()
#Do stuff
end = datetime.datetime.now()
print end - start

"""The point of this is to have one line that is tens of thousands of bytes (10-100 KB), them duplicate it that many times in one call, making it quadratic in size.
This would take up several GB and entirely too much processing time. This example is much smaller for obvious reasons."""
