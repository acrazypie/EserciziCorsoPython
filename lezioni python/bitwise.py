a = 10  # 1010 in binario
b = 6  # 0110 in binario

print(f"a = {a} ({bin(a)})")
print(f"b = {b} ({bin(b)})")

print(f"a & b (AND) = {a & b} ({bin(a & b)})")  # AND -> entrambi i bit devono essere 1
print(f"a | b (OR) = {a | b} ({bin(a | b)})")  # OR  -> almeno un bit deve essere 1
print(f"a ^ b (XOR) = {a ^ b} ({bin(a ^ b)})")  # XOR -> i bit devono essere diversi

print(f"~a (NOT) = {~a} ({bin(~a)})")  # NOT -> inverte i bit
print(f"~b (NOT) = {~b} ({bin(~b)})")  # NOT -> inverte i bit


"""
Conversione in binario:

Le posizioni sono:

    0 0 1 0 0 0 1 0
    | | | | | | | |
    | | | | | | | +-- 2^0 = 1
    | | | | | | +---- 2^1 = 2
    | | | | | +------ 2^2 = 4
    | | | | +-------- 2^3 = 8
    | | | +---------- 2^4 = 16
    | | +------------ 2^5 = 32
    | +-------------- 2^6 = 64
    +---------------- 2^7 = 128
    
34 in binario è 00100010
    -> 1*2^5 + 1*2^1 = 32 + 2 = 34
    
20 in binario è 00010100
    -> 1*2^4 + 1*2^2 = 16 + 4 = 20

18 in binario è 00010010
    -> 1*2^4 + 1*2^1 = 16 + 2 = 18

68 in binario è 01000100
    -> 1*2^6 + 1*2^2 = 64 + 4 = 68
"""
