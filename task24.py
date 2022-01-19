class Drivinglicense:
    def __init__(self ,adhaar_card,tenth_certificate,photo_copy, signature):
        self.z= adhaar_card
        self.x= tenth_certificate
        self.c=photo_copy
        self.v= signature
    def output(self):
        print('your adha_card number is:',self.z)
        print('your tenth_certificate is:',self.x)
        print('your photo_copy is:',self.c)
        print('your signature is:',self.v)
while True:
    a= input('enter adhaarcard: ')
    s= input('enter the tenth_certificate')
    d= input('enter photo_copy:')
    f = input('enter the signature:')
    oreo=Drivinglicense(a, s, d, f)
    oreo.output()