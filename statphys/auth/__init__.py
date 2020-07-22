import os
import pkg_resources
import pickle
import hmac
import hashlib

passwd = '04e44b792a2bde78b7f7c890d048948a4f611e52'
data = b'\x80\x03}q\x00(X\r\x00\x00\x00junghoon jungq\x01J\xa3\x9a\xad\x17X\x0b\x00\x00\x00chulung wooq\x02J\xb8?\xda@X\x0b\x00\x00\x00gyoheon leeq\x03JT\x0f\xc3Bu.'

if hmac.new(b'statphys_lab', data, hashlib.sha1).hexdigest() == passwd: #sha1 encrypt
    users = pickle.loads(data)
else:
    raise Warning("Data curruption.")

def auth_user():
    '''user identifying.'''
    global users
    #refer  configure of home
    home = os.path.expanduser('~')
    if os.path.isfile(os.path.join(home, '.statphys_bot','config')):
        with open(os.path.join(home, '.statphys_bot','config')) as f:
            name = f.readline().rstrip()
    else:
        name = input("Please let me know your name : ")

        if name in users:                                                   # check user list
            os.makedirs(os.path.join(home, '.statphys_bot'), exist_ok = True)  # make configure folder
            with open(os.path.join(home, '.statphys_bot','config'),'w') as f:   # save user name
                f.write(name)
        else:
            raise NameError("Invaild name (If you are member of statphys lab, please let me know).")


    return name, users[name]
