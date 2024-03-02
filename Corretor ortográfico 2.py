import difflib	
palavras=["paz", "não", "céu", "ser", "sob", "mal", "mãe", "ver", "ter", "ego", "bem", "mas", "bom", "sim", "vir", "vão", "dar", "são", "que", "era", "coisa", "tempo", "casa", "que", "ano", "dia", "vez", "homem","senhor", "senhora", "grande", "melhor", "está", "pior", "certo", "último", "próprio", "estar", "haver", "fazer", "ficar", "poder", "mais", "muito", "já", "quando", "mesmo", "depois", "ainda", "a", "o", "um", "uma", "você", "pode", "isso", "agora", "tu", "hoje", "ontem", "amanhã", "que", "mulher", "sou", "novo", "natural", "se", "vai", "a", "para"]
frase=input("Digite a frase:")
frase=frase.split()
for n in frase:
	print("{}:{}".format(n, difflib.get_close_matches(n, palavras, cutoff=0))