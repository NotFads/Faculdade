#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Estrutura para um contato
typedef struct Contato {
    char nome[50];
    char celular[15];
    struct Contato* esquerda;
    struct Contato* direita;
} Contato;

// Protótipos das funções
Contato* inserir(Contato* raiz, Contato* novo);
Contato* buscar(Contato* raiz, const char* nome);
Contato* remover(Contato* raiz, const char* nome);
void ImprimirArvoreDeContatos(Contato* raiz);
void menu();

// Função auxiliar para encontrar o menor nó (usada na remoção)
Contato* encontrarMinimo(Contato* node) {
    Contato* atual = node;
    // Percorre para encontrar a folha mais à esquerda
    while (atual && atual->esquerda != NULL) {
        atual = atual->esquerda;
    }
    return atual;
}

int main() {
    Contato* raiz = NULL;
    int opcao;

    do {
        menu();
        scanf("%d", &opcao);

        switch (opcao) {
            case 1: {
                // Adicionar contato
                Contato* novo = (Contato*)malloc(sizeof(struct Contato));
                if (novo == NULL) {
                    printf("Erro ao alocar memória.\n");
                    break;
                }
                printf("Nome: ");
                scanf("%s", novo->nome);
                printf("Celular: ");
                scanf("%s", novo->celular);
                novo->esquerda = NULL;
                novo->direita = NULL;
                
                raiz = inserir(raiz, novo);
                printf("Contato inserido com sucesso!\n");
                break;
            }
            case 2: {
                // Buscar contato
                char nome[50];
                printf("Nome para buscar: ");
                scanf("%s", nome);
                Contato* encontrado = buscar(raiz, nome);
                if (encontrado) {
                    printf("\n--- Contato Encontrado ---\n");
                    printf("Nome: %s\nCelular: %s\n", encontrado->nome, encontrado->celular);
                    printf("--------------------------\n");
                } else {
                    printf("Contato não encontrado.\n");
                }
                break;
            }
            case 3: {
                // Remover contato
                char nome[50];
                printf("Nome para remover: ");
                scanf("%s", nome);
                raiz = remover(raiz, nome);
                printf("Operação de remoção finalizada.\n");
                break;
            }
            case 4: {
                // Imprimir contatos
                printf("\n--- Lista de Contatos (Ordem Alfabética) ---\n");
                ImprimirArvoreDeContatos(raiz);
                printf("--------------------------------------------\n");
                break;
            }
            case 5:
                printf("Saindo...\n");
                break;
            default:
                printf("Opção inválida! Tente novamente.\n");
        }
    } while (opcao != 5);

    return 0;
}

// --- IMPLEMENTAÇÃO DAS FUNÇÕES ---

// 1. Inserir: Coloca menores à esquerda e maiores à direita (ordem alfabética)
Contato* inserir(Contato* raiz, Contato* novo) {
    // Se a árvore estiver vazia, o novo nó é a raiz
    if (raiz == NULL) {
        return novo;
    }

    // Compara strings: strcmp retorna < 0 se novo->nome vier antes de raiz->nome
    if (strcmp(novo->nome, raiz->nome) < 0) {
        raiz->esquerda = inserir(raiz->esquerda, novo);
    } 
    else if (strcmp(novo->nome, raiz->nome) > 0) {
        raiz->direita = inserir(raiz->direita, novo);
    }
    else {
        printf("Erro: Já existe um contato com este nome.\n");
    }

    return raiz;
}

// 2. Buscar: Navega pela árvore comparando os nomes
Contato* buscar(Contato* raiz, const char* nome) {
    // Caso base: raiz é nula ou nome encontrado
    if (raiz == NULL || strcmp(raiz->nome, nome) == 0) {
        return raiz;
    }

    // Se o nome buscado for menor, vai para esquerda
    if (strcmp(nome, raiz->nome) < 0) {
        return buscar(raiz->esquerda, nome);
    }

    // Caso contrário, vai para direita
    return buscar(raiz->direita, nome);
}

// 3. Remover: Lida com casos de nó folha, nó com 1 filho ou nó com 2 filhos
Contato* remover(Contato* raiz, const char* nome) {
    if (raiz == NULL) return raiz;

    // Procura o nó a ser removido
    if (strcmp(nome, raiz->nome) < 0) {
        raiz->esquerda = remover(raiz->esquerda, nome);
    } 
    else if (strcmp(nome, raiz->nome) > 0) {
        raiz->direita = remover(raiz->direita, nome);
    } 
    else {
        // Nó encontrado! Vamos remover.
        
        // Caso 1 e 2: Nó com um filho ou nenhum filho
        if (raiz->esquerda == NULL) {
            Contato* temp = raiz->direita;
            free(raiz);
            return temp;
        } else if (raiz->direita == NULL) {
            Contato* temp = raiz->esquerda;
            free(raiz);
            return temp;
        }

        // Caso 3: Nó com dois filhos
        // Encontra o sucessor (menor nó da subárvore à direita)
        Contato* temp = encontrarMinimo(raiz->direita);

        // Copia os dados do sucessor para este nó
        strcpy(raiz->nome, temp->nome);
        strcpy(raiz->celular, temp->celular);

        // Remove o sucessor original
        raiz->direita = remover(raiz->direita, temp->nome);
    }
    return raiz;
}

// 4. Listar: Percurso "Em Ordem" (In-Order) para imprimir alfabeticamente
void ImprimirArvoreDeContatos(Contato* raiz) {
    if (raiz != NULL) {
        ImprimirArvoreDeContatos(raiz->esquerda); // Visita esquerda
        printf("Nome: %-20s | Celular: %s\n", raiz->nome, raiz->celular); // Visita raiz
        ImprimirArvoreDeContatos(raiz->direita);  // Visita direita
    }
}

void menu() {
    printf("\nMenu:\n");
    printf("1. Adicionar contato\n");
    printf("2. Buscar contato\n");
    printf("3. Remover contato\n");
    printf("4. Listar contatos\n");
    printf("5. Sair\n");
    printf("Escolha uma opção: ");
}