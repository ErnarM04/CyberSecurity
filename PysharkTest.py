import binascii, pyshark

def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(' ', '').replace('0x', '').replace('\t', '').replace('\n', '')
    ascii_str = binascii.unhexlify(hex_str)
    return ascii_str

cap = pyshark.FileCapture('dnstunnel_2.pcapng', display_filter='dns.qry.name.len > 64')

for packet in cap:
    hex = packet.dns.qry_name
    hex = hex.replace('t.freeserver.site', '').replace('Home', '').replace('.', '')
    text = format(hex_to_ascii(hex))
    if 'hidden' in text:
        print(packet.frame_info.number, ':', text)
        print("HEX Flag:", hex)
        print(packet.dns.flags)
