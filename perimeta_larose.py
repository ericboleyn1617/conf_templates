import jinja2
from jinja2 import Environment, FileSystemLoader
#This line uses the current directory
file_loader = FileSystemLoader('.')
# User Input Circuit_ID
circuit_id = raw_input ("Please Enter the Circuit ID (MAX 30 CHARS): ")
print "You have entered: ", circuit_id, '\n'
print "#####################################################################" '\n'
# User Input Network ID Prefix
network_id = raw_input ("Please Enter the Network ID for the trusted addresses: ")
print "You have entered: ", network_id;
print "#####################################################################" '\n'
# User Input  Network  Prefix Length
ip_prefix = raw_input ("Please Enter Prefix Length for the trusted addresses: ")
print "You have entered: ", ip_prefix; '\n'
print "#####################################################################" '\n'
# User Input Network SIP Trunk Peering IP Address
peer_ip = raw_input ("Please Enter the subscribers IP Address for SIP Signaling: ")
print "You have entered: ", peer_ip; '\n'
print "#####################################################################" '\n'
# Import Environment, File, and set variables to user input
env = Environment(loader=file_loader)
template = env.get_template('perimeta_larose.j2')
output = template.render(circuit_id=circuit_id,network_id=network_id,ip_prefix=ip_prefix,peer_ip=peer_ip)
#Print the output
print(output)

# Write to Output file
with open ("conf_template_output.txt","w") as fh:
   fh.write(output)
    
