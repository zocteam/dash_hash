#include "zeroone.h"
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdio.h>
#include "sha3/neoscrypt.h"

void zeroone_hash(const char* input, int len, char* output)
{
    uint32_t hash[16];
    unsigned int profile = 0x0;
    neoscrypt((unsigned char *) input,(unsigned char *) hash, profile);
    memcpy(output, hash, 32);
}
