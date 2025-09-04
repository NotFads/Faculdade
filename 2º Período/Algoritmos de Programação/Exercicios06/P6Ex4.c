#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char nome[50],sobrenome[50],str_final[100];
    int len; 

    printf("Entre com o seu nome: ");
    scanf(" %[^\n]",&nome);
    printf("Entre com o seu sobrenome: ");
    scanf(" %[^\n]", &sobrenome);
    str_final = strcat(nome,sobrenome);
    len = strlen(str_final);
    printf("%s\n%d\n%c %c",str_final,len,str_final[0],str_final[len]);

    return 0;
}
