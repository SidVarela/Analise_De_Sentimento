###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF968 -- Programacao 1
#
# Autor:   Sidarta Varela
#
# Email:    sllv@cin.ufpe.br
#
# Data:        2016-21-06
#
# Descricao:  Este e' um modelo de arquivo para ser utilizado para a implementacao
#                do projeto pratico da disciplina de Programacao 1. 
#                 A descricao do projeto encontra-se no site da disciplina e trata-se
#                de uma adaptacao do projeto disponivel em 
#                http://nifty.stanford.edu/2016/manley-urness-movie-review-sentiment/
#                O objetivo deste projeto e' implementar um sistema de analise de
#                sentimentos de comentarios de filmes postados no site Rotten Tomatoes.
#
# Licenca: The MIT License (MIT)
#            Copyright(c) 2016 Sidarta Leoni Lins Varela
#
###############################################################################


import sys
import re

def split_on_separators(original, separators):
    return filter(lambda x: x != '',re.split('[{0}]'.format(separators),original))
                    
def limpar(s):
    punctuation = ''''!"',;:.-?)([]<>*#\n\t\r'''
    result = s.lower().strip(punctuation)
    return result

stopwords = open('stopwords.txt','r')
listaStop = stopwords.readlines()

for word in listaStop :
    wordd = limpar(listaStop.pop(0))
    listaStop.append(wordd) 




def readTrainingSet(fname):
    treino = open(fname,'r')
    words = dict()
    listaTreino = treinamento.readlines()
    listaPalavras = []

    for linha in listaTreino:
        palavrasSeparadas = list(split_on_separators(linha[2:]," ")) #Separando as palavras
        for palavra in palavrasSeparadas:
            palavra = limpar(palavra) #Limpando as palavras(pontuação removida e letras padronizadas)
            if palavra != "" and palavra not in stopLista: #Conferindo se a palavra é válida, e armazenando na lista.
                listaPalavras.append(palavra)
                listaPalavras.append(int(linha[0]))

    notas = [0,1,2,3,4] #Valores possíveis para os comentários.

    for palavra in listaPalavras:
        if palavra not in notas: #Triagem para não receber as notas
            listaEscores = []
            frequencia = listaPalavras.count(palavra)
            i = 0

            while i < frequencia:
                sentimento = listaPalavras[(listaPalavras.index(palavra)+1)]
                listaEscores.append(sentimento)
                listaPalavras.remove(palavra)
                i = i+1
            escore = sum(listaEscore)/frequencia
            words[palavra] = (frequencia,escore)

        sentimento = 0 #Zerando para a próxima iteração
        frequencia = 0 #O mesmo aqui.
        

    return words


def readTestSet(fname):
    reviews = []    #Comentários separados e sem acento.
    reviews2 = [] #Comentários em sua forma original.

    comentario = []

    testSet = open(fname,"r")
    lista_testSet = testSet.readlines()
    
    for linha in lista_testSet :
        reviews2.append((int(linha[0]), linha[2:])) #guarda o escore (posicao 0) e o comentario na lista

    for x in reviews2 :
        palavras_separadas = list(split_on_separators(x[1]," ")) 

        for palavra in palavras_separadas:
            palavra = limpar(palavra)
            if palavra != "" : #Conferindo se é uma palavra válida.
                comentario.append(palavra)

        reviews.append((int(x[0]), comentario))
        comentario = [] #Reiciando a lista para a próxima iteração.

    return reviews

def computeSentiment(review,words):
    listaEscores = []
    frase = review[1]
    count = len(review[1])

    for palavra in frase:
        if palavra not in word.keys(): #Ou seja, se a palavra não apareceu no treino...
            escore = 2
            listaEscores.append(escore)
        else:
            escore = words[palavra][1]
            listaEscores.append(escore)
    score = sum(listaEscores)

    return score/count

def QuadradoDosErros(reviews,words):
    diferencaTotal = 0
    for comentario in reviews:
        sentimento = computeSentiment(comentario,words)
        escoreFinal= comentario[0]
        diferenca = sentimento - escoreFinal
        errosErros = diferenca * diferenca #errosErros é Quadrado dos erros :D
        diferencaTotal = diferencaTotal * errosErros 

    comentariosTotal = len(reviews)

    sse = diferencaTotal/comentariosTodos

    return sse


def main():
    if len(sys.argv) < 3:
        print ("Numero invalido de argumentos")
        print ("O programa deve ser executado como python sentiment_analysis.py <arq-treino> <arq-teste>")
        sys.exit(0)

    words = readTrainingSet(sys.argv[1])

    reviews = readTestSet(sys.argv[2])
        
    sse = QuadradosDosErros(reviews,words)
    
    print ('A soma do quadrado dos erros e\': {0}'.format(sse))
            

if __name__ == '__main__':
   main()
   
