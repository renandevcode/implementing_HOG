# Histogram of Oriented Gradients (HOG)

## Introdução à Visão Computacional

Este repositório tem como objetivo explicar, de forma **didática e visual**, o funcionamento do **Histogram of Oriented Gradients (HOG)**, um dos descritores de características mais clássicos da Visão Computacional.

O foco aqui é **entender o conceito**, e não apenas usar a técnica como uma “caixa preta”.

---

## Como o computador enxerga uma imagem

Diferente dos humanos, computadores **não interpretam imagens semanticamente**.  
Eles não veem objetos, frutas ou pessoas — apenas **números organizados em uma matriz**.

Esses números representam **pixels**.

### O que é um pixel?

Um pixel é a menor unidade de uma imagem digital.  
Em imagens em tons de cinza, cada pixel representa um valor de intensidade (do preto ao branco).  
Em imagens coloridas, cada pixel é composto por valores de **vermelho, verde e azul (RGB)**.

Podemos imaginar os pixels como **pequenos quadrados de cor** que, juntos, formam a imagem completa.

---

## Exemplo visual: imagem de uma maçã

Abaixo podemos analisar melhor a formação da imagem por pixels
<img width="882" height="281" alt="image" src="https://github.com/user-attachments/assets/b912771e-1685-4d52-bb0f-305f86110f56" />


Ao aproximar a imagem, fica claro que ela é composta por **pequenos blocos quadrados**, que são os pixels.  
É exatamente sobre essa estrutura que os algoritmos de visão computacional operam.

---

## O que é o HOG?

O **Histogram of Oriented Gradients (HOG)** é um **descritor de características** usado para:

- detecção de objetos
- reconhecimento de padrões
- análise de formas e contornos

Em vez de trabalhar diretamente com os valores brutos dos pixels, o HOG analisa algo mais informativo:

> **as variações de intensidade da imagem**, chamadas de **gradientes**.

---

## Gradientes: a base do HOG
<img width="422" height="310" alt="image" src="https://github.com/user-attachments/assets/9d373510-c121-4369-a9f4-1d2686d721c3" />


Um **gradiente** indica:
- **quanto** a intensidade muda (gradient magnitude)
- **em qual direção** essa mudança acontece(gradient direction)

Em regiões homogêneas da imagem, os gradientes são fracos, devido a baixa variação de magnitude  
Em regiões onde há bordas ou transições fortes (como o contorno da maçã), os gradientes são intensos.

Esses gradientes carregam informações importantes sobre a **estrutura geométrica** da imagem.

---

## Células (Cells)

Para organizar essas informações, o HOG divide a imagem em pequenas regiões chamadas de **células**.

- Tamanho comum: **8×8 pixels**
- Em cada célula:
  - calcula-se o gradiente de cada pixel
  - cria-se um **histograma de orientações**
  - cada bin representa um intervalo de ângulos (ex.: 0–180°)

O resultado é uma representação local da estrutura da imagem.

---

## Blocos (Blocks) e normalização

As células são então agrupadas em **blocos**, normalmente de:

- **2×2 células**
- totalizando **16×16 pixels**

O papel do bloco é **normalizar os valores** das células, tornando o descritor mais robusto a variações de iluminação e contraste.

Os blocos são **sobrepostos**, o que melhora a estabilidade do descritor.

---

<img width="388" height="472" alt="image" src="https://github.com/user-attachments/assets/ee9d40b8-2d81-4ad7-a086-b08d3af336fd" />


## Vetor final de características

Após processar toda a imagem:

1. cada bloco gera um vetor normalizado
2. todos esses vetores são concatenados
3. forma-se um **grande vetor numérico**

Esse vetor é a **representação HOG da imagem**.

> O HOG não reconhece objetos sozinho.  
> Ele apenas transforma a imagem em uma **assinatura numérica baseada em gradientes**.

---

## Classificação

Esse vetor HOG pode ser enviado para um classificador, como:

- SVM (Support Vector Machine)

O classificador aprende padrões estatísticos desses vetores e decide, por exemplo, se a imagem contém:
- uma maçã
- uma pessoa
- ou outro objeto

---

## Conclusão

O HOG é uma técnica clássica, eficiente e conceitualmente importante porque:

- ensina como imagens podem ser descritas matematicamente
- mostra a separação entre **extração de características** e **classificação**
- ajuda a entender a base de métodos mais modernos, como CNNs

Mesmo com o avanço das redes neurais, o HOG continua sendo uma excelente ferramenta **educacional** e histórica na Visão Computacional.

---
