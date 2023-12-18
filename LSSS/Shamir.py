import random
from utils.polynomial import *
class ShamirSS:
    """
    t: threshold
    n: parties
    (t,n): t parits can reconstruct the secret
    degree = t-1
    """
    __t =0
    __n = 0
    __module = 0
    __shares = []

    def __init__(self,t,n,module):
        if t > n:
            raise ValueError("The threshold  should be less than or equal to the total number of shares n.")
        self.__t = t
        self.__n = n
        self.__module = module
    @property
    def t(self):
        return self.__t
    @property
    def n(self):
        return self.__n
    @property
    def module(self):
        return self.__module
    @property
    def shares(self):
        return self.__shares
    @shares.setter
    def shares(self, values):
        self.__shares = values
    def share(self,secret):
        """
        选择一个随机多项式，使得其0点的值=secret
        :param secret:
        :return:
        """
        coef = poly.random_polynomial(self.__t-1,secret,self.__module)
        shares = []
        for i in range(1,self.__n+1):
            shares.append(poly.get_polynomial_points(coef,i,self.__module))
        self.__shares = shares
        return None
    def get_share(self,id):
        return self.__shares[id-1]
    def reconstruct(self, shares):
        """
        :param shares:
        [(x_1,f(x_1)),...,(x_t,f(x_t))]
        :return: f(0)
        """
        return poly.lagrange_interpolation_x(shares, self.__module, 0)
    def add(self,shamirss):
        """
        份额加法
        :param  shamirss: An instance of ShamirSS
        :return: A new instance
        """
        if not self.__t == shamirss.t :
            raise ValueError("t error")
        if not self.__n == shamirss.n :
            raise ValueError("n error")
        if not self.__module == shamirss.module :
            raise ValueError("module error")
        new_share = ShamirSS(self.__t,self.__n,self.__module)
        shares = []
        for i in range(self.__n):
            shares.append((self.__shares[i]+ shamirss.shares[i]) % mod)
        new_share.shares = shares
        return new_share
    def cmult(self,c):
        """
        标量乘
        :param c: Constant
        :return: A new instance
        """
        new_share = ShamirSS(self.__t, self.__n, self.__module)
        shares = []
        for i in range(self.__n):
            shares.append( (self.__shares[i] * c) % self.__module)
        new_share.shares = shares
        return new_share
if __name__ == "__main__":
    print("Test: Shamir")
    secret_1 = 42
    secret_2 = 500
    n =5
    t= 3
    mod = 997

    test_shamir_1 = ShamirSS(t,n,mod)
    test_shamir_2 = ShamirSS(t,n,mod)
    test_shamir_1.share(secret_1)
    test_shamir_2.share(secret_2)
    test_shamir_3 = test_shamir_1.add(test_shamir_2)
    share_1 = []
    share_2 = []
    share_3 = []
    for i in range(1,n+1):
        share_1.append((i,test_shamir_1.get_share(i)))
        share_2.append((i, test_shamir_2.get_share(i)))
        share_3.append((i, test_shamir_3.get_share(i)))
    print("share_1:")
    print(share_1)
    print("share_2:")
    print(share_2)
    print("share_3:")
    print(share_3)
    def random_select_numbers(n, t):
        numbers = list(range(1, n + 1))
        selected_numbers = random.sample(numbers, t)
        return selected_numbers
    #
    parties_id = random_select_numbers(5,3)
    print(parties_id)
    re_share1 = []
    re_share2 = []
    re_share3 = []
    for i in parties_id:
        re_share1.append((i,test_shamir_1.get_share(i)))
        re_share2.append((i,test_shamir_2.get_share(i)))
        re_share3.append((i, test_shamir_3.get_share(i)))
    print(test_shamir_1.reconstruct(re_share1))
    print(test_shamir_2.reconstruct(re_share2))
    print(test_shamir_3.reconstruct(re_share3))







