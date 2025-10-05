#include <stdio.h>
#include <string.h>
#include <stdbool.h>

typedef struct 
{
    char nome[50];
    int idade;
}Pessoa;

void imprimirDados(Pessoa p)
{
    printf("Nome: %s\n", p.nome);
    printf("Idade: %d\n", p.idade);
}

void imprimirDadosRef(const Pessoa *p)
{
    printf("Nome: %s\n", p->nome);
    printf("Idade: %d\n", p->idade);
}

const char* pessoaMaisVelha(const Pessoa *pessoa1,const Pessoa *pessoa2)
{
    if (pessoa1->idade > pessoa2->idade)
    {
        return pessoa1->nome;
    }
    else
    {
        return pessoa2->nome;
    }
}

bool verificarMaioridade(Pessoa p)
{
    if(p.idade >= 18)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void 


int main(int argc, char const *argv[])
{
    Pessoa p1;
    strcpy(p1.nome, "Felipe Augusto");
    p1.idade = 18;
    Pessoa p2;
    strcpy(p2.nome, "Lorenzo");
    p2.idade = 12;
    imprimirDados(p1);
    imprimirDadosRef(&p1);
    printf("A pessoa mais velha e o(a) %s\n",pessoaMaisVelha(&p1,&p2));
    if(verificarMaioridade(p1))
    {
        printf("O(A) %s e maior de idade.",p1.nome);
    }
    else
    {
        printf("O(A) %s nao e maior de idade.",p1.nome);
    }

    int num_pessoas = 3;
    Pessoa pessoasVet[num_pessoas];
    strcpy(pessoasVet[0].nome, "Thais");
    pessoasVet[0].idade = 47;
    strcpy(pessoasVet[1].nome, "Hermes");
    pessoasVet[1].idade = 1;
    strcpy(pessoasVet[2].nome, "Nega");
    pessoasVet[2].idade = 15;
    return 0;
}
