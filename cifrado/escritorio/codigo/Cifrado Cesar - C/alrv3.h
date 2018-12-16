/*include <stdlib.h>
#include <string.h>
#include <stdio.h>*/

void alrev(char *mensaje,int inicio,int grupo){
  int i,j=0;
  char copia[grupo];
  for(i=inicio;i<inicio+grupo;i++){
    copia[j]=*(mensaje+i);
    j++;
  }
  j=0;
  for(i=inicio;i<inicio+grupo;i++){
    *(mensaje+i)=copia[(grupo-1)-j];
    j++;
  }
}

void alrv(char *mensaje,int grupo){
  //printf("%i\n",grupo );
  int veces=strlen(mensaje)/grupo;
  int indice=0;
  //printf("%i\n",veces);
  for(int j=0;j<veces;j++){
    alrev(mensaje,indice,grupo);
    indice=indice+grupo;
  }
}

/*int main(int argc, char const *argv[]) {*/
  /* code */
  /*char mensaje[]="hola que hace";
  alrv(mensaje);
  printf("%s\n",mensaje );
  return 0;
}*/
