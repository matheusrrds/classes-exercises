"""
Bot 'Random' para o jogo de dominó

Este módulo implementa um bot chamado 'Random' para o jogo de dominó.
O bot 'Random' seleciona aleatoriamente uma jogada dentre todos os movimentos válidos.
Caso não haja movimentos válidos, passa.

ENTREGUE PELO PROFESSOR

"""

import random

NOME_ESTUDANTE = "Random"

NOME_ESTUDANTE = "Bot do chatGPT"

TOTAL_OCORRENCIAS_POR_NUMERO = 8
VALOR_VITORIA_IMEDIATA = 100000


def _normalizar_peca(peca):
    a, b = peca
    return (a, b) if a <= b else (b, a)


def _outro_lado_da_peca(peca, lado_jogado):
    a, b = peca
    if a == lado_jogado:
        return b
    return a


def _contar_mao(mao):
    freq = {i: 0 for i in range(7)}
    for a, b in mao:
        freq[a] += 1
        freq[b] += 1
    return freq


def _historico_da_rodada(estado):
    rodada_atual = estado["rodada"]
    return [ev for ev in estado.get("historico", []) if ev.get("rodada") == rodada_atual]


def _contar_jogados_e_passes(estado):
    jogados = {i: 0 for i in range(7)}
    passes = {i: 0 for i in range(7)}

    for ev in _historico_da_rodada(estado):
        jogada = ev.get("jogada")

        if jogada in ("comeco", "joga"):
            peca = ev.get("peca")
            if isinstance(peca, (tuple, list)) and len(peca) == 2:
                a, b = int(peca[0]), int(peca[1])
                if 0 <= a <= 6 and 0 <= b <= 6:
                    jogados[a] += 1
                    jogados[b] += 1

        elif jogada == "passo":
            esq = ev.get("mesa_esquerda")
            dir_ = ev.get("mesa_direita")
            if esq is not None:
                passes[int(esq)] += 1
            if dir_ is not None:
                passes[int(dir_)] += 1

    return jogados, passes


def _candidatos(movimentos):
    candidatos = []
    for peca in movimentos["esquerda"]:
        candidatos.append((peca, "esquerda"))
    for peca in movimentos["direita"]:
        candidatos.append((peca, "direita"))
    return candidatos


def _movimentos_futuros(mao_restante, novo_esquerda, novo_direita):
    total = 0
    for a, b in mao_restante:
        if novo_esquerda is not None and (a == novo_esquerda or b == novo_esquerda):
            total += 1
        if novo_direita is not None and (a == novo_direita or b == novo_direita):
            total += 1
    return total


def _avaliar_jogada(estado, peca, lado, freq_mao, restantes, pressao_passes):
    mao_restante = [x for x in estado["mao"] if x != peca]

    esquerda = estado["esquerda_end"]
    direita = estado["direita_end"]

    if lado == "esquerda":
        exposto = _outro_lado_da_peca(peca, esquerda)
        outro = direita
        novo_esquerda = exposto
        novo_direita = outro
    else:
        exposto = _outro_lado_da_peca(peca, direita)
        outro = esquerda
        novo_esquerda = outro
        novo_direita = exposto

    if not mao_restante:
        return VALOR_VITORIA_IMEDIATA + sum(peca)

    score = 0.0

    score += 8.0 * _movimentos_futuros(mao_restante, novo_esquerda, novo_direita)

    score += 14.0 * freq_mao.get(exposto, 0)
    if outro is not None:
        score += 8.0 * freq_mao.get(outro, 0)

    score += 5.0 * (TOTAL_OCORRENCIAS_POR_NUMERO - restantes.get(exposto, 0))
    if outro is not None:
        score += 2.0 * (TOTAL_OCORRENCIAS_POR_NUMERO - restantes.get(outro, 0))

    score += 2.5 * pressao_passes.get(exposto, 0)
    if outro is not None:
        score += 1.0 * pressao_passes.get(outro, 0)

    score += 0.8 * sum(peca)

    if peca[0] == peca[1]:
        score += 3.0
        if peca[0] == exposto:
            score += 6.0

    max_freq = max(freq_mao.values()) if freq_mao else 0
    if freq_mao.get(exposto, 0) == max_freq and max_freq > 0:
        score += 12.0
    if outro is not None and freq_mao.get(outro, 0) == max_freq and max_freq > 0:
        score += 6.0

    if freq_mao.get(exposto, 0) <= 1:
        score -= 4.0
    if outro is not None and freq_mao.get(outro, 0) <= 1:
        score -= 2.0

    if restantes.get(exposto, 0) <= 1:
        score += 10.0
    elif restantes.get(exposto, 0) <= 2:
        score += 5.0

    if novo_esquerda == novo_direita:
        score += 4.0

    saldo = estado["pontuacoes"][estado["time"]] - estado["pontuacoes"][1 - estado["time"]]
    if saldo < 0:
        score += (-saldo) * 0.15 * (TOTAL_OCORRENCIAS_POR_NUMERO - restantes.get(exposto, 0))
    else:
        score += saldo * 0.03 * freq_mao.get(exposto, 0)

    if len(mao_restante) <= 2:
        score += 5.0 * (estado.get("passes_em_sequencia", 0) + 1)

    return score


def joga(estado):
    movimentos = estado["movimentos_validos"]
    candidatos = _candidatos(movimentos)

    if not candidatos:
        return {"jogada": "passa"}

    if len(candidatos) == 1:
        peca, lado = candidatos[0]
        return {
            "jogada": "joga",
            "peca": peca,
            "lado": lado
        }

    freq_mao = _contar_mao(estado["mao"])
    jogados, pressao_passes = _contar_jogados_e_passes(estado)

    restantes = {}
    for n in range(7):
        restantes[n] = max(0, TOTAL_OCORRENCIAS_POR_NUMERO - freq_mao[n] - jogados[n])

    melhor = None
    melhor_score = float("-inf")

    for peca, lado in candidatos:
        score = _avaliar_jogada(
            estado=estado,
            peca=peca,
            lado=lado,
            freq_mao=freq_mao,
            restantes=restantes,
            pressao_passes=pressao_passes,
        )

        if (
            score > melhor_score
            or (
                score == melhor_score
                and melhor is not None
                and sum(peca) > sum(melhor[0])
            )
        ):
            melhor_score = score
            melhor = (peca, lado)

    if melhor is None:
        peca, lado = candidatos[0]
    else:
        peca, lado = melhor

    return {
        "jogada": "joga",
        "peca": peca,
        "lado": lado
    }