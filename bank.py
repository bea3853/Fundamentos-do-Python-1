saldo  =  [100.50]
ap = input('Deseja fazer alguma operação? ')
while ap  == 's':
    op = input('operação: 1 saque , 2 deposito, 3 extrato')
    if op == '1':
        valor  = float(input('R$'))
        while sum(saldo) < valor:
            print('Saldo insuficiente')
            valor  = float(input('R$'))
        else:    
            t =  sum(saldo) -  valor
            print('SAQUE R$', valor)
            print('Saldo', t)
            v_n = -(valor)
            saldo.append(v_n)
            print('extrato', saldo)  
        ap = input('deseja fazer novamente? ')
    elif  op  == '2':
            
        valor  = float(input('R$'))
        saldo.append(valor)
        t =  sum(saldo)
        print('ADD R$', valor)
        print('Saldo', t)
        print('lista', saldo)  
        ap = input('deseja fazer nobamente? ')
            
    elif  op  == '3':
            
          print('lista', saldo)        
          s =  sum(saldo)
          print(s)
          ap = input('Deseja fazer alguma operação? ')
          
          
else:
    print('Até logo')