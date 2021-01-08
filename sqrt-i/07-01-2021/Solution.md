#breaking bad

primeiramente eu precisei de uma lista com todos os nomes e apelidos dos personagens de breaking bad, pra isso fiz um http request para [ breaking bad API]( https://breakingbadapi.com) 
e salvei o arquivo json contendo informações de todos os personagens, apos isso criei uma lista contendo o nome + apelido de cada personagem. Encryptei todos elementos desta lista 
usando md5Hash e adicionei essese valores como chave a um dicionario onde o nome + apelido dos personagens seriam os valores. apos isso era so ir extraindo os arquivos do zip
recursivamente usando do dicionario para descobrir a senha dos arquivos até que um arquivo diferente de .zip seja encontrado.
