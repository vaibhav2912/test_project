
def add_http_info(func):
    def wrapper(website):
        website = "http://www." + website
        func(website)
    return wrapper


def hyperlink():
    website = input("Enter website: ")
    connect(website)
    
    

@add_http_info    
def connect(website):
    print("Connecting to {}".format(website))


if __name__ == "__main__":
	hyperlink()