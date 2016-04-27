#include <iostream>

class Conteiner{
private:
    int nome;

public:
    void setNome(int pNome){
        this->nome = pNome;
    }

    int getNome(){
        return this->nome;
    }
};

class No{
public:
    Conteiner item;
    No *proxNo;
    No(){}

};


class Pilha{

public:
    No *topo,*fundo;
    Pilha *proxPilha;

    Pilha(){
        this->fundo = new No();
        this->fundo->proxNo = NULL;
        this->topo = this->fundo;
        this->proxPilha = NULL;
    }

    void empilhar(Pilha P, Conteiner pItem){
        No *aux;
        aux = new No();
        P.topo->item = pItem;
        aux->proxNo = P.topo;
        P.topo = aux;
    }

    void desempilhar(Pilha P, Conteiner pItem){
        No *aux;
        aux = P.topo;
        P.topo = P.topo->proxNo;
        pItem = P.topo->item;
        delete(aux);
    }

    bool busca(Pilha P, Conteiner pItem){
        No *p = P.topo->proxNo;
        while ((p != NULL) && (p->item.getNome() != pItem.getNome())){
            p = p->proxNo;
        }
        if (p == NULL){
            return true;
        } else {
            return false;
        }
    }
};

class Lista{

Pilha *prim,*ult;

    void cria(Lista L, Pilha P){
        L.prim = new Pilha(P);
        L.ult = L.prim;
    }
    void insere(Lista L, Pilha P){
        L.ult->proxPilha = new Pilha(P);
        L.ult = L.ult->proxPilha;
        L.ult->proxPilha = NULL;
    }

};


class Fila{

No *frente, *tras;

    Fila(){
        this->frente = new No();
        this->tras = this->frente;
        this->frente->proxNo = NULL;
    }

    void enfileira(Fila F, Conteiner Pitem){
        F.tras->proxNo = new No();
        F.tras = F.tras->proxNo;
        F.tras->item = Pitem;
        F.tras->proxNo = NULL;
    }

    void desenfilera(Fila F, Conteiner pItem){
        No *aux = F.frente;
        F.frente = F.frente->proxNo;
        pItem = F.frente->item;
        delete(aux);
    }


};


using namespace std;

int main(){





}




