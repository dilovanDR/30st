
from openseespy.opensees import *

# Define GMX and GMY files separately
GMX_files = [
    'GM1X.txt', 'GM2X.txt', 'GM3X.txt', 'GM4X.txt', 'GM5X.txt',
    'GM6X.txt', 'GM7X.txt', 'GM8X.txt', 'GM9X.txt', 'GM10X.txt', 'GM11X.txt'
]

GMY_files = [
    'GM1Y.txt', 'GM2Y.txt', 'GM3Y.txt', 'GM4Y.txt', 'GM5Y.txt',
    'GM6Y.txt', 'GM7Y.txt', 'GM8Y.txt', 'GM9Y.txt', 'GM10Y.txt', 'GM11Y.txt'
]


step_size = [ 0.01, 0.005, 0.01, 0.01, 0.01, 0.005, 0.005, 0.01, 0.005, 0.005, 0.005]

duration = [ 5346, 7529, 2700, 2230, 5400, 5437, 5177, 10000, 11292, 20000, 30000]




# Print the lists
print("GMX Files:", GMX_files)
print("GMY Files:", GMY_files)
