import codecs
import os
import sys
import optparse
from base64 import urlsafe_b64encode
from paste.script.copydir import substitute_content

try:
    from hashlib import sha1
except ImportError:
    from sha import sha as sha1

def get_ssha_encoded_string(password):
    """Encode the given `string` using "Secure" SHA.

    Taken from zope.password.password but we cannot depend on that package.
    """
    encoder = codecs.getencoder('utf-8')
    _hash = sha1(encoder(password)[0])
    salt = os.urandom(4)
    _hash.update(salt)
    return b'{SSHA}' + urlsafe_b64encode(_hash.digest() + salt)


def main():
    usage = "usage: %prog [options]"
    parser = optparse.OptionParser(usage=usage)
    # parser.add_option(
    #     '--svn-repository', dest="repos", default=None, help=(
    #     "Import project to given repository location (this "
    #     "will also create the standard trunk/ tags/ branches/ "
    #     "hierarchy)."))
    parser.add_option(
        '-u', '--user', dest="username",  default=None, help=("Provide a user name for the master account"))    
    parser.add_option(
        '-p', '--password', dest="password",  default=None, help=("Provide a password for the master account"))
    
    options, args = parser.parse_args()
    if options.username is None or options.password is None:
        parser.print_help()
        return 1

    username = f'"{options.username}"'
    password = f'"{get_ssha_encoded_string(options.password).decode()}"'
    
    source = "/opt/gserver/etc/site.zcml.in_tmpl"
    with open(source, "r") as f:
        target = source.replace("_tmpl", "")
        content = f.read()
        content = substitute_content(content, {'username':username, 'password':password}, filename=target)
    with open(target, "w") as o:
        o.write(content)
    parts_target = "/opt/gserver/parts/etc/site.zcml"
    with open(parts_target, "w") as o:
        o.write(content)
        

if __name__ == "__main__":
    main()

