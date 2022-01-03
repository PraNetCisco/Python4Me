def banner(message, border='+'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)
    
def main():
    banner("Pradeep Sharma", "*")
    
main()
