senha =  '123'
usuario = 'x'

for chances in range(3):
    senha_us =  input('Senha: ')
    usuario_ = input('Usuario: ')
    if senha_us == senha and usuario_ == usuario:
        cadastra_n = input('deseja registrar as nostas? ')
        while cadastra_n == 'sim':
            nome =  input('Nome do aluno: ')
            n1  =  float(input('Nota 1'))
            n2  =  float(input('Nota 2'))
            n3  =  float(input('Nota 3'))
            media  =  (n1 +  n2 + n3) / 3
            print('Media do aluno',nome, '-', round(media, 2) )
            cadastra_n = input('deseja continuar com o registro de  nostas? ')
        else:
            print('Deslogar ...')
else:
    print('Conta bloqueada!!! ')