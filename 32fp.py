# Your name:Xingtong Zhou
#
# IEEE 754 32-bit Floating-Point Translator (Homework 2-2) starter code
# CSE 101, Fall 2018

# DO NOT MODIFY THE FOLLOWING HELPER FUNCTION!!!

def binToHex(bitstring):
    equivalents = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    result = ''
    bitstring.strip()

    for i in range(0, len(bitstring), 4):
        result += equivalents[bitstring[i:i+4]]

    return result

# Complete the functions that follow for this assignment
def fractionToBinary(value): # value is a string containing a base-10 value
    a = value.count(".")
    if a==0 or a>1:
        return None
    V = float(value)
    result=""
    power = 0.5
    while V>0:
        if power <=V:
            V-=power
            result += "1"
        else:
            result += "0"
        power/=2
    
    return result

def shiftBinaryPoint(bitstring):
    New_list = []
    b=bitstring.count(".")
    if b >1:
        return None
    elif b==0:
        bitstring += ".0"
    parameter =bitstring.split(".")
    if "1" in parameter[0]:
        exponent = parameter[0][parameter[0].find("1")+1:len(parameter[0])]
        exponent = len(exponent)
        mantissa = parameter[0][parameter[0].find("1")+1:len(parameter[0])] + parameter[1]
        if len(mantissa) > 23:
            mantissa = mantissa[0:23]
    else:
        f= parameter[1].find("1")
        exponent = (-1)*(f+1)
        mantissa = parameter[1][f+2:len(parameter[1])]
        if len(mantissa) >23:
            mantissa = mantissa[0:23]
    New_list.append(exponent)
    New_list.append(mantissa)
                                
        

    return New_list

def getBiasedExponent(exp): # exp is an integer
    if exp < -127 or exp > 128:
        return None
    else:
        exp += 127
        New_string= bin(exp)[2:]
        while len(New_string) <8:
            New_string = "0" + New_string
            
    return New_string

def assembleValue(isNegative, exponent, mantissa):
    NNew_string=""
    if isNegative is True:
        NNew_string += "1" + exponent + mantissa
    else:
        NNew_string += "0" + exponent + mantissa
    while len(NNew_string) <32:
        NNew_string += "0"
        
    return NNew_string
    
def encode(original): # original is a base-10 floating-point value
    if original <0:
        variable = True
        original *= -1
    else:
        variable = False
    original = str(original)
    if"." not in original:
        original += ".0"
    NNNew_string = bin(int(original[:original.find(".")]))[2:]
    fract = fractionToBinary("0"+original[original.find("."):])
    if fract == "None":
        return None
    shift = shiftBinaryPoint(NNNew_string+"."+str(fract))
    if shift == "None":
        return None
    result = assembleValue(variable,getBiasedExponent(shift[0]),shift[1])
    resultb = binToHex(result)
    
    
        
    
        
    return resultb



# DO NOT modify or remove the code below! You can use it to test your work.

if __name__ == "__main__":
    print('Testing fractionToBinary("0.5"):     ', fractionToBinary("0.5"))
    print('Testing fractionToBinary("0..25"):   ', fractionToBinary("0..25"))
    print('Testing fractionToBinary("0.75"):    ', fractionToBinary("0.75"))
    print('Testing fractionToBinary("0.0625"):  ', fractionToBinary("0.0625"))
    print('Testing fractionToBinary("0.328125"):', fractionToBinary("0.328125"))
    print()

    print('Testing shiftBinaryPoint("01101.10100"):', shiftBinaryPoint("01101.10100"))
    print('Testing shiftBinaryPoint("1.001"):      ', shiftBinaryPoint("1.001"))
    print('Testing shiftBinaryPoint("11"):         ', shiftBinaryPoint("11"))
    print('Testing shiftBinaryPoint("1..1"):       ', shiftBinaryPoint("1..1"))
    print('Testing shiftBinaryPoint("0.011010101"):', shiftBinaryPoint("0.011010101"))
    print()

    print('Testing getBiasedExponent(25):  ', getBiasedExponent(25))
    print('Testing getBiasedExponent(130): ', getBiasedExponent(130))
    print('Testing getBiasedExponent(0):   ', getBiasedExponent(0))
    print('Testing getBiasedExponent(-3):  ', getBiasedExponent(-3))
    print('Testing getBiasedExponent(-203):', getBiasedExponent(-203))
    print()

    print('Testing assembleValue(False, "10000010", "011100"):     ', assembleValue(False, "10000010", "011100"))
    print('Testing assembleValue(False, "10000101", "00110101100"):', assembleValue(False, "10000101", "00110101100"))
    print('Testing assembleValue(True, "10000100", "000000110"):   ', assembleValue(True, "10000100", "000000110"))
    print('Testing assembleValue(True, "10000101", "101011100"):   ', assembleValue(True, "10000101", "101011100"))
    print()

    print('Testing encode(77.375): ', encode(77.375))
    print('Testing encode(-32.375):', encode(-32.375))
    print('Testing encode(11.5):   ', encode(11.5))
    print('Testing encode(-18.25): ', encode(-18.25))
    print('Testing encode(0.101):  ', encode(0.101))
    print('Testing encode(-21):    ', encode(-21))

    print()
    
