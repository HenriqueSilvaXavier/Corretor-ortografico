def search(palavra, l):
	c=0
	positions=[]
	for n in palavra:
		if n==l:
			positions.append(c)
		c=c+1
	return positions
	
palavras=["paz", "não", "céu", "ser", "sob", "mal", "mãe", "ver", "ter", "ego", "bem", "mas", "bom", "sim", "vir", "vão", "dar", "são", "que", "era", "coisa", "tempo", "casa", "que", "ano", "dia", "vez", "homem","senhor", "senhora", "grande", "melhor", "está", "pior", "certo", "último", "próprio", "estar", "haver", "fazer", "ficar", "poder", "mais", "muito", "já", "quando", "mesmo", "depois", "ainda", "a", "o", "um", "uma", "você", "pode", "isso", "agora", "tu", "hoje", "ontem", "amanhã", "que", "mulher", "sou", "novo", "natural", "se", "vai", "pai", "pão", "também", "porque", "porquê", "assim", "eu", "pelo", "com", "e", "sem"]
frase=input("Digite a frase:")
frase=frase.split()
for n in frase:
	if type(frase)!=list:
		frase=frase.split()
	intercessoes=[]
	for k in range(0, len(palavras)):
		c=0
		lista=[]
		for l in palavras[k]:
			lista.append(l)
		if len(lista)>len(n):
			R=len(lista)
		elif len(lista)<=len(n):
			R=len(n)
		for p in range(0, len(n)):
			if n[p] in lista:
				c=c+1
				lista.remove(n[p])
		intercessoes.append(c/R)
	i1=search(intercessoes, max(intercessoes))
	palavras2=[]
	for x in i1:
		palavras2.append(palavras[x])
	intercessoes2=[]
	for k in range(0, len(palavras2)):
		c=0
		for p in range(0, len(n)):
			if p==len(palavras2[k]):
				break
			if n[p]==palavras2[k][p]:
				c=c+1
		intercessoes2.append(c)
	i2=intercessoes2.index(max(intercessoes2))
	frase=" ".join(frase)
	if n not in palavras:
		frase=frase.replace(n, palavras2[i2])
	lista4=[]
	r=True
	for p in palavras:
		c1=0
		c2=0
		for y in range(0, len(n)):
			if len(p)==y or len(n)==y:
				break
			if n[y]==p[y]:
				c1=c1+1
		numeros=[len(p), len(n)]
		if max(numeros)==len(p):
			num=p
		elif max(numeros)==len(n):
			num=n
		for y in num:
			c2=c2+1
		if (c1/c2)>(2/3):
			if r==True:
				frase=frase.replace(palavras2[i2], p)
				p2=p
				r=c1/c2
			if (c1/c2)>r:
				frase=frase.replace(p2, p)
				p2=p
				r=c1/c2
			r=False
print(frase)