"""
blocklist.py

This file just contains the blocklist of JWT tokns. It will be imported by th eapp and the logout resource so that tokens can be added to the blocklist when the user logs out.
"""

# this should be a database or reddis!
BLOCKLIST = set()