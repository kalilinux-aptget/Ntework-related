import optparse as optp
import scapy.all as scapy
def user_ip(ip):
  arp_packet=scapy.ARP(pdst=ip)
  broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff:ff")
  combined_packet=broadcast_packet/arp_packet
  ans_list,unans_list=scapy.srp(combined_packet,timeout=1)
  ans_list.summary()

def parsing():
    parse_obj=optp.OptionParser()
    parse_obj.add_option("-i",dest="ip_addr",help="enter the ip whose mac you want")
   # parse_obj.add_option("-o",dest="output_file",help="enter the file for storing the output")
    user,args=parse_obj.parse_args()
    if not user.ip_addr:
        print("we need the target ip")
    return user

user_input=parsing()
user_ip(user_input.ip_addr)