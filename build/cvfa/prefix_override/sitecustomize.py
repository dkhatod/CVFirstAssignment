import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/mnt/c/Users/mphat/OneDrive/Documents/college/RG_first_assignment/CVFirstAssignment/install/cvfa'
