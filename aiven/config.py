import os


def create_pem_file(cwd=os.getcwd()):
    f = open(os.path.join(cwd, 'apps/common/cq.pem'), "w")
    ar_pem = os.environ.get("CA_PEM").split(' ')
    pembegin = f'{ar_pem.pop(0)} {ar_pem.pop(0)}'
    pemend = f'{ar_pem.pop(-2)} {ar_pem.pop()}'
    pembody = f'\n'.join(ar_pem)
    pem = f'\n'.join((pembegin, pembody, pemend))
    f.write(pem)
    f.close()


def delete_pem_at_exit():
    try:
        os.remove(os.path.join(os.getcwd(), 'apps/common/cq.pem'))
    except FileNotFoundError:
        os.remove(os.path.join(os.path.dirname(os.getcwd()), 'apps/common/cq.pem'))
