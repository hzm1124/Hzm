require('./webpack')


var a = loader('68b2').sm2.doSignature;

function get_sign_data(r, d) {
    return a(r, d, {'hash': true});
}

var r = 'appCode=T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ&data={"medListCodg":"X","pageNo":"12","pageSize":"10"}&encType=SM4&signType=SM2&timestamp=1754448244&version=1.0.0&key=NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P';
var privateKey = '009c4a35d9aca4c68f1a3fa89c93684347205a4d84dc260558a049869709ac0b42';
console.log(get_sign_data(r, privateKey));
