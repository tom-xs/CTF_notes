#include <stdio.h>

void print_bytes(void *ptr, int size)
{
    unsigned char *p = ptr;
    int i;
    for (i=0; i<size; i++) {
        printf("%02hhX ", p[i]);
    }
    printf("\n");
}

int main(void) {
    char inp[12];
    long x = 0xcafebabe;

    printf("Here's the stack: \x1b[33m");
    print_bytes(inp, 32);
    printf("\x1b[37m");

    scanf("%s", inp);
    printf("Here's the stack now: \x1b[33m");
    print_bytes(inp, 32);
    printf("\x1b[37m");

    if (x == 0x66746369) {
        system("cat flag.txt");
    }

    return 0;
}