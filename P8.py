data = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
length = len(data)


#takes the string and gets a product
#could be improved by using the previous product, dividing by it's first digit
#and multiplying. not the most interesting problem so i'll stick with the brute force
def product(data):
    prod = 1
    for i in range(len(data)):
        prod =  prod*int(data[i])
    return prod



clean_data = []
for i in range(length -13):
    substring = data[i:i+13]
    if "0" not in substring and substring:
        clean_data.append(substring)

max_num = 0
max_str = ""
for sequence in clean_data:
    seq_prod = product(sequence)
    if seq_prod > max_num:
        max_num = seq_prod
        max_str = sequence
        print "string is: " + max_str + " product: " + str(max_num)

#thi


