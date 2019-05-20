# Automato-de-Pilha
Programa para provar equivalencias entre os automatos de pilha que acietam por estado final e os que aceitam por pilha vazia. 
O codigo jflap-pda2utfpr.py faz a conversão do automato de pilha, criado no JFLAP, para uma descrição em arquivo txt. Após isso, executa-se equivalpilha.py, que detecta se o atual automato de pilha esta aceitando por pilha vazia ou estado de aceitação, e então é gerado o equivalente (se era por estado de aceitação agora aceita por pilha vazia e se era por pilha vazia agora aceita por estado de aceitação) em um arquivo txt. Para executar e testar se a equivalencia funciona, é usado o arquivo main.py.

Passo a passo:
*python jflap-pda2utfpr.py (arquivo JFLAP) ab.txt 
*python equivalpilha.py ab.txt 
*python fla/main.py Out.txt (palavra de entrada)
