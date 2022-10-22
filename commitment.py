def is_prime():
    raise Exception("not implemented")

def generate_prime():
    raise Exception("not implemented")

def create_commitment(g, p, r, a):
    """
    :param g: The shared base/generator
    :param p: The shared prime
    :param r: TODO
    :param a: TODO 
    :return: TODO
    """
    return pow(g, (x+a*r), p)

def create_commitment(g, p, a):
    """
    :param g: The shared base/generator
    :param p: The shared prime
    :return: TODO
    """
    raise Exception("not implemented")

def open_commitment(g, p, r, a, d):
    raise Exception("not implemented")