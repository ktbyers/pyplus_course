Value PORT_NAME (\S+)

Start
  ^Port.*Type\s*$$ -> ShowIntTable

ShowIntTable
  ^${PORT_NAME} -> Record

# Port      Name               Status       Vlan       Duplex  Speed Type 
# Gi0/1/0                      notconnect   1            auto   auto 10/100/1000BaseTX
# Gi0/1/1                      notconnect   1            auto   auto 10/100/1000BaseTX
# Gi0/1/2                      notconnect   1            auto   auto 10/100/1000BaseTX
# Gi0/1/3                      notconnect   1            auto   auto 10/100/1000BaseTX
#  ^${PORT_NAME}\s+ -> Record
