(24).as_integer_ratio()

(12).bit_length()
x=45
binario= '1101101'
int(binario, base=2)

octal ='67'
int(octal,base=8)
hexadecimal ='1b'
int(hexadecimal,base=16)
(234152).bit_length()
(-234152).bit_length()

int.from_bytes(b'\xf2\xff',byteorder='little')
int.from_bytes(b'\xf2\xff',byteorder='big')
int.from_bytes(b'\xf2\xff',byteorder='little',signed=True)
int.from_bytes(b'\xf2\xff',byteorder='big',signed=True)
(23152).to_bytes(2,byteorder='little')
(23152).to_bytes(2,byteorder='big')
(-247).to_bytes(2,byteorder='little',signed=True)
(-247).to_bytes(2,byteorder='big',signed=True)
x.imag, x.real 