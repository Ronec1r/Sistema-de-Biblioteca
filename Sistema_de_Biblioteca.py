from datetime import datetime, timedelta

def cadastro(): #função designada a CADASTRO dos livros
    limite_lista=len(lista)-1
    cod=int(lista[1])
    name= " ".join(lista[3:limite_lista])
    tip=lista[2]
    tip_cadastro=lista[-1]
    if tip_cadastro=='&add':
        if cod in usuario:
     	   print('Insucesso no cadastro. Código de usuário já existente!!')
        else:
            if tip=='alu':
                print('Sucesso no cadastro!!')
                usuario[cod]= {'nome': name, 'codigo': cod,'tipo': tip, 'emp': [], 'lim': 3, 'res': 3, 'data':[], 'exemplar': [], 'todos_emp': [], 'data_reserva': [], 'reservados':[]}
            elif tip=='tec':
                print('Sucesso no cadastro!!')
                usuario[cod]= {'nome': name, 'codigo': cod,'tipo': tip, 'emp': [], 'lim': 4, 'res': 3, 'data':[], 'exemplar': [], 'todos_emp': [], 'data_reserva': [], 'reservados':[]}
            elif tip=='pro':
                print('Sucesso no cadastro!!')
                usuario[cod]= {'nome': name, 'codigo': cod,'tipo': tip, 'emp': [], 'data':[], 'exemplar': [], 'todos_emp': []}
            else:
                print('Insucesso no cadastro. Tipo de usuário inválido!!')
    elif tip_cadastro=='&upd':
        if not(cod in usuario):
     	   print('Insucesso na atualização de dados. Código de usuário não consta no banco de dados!!!')
        else:
            if tip!='pro' and tip!='alu' and tip!='tec':
               print('Insucesso na atualização de dados. Tipo de usuário inválido!!')
            else:
               print('Sucesso na atualização dos dados!!')
               usuario[cod]['tipo']=tip
               usuario[cod]['nome']=name
    else:
       print('Insucesso. Código de cadastro ou atualização inválido!!')
        

def emprof(): #função designada a EMPRÉSTIMO PROFESSOR dos livros
    cod=int(lista[1])
    cod_livro=int(lista[2]) 
    validade=False
    if cod_livro in livros: # checagem livros
        if livros[cod_livro]['exemp']>0:
            validade=True
        else:
            print('Insucesso. Livro buscado não possui exemplares disponíveis!!')
    else:
        print('Insucesso. Livro não consta no banco de dados!!')
    if validade==True: # checagem tempo
        presente= datetime.now()
        atrasado= True
        lendata= len(usuario[cod]['data'])
        if lendata==0:
            atrasado=False
        else:
            for i in usuario[cod]['data']:
                atraso= i+ timedelta(days=14)
                if atraso<presente:
                    atrasado=True
                    print("Insucesso. Usuário possui pelo menos um livro em atraso!!")
                    break
                else:
                    atrasado=False
        if (atrasado==False): # realização do empréstimo
            dataemp= datetime.now()
            usuario[cod]['data'].append(dataemp)
            usuario[cod]['emp'].append(cod_livro)
            if not(cod_livro in usuario[cod]['todos_emp']):
                usuario[cod]['todos_emp'].append(cod_livro)
            livros[cod_livro]['exemp']-=1
            exemp= livros[cod_livro]['cod_exemp'][0]
            livros[cod_livro]['exemp_emp'].append(cod)
            usuario[cod]['exemplar'].append(exemp)
            del(livros[cod_livro]['cod_exemp'][0])
            print("Sucesso. Emprestimo realizado!!")
            
def emprestimo(): #função designada a EMPRÉSTIMO dos livros
    cod=int(lista[1])
    cod_livro=int(lista[2])
    validade=False
    # checagem usuários/livros
    if cod in usuario:
        if usuario[cod]['tipo']!='pro':
            if usuario[cod]['lim']>0: 
                if cod_livro in livros:
                    lenreserv= len(livros[cod_livro]['reserva'])
                    if livros[cod_livro]['exemp']>0:
                        if lenreserv<livros[cod_livro]['exemp']:
                            if cod_livro in usuario[cod]['emp']:
                                validade=False
                                print('Insucesso. Usuário já está com o livro emprestado')
                            else:
                                validade=True
                        elif cod in livros[cod_livro]['reserva']:
                            if cod_livro in usuario[cod]['emp']:
                                validade=False
                                print('Insucesso. Usuário já está com o livro emprestado')
                            else:
                                validade=True
                        else:
                            print('Insucesso. Livro buscado está reservado!!')
                    else:
                        print('Insucesso. Livro buscado não possui exemplares disponíveis!!')
                else:
                    print('Insucesso. Livro não consta no banco de dados!!')
            else:
                print('Insucesso. Limite de empréstimos do usuário excedido!!')
        else:
            emprof()
    else:
        print('Insucesso. Usuário não consta no banco de dados!!')

    if validade==True: # checagem tempo
        presente= datetime.now()
        atrasado= True
        lendata= len(usuario[cod]['data'])
        if lendata==0:
            atrasado=False
        else:
            for i in usuario[cod]['data']:
                if usuario[cod]['tipo'] == 'tec':
                    atraso= i + timedelta(days=7)
                elif usuario[cod]['tipo'] == 'alu':
                    atraso= i + timedelta(days=5)
                if atraso<presente:
                    atrasado=True
                    print("Insucesso. Usuário possui pelo menos um livro em atraso!!")
                    break
                else:
                    atrasado=False
        if (atrasado==False): # realização do empréstimo
            dataemp= datetime.now()
            usuario[cod]['data'].append(dataemp)
            usuario[cod]['lim']-=1
            usuario[cod]['emp'].append(cod_livro)
            if not(cod_livro in usuario[cod]['todos_emp']):
                usuario[cod]['todos_emp'].append(cod_livro)
            livros[cod_livro]['exemp']-=1
            exemp= livros[cod_livro]['cod_exemp'][0]
            livros[cod_livro]['exemp_emp'].append(cod)
            usuario[cod]['exemplar'].append(exemp)
            del(livros[cod_livro]['cod_exemp'][0])
            i=0
            while i<len(livros[cod_livro]['reserva']):
                if cod==livros[cod_livro]['reserva'][i]:
                    del(usuario[cod]['reservado'][i])
                    del(livros[cod_livro]['reserva'][i])
                    del(usuario[cod]['data_reserva'][i])
                    usuario[cod]['res']+=1
                i+=1
            print("Sucesso. Emprestimo realizado!!")
        
def devolucao(): #função designada a DEVOLUÇÃO dos livros
    i=0
    cod=int(lista[1])
    cod_livro=int(lista[2])
    validade=False
    if cod in usuario:
        if cod_livro in livros: 
            while i<len(usuario[cod]['emp']): #usar um loop para verificar cada item da lista de emprestimos
                if cod_livro==usuario[cod]['emp'][i]:
                    livros[cod_livro]['exemp']+=1                    
                    exemp= usuario[cod]['exemplar'][i]
                    livros[cod_livro]['cod_exemp'].append(exemp)
                    index=livros[cod_livro]['exemp_emp'].index(cod)
                    del(livros[cod_livro]['exemp_emp'][index])
                    del(usuario[cod]['emp'][i])
                    del(usuario[cod]['data'][i])
                    del(usuario[cod]['exemplar'][i])
                    validade=True
                    break
                i+=1
            if validade==True:
                print('Sucesso. Livro devolvido!!')
            else:
                print('Insucesso. Usuário não está com livro que quer devolver!!')
        else:
            print('Insucesso. O livro não consta no banco de dados!!')
    else:
        print('Insucesso. Usuário não consta no banco de dados!!')

def reserva(): #função designada a RESERVA dos livros
    cod=int(lista[1])
    cod_livro=int(lista[2])        
    if cod in usuario:
        if cod_livro in livros:     
            if usuario[cod]['tipo']!='pro':
                if usuario[cod]['res']>0:
                    if cod in livros[cod_livro]['reserva']:
                        print('Insucesso. Livro já reservado por esse usuário!!')
                    else:
                        livros[cod_livro]['reserva'].append(cod)
                        usuario[cod]['reservados'].append(cod_livro)            
                        data_res=datetime.now()
                        usuario[cod]['data_reserva'].append(data_res)
                        usuario[cod]['res']-= 1
                        print('Sucesso. Livro reservado!!')
                else:
                    print('Insucesso. O limite de reservas do usuário excedido!!')
            else:
                print('Professor não necessita de reserva!!')
        else:
            print('Insucesso. O livro não consta no banco de dados!!')
    else:
        print('Insucesso. Usuário não consta no banco de dados!!')

def consulta(): #função designada a CONSULTA dos livros
    param= lista[1]
    if param=='*':
        for i in livros:
            name= livros[i].get('nome')
            codigo= livros[i].get('codigo')
            editora= livros[i].get('edit')
            autor= livros[i].get('autor')
            edicao= livros[i].get('edic')
            ano= livros[i].get('ano')
            print("(i)", codigo, "(ii)", name, "(iii)", editora, "(iv)", autor, "(v)", edicao, "(vi)", ano )     
    else:
        usu=[]
        if param.isdigit()==True: # checagem da validade do parâmetro(código do livro)
            cod_livro=int(param)
            if cod_livro in livros:
                name= livros[cod_livro].get('nome')
                if len(livros[cod_livro]['reserva'])<=0: # checagem das RESERVAS para consulta
                    res= 0
                else:
                    res=len(livros[cod_livro]['reserva'])
                    for i in livros[cod_livro]['reserva']: 
                        cod= i
                        nomeusu= usuario[cod].get('nome')
                        usu.append(nomeusu)
    
                if livros[cod_livro]['exemp']>=0: # print com exemplares existentes
                    if len(livros[cod_livro]['exemp_emp'])==0: # print sem exemplares EMPRESTADOS
                        if res==0: # sem reservas
                            print(' (i)', name,'\n','(ii) Reserva(s):', res)
                            print(' (iii) Exemplares: ')
                            for i in livros[cod_livro]['cod_exemp']:
                                print(' ', i, '- Disponível')
                        else: # com reservas
                            print(' (i)', name,'\n','(ii) Reserva(s):', res,'\n','Usuários com reserva:','\n ','\n  '.join(map(str, usu)))
                            print(' (iii) Exemplares: ')
                            for i in livros[cod_livro]['cod_exemp']:
                                print(' ', i, '- Disponível')
                    else: # print com exemplares EMPRESTADOS
                        if res==0: # sem reservas
                            print(' (i)', name,'\n','(ii) Reserva(s):', res)
                            print(' (iii) Exemplares: ')
                            if len(livros[cod_livro]['cod_exemp'])>=0:
                                for i in livros[cod_livro]['cod_exemp']:
                                    print(' ', i, '- Disponível')
                            for i in livros[cod_livro]['exemp_emp']:
                                nome= usuario[i].get('nome')
                                index= usuario[i]['emp'].index(cod_livro)
                                exemp= usuario[i]['exemplar'][index]
                                data= usuario[i]['data'][index]
                                if usuario[i]['tipo']=='alu':
                                    devolu= data + timedelta(days=5)
                                elif usuario[i]['tipo']=='tec':
                                    devolu= data + timedelta(days= 7)
                                elif usuario[i]['tipo']=='pro':
                                    devolu= data + timedelta(days=14)
                                print(' ', exemp,'- Emprestado: ', '\n', 'Usuário- ', nome, '\n', 'Data de Empréstimo- ', data.strftime('%d/%m/%Y'), '\n', 'Data prevista de devolução- ', devolu.strftime('%d/%m/%Y'), '\n')
                        else: # com reservas
                            print(' (i)', name,'\n','(ii) Reserva(s):', res,'\n','Usuários com reserva:','\n ','\n  '.join(map(str, usu)))
                            print(' (iii) Exemplares: ')
                            if len(livros[cod_livro]['cod_exemp'])>=0:
                                for i in livros[cod_livro]['cod_exemp']:
                                    print(' ', i, '- Disponível')
                            for i in livros[cod_livro]['exemp_emp']:
                                nome= usuario[i].get('nome')
                                index= usuario[i]['emp'].index(cod_livro)
                                exemp= usuario[i]['exemplar'][index]
                                data= usuario[i]['data'][index]
                                if usuario[i]['tipo']=='alu':
                                    devolu= data + timedelta(days=5)
                                elif usuario[i]['tipo']=='tec':
                                    devolu= data + timedelta(days= 7)
                                elif usuario[i]['tipo']=='pro':
                                    devolu= data + timedelta(days=14)
                                print(' ', exemp,'- Emprestado: ', '\n', 'Usuário- ', nome, '\n', 'Data de Empréstimo- ', data.strftime('%d/%m/%Y'), '\n', 'Data prevista de devolução- ', devolu.strftime('%d/%m/%Y'), '\n')
                else: # print sem exemplares existentes
                    if res==0: # sem reservas
                        print('(i)', name, '(ii) Reserva(s):', res, '(iii) O livro em questão não possui exemplares cadastrados!')
                    else: # com reservas
                        print(' (i)', name,'\n','(ii) Reserva(s):', res,'\n','Usuários com reserva:','\n ','\n  '.join(map(str, usu)),'\n','(iii) O livro em questão não possui exemplares cadastrados!')
            else:
                print('Insucesso. O livro não consta no banco de dados!!')
        else:
            print('Insucesso. Parâmetro de verificação inválido!!')

def consulta_usuario():
    cod=int(lista[1])
    j=0
    k=0
    if cod in usuario:
        print('(i)Código do usuário:',cod,'\n Nome do usuário:',usuario[cod]['nome'],'\n Tipo do usuário:',usuario[cod]['tipo'])
        print('(ii)Empréstimos:')
        for i in usuario[cod]['todos_emp']:
            cod_livro=i
            print('Nome:',livros[cod_livro]['nome'])
            print('Data do empréstimo:',usuario[cod]['data'][k])
            if cod_livro in usuario[cod]['emp']:
                print('Status: Em curso')
                if usuario[cod]['tipo']=='alu':
                    devo=usuario[cod]['data'][k]+timedelta(days=5)
                elif usuario[cod]['tipo']=='tec':
                    devo=usuario[cod]['data'][k]+timedelta(days=7)
                elif usuario[cod]['tipo']=='pro':
                    devo=usuario[cod]['data'][k]+timedelta(days=14)
                print('Data de devolução:',devo)
            else:
                print('Status: Finalizado') 
            k+=1
        if usuario[cod]['tipo']=='pro':
            print('(iii)Professor nao faz reserva!!')
        else:
            print('(iii)Reservas:')
            for i in usuario[cod]['reservados']:
                cod_livro=i
                print('Nome:',livros[cod_livro]['nome'])
                print('Data de reserva:',usuario[cod]['data_reserva'][j])
                j+=1
    else:
        print('Insucesso. Código de usuário não consta no banco de dados!!')
        
            
        
            
            	
        


# DICIONÁRIO dos LIVROS
livros= {
    100: {'nome': 'Engenharia de Software', 'edit': 'Addison-Wesley', 'autor': 'Ian Sommervile', 'edic': '6ª', 'ano': '2000', 'codigo': 100, 'exemp':2, 'reserva':[], 'cod_exemp':['01', '02'], 'exemp_emp': []},
    101: {'nome': 'UML - Guia do Usuário', 'edit': 'Campus', 'autor': 'Grady Booch, James Rumbaugh, Ivar Jacobson','edic': '7ª', 'ano': '2000', 'codigo':101, 'exemp':1, 'reserva':[], 'cod_exemp':['03'], 'exemp_emp': []},
    200: {'nome': 'Code Complete', 'edit': 'Microsoft Press', 'autor': 'Steve McConnell', 'edic': '2ª', 'ano': '2014', 'codigo':200, 'exemp': 1, 'reserva':[], 'cod_exemp':['04'], 'exemp_emp': []},
    201: {'nome': 'Agile Software Development , Principles, Patterns, and Practices', 'edit': 'PrenticeHall', 'ano': '2002', 'autor': 'Robert Martin', 'edic': '1ª', 'codigo':201, 'exemp':1, 'reserva':[], 'cod_exemp':['05'], 'exemp_emp': []},
    300: {'nome': 'Refactoring: Improving the Design of Existing Code', 'edit': 'Addison Wesley Professional', 'ano': '1999', 'autor': 'Martin Fowler', 'edic': '1ª', 'codigo':300, 'exemp':2, 'reserva':[], 'cod_exemp':['06', '07'], 'exemp_emp': []},
    301: {'nome': 'Software Metrics: A Rigorous and Practical Approach', 'edit': 'CRC Press', 'autor': 'Norman Fenton, James Bieman', 'edic': '3ª', 'ano': '2014', 'codigo':301, 'exemp':-1, 'reserva':[], 'cod_exemp':'Não existe exemplar cadastrado'},
    400: {'nome': 'Design Patterns: Elements of Reusable Object Oriented Software', 'edit': 'Addison-Wesley Professional', 'autor': 'Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides', 'edic': '1ª', 'ano': '1994', 'codigo':400, 'exemp':2, 'reserva':[], 'cod_exemp':['08', '09'], 'exemp_emp': []},
    401: {'nome': 'UML Distilled: A Brief Guide to the Standard Object Modeling Language', 'edit': 'Addison-Wesley Professional', 'autor': 'Martin Fowler', 'edic': '3ª', 'ano': '2003', 'codigo':401, 'exemp':-1, 'reserva':[], 'cod_exemp':'Não existe exemplar cadastrado'}
}
# DICIONÁRIO dos USUÁRIOS
usuario= {
    200: {'nome': 'Alexsandra Prata', 'codigo': 200, 'tipo': 'pro', 'emp': [], 'data':[], 'exemplar': [], 'todos_emp': []},
    123: {'nome': 'Ana Luzia', 'codigo': 123, 'tipo': 'alu', 'emp': [], 'lim': 3, 'res': 3, 'data':[], 'exemplar': [], 'todos_emp': [], 'data_reserva': [], 'reservados':[]},
    456: {'nome': 'Telma Alves', 'codigo': 456, 'tipo': 'tec', 'emp': [], 'lim': 4, 'res': 3, 'data':[], 'exemplar': [], 'todos_emp': [], 'data_reserva': [], 'reservados':[]},
    789: {'nome': 'Alan Lucas', 'codigo': 789, 'tipo': 'alu', 'emp': [], 'lim': 3, 'res': 3, 'data':[], 'exemplar': [], 'todos_emp': [], 'data_reserva': [], 'reservados':[]},
    100: {'nome': 'Paulo Perreira', 'codigo': 100, 'tipo': 'pro', 'emp': [], 'data':[], 'exemplar': [], 'todos_emp': []}
}

# mensagem inicial
print('=' *31)
print('   Sistema de biblioteca IFS')
print('=' *31)

inpt= input(': ')
#LOOP input/triagem
while inpt.upper()!= 'SAI':
    lista= list(inpt.split(" "))
    if len(lista)>1:
        comand= lista[0]
        cod= lista[1]
        if (comand!='usu') and (comand!='liv') and (comand!='emp') and (comand!='dev') and (comand!='res'):
            print('Comando inexistente.')
        else:
            if comand=='liv':
                consulta()
            elif (cod.isdigit()==False):
                print('Código inválido.')
            else:
                if comand=='usu':
                    if len(lista)==2:
                        consulta_usuario()
                    else:
                        cadastro() 
                else:
                    cod_livro= lista[2]
                    if cod_livro.isdigit()==False:
                        print('Código inválido.')
                    elif comand=='emp':
                        if len(lista)>2:
                            emprestimo()
                        else:
                            print('Comando inválido')
                    elif comand=='dev':
                        devolucao()
                    elif comand=='res':
                        reserva()
                    else:
                        print('Comando inexistente.')
    else:
        print('Comando inexistente!!')
    inpt=input(': ')