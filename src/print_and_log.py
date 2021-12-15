import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.INFO)

# userName ="a string"
# result = 1
def pnl(string):
    print(string)
    logging.info(string)


# print_and_log("New employee {} was added \nThe employee id is {}".format(userName,result))