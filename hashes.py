algorithmlist = []


def compare_algorithms(hash):
    # SHA-1
    size = "86f7e437faa5a7fce15d1ddcb9eaeaea377667b8"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA-1")

    # SHA2-224
    size = "abd37534c7d9a2efb9465de931cd7055ffdb8879563ae98078d6d6d5"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA2-224")

    # SHA2-256
    size = "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA2-256")

    # SHA2-384
    size = "54a59b9f22b0b80880d8427e548b7c23abd873486e1f035dce9cd697e85175033caa88e6d57bc35efae0b5afd3145f31"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA2-384")

    # SHA2-512
    size = "1f40fc92da241694750979ee6cf582f2d5d7d28e18335de05abc54d" \
           "0560e0f5302860c652bf08d560252aa5e74210546f369fbbbce8c12cfc7957b2652fe9a75"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA2-512")

    # SHA2-512/224
    size = "d5cdb9ccc769a5121d4175f2bfdd13d6310e0d3d361ea75d82108327"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA2-512/224")

    # SHA2-512/256
    size = "455e518824bc0601f9fb858ff5c37d417d67c2f8e0df2babe4808858aea830f8"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA2-512/256")

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

    # SHA1 SALTED
    size = "F4B20E635923AC7C955821F90F2EBE85D364CECF"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA-1 (SALTED)")

    # SHA-256 SALTED
    size = "d15ef5ecb8b8be75e9f872e91e519778974e65f5a01902fcc1a55438b5426ac4"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHA-256 (SALTED)")

    # MD2
    size = "32ec01ec4a6dac72c0ab96fb34c0b5d1"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("MD2")

    # MD4
    size = "bde52cb31de33e46245e05fbdbd6fb24"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("MD4")

    # MD5
    size = "0cc175b9c0f1b6a831c399e269772661"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("MD5")

    # MD5 SALTED
    size = "6bcb17ba258af33436a56849a5ae175f"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("MD5 (SALTED)")

    # MD6-128
    size = "0eb5dab7abbebb9f9d245cbb5e15fd52"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("MD6-128")

    # MD6-256
    size = "382879cc51ad935917916f908d118079c801cccaea8ec4629702c3c7f27c97ee"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHAKE - 158 (256 OUTPUT BITS)")

    # MD6-512
    size = "3bc9618bb17d6ac8698cbbff8dcb8178ecfc450bbce461" \
           "a5db98aa63287b0d0c5c04c47f898045ab25a9baa5ea397d4b67feb81c32b351b1a62c706380a20ac1"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("MD6-512")

    # NTLM
    size = "186CB09181E2C2ECAAC768C47C729904"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("NTLM")

    # CRC-16
    size = "e8c1"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("CRC-16")

    # CRC-32
    size = "e8b7be43"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("CRC-32")

    # SHAKE-158 (256 OUTPUT BITS)
    size = "a5ba3aeee1525b4ae5439e54cd711f14850251e02c5999a53f61374c0ae089ef"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHAKE - 158 (256 OUTPUT BITS)")

    # SHAKE-256 (512 OUTPUT BITS)
    size = "5e6812c0bbaaee6440dcc8b81ca6809645f7512e06cf5acb57bd16dc" \
           "3a2bfc57dc2bf9e6d8941950594bef5191d8394691f86edffcad6c5ebad9365f282f37a8"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("SHAKE-256 (512 OUTPUT BITS)")

    # Whirlpool
    size = "3ACB384B67995724469EDC254C71F4FFCB699424606BF018254FAD2E42ED613BD4A" \
           "350453498A354A60DD8BD7C2AD141FB4611A7460A8F50841E569749DC32CA"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("Whirlpool")

    # RIPEMD-128
    size = "86be7afa339d0fc7cfc785e72f578d33"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("RIPEMD-128")

    # RIPEMD-169
    size = "0bdc9d2d256b3ee9daae347be6f4dc835a467ffe"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("RIPEMD-169")

    # RIPEMD-256
    size = "f9333e45d857f5d90a91bab70a1eba0cfb1be4b0783c9acfcd883a9134692925"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("RIPEMD-256")

    # RIPEMD-320
    size = "ce78850638f92658a5a585097579926dda667a5716562cfcf6fbe77f63542f99b04705d6970dff5d"
    if len(hash) == len(size) and hash.isdigit() == False and hash.isalpha() == False and hash.isalnum() == True:
        algorithmlist.append("RIPEMD-320")

    # Adler-32
    size = "00620062"
    if len(hash) == len(size) and hash.isdigit() == True:
        algorithmlist.append("Adler-32")

    return algorithmlist


def clear_algo_list():
    algorithmlist.clear()
