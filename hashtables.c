#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define the structure for a hash table entry
typedef struct HashNode {
    char *key;
    char *value;
    struct HashNode *next;
} HashNode;
