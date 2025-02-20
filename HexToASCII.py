import binascii, pyshark

def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(' ', '').replace('0x', '').replace('\t', '').replace('\n', '')
    ascii_str = binascii.unhexlify(hex_str)
    return ascii_str

hex_input = '7BC401900Eb587d394666C61677B746869735F69735F615F68696464656E5F6D6573736167655F696E5F646E735F72657175657374737D0D0A433A5C55736572735C67646673645C446F63756D656E74733E'
ascii_output = hex_to_ascii(hex_input)

print(format(ascii_output))