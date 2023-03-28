from passlib.context import CryptContext


CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
    Função para verificar se senha está correta comparando
    a senha em texto puro informada pelo usuário e o
    hash da senha que estará salvo no banco de
    dados durante a criação da conta
    :param senha:
    :param hash_senha:
    :return: True or False
    """

    return CRIPTO.verify(senha, hash_senha)


def gerar_hash_senha(senha: str) -> str:
    """
    Função que retorna o Hash da senha
    :param senha:
    :return: str
    """
    return CRIPTO.hash(senha)
