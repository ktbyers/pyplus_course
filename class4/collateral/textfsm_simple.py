from pprint import pprint
import textfsm

template_file = "show_ip_int_brief.template"
template = open(template_file)

with open("show_ip_int_brief.txt") as f:
    raw_text_data = f.read()

# The argument 'template' is a file handle and 'raw_text_data' is a string.
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

print("\nPrint the header row which could be used for dictionary construction")
print(re_table.header)
print("\nOutput Data: ")
pprint(data)
print()
