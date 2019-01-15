Value PORT_NAME (\S+)

Start
  ^Port.*Type\s*$$ -> ShowIntTable

ShowIntTable
  ^${PORT_NAME} -> Record
