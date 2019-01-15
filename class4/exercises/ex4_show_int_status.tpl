Value PORT_NAME (\S+)
Value STATUS (\S+)
Value VLAN (\S+)
Value DUPLEX ((auto|full|half))
Value SPEED (\S+)

Start
  ^Port.*Type\s*$$ -> Header

Header
  ^---------- -> ShowIntTable

ShowIntTable
  ^${PORT_NAME}\s+--\s+${STATUS}\s+${VLAN}\s+${DUPLEX}\s+${SPEED} -> Record
