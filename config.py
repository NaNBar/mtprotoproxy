PORT = 420

# name -> secret (32 hex chars)
USERS = {
    "tg":  "9d4ea9da397079266000cc26d6b30bd5",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "www.cloudflare.com"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "b306c7fb16359572a01e7a5732863036"
