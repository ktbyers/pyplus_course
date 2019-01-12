import textfsm

template_file = "show_int_status.template"
template = open(template_file)

with open("show_int_status.txt") as f:
    raw_text_data = f.read()

import ipdb
ipdb.set_trace()

# The argument 'template' is a file handle and 'raw_text_data' is a string.
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)

template.close()
