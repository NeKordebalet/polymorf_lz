import pandas as pd

class Cash:
    def __init__(self):
        self.df = None
        self.duplicates_count = 0
    def load_and_process_data(self):
        self.df = pd.read_csv('var10.csv')
        initial_count = len(self.df)
        self.df = self.df.drop_duplicates()
        self.duplicates_count = initial_count - len(self.df)

        df_zero_cashback = self.df[self.df['Сумма cash-back'] == 0.00]    
        df_non_zero_cashback = self.df[self.df['Сумма cash-back'] > 0.00]    
        df_zero_cashback.to_csv('f1.csv', index=False)  
        df_non_zero_cashback.to_csv('f2.csv', index=False)  

    def __invert__(self):
        print(f"Всего удаленных дубликатов: {self.duplicates_count}")
    def __del__(self):
        print("Объект класса Cash удален.")
def main(): 
    processor = Cash()
    processor.load_and_process_data()
    ~pro
if __name__ == "__main__":
    main()