       IDENTIFICATION DIVISION.
       PROGRAM-ID. Soma.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 NUM1 PIC 9(4).
       01 NUM2 PIC 9(4).
       01 SOMA PIC 9(4).

       PROCEDURE DIVISION.
           DISPLAY "Digite o primeiro número: " WITH NO ADVANCING
           ACCEPT NUM1

           DISPLAY "Digite o segundo número: " WITH NO ADVANCING
           ACCEPT NUM2

           COMPUTE SOMA = NUM1 + NUM2

           DISPLAY "A soma de " NUM1 " e " NUM2 " é " SOMA

           STOP RUN.
