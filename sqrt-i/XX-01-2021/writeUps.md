# WriteUps

### a-fine-year
##### Description
>Last year has been tough for a lot of us. Congratulations on making it through.
Have fun with the CTFs.
##### Attachments
>bfyq{gpssz_cvj_zvpi_gxsbcl_qxi_p_kvyyvi_xcv}
##### Category
>Crypto
##### Points
>75
##### solução:
>sabe-se que todas flags se iniciam com `ictf{` logo, fazendo uma simples substituição, pudemos supor o restante da String, obtendo a flag `ictf{happy_new_year_hoping_for_a_better_one}`.
---
### Format
##### Description
>I used a keyword cipher to encode this. I wonder if you can just guess the 4 letter keyword... Note: The flag is in flag format ICTF{YOUR_FLAG_HERE} in all caps.
##### Attachments
>FMTB{USA_TDA_BJHC_BNRKHT}
##### Category
>Crypto
##### Points
>100
##### solução:
>similar a solução do a-fine-year, sabemos como a flag se inicia, fazendo substituição e supondo alguns outros valores temos `ICTF{USE_THE_FLAG_FORMAT}`
---
### Web comments
##### Description
>I like commenting on websites, but this site went too fast... :(
##### Attachments
>http://oreos.ctfchallenge.ga/
##### Category
>Web Explotation
##### Points
>100
##### solução:
>o site redireciona quem o visita para um rickroll, basta parar o carregamento da pagina enqt ela carrega e checar o código-fonte da página, onde encontramos um comentário que contem a flag `ictf{M@yb3_I_lik3_l33t}`
---
### Breaking Bad
##### Description
>A friend gave me this nested zip file and wants me to open it. Every password is the name of a Breaking Bad character followed by two underscores and then their nickname. He also named the zip files as md5 of the password used. (For example, the password for a file can be Walter White__Heisenberg and its name would be 512a73318ba4dd5c424fcec5ee2c04f3.zip)
By the way, do you know what an API is?
##### Attachments
>https://fdownl.ga/930E810D53
##### Category
>Cracking/Programming
##### Points
>125
##### solução:
>seguindo a dica, ao procurar uma api que contenha informações sobre breaking-bad encontramos [breaking bad API](https://breakingbadapi.com) e salvamos um json com as informações de cada personagem. Desse json criamos uma lista no formato mostrado criamos um script para desempacotar esses arquivos ate encontrar a flag `ictf{4ut0mat10n_1zz_da_wa3}` 
---
### Ballymote
##### Description
>Ballymote is an interesting place to visit! Note: The flag format is all caps, with no underscores.
##### Attachments
>https://fdownl.ga/5713BC3A75
##### Category
>Crypto
##### Points
>100
##### solução:
>seguindo a descrição do desafio, ao pesquisar ballymote no google descobre-se que esse nome esta presente no livro de ballymote, 
um livro no qual podemos perceber escritos parecido com o da imagem do desafio. Depois de investigar mais um pouco percebe-se que esses escritos estão em ogham, um alfabeto irlandes antigo. traduzindo o texto conseguios `ictf{CREATINGTHECHALL}`
---
### Esolang
##### Description
>I thought I knew all the languages, but this one stumped me. Can you figure out what it is?
##### Attachments
>https://fdownl.ga/1AC9D811F4
##### Category
>Misc
##### Points
>100
##### solução:
>seguindo a dica, ao procurar as linguagens esolangs mais famosas encontra-se [este site](https://ourcodeworld.com/articles/read/427/top-10-most-complex-and-bizarre-esoteric-programming-languages) onde descobrimos que a lingaguem está em Malbolge. traduzindo o texto conseguimos a flag `ictf{n0_est03r1c_n0_pr0bl3m}`
---
### Denso's Matrix
##### Description
>I was talking to Denso today, and he said he wanted me to solve a puzzle about a matrix. I didn't think it would be made out of these! What do they mean???
##### Attachments
>https://fdownl.ga/AB72469D7A
##### Category
>Forensics
##### Points
>50
##### solução:
>analisando a imagem, percebe-se que um pequeno chunk não segue o mesmo padrão dos outros códigos qr, lendo este código conseguimos `ictf{w31c0m3_70_7h3_m47r1x_0f_QRC0D3}`
---
### CeWL
##### Description
>I am really close to finding out my surgeon friend's password. I currently have a SHA256 hash and I am dead sure he used one of the long medical terms from [here](https://en.wikipedia.org/wiki/Coronary_artery_bypass_surgery) and salted it with surgeon. Help me recover the plaintext please.
Note: The flag is ictf{plaintext_you_got}
##### Attachments
>86515c560fe63bb69f89661e9c6a9a0b5f9a79703af9ddf5eee6e27a117ea1e1
##### Category
>Cracking
##### Points
>75
##### solução:
>Cewl é um programa escrito em ruby que detecta palavras chaves de um determinado site. pegamos tais palavras do site linkado na descrição e salteamos cada uma com `surgeon`, apos isso convertemos todas a SHA256 e comparamos com o attachment, o que nos da `ictf{Revascualrisationsurgeon}` 
---
### Weird RSA
##### Description
>We leaked some info on this RSA ciphertext and public key. Please find the plaintext.
##### Attachments
>https://fdownl.ga/206187E89D
##### Category
>Crypto
##### Points
>150
##### solução:
>realizando os seguintes calculos:
>
>![](https://render.githubusercontent.com/render/math?math=n=pq)
>
>![](https://render.githubusercontent.com/render/math?math=\phi(n)=(p-1)(q-1))
>
>![](https://render.githubusercontent.com/render/math?math=2pq-p-q=x)
>___
><img src="https://latex.codecogs.com/png.latex?\begin{cases}&space;pq-p-q&plus;1=\phi(n)&space;\\&space;2pq-p-q-x=0\\&space;\end{cases}&space;\rightarrow{\begin{cases}&space;pq-p-q&plus;1=\phi(n)&space;\\&space;-2pq&plus;p&plus;q&plus;x=0\\&space;\end{cases}&space;}" title="\begin{cases} pq-p-q+1=\phi(n) \\ 2pq-p-q-x=0\\ \end{cases} \rightarrow{\begin{cases} pq-p-q+1=\phi(n) \\ -2pq+p+q+x=0\\ \end{cases} }" />
>
>___
>
>![](https://render.githubusercontent.com/render/math?math=$-pq%2Bx%2B1=\phi(n)\rightarrow-n%2Bx%2B1=\phi(n)$)
>
>pode-se escrever um script para decriptar a cifra agora que sabe-se o valor de ![](https://render.githubusercontent.com/render/math?math=\phi(n)) (que com ele pode-se achar **d**) e então econtra-se a chave `ictf{subtract_n_then_use_simons_favorite_factoring_trick_to_find_totient!}`
---
### Weird RSA 2
##### Description
>Uggh, polynomials...
##### Attachments
>https://fdownl.ga/E17D4AA082
##### Category
>Crypto
##### Points
>175
##### solução:
>similar a weird rsa1, e resolvendo as equações:
>
>![](https://render.githubusercontent.com/render/math?math=\phi(n)=(p-1)(q-1)=pq-p-q%2B1\rightarrow{pq-p-q=\phi(n)-1})
>___
>![](https://render.githubusercontent.com/render/math?math=p^4q^2(q-1)^2%2Bp^2q^4-2p^3q^3(q-1)=x)
>
>
>![](https://render.githubusercontent.com/render/math?math=p^2q^2[p^2(q-1)^2%2Bq^2-2pq(q-1)]=x)
>
>![](https://render.githubusercontent.com/render/math?math=p^2q^2[p(q-1)-q]^2=x\rightarrow{(pq)^2(pq-p-q)^2=x}\rightarrow{n^2(pq-p-q)^2=x})
>___
>sabendendo que ![](https://render.githubusercontent.com/render/math?math=pq-p-q=\phi(n)-1) então:
>
>![](https://render.githubusercontent.com/render/math?math=n^2(\phi(n)-1)^2=x\rightarrow{n(\phi(n)-1)=\sqrt{x}}\rightarrow{\phi(n)=\frac{\sqrt{x}}{n}%2B1})
>
>pode-se escrever um script para decriptar a mensagem agora que sabe-se o valor de ![](https://render.githubusercontent.com/render/math?math=\phi(n)) (que com ele pode-se achar **d**) e então econtra-se a chave `ictf{nice_job_found_totient_AGAIN}`
---
### php-comparison2
##### Description
>Several of you raised support tickets for and solved php-comparison in December, with a lot of positive feedback. Here is another challenge where you need to exploit type juggling.
##### Attachments
>http://php2-ictf.rf.gd/
##### Category
>Web
##### Points
>150
##### solução:
>analisando o código em php no site percebe-se que precisamos de uma string que seja igual a sua encriptação md5. Para isso utiliza-se magic hashes, pois em php qlqr string que comece com `0e` seguido por apenas números é considerado um numero cientifico igual a `0`. logo escreve-se um script para encontrar quais são algumas dessas strings (so precisamos de 2) e passamos tais strings como parametros para o site. a flag é `ictf{7h15_15_h1lari0u5!_5tr1ng_3qual5_ha5h_0f_1t53lf}`
---
### Javavava
##### Description
>A little birdie told me java is a repetitive language...
##### Attachments
>https://fdownl.ga/122779A6AA
##### Category
>Reversing
##### Points
>125
##### solução:
>simples desafio de programação, basta fazer o caminho inverso. Neste caso a unica parte que "importa" do código é `char d = (char) ((ind ^ 15) + (2 * a))`, basta criar um alogritmo que inverta cada char baseado nisso, obtendo a flag `ictf{jAvA_i$_c00l}`
---
### php-comparison3
##### Description
>Yet another web challenge with PHP type-juggling vulnerability
##### Attachments
>http://php3-ictf.rf.gd/
##### Category
>Web
##### Points
>125
##### solução:
>mais uma vulnerabilidade de tipos em php, neste caso basta passar um array como param1 e param2, a flag é `ictf{7h3_pr1c3_f0r_b31ng_w3akly_typ3d}`
---
### php-sqli
##### Description
>Look carefully at the code and find out the PHP vulnerability (it is not type juggling this time). Have fun!
##### Attachments
>http://php4-ictf.rf.gd/
##### Category
>Web
##### Points
>150
##### solução:
>simples injeção de sql, so que explorando algumas propriedades da função md5, a [parte 3 deste site](https://medium.com/@Asm0d3us/part-1-php-tricks-in-web-ctf-challenges-e1981475b3e4) tem uma explicação mais completa, flag`ictf{expl0it_md5_raw_0utput_f0r_sql_1nj3cti0n}`
---
### AreEsYay
##### Description
>This challenge has two parts: reverse engineering, and then cryptography. Have fun.
Hint: most variable's names have no significance. The ones that do stand out.
##### Attachments
>https://fdownl.ga/7E2D5C6856
##### Category
>Reversing, Crypto
##### Points
>200
##### solução:
>acabaram leakando o código com a solução, é so copiar e colar o output com a flag `ictf{rsA_and_HasTard_ar3_c00l_bu7_y0u_ar3_c00l3r!}`
---
### You can't do that!
##### Description
>Wait this isn't reversing...
##### Attachments
>https://imaginary.ml/files/super_secret.html
##### Category
>Reversing
##### Points
>105
##### solução:
>ao inspecionar o código da pagina achamos uma string em base64 e um link, ao abrir este link encontra-se uma imagem de código qr. decrifando a string base64 econtramos um link para uma sessão do cyberchef. Agora é so fazer o caminho reverso a partir da imagem com o "código" em cyberchef. a flag é `ictf{and_you_thought_u_couldnt_program_in_cyberchef}`
---
### Build-a-Cipher 3
##### Description
>Lets try mixing some things up...  
##### Attachments
>f\`k\0\kmqd-\^40ecokhetbx^\\..\o\`q_kp`z-!od\\.
>
>https://fdownl.ga/422A87CD5B
##### Category
>Crypto/Reversing
##### Points
>100
##### solução:
>simples desafio de programação reversa(está comentado nos códigos da pasta `sqrt-i\XX-01-2021\25-01-2021` o que cada parte faz), a flag é `ictf{c0ngrat$_0n_br3ak1ng_7h1s_n3w_c1pher}`
---
### Windows
##### Description
>Ishida gave me this puzzle, reminded me of sudoku, but at the same time different. Said something about windows?
##### Attachments
>https://fdownl.ga/B664193799
##### Category
>Miscellaneous
##### Points
>100
##### solução:
>nonogramazinho padrão, só colocar num solver online e ir supondo umas partes meio ilegíveis, flag: `ICTF{NONOSQUAREFUNS}`
---
### english
##### Description
>Timothy found this file on a usb he found in his house. Could you help him find the flag? Please do not attempt to crack the RSA, that is not the challenge.
>
>Note: please put the flag wrapper around your answer.
##### Attachments
>https://fdownl.ga/D65B5D7952
##### Category
>Reversing/Programming
##### Points
>150
##### solução:
>procuramos uma lista com palavras grandes, e executamos o código para cada palavra, comparando o numero encontrado com o output desejado, encontrando a flag`ictf{microspectrophotometrically}` 
---
>cabou :)
