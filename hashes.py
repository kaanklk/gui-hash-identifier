algorithmlist = []


def compare_algorithms(hash):
    # SHA-1
    size = "86f7e437faa5a7fce15d1ddcb9eaeaea377667b8"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA-1")

    # SHA-224
    size = "abd37534c7d9a2efb9465de931cd7055ffdb8879563ae98078d6d6d5"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA-224")

    # SHA-256
    size = "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA-256")

    # SHA-384
    size = "54a59b9f22b0b80880d8427e548b7c23abd873486e1f035dce9cd697e85175033caa88e6d57bc35efae0b5afd3145f31"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA-384")

    # SHA-512
    size = "1f40fc92da241694750979ee6cf582f2d5d7d28e18335de05abc54d0560e0f5" \
           "302860c652bf08d560252aa5e74210546f369fbbbce8c12cfc7957b2652fe9a75"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA-512")

    # SHA3-224
    size = "9e86ff69557ca95f405f081269685b38e3a819b309ee942f482b6a8b"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA3-224")

    # SHA3-256
    size = "80084bf2fba02475726feb2cab2d8215eab14bc6bdd8bfb2c8151257032ecd8b"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA3-256")

    # SHA3-384
    size = "1815f774f320491b48569efec794d249eeb59aae46d22bf77dafe25c5edc28d7ea44f93ee1234aa88f61c91912a4ccd9"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA3-384")

    # SHA3-512
    size = "80084bf2fba02475726feb2cab2d8215eab14bc6bdd8bfb2c8151257032ecd8b"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA3-512")

    return algorithmlist


def clear_algo_list():
    algorithmlist.clear()
