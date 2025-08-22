#include <stdio.h>

int main(int argc, char const *argv[])
{
    int vec[10] = {1,2,3,4,5,6};
    for(int i = 7; i >= 3; i--)
    {
        vec[i] = vec[i - 1];
    }
    vec[3] = 7;
    for(int i = 2; i < 7; i++)
    {
        vec[i] = vec[i + 1];
    }
    for(int i = 0; i < 10; i++)
    {
        printf("%d\n", vec[i]);
    }
    return 0;
}
