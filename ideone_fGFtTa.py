__author__ = 'thunder'

from sys import stdin

data =  (
            ('0', 'no'),
            ('1', 'pa'),
            ('2', 're'),
            ('3', 'ci'),
            ('4', 'vo'),
            ('5', 'mu'),
            ('6', 'xa'),
            ('7', 'ze'),
            ('8', 'bi'),
            ('9', 'so'),
        )

def blocky_changer(source, dict_of_replaces, block_size=2):

    def split_len(seq, length):
        return [seq[i:i+length] for i in range(0, len(seq), length)]

    blocks = split_len(source, block_size) if block_size > 1 else source
    return map(lambda x: dict_of_replaces[x], blocks)


def str_blocky_changer(source_string, dict_of_replaces, block_size=1):
    return "".join(blocky_changer(source_string, dict_of_replaces, block_size))

int_li_dict = dict(data)
li_int_dict = {v: k for k, v in int_li_dict.iteritems()}


def namcu_to_int(text):
    return int(str_blocky_changer(text, li_int_dict, 2))

def int_to_namcu(number):
    return str_blocky_changer(str(number), int_li_dict)
    
if __name__ == "__main__":
	number_or_namcu = stdin.read()
	
	number = None
	namcu = None
	
	try:
		number = int(number_or_namcu)
	except ValueError:
		namcu = number_or_namcu
	
	if number:
		print int_to_namcu(number)
	else:
		print namcu_to_int(namcu)
