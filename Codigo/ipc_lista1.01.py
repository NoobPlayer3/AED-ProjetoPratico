#include <iostream>

class Conteiner{
int nome;
};

class No{
public:
    Conteiner item;
    No *prox;

};


class Pilha{

public:
    No *topo,*fundo;
    Pilha *prox;

    Pilha(){
        fundo = new No();
        fundo->prox= NULL;
        topo = fundo;
        prox = NULL;
    }

    void empilhar(Pilha P, Conteiner x){
        No *aux;
        aux = new No();
        P.topo->item = x;
        aux->prox = P.topo;
        P.topo = aux;
    }

    void desempilhar(Pilha P, Conteiner x){
        No *aux;
        aux = P.topo;
        P.topo = P.topo->prox;
        x = P.topo->item;
        delete(aux);
    }
    
    void busca(Pilha P, Conteiner x){
        
    }
};

class Lista{

Pilha *prim,*ult;

    void cria(Lista L, Pilha P){
        L.prim = new Pilha(P);
        L.ult = L.prim;
    }
    void insere(Lista L, Pilha P){
        L.ult->prox = new Pilha(P);
        L.ult = L.ult->prox;
        L.ult->prox = NULL;
    }

};


using namespace std;

int main()
{


}
