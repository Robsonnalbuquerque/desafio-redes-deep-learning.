def descricao_rede(tipo):
        if tipo == "redes neurais convolucionais":
                return "especializadas em processamento de imagens"
                    elif tipo == "redes neurais recorrentes":
                            return "projetadas para processar dados sequenciais"
                                elif tipo == "redes neurais de memória de longa e curta duração":
                                        return "podem aprender dependências de longo prazo em dados sequenciais"
                                            elif tipo == "autoencoders":
                                                    return "usadas para compressão e reconstrução de dados"
                                                        else:
                                                                return "Tipo de rede não reconhecido"

                                                                # Exemplo de entrada
                                                                entrada = input()
                                                                print(descricao_rede(entrada))
                                                                