from hashlib import sha256
import time

def aplicar_sha256(texto)
    return sha256(texto.encode("ascii")).hexdigest()

def minerar(num_bloco, transacoes, hash_anterios, qtde_zeros):
    nonce = 0
    while True
        texto = str(num_bloco) + transacoes + hash_anterios + str(nonce)
        meu_hash = aplicar_sha256(texto)
        if meu_hash.startswith("0" * qtde_zeros)
            return nonce, meu_hash

if __name__ == "__main__":
    num_bloco =
    transacoes = """
    """
    qtde_zeros =
    hash_anterios =
    inicio = time.time()
    resultado = minerar(num_bloco, trasacoes, hash_anterios, qtde_zeros)
    print(resultado)
    print (time.time() - inicio)-