
""" Run this code in 1)   >>  https://sagecell.sagemath.org/     <<
# OR
# if not then in  CoCalc using jupyter notebook and change the kernel to SageMath 9.5

"""


def calculate_m(pol):
    term_1 = 1**2
    term_2 = pol.degree()
    term_3 = 1/7
    ans = ceil(term_1/(term_2 * term_3))
    return ans


def calculate_t(beta, x, pol):
    term_1 = pol.degree()
    term_2 = 1/beta
    ans = floor(term_1 * (term_2 - 1)* x)
    return ans


def calculate_x(pol, N):
    term_1 = 1/7
    term_2 = pol.degree()
    term_3 = 1**2
    ans = ceil(N**((term_3/term_2) - term_1))
    return ans


def get_unicode(p):
    hex_p = []
    for x in p:
        hex_p.append('{0:08b}'.format(ord(x)))   
    bin_p = ''.join(hex_p)
    return bin_p


def get_Polynomial(e, fx, M, C):
    term_1 = fx + M
    term_2 = term_1^e
    ans = term_2 - C
    return ans

def get_key_in_binary(x):
    pp = x[0]
    ans = bin(pp)
    ans = ans[2:]
    return ans


# ## The Copper Hograve algorithm

def Coppersmith_hograve_univariate(X, polynomial, t, modulus, m, beta):   
    
    polynomials = [] # Polynomials    
    polynomial = polynomial.change_ring(ZZ)

    x = polynomial.change_ring(ZZ).parent().gen()
    degree = polynomial.degree()

    for i in range(m):
        for j in range(degree):
            ppop = x*X
            polynomials = polynomials + [ppop**j * polynomial(ppop)**i * modulus**(m - i) ]
            
    for i in range(t):
        ppop = x*X
        polynomials = polynomials + [ppop**i * polynomial(ppop)**m]
       
    y = t + m* degree
    lattice_B = Matrix(ZZ, y) 
    
    polynomial = 0
    for i in range(y):
        for j in range(i+1):
            lattice_B[i, j] = polynomials[i][j]
    lattice_B = lattice_B.LLL() 
    
    for i in range(y):
        term_1 = x**i
        term_2 = X**i
        polynomial = polynomial + term_1 * lattice_B[0, i] / term_2

    possible_roots = polynomial.roots() 
    
    roots = [] 
    for root in possible_roots:
        if root[0].is_integer():
            result = polynomial(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots = roots+[ZZ(root[0])]

    return roots


def init():
    unicode_p = get_unicode(p) 
    beta = 1
    eps = beta/7
    label = 0
    return unicode_p,beta,eps,label


# ## RSA Algorithm for final answer


def run_RSA_Algo(N, e, p, C, len_M):
    unicode_p,beta,eps,label=init()
    
    for i in range(0, len_M+1, 4):
        pop = 2**i
        fx = (int(unicode_p, 2 )*pop) 
        P.<M> = PolynomialRing(Zmod(N))
        poly = get_Polynomial(e, fx, M, C)
        m = calculate_m(poly)    
        x = calculate_x(poly, N)
        t = calculate_t(beta, m, poly )
        
        roots = Coppersmith_hograve_univariate(x, poly, t, N, m, beta)     
        if roots:
            return(get_key_in_binary(roots))
  


# ## Parameters


n = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
e = 5 
p = "Enigma: This door has RSA encryption with exponent 5 and the password is "
c = 27134610716011038218289414701061334057796564566307454673763149698383784153702624439723336393385481090925713689618104277351967643197850119631689910812314413574403085220433269257896456369146799855511896598939510231293510611727720682868090266213632324508143584153600406326497375115831653763179010124533130613421
leng = 200


# ## Running the RSA Algorithm

roots = run_RSA_Algo(n, e, p, c, leng)
roots = '0' + roots


# ## changing binary root to its Ascii value to get the password


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


print("Password for this assignment is : " ,text_from_bits(roots))
