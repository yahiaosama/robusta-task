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


## Docker Image

> The docker image for this app is based on the ubuntu 16.04 base image and uses python 3.7.
