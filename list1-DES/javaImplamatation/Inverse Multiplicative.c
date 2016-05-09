//
//  main.c
//  Extended Euclidean Algorithm implemented in language c
//
//  Created by Gustavo Moreira on 18/04/16.
//  Copyright © 2016 Gustavo Moreira. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>

int gcdExtended(int a, int b, int *x, int *y) {

    if (a == 0) {
        *x = 0;
        *y = 1;
        return b;
    }
    
    int x1, y1;
    int gcd = gcdExtended(b%a, a, &x1, &y1);
    
    *x = y1 - (b/a) * x1;
    *y = x1;
    
    return gcd;

}

int main() {
    
    int x, y;
    int a = 0, b = 0;
    
    scanf("%d %d", &a, &b);
    
    int g = gcdExtended(a, b, &x, &y);
    
    if(g == 1) {
        printf("%d\n", x);
    } else if(g != 1) {
        printf("Nao existe\n");
    }
    
    return 0;
}