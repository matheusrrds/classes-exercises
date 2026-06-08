"""

if movimentos["esquerda"]:
		return {
			"jogada": "joga",
			"peca": movimentos["esquerda"][0],
			"lado": "esquerda"
		}
		
	if movimentos["direita"]:
		return {
			"jogada": "joga",
			"peca": movimentos["direita"][0],
			"lado": "direita"
		}

	BOT PRODUZIDO POR MIM

"""

NOME_ESTUDANTE = "Matheus Ramos Rodrigues de Souza"

def unique_play(movimentos) :
	if len(movimentos["esquerda"]) == 1 and len(movimentos["direita"]) == 0 :

		return {
			"jogada": "joga",
			"peca": movimentos["esquerda"][0],
			"lado": "esquerda"
		}

	if len(movimentos["esquerda"]) == 0 and len(movimentos["direita"]) == 1 :

		return {
			"jogada": "joga",
			"peca": movimentos["direita"][0],
			"lado": "direita"
		}
	
	if len(movimentos["esquerda"]) == 0 and len(movimentos["direita"]) == 0 :

		return {
			"jogada": "passa"
		}
	
	return

def simple_play(estado) :

	for piece in estado["mao"] :

		if estado["esquerda_end"] in piece :

			return {
						"jogada": "joga",
						"peca": piece,
						"lado": "esquerda"
					}
		
		elif estado["direita_end"] in piece :
			
			return {
						"jogada": "joga",
						"peca": piece,
						"lado": "direita"
					}

def joga(estado):
    movimentos = estado["movimentos_validos"]

    if unique_play(movimentos):
        return unique_play(movimentos)

    return simple_play(estado)

	
	


	

