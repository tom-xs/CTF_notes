#FIRST PART

def ReRock(i,it,num,strr):
    for char in strr:
        char = ord(char)
        #print(str(char))
        first = char + sum([ord(x) for x in str(num)])
        #print(str(first))
        second = chr(first - sum([ord(x) for x in str(i)]))
        #print(str(second))
        it += str(second)
    return(it)
    #print(it)

#ReRock(2,"",9,"+0-,-+,*/,210*,))--).,*1*+1-.+/01+0/)++*)-/)2,.-21,,..1)*./0.*-..+,.,--/2,1,21*+*0-0**/-0+1)-.-/0*1./21./2-)1+/0+*0-)-./.0/1./1*+0+1)-22+-,/1-2/.--2-++*..01*,.1)00.2.1,0-2/1,2,0.)1)2//).2/0.+,-0**0121)+,.+-0/)0/)-/20-.,)10*/0-1-1.)1+/.0,1-//1,*20*.***2-+)-.,*++221)1-1*-+)2)*0.100+//2.0),,++-.+**.0-2/")


#SEOCND PART
def ReIdontlikersasatroll(c,key,m):
    m=("")
    #print("COOL: " + key)
    for i_s,k in zip(c, key):
        a=chr(ord(i_s) ^ int(k))
        m+=a
    # print("".join(m))
    return("".join(m))


N1_c=("-+/,01)1+)2,)*2)1*,+-*)*/.,),.1,)-*-01/2*/+.//*.02201)-0+2,201.-*)/.**2,2/1+/)0)+)-)-,*-)-/.0+..,211+/+++/,2.*1.)01,2*-.+/+-2.*0))/.*,+0*.,-...11//-.)1).*120,-21))2.*00.)*-1-/*2//1*,2-./-*/++-.2+/*/.)0+0)),2+2.*.1/*)++0.211+10)012*)-.,*.-+.2-22+*.1*1/.+,2.1+.*/*,/1*1+.*.0,//++2,1020-***++/+*/-.,2-/1+")
N2_c=("..1*-),.1.,*220.0/1+-))/0+2-2+/+/.)1.,121)-),)+0+/)),)10/11)*)---)2,*0,+)-*)11*//21-+000-.),.*/)/00+0,,--*01,+21,+-)./,.21+1-0-+,)/20/1+1*,/++,,)+0)*210.-,)0/.1.,/*),--)/)/)2/).2.+2,+).11.)-0,/01,,,0)01+,*)+0-..*2+)2)2*0-*.*-.,/2+2.+12-1).00-+2+)/.--.),2+02/1.))++00-,,2)./)).*22,))*-)210+11)*/.2/,1*+")
N3_c=("0-2,*/1200-/+0)*.02,/-011*++0*-.0-/+)++*+-.,1,//.+02+11.-2.**,+)02,-/-2/*--+2)22)/,*2*2,++.,,,+2,0/2*),1.-,20/11121,,22-,*-),/*12*2*,-,+)-01*///,/*)/,2,2*22-.+.0,/.220.,-11-0,0*1,/0+,.12+,/01/*,*1,+-.)-0++0*-++01-2,)1+11/*,0))/.0)1+.0+**,1)0)++.21+-,+-*2+0/*/+20)1-*.+*0/+2*2)+,.--/-/**0)1-/.).+)/)-01")
C1_c=("+2-),)+110/,1-*0+)1020/,/-2**0*.-*-*.1-1+-/.)0)222+0-121+,,*/*0//*.*-0*-)-0)))101-22.))2-/,1+2)))-020*20)*))2),)2*1),0-22),1-0-2/..21--//+,21,0/.2+2+0/0+/)..10/,2,*.10/222-2,2-/)*)1)0+*22*..*+*1/.01,/).,2/100*1)-.,,+0)1/)0.2,-.0.-++020)0+2+.0..202/01.2/)+.))///12+//*1)/)+/20,0-.//*1-+001--,-10/.10/).")
C2_c=(".,,-)+20-2-*0,.+)+0,,/*0)212./)1+22*21-0///1)0+1*)21-1,1*22)*,0/+0/--..2*,1,,-)-.)210/,.,*22+--0--)0)++//0*)*1200.*++*01/+*,)+**/+1..+0/11-0-/2+-..)0-11*),//)1**/0**+/1.+*/*.,/2**.0/2-+00)01./00.21/21,+0+.22,-,./*2-+201,,,2)1/)).1*-1,)1).+12)1)/+/.*+)),..-12.++)),*)2-122).)/)1)*02,*).,+2*12)0,+01,0,0")
C3_c=(")*-*+*).2-/110/+.1,)**/.)//-)/1*,---*,1*0+-).+*0+-*-2-+0,.,-2202.,-12//2/2/2//+*100*-02,,02,*02-)0200,0-/,)/1)-./0,*02.1-)2-,*0/*12.--*.*)020-*)+/-1)-/21**0.*,0+*-*/)/0*)/*),1+))12/122.)1/*./2,./..+-0+)/1,,0,-,,+2).*-/-,-,/2+*/*/1.,+.2*/*./++)11)))-.1)1*0-.),+,)/0+**)/,/2*./,0-))12/01*-+2*.012112*-+,")

N1=ReIdontlikersasatroll(ReRock(2,"",9,N1_c),"1001100001010110100110111001101000011101011011000100100001001001011011111011110110010101010110101101010011000010111101110110010101100011110110110000001010100001100110010101001011110111110010110000001001010111001011101001001011010100100011100111010101111010101000000001100011110111001010011000001010101","")
N2=ReIdontlikersasatroll(ReRock(2,"",9,N2_c),"1001100001010110100110111001101000011101011011000100100001001001011011111011110110010101010110101101010011000010111101110110010101100011110110110000001010100001100110010101001011110111110010110000001001010111001011101001001011010100100011100111010101111010101000000001100011110111001010011000001010101","")
N3=ReIdontlikersasatroll(ReRock(2,"",9,N3_c),"1001100001010110100110111001101000011101011011000100100001001001011011111011110110010101010110101101010011000010111101110110010101100011110110110000001010100001100110010101001011110111110010110000001001010111001011101001001011010100100011100111010101111010101000000001100011110111001010011000001010101","")
C1=ReIdontlikersasatroll(ReRock(2,"",9,C1_c),"1001100001010110100110111001101000011101011011000100100001001001011011111011110110010101010110101101010011000010111101110110010101100011110110110000001010100001100110010101001011110111110010110000001001010111001011101001001011010100100011100111010101111010101000000001100011110111001010011000001010101","")
C2=ReIdontlikersasatroll(ReRock(2,"",9,C2_c),"1001100001010110100110111001101000011101011011000100100001001001011011111011110110010101010110101101010011000010111101110110010101100011110110110000001010100001100110010101001011110111110010110000001001010111001011101001001011010100100011100111010101111010101000000001100011110111001010011000001010101","")
C3=ReIdontlikersasatroll(ReRock(2,"",9,C3_c),"1001100001010110100110111001101000011101011011000100100001001001011011111011110110010101010110101101010011000010111101110110010101100011110110110000001010100001100110010101001011110111110010110000001001010111001011101001001011010100100011100111010101111010101000000001100011110111001010011000001010101","")
print("N1: " + N1)
print("N2: " + N2)
print("N3: " + N3)
print("C1: " + C1)
print("C2: " + C2)
print("C3: " + C3)
#RSA
import functools
import itertools

def chinese_remainder(n, a): 
    sum = 0
    prod = functools.reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b): 
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def inv_pow(c, e):
    low = -1
    high = c+1
    while low + 1 < high:
        m = (low + high) // 2
        p = pow(m, e)
        if p < c:
            low = m
        else:
            high = m
    m = high
    assert pow(m, e) == c
    return m
 
N = [int(N1), int(N2), int(N3)]
C = [int(C1), int(C2), int(C3)]

# for n in N:
#     print("N: \n" + str(n) )
	#print("C: \n" + c )
e = len(N)
a = chinese_remainder(N, C)

# for n, c in zip(N, C):
#     #print("1: " + str(a % n == c))
#     assert a % n == c

m = inv_pow(a, e)
print("M: " + str(m))
print(bytes.fromhex(hex(m)[2:]).decode())