def user_class(ip_address):
    user_ip = ip_address.split(".")
    oct_one = int(user_ip[0])
    cidr = 0
    if oct_one <= 127:
        cidr = 8
    elif 128 <= oct_one <= 191:
        cidr = 16
    elif 192 <= oct_one <= 223:
        cidr = 24
    else:
        return cidr
    return cidr

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    print(decimal, end='.')

def cidrToSubnetmask(cidr):
    binaryMask = []
    for i in range(cidr):
        binaryMask.append('1')
    for i in range(32 - cidr):
        binaryMask.append('0')
    arrayop = ''.join(binaryMask)
    sliceAAA = []
    while arrayop:
        sliceAAA.append(arrayop[:8])
        arrayop = arrayop[8:]
    for i in sliceAAA:
        binaryToDecimal(int(i))

def validation(ipAddress, fields, limit):
    array = ipAddress.split(".")
    if len(array) == fields:
        for i in array:
            if i.isdigit() and i < limit:
                pass
            else:
                return False
        return array
    else:
        return False

def nextPowerOf2(n):
    count = 0
    if (n and not (n & (n - 1))):
        return n

    while (n != 0):
        n >>= 1
        count += 1

    return 1 << count

def hostOrSunbnet(user_choice):
    divide_by = nextPowerOf2(int(user_choice[1]))
    cidr = 0
    if user_choice[0] == 1:
        counter = 1
        base = 1
        while base <= divide_by:
            base *= 2
            counter += 1
        cidr = 32 - counter + 2
    else:
        counter = 7
        base = 2 ** 24
        while base >= nextpower:
            base /= 2
            counter += 1
        cidr = counter
    return cidr

def userChoice():
    print("if u want to use partitoning please choose an option: ")
    print("A) partitoning by host number")
    print("B) partitoning by subnet number")
    choice = input("please type your choice : ")
    host_num = 0
    sub_num = 0
    user_choice = []
    match choice:

        case "A":
            user_choice.append(1)
            host_num = input("please enter the host number: ")
            user_choice.append(host_num)
            return user_choice

        case "B":
            user_choice.append(2)
            sub_num = input("please enter the subnet number: ")
            user_choice.append(sub_num)
            return user_choice
        case unknown_command:
            print("You have entered unknown option.. Let's try again.. ")

def network_cal(ip_number, cidr):
    print(cidrToSubnetmask(cidr))

def main():
    print("Hello Humen!!!")
    ip_number = input("Plese enter a valid IP address to calculate: ")
    if validation(ip_number, 4, 255):
        cidr = input("And now, enter a CIDR num. by default, we calculate it for you: ")
        if cidr == '':
            cidr = user_class(ip_number)
            print("We calculate the CIDR for you! your CIDR is /", cidr)
        if validation(str(cidr), 1, 32):
            user_choice = userChoice()
            cidr = hostOrSunbnet(user_choice)
            print("Your new CIDR is: /", cidr)
        network_cal(ip_number, cidr)
    else:
        print("We are so sorry. somthing wrong. let's try again..")
        main()

if __name__ == "__main__":
    main()
