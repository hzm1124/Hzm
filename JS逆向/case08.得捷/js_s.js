function get_s(e) {
    var t = 6;
    var r = function (e) {return 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-$'.charAt(e)};

    function _compress(e, t, r) {
    if (null == e)
        return "";
    var n, o, i, a = {}, s = {}, l = "", u = "", c = "", f = 2, d = 3, p = 2, g = [], h = 0, v = 0;
    for (i = 0; i < e.length; i += 1)
        if (l = e.charAt(i),
        Object.prototype.hasOwnProperty.call(a, l) || (a[l] = d++,
            s[l] = !0),
            u = c + l,
            Object.prototype.hasOwnProperty.call(a, u))
            c = u;
        else {
            if (Object.prototype.hasOwnProperty.call(s, c)) {
                if (256 > c.charCodeAt(0)) {
                    for (n = 0; n < p; n++)
                        h <<= 1,
                            v == t - 1 ? (v = 0,
                                g.push(r(h)),
                                h = 0) : v++;
                    for (n = 0,
                             o = c.charCodeAt(0); n < 8; n++)
                        h = h << 1 | 1 & o,
                            v == t - 1 ? (v = 0,
                                g.push(r(h)),
                                h = 0) : v++,
                            o >>= 1
                } else {
                    for (n = 0,
                             o = 1; n < p; n++)
                        h = h << 1 | o,
                            v == t - 1 ? (v = 0,
                                g.push(r(h)),
                                h = 0) : v++,
                            o = 0;
                    for (n = 0,
                             o = c.charCodeAt(0); n < 16; n++)
                        h = h << 1 | 1 & o,
                            v == t - 1 ? (v = 0,
                                g.push(r(h)),
                                h = 0) : v++,
                            o >>= 1
                }
                0 == --f && (f = Math.pow(2, p),
                    p++),
                    delete s[c]
            } else
                for (n = 0,
                         o = a[c]; n < p; n++)
                    h = h << 1 | 1 & o,
                        v == t - 1 ? (v = 0,
                            g.push(r(h)),
                            h = 0) : v++,
                        o >>= 1;
            0 == --f && (f = Math.pow(2, p),
                p++),
                a[u] = d++,
                c = String(l)
        }
    if ("" !== c) {
        if (Object.prototype.hasOwnProperty.call(s, c)) {
            if (256 > c.charCodeAt(0)) {
                for (n = 0; n < p; n++)
                    h <<= 1,
                        v == t - 1 ? (v = 0,
                            g.push(r(h)),
                            h = 0) : v++;
                for (n = 0,
                         o = c.charCodeAt(0); n < 8; n++)
                    h = h << 1 | 1 & o,
                        v == t - 1 ? (v = 0,
                            g.push(r(h)),
                            h = 0) : v++,
                        o >>= 1
            } else {
                for (n = 0,
                         o = 1; n < p; n++)
                    h = h << 1 | o,
                        v == t - 1 ? (v = 0,
                            g.push(r(h)),
                            h = 0) : v++,
                        o = 0;
                for (n = 0,
                         o = c.charCodeAt(0); n < 16; n++)
                    h = h << 1 | 1 & o,
                        v == t - 1 ? (v = 0,
                            g.push(r(h)),
                            h = 0) : v++,
                        o >>= 1
            }
            0 == --f && (f = Math.pow(2, p),
                p++),
                delete s[c]
        } else
            for (n = 0,
                     o = a[c]; n < p; n++)
                h = h << 1 | 1 & o,
                    v == t - 1 ? (v = 0,
                        g.push(r(h)),
                        h = 0) : v++,
                    o >>= 1;
        0 == --f && (f = Math.pow(2, p),
            p++)
    }
    for (n = 0,
             o = 2; n < p; n++)
        h = h << 1 | 1 & o,
            v == t - 1 ? (v = 0,
                g.push(r(h)),
                h = 0) : v++,
            o >>= 1;
    for (; ;) {
        if (h <<= 1,
        v == t - 1) {
            g.push(r(h));
            break
        }
        v++
    }
    return g.join("")
};

    return _compress(e, t, r);
}

var e = '{"5":{"p":12,"pp":25}}';
console.log(get_s(e));
