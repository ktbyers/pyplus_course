Value PORT_NAME (\S+)
Value LINE_STATUS ((up|down))
Value ADMIN_STATE ((up|down))
Value MAC_ADDRESS ([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})
Value MTU (\d+)
Value DUPLEX ((full|half)-duplex)
Value SPEED (\d+)

Start
  ^${PORT_NAME} is ${LINE_STATUS}$$
  ^admin state is ${ADMIN_STATE},
  ^  Hardware:.*address: ${MAC_ADDRESS}\s
  ^  MTU ${MTU} bytes
  ^  ${DUPLEX}, ${SPEED} Mb/s -> Record
