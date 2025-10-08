#include <stdio.h>

// Extern decalration that will prompt compiler to
// search for the variable ext_var in other files
extern int ext_var;

void printExt() {
  	printf("%d", ext_var);
}
int main() {
    printExt();
    return 0;
}