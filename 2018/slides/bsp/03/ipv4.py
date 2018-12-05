# 255.255.255.0
subnet_24 = 4294967040


def convert_ip(ip):
    '''converts an int IP to classic IP representation WWW.XXX.YYY.ZZZ'''
    classic_ip = [None]*4
    classic_ip[0] = (ip & (255 << 24)) >> 24
    classic_ip[1] = (ip & (255 << 16)) >> 16
    classic_ip[2] = (ip & (255 << 8)) >> 8
    classic_ip[3] = (ip & (255))
    str_ip = list(map(lambda x: str(x), classic_ip))

    return ".".join(str_ip)

def ip_to_int(ip):
    '''converts classic IP representation to int IP'''
    ip_parts = [int(x) for x in ip.split('.')]
    int_ip = ip_parts[0] << 24
    int_ip += ip_parts[1] << 16
    int_ip += ip_parts[2] << 8
    int_ip += ip_parts[3]
    return int_ip

def is_same_subnet(ip1, ip2, sub=subnet_24):
    '''returns True if ip1 and ip2 are on the same subnet'''
    assert int(ip1)
    assert int(ip2)
    if (ip1 & sub) == (ip2 & sub):
        return True
    return False

def device_number(ip, sub=subnet_24):
    '''returns address of device on the subnet'''
    return ((ip & sub) ^ ip)
