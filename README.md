# CLI Ciphering tool

## Introduction

> This is a command line tool that let you interactively encrypt or decrypt strings using a chosen cipher algorithm. 

## Installation

> 1- Before running the tool make sure you have **docker** and **docker-compose** installed. <br  />
2- Open a terminal in the cloned repository directory. <br />
3- Run ```sudo docker-compose build && sudo docker-compose run cipher```

## To run unit tests for shift and matrix ciphers

> 1- Open a terminal in the cloned repository directory <br />
  2- Run ```python test_shift_cipher.py``` for shift cipher <br />
  3- Run ```python test_matrix_cipher.py``` for matrix cipher <br />

## A running example
>
```
String to be encrypted or decrypted: hello world
Matrix to be decrypted only works with matrix cipher [()]: 1 2 3 --> this is only used in when decryption is chosen with matrix cipher!
Algorithm name to be used (Shift, Matrix, Reverse): Matrix
Method to be used (Encrypt, Decrypt): Encrypt
The encrypted result is: 6.0 13.0 6.0 17.0 11.0 15.0 11.0 14.0 18.0 7.0 12.0 12.0 15.0 19.0 15.0 22.0 
11.0 22.0 18.0 25.0 14.0 23.0 12.0 17.0 22.0 11.0 19.0 15.0 21.0 29.0 18.0 22.0 
12.0 19.0 13.0 25.0 16.0 22.0 16.0 19.0 24.0 9.0 21.0 18.0 24.0 26.0 22.0 31.0 
12.0 19.0 13.0 25.0 16.0 22.0 16.0 19.0 24.0 9.0 21.0 18.0 24.0 26.0 22.0 31.0 
15.0 24.0 20.0 35.0 25.0 29.0 24.0 19.0 35.0 20.0 25.0 24.0 31.0 36.0 27.0 38.0 
1.0 7.0 3.0 6.0 0.0 9.0 3.0 5.0 3.0 6.0 4.0 4.0 2.0 5.0 3.0 5.0 
15.0 30.0 19.0 30.0 29.0 29.0 20.0 21.0 30.0 24.0 25.0 30.0 27.0 37.0 21.0 35.0 
15.0 24.0 20.0 35.0 25.0 29.0 24.0 19.0 35.0 20.0 25.0 24.0 31.0 36.0 27.0 38.0 
9.0 19.0 5.0 16.0 21.0 15.0 12.0 16.0 20.0 19.0 16.0 24.0 16.0 21.0 12.0 26.0 
12.0 19.0 13.0 25.0 16.0 22.0 16.0 19.0 24.0 9.0 21.0 18.0 24.0 26.0 22.0 31.0 
11.0 17.0 11.0 19.0 11.0 16.0 9.0 17.0 18.0 8.0 19.0 15.0 19.0 20.0 16.0 22.0
``` <br />

## A reverse running example
>
```
String to be encrypted or decrypted: siso
Matrix to be decrypted only works with matrix cipher [()]: 6 13 6 17 11 15 11 14 18 7 12 12 15 19 15 22 11 22 18 25 14 23 12 17 22 11 19 15 21 29 18 22 12 19 13 25 16 22 16 19 24 9 21 18 24 26 22 31 15 24 20 35 25 29 24 19 35 20 25 24 31 36 27 38 1 7 3 6 0 9 3 5 3 6 4 4 2 5 3 5 15 30 19 30 29 29 20 21 30 24 25 30 27 37 21 35 15 24 20 35 25 29 24 19 35 20 25 24 31 36 27 38 9 19 5 16 21 15 12 16 20 19 16 24 16 21 12 26 12 19 13 25 16 22 16 19 24 9 21 18 24 26 22 31 11 17 11 19 11 16 9 17 18 8 19 15 19 20 16 22
Algorithm name to be used (Shift, Matrix, Reverse): Matrix
Method to be used (Encrypt, Decrypt): Decrypt
The decrypted result is: helo world
````
NOTE: The input stream of the matrix to be decrypted that will be used in case of matrix decryption must be a multiple of 16!.



## Docker Image

> The docker image for this app is based on the ubuntu 16.04 base image and uses python 3.7.
