import difflib
palavras=["paz", "não", "céu", "ser", "sob", "mal", "mãe", "ver", "ter", "ego", "bem", "mas", "bom", "sim", "vir", "vão", "dar", "são", "que", "era", "coisa", "tempo", "casa", "que", "ano", "dia", "vez", "homem","senhor", "senhora", "grande", "melhor", "está", "pior", "certo", "último", "próprio", "estar", "haver", "fazer", "ficar", "poder", "mais", "muito", "já", "quando", "mesmo", "depois", "ainda", "a", "o", "um", "uma", "você", "pode", "isso", "agora", "tu", "hoje", "ontem", "amanhã", "que", "mulher", "sou", "novo", "natural", "se", "vai", "a", "para", "palavra"]
frase=input("Digite a frase:")
frase=frase.split()
for n in frase:
	lista=difflib.get_close_matches(n, palavras)
	lista2=[]
	for k in range(0, len(lista)):
		c=0
		for l in range(0, len(lista[k])):
			if len(lista[k])==l or len(n)==l:
				break
			if n[l]==lista[k][l]:
				c=c+1
		if len(lista[k])>=len(n):
			R=len(lista[k])
		elif len(lista[k])<len(n):
			R=len(n)
		lista2.append(c/R)
	m=lista2.index(max(lista2))
	frase=" ".join(frase)
	frase=frase.replace(n, lista[m])
	frase=frase.split()
frase=" ".join(frase)
print(frase)