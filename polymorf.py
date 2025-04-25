import pandas as pd

class Cash:

    def data(self):
        df = pd.read_csv('var10.csv')
        df = df.drop_duplicates()
        df1 = df[df['Сумма cash-back'] == 0.00]    
        df2 = df[df['Сумма cash-back'] > 0.00]    
        df1.to_csv('f1.csv', index=False)  
        df2.to_csv('f2.csv', index=False)  
        self.duplicates1 = df1.duplicated()
        self.duplicates2 = df2.duplicated()
    def __invert__(self):
        self.num_duplicates1 = self.duplicates1.sum()
        self.num_duplicates2 = self.duplicates2.sum()
        total_duplicates = self.num_duplicates1 + self.num_duplicates2
        print(f"Всего дубликатов: {total_duplicates}")
    def __del__(self):
        print("DEL")
def main(): 
    pro = Cash()
    pro.data()
    ~pro
if __name__ == "__main__":
    main()