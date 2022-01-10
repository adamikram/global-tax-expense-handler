
# parses csv file and stores in a data
class CsvParse:
    def __init__(self, file_path, is_initital=True):
        if is_initital:
            self.parse(file_path)
    def parse(self, file_path):
        self.df = pd.read_csv(file_path)
        self.df = self.df.fillna('')

    # gets the heading of a data frame
    def get_headings(self):
        return self.df.columns

    # gets the specified column of a data frame without blanks
    def get_column(self,column, remove_blanks=True):
        # arr = self.df[column].fillna('')
        arr = self.df[column].tolist()
        if remove_blanks:
            while True:
                try:
                    arr.remove('')
                except ValueError:
                    break
            return arr
        else:
            return arr
    def save(self,path):
        pass

if __name__=="__main__":
    print('bruh')