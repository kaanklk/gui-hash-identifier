def writefile(data):
    try:
        file = open("output.txt", mode='w', encoding='utf-8')
        file.write(data)
        file.close()
    except:
        print("File not found!")
        file.close()
