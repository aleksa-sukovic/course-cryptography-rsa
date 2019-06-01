# RSA Algorithm

This is my implementation of RSA algorithm.

This project was done as an assignment task for my *Cryptography* college course.

## Features

Idea was to enable user to set-up RSA system, encrypt and decrypt data. According to that, user can do the following:

1. Generate a prime number(s) of arbitrary bit length.
    * I am using MIller-Rabin algorithm for testing primality of a number.
2. Set up RSA system.
    * Generates all of the parameters needed for RSA encryption and decryption:
        * Two prime numbers *p* and *q*.
        * Number *N* such that *N=p * q*.
        * Totient function of *N*, *Phi(N) = (p-1) * (q - 1)*
        * Exponent *e* such that *e* must be:
            * Whole number.
            * Can not divide *N*.
            * *1 < e < Phi(N)*.
        * Private key *d* such that *d = (k * Phi(N) + 1) / e* where *k* can be an arbitrary integer.
3. Encrypt data.
    * Given the public key par (N, e) user can encrypt given text.
    * User can load text to be encrypted from keyboard or from a file.
    * User can choose to print encrypted text to console and/or save it to a file.
4. Decrypt data.
    * Given a pair (N, d) user can decrypt given encrypted content.
    * User can load encrypted text from keyboard or from a file.
    * User can choose to print decrypted text to console and/or save it to a file.

## How to set-up ?
The following commands will build and run Docker image.

Docker image is configure to run indefinitely, so you can execute interactive bash process against running container anytime to gain full control.

1. `cd .docker`
2. `docker-compose build`
3. `docker-compose up`
4. `docker exec -it $(docker ps -qf "name=python") bash`
5. `python main.py`

If you want to create executable, you can run (from inside of the container):

`pyinstaller main.py --onefile`

## What have I learned ?
1. RSA algorithm (principles behind it).
2. Miller-Rabin primality test.
3. Python (my first project using this language).
