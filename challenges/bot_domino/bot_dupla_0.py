NOME_ESTUDANTE = "Matheus Ramos Rodrigues de Souza"

# basicamente o meu bot ele primeiramente avalia se existe apenas uma possibilidade de jogada ou nem uma, caso verdadeiro ele faz essa jogada ou passa sem perder tempo

# Caso haja mais de uma opção de peça ele pontua as peças de acordo com alguns fatores como inimigo mostrou que não tem, aliado mostrou
# que possui, tenho bastante em minha mao, atribui pontuações a mais para essas jogadas e joga sempre uma dentre as jogadas com
# a MAIOR pontuação

# Além disso o bot, caso possua uma soma muito pequena em sua mão ele busca fechar o jogo, e se tiver uma soma muito alta em
# sua mao ele tenta NÃO trancar o jogo, usando as informações de passes dos jogadores

def joga(estado):

	movimentos = estado["movimentos_validos"]

	def only_one_play() :

		if len(movimentos['esquerda']) + len(movimentos['direita']) == 1 :
			
			if len(movimentos['esquerda']) != 0 :

				return {
					'jogada': 'joga',
					'peca': movimentos['esquerda'][0],
					'lado': 'esquerda'
				}
			
			else :

				return {
					'jogada': 'joga',
					'peca': movimentos['direita'][0],
					'lado': 'direita'
				}
		
		elif len(movimentos['esquerda']) + len(movimentos['direita']) == 0 :

			return {
				'jogada': 'passa'
			}

	forced = only_one_play() 

	if forced :	
		return forced
		
	soma_minha_mao = sum(a + b for a, b in estado["mao"])

	pass_enemy = set()
	pass_ally = set()

	for evento in estado['historico'] :
		
		if evento['rodada'] != estado['rodada'] :
			continue

		if evento['jogada'] == 'passo' :

			player = evento['jogador']
			left = evento['mesa_esquerda']
			right = evento['mesa_direita']

			if player == estado['parceiro'] or player == estado['jogador'] :

				if left is not None :
					pass_ally.add(left)
				
				if right is not None :
					pass_ally.add(right)
			
			else :

				if left is not None :
					pass_enemy.add(left)
				
				if right is not None :
					pass_enemy.add(right)

	
	def freq_hand() :

		frequency = {num: 0 for num in range(7)}
		greatestf = 0

		for peca in estado['mao'] :

			for lado in peca :

				frequency[lado] += 1
		
		for freq in frequency.values() :

			greatestf = max(freq, greatestf)

		return frequency, greatestf
      

	def best_play():
			best_score = -9999
			best_plays = []

			freq, greatestf = freq_hand()

			for peca in movimentos['esquerda']:
				score = 0
				a, b = peca[0], peca[1]

				freq_a = freq[a]
				freq_b = freq[b]

				novo_extremo_esq = b if a == estado['esquerda_end'] else a
				extremo_dir_atual = estado['direita_end']

				if novo_extremo_esq in pass_enemy and extremo_dir_atual in pass_enemy:
					if soma_minha_mao < 10:
						score += 50  
					elif soma_minha_mao > 25:
						score -= 50  

				if a == b:
					score += 3

				if a + b > 6:
					score += 2

				if estado['esquerda_end'] == a and b in pass_enemy:
					score += 5
				elif estado['esquerda_end'] == b and a in pass_enemy:
					score += 5

				if estado['esquerda_end'] == a and b in pass_ally:
					score -= 5
				elif estado['esquerda_end'] == b and a in pass_ally:
					score -= 5

				if estado['esquerda_end'] == a and freq_b >= 3:
					score += 3
					if freq_b > 4:
						score += 3
				elif estado['esquerda_end'] == b and freq_a >= 3:
					score += 3
					if freq_a > 4:
						score += 3

				if score > best_score:
					best_score = score
					best_plays = [{'jogada': 'joga', 'peca': peca, 'lado': 'esquerda'}]
				elif score == best_score:
					best_plays.append({'jogada': 'joga', 'peca': peca, 'lado': 'esquerda'})
			
			for peca in movimentos['direita']:
				score = 0
				a, b = peca[0], peca[1]

				freq_a = freq[a]
				freq_b = freq[b]

				novo_extremo_dir = b if a == estado['direita_end'] else a
				extremo_esq_atual = estado['esquerda_end']

				if novo_extremo_dir in pass_enemy and extremo_esq_atual in pass_enemy:
					if soma_minha_mao < 10:
						score += 50  
					elif soma_minha_mao > 25:
						score -= 50  

				if a == b:
					score += 3

				if a + b > 6:
					score += 2

				if estado['direita_end'] == a and b in pass_enemy:
					score += 7
				elif estado['direita_end'] == b and a in pass_enemy:
					score += 7

				if estado['direita_end'] == a and b in pass_ally:
					score -= 5
				elif estado['direita_end'] == b and a in pass_ally:
					score -= 5

				if estado['direita_end'] == a and freq_b >= 3:
					score += 3
					if freq_b > 4:
						score += 3
				elif estado['direita_end'] == b and freq_a >= 3:
					score += 3
					if freq_a > 4:
						score += 3

				if score > best_score:
					best_score = score
					best_plays = [{'jogada': 'joga', 'peca': peca, 'lado': 'direita'}]
				elif score == best_score:
					best_plays.append({'jogada': 'joga', 'peca': peca, 'lado': 'direita'})
			
			return best_plays[0]
			
	return best_play()


	
