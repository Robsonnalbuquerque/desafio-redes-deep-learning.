```python
def descricao_rede(tipo):
    if tipo == "redes neurais convolucionais":
            return "Especializadas em processamento de imagens."
                elif tipo == "redes neurais recorrentes":
                        return "Projetadas para processar dados sequenciais."
                            elif tipo == "redes neurais de memória de longa e curta duração":
                                    return "Capazes de aprender dependências de longo prazo em sequências."
                                        elif tipo == "autoencoders":
                                                return "Usadas para compressão e reconstrução de dados."
                                                    else:
                                                            return "Tipo de rede não reconhecido. Verifique a grafia e tente novamente."
                                                            
                                                            print("Tipos de redes disponíveis:")
                                                            print("- redes neurais convolucionais")
                                                            print("- redes neurais recorrentes")
                                                            print("- redes neurais de memória de longa e curta duração")
                                                            print("- autoencoders")
                                                            
                                                            entrada = input("\nDigite o tipo de rede que deseja saber mais: ")
                                                            print("\nDescrição:")
                                                            print(descricao_rede(entrada))
                                                            ```