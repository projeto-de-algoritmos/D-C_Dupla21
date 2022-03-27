N_int = 1
aux = 0

def mergeSort(data, aux):
    m = 0
    array_final = data
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid] #lista do inicio ate o meio
        right = data[mid:] # lista do meio ate o fim

        mergeSort(left, aux)
        mergeSort(right, aux)

        j, j, k = 0, 0, 0
        i = 0

        #roda do inicio ate o fim
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              data[k] = left[i]
              i += 1
            else:
                while m < len(array_final):
                    if left[i] == array_final[m-1] and right[j] == array_final[m]:
                        aux = aux+1
                        print('cheguei', aux)
                        data[k] = right[j]
                        print(left[i], right[j])
                    m = m+1
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1


        while j < len(right):
            data[k]=right[j]
            j += 1
            k += 1

    return aux

while N_int != 0:
    array = input()
    my_array = array.split()
    # N_int = int(my_array[0])
    array_int = list(map(int, my_array))
    N_int = array_int.pop(0)

    if N_int == 0:
        break
    final = mergeSort(array_int, aux)
    print(final)
    if final % 2 == 0:
        print('Carlos')
    else:
        print('Marcelo')


