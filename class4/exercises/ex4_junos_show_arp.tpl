Value MAC_ADDRESS ([0-9a-f:]+)
Value IP_ADDRESS ([0-9\.]+)
Value NAME (\S+)
Value INTERFACE (\S+)

Start
  ^MAC Address.*Flags.*$$ -> ARPTable

ARPTable
  ^${MAC_ADDRESS}\s+${IP_ADDRESS}\s+${NAME}\s+${INTERFACE}\s+ -> Record
