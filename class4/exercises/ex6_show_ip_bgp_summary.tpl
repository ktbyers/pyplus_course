Value Filldown BGP_ROUTER_ID ([0-9\.]+)
Value Filldown LOCAL_AS (\d+)
Value PEER_IP ([0-9\.]+)
Value REMOTE_AS (\d{4,6})
Value UP_DOWN (\S+)
Value STATE_PFXRCD (\S+)

Start
  ^BGP router identifier ${BGP_ROUTER_ID}, local AS number ${LOCAL_AS}\s*$$
  ^Neighbor.*State.PfxRcd.*$$ -> BGPTable

BGPTable
  ^${PEER_IP}\s+4\s+${REMOTE_AS}\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+${UP_DOWN}\s+${STATE_PFXRCD} -> Record

EOF
