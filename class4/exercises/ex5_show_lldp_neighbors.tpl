Value DEVICE_ID (\S+)
Value LOCAL_INTF (\S+)
Value CAPABILITY (\w+)
Value REMOTE_PORT (\S+)

Start
  ^Device ID.*Port ID -> LLDPTable

LLDPTable
  ^${DEVICE_ID}\s+${LOCAL_INTF}\s+\d+\s+${CAPABILITY}\s+${REMOTE_PORT} -> Record
