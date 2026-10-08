
# we are assuming log.txt is in the directory alongside the script before parsing
import datetime
counts = {}
def read_file():
    file_path = str(input("Input the absolute file path of your log file: "))
    try:
        with open(file_path, "r") as f:
             file_content = f.readlines()
            
    except FileNotFoundError:
            return False    
        
             #here we read the entire file, this returns a list of lines
    for line in file_content: # for each line in the file split the file into a list with each part of the log in it
        log_tokens = line.split(" ") 
        if len(log_tokens) == 1:
             continue;
        parseLog(log_tokens)
    return True

def parseLog(log_tokens):
    log_tokens = [token.strip() for token in log_tokens]
    log_tokens = list(filter(lambda a: a != "-", log_tokens))
    ip = log_tokens[0]
    name = log_tokens[1]
    date = log_tokens[2].strip("[") + log_tokens[3].strip("]")
    http_code = log_tokens[-2]
    response_size = log_tokens[-1]
    key = (ip, name)
    if http_code in ["400", "404", "401", "403"]:
        if key in counts:
            counts[key][1] += 1
        else:
            counts[key] = [name, 1]
    return counts

def printMost():
    sorted_counts = dict(sorted(counts.items(), key = lambda item: item[1][1], reverse = True))
    print("IP Addresses and Names of Failed Attempts")
    for key, value in list(sorted_counts.items())[:5]:
         print("IP Address: " + str(key[0]).strip("(").strip(")").strip("'") + ", User: " + value[0] + ", # Failed Attempts: " + str(value[1]))


def main():
    if (not read_file()):
            print("File not located. Terminating the program.")
            exit(0)
    printMost()

if __name__ == "__main__":
    main()

