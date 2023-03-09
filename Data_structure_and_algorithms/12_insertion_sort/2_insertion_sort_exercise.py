def find_midean(elements):
    midean_list = []
    midean_list.append(elements[0])

    for i in range(1,len(elements)):
        anchor = elements[i]
        j =i -1
        while j >=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j -=1
        elements[j+1] = anchor

        if i % 2 == 1:
            median = (elements[i//2] + elements[i//2 +1])/2
            midean_list.append(median)
        else:
            midean_list.append(elements[i//2+i%2])

    return midean_list

if __name__ == '__main__':
    elements = [2,1,5,7,2,0,5]
    print(find_midean(elements))