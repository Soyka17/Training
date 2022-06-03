# Сравнить, насколько строки Q и S совпадают
# если Q[i] == S[i] -> correct
# если Q[i] != S[i] && Q[i] in S -> present
#       При этом несколько Q[i] не могут ссылаться на один S[j]
# если Q[i] not in S -> absent

# Compare how strings Q and S match
# if Q[i] == S[i] -> correct
# if Q[i] != S[i] && Q[i] in S -> present
#       At the same time, several Q[i] cannot refer to one S[j]
# if Q[i] not in S -> absent

S = input()
Q = input()

result = [0 * i for i in range(0, len(S))]

i = 0
while i < len(S):
    if Q[i] in S:
        if Q[i] == S[i]:
            result[i] = "correct"
            S = S[:i] + chr(0) + S[i + 1:]
        else:
            for j in range(0, len(S)):
                if Q[i] == S[j] and Q[j] != S[j]:
                    S = S[:j] + chr(0) + S[j + 1:]
                    result[i] = "present"
                    break
                else:
                    result[i] = "absent"
    else:
        result[i] = "absent"
    i += 1

for i in range(0, len(result)):
    print(result[i])
