from hashlib import md5


def get_sign(d, e, u, t):
    md5_ = md5()

    md5_.update(f'client={d}&mysticTime={e}&product={u}&key={t}'.encode())
    sign = md5_.hexdigest()

    print(f'sign: {sign}')

    return sign
