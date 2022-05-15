# Sistema-de-Biblioteca

## Objetivo do Projeto : 
O Objetivo do projeto era a construção de um sistema de biblioteca, de pequeno porte e sem interface gráfica, para gerenciamento de livros e usuários. Projeto da Disciplina de Linguagem de Programação I, feito em duplas.

## Visão geral do Projeto:
O sistema de biblioteca consiste no gerenciamento e manutenção de livros disponíveis em uma  biblioteca acadêmica. Ele permite que três tipos de usuários (alunos, técnicos administrativos e  professores) realizem o empréstimo, devolução e reserva de livros disponíveis.

Um livro específico pode dispor na biblioteca de mais de um exemplar. Assim, é possível encontrar na  biblioteca dois ou mais exemplares de um mesmo livro. 
Cada livro deve possuir um código que o identifique e um título. Além do código e do título, os livros  devem manter as seguintes informações adicionais: editora, autores, edição e ano da publicação.

Cada usuário deve ter um código de identificação e nome. Cada um dos três tipos de usuários possui regras específicas para poder pegar livro emprestado. Regras essas explicadas posteriormente.

Além disso, a cada tipo de usuário é  permitido um determinado intervalo de tempo, em dias, durante o qual ele pode ficar com o livro emprestado. Alunos podem ficar por 5 dias, técnicos administrativos podem ficar por 7 dias, e professores podem ficar por 14 dias. Sempre que o empréstimo de um livro é solicitado na biblioteca, é  feito o registro daquela operação no sistema e é fixada uma data de devolução baseada no tempo de  empréstimo do tipo de usuário. 

Usuários têm também o direito de realizar reservas de livros. A reserva de um livro garante a prioridade  no seu empréstimo apenas entre os alunos, como ficará mais claro nas regras de empréstimo,  detalhadas na Seção 3. A reserva também tem que ser registrada no sistema. 

## Funcionalidades:

1. O sistema deve permitir o cadastramento de um novo usuário. Durante o cadastramento, o  usuário informará o comando “usu” seguido do código do usuário, sigla do tipo do usuário e do  nome do usuário, separados por espaço em branco. Ex.: “usu 200 pro Alexsandra Prata”. O  cadastramento do novo usuário só será concretizado se não existir outro usuário cadastrado  com o mesmo código do usuário. Ao final do procedimento o sistema deve emitir uma  mensagem de sucesso ou insucesso. Se for uma mensagem de insucesso, ela deve também  mencionar o motivo do insucesso. 

2. O sistema deve permitir o empréstimo de livros. Durante o empréstimo, o usuário informará o  comando “emp” seguido do código do usuário e do código do livro, separados por espaço em branco. Ex.: “emp 123 100”. Caso o usuário tenha uma reserva feita previamente por ele para  o dado livro, a reserva deve ser excluída e o empréstimo efetivado. Ao final do procedimento o  sistema deve emitir uma mensagem de sucesso ou insucesso, que mencione o nome do  usuário e o título do livro. Se for uma mensagem de insucesso, ela deve também mencionar o  motivo do insucesso. 
O empréstimo do livro só será concretizado para um aluno ou um técnico administrativo se:  (i) houver a disponibilidade de algum exemplar daquele livro na biblioteca; (ii) o usuário não  estiver “devedor” de um livro em atraso; (iii) forem obedecidas as regras específicas daquele  tipo de usuário no que se refere à quantidade máxima de empréstimos, onde alunos podem pegar até 3 livros, técnicos até 5 livros, e professores não possuem limite. (iv) a quantidade de reservas existentes do livro for menor do que a quantidade de  exemplares disponíveis, caso o usuário não tenha reserva para ele; (v) a quantidade de  reservas for maior ou igual a de exemplares, mas uma das reservas é do usuário; e (vi) o usuário  não tiver nenhum empréstimo em andamento de um exemplar daquele mesmo livro.O empréstimo do livro só será concretizado para um professor se: (i) houver a disponibilidade  de algum exemplar daquele livro na biblioteca; e (ii) o usuário não estiver “devedor” de um livro  em atraso. Note que os professores não têm empréstimo negado caso haja reservas para aquele livro e  não têm limite da quantidade de livros que pode pegar emprestado. 

3. O sistema deve permitir a devolução de um dado livro. Durante a devolução, o usuário deve  digitar o comando “dev” seguido do código de identificação do usuário e do código de  identificação do livro emprestado. Ao final, o sistema deve emitir uma mensagem de sucesso  ou insucesso da devolução, que mencione o nome do usuário e o título do livro. A mensagem  de insucesso deve dizer o motivo. Nesse caso, o insucesso só ocorre se não houver empréstimo  em aberto daquele livro para aquele usuário. Ex.: “dev 123 401”. 

4. O sistema deve permitir a reserva de um livro. Durante esse processo de reserva, o usuário  deve digitar o comando “res”, o código de identificação do usuário e o código de identificação  do livro que o usuário deseja reservar. Será permitida a reserva de apenas 3 livros por usuário.  Ao final, o sistema deve emitir uma mensagem de sucesso ou insucesso da reserva, que  mencione o nome do usuário e o título do livro. A mensagem de insucesso deve dizer o motivo.  Ex.: “res 123 401”. 

5. O sistema deve fornecer as seguintes consultas: 
a. Consulta de todos os livros cadastrados. O sistema deve apresentar suas informações da  seguinte forma: (i) Código, (ii) Título, (iii) Editora, (iv), (v) Autores, (vi) Edição e (vii) Ano  Publicação. Para solicitar tal consulta, o usuário deverá digitar o comando “liv”, seguido do  coringa “*”. Ex.: “liv *”. 
b. Consulta de livro na íntegra de forma detalhada. Dado o código de um livro, o sistema deve  apresentar suas informações da seguinte forma: (i) título, (ii) quantidade de reservas para  aquele livro, e, se diferente de zero, devem ser também apresentados o nome dos usuários  que realizaram cada reserva, (iii) para cada exemplar, deve ser apresentado seu código,  seu status (disponível ou emprestado), e em caso do exemplar está emprestado deverá ser  exibido o nome do usuário que realizou o empréstimo, a data de empréstimo e a data  prevista para devolução. Para solicitar tal consulta, o usuário deverá digitar o comando “liv”,  seguido do código do livro. Ex.: “liv 401”. 

6. O sistema deve ter a opção de sair do programa. Para isso, basta o usuário digitar o comando  “sai”. 

## Base de dados usada:

![image](https://user-images.githubusercontent.com/85186341/168453412-23f32a30-261d-4e78-9cc5-d7e8381b0f6d.png)
![image](https://user-images.githubusercontent.com/85186341/168453366-926a0082-6c21-4f21-a6c8-ee8987440b51.png)
![image](https://user-images.githubusercontent.com/85186341/168453378-821ab6ef-5d09-452f-8f95-6bbb27d79341.png)


