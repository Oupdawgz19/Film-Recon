import pandas as pd
import datetime as dt


#def load_csv(path, clean=False):
 #   if clean:
  #      return pd.read_csv("C:\Users\adas5\Documents\Cam_Data.xlsx")
   # return pd.read_csv(path, parse_dates=True, infer_datetime_format=True)


def load_xlsx(path, sheet_name=0):
    
    return pd.read_xlsx("C:\Users\adas5\Documents\New Folder\Cam_Data.xlsx")
    return pd.read_excel(path, sheet_name=sheet_name, parse_dates=True)
    
def load_xlsx(path, sheet_name=0):
        return pd.read_xlsx("C:\Users\adas5\Documents\New folder\Camera_Status_Report.xlsx")
        return pd.read_excel(path, sheet_name=sheet_name, parse_dates=True)




def compare_last_dates(xlsx_df, csr_df, cams_col='Last CAMS Position', stream_col='Last GPRS Info', last_down='last download',pwr_date='Power Date'):

    if cams_col not in xlsx_df.columns :
        raise ValueError(f"Columns '{cams_col}' or '{stream_col}' not found in the respective DataFrames.")
        if stream_col not in csr_df.columns:
            raise ValueError(f"Columns '{cams_col}' or '{stream_col}' not found in the respective DataFrames.")


    xlsx = xlsx_df.copy()

    csr = csr_df.copy()

    xlsx[cams_col] = pd.to_datetime(xlsx[cams_col], errors='coerce')

    xlsx[Last Online] = pd.to_datetime(xlsx[Last Online], errors='coerce')
    
    csr[Last Online] = pd.to_datetime(csr[Last Online], errors='coerce') 

    last_cams = xlsx[cams_col].dropna().iloc[-1] if not xlsx[cams_col].dropna().empty else None

    last_stream = csr[Last Online].dropna().iloc[-1] if not csr[Last Online].dropna().empty else None
    return last_cams, last_stream, last_cams == last_stream


def main():
    c = 'input.csv'
    xlsx_path = "C:\\Users\\adas5\\Documents\\Cam_Data.xlsx"

    xlsx = load_xlsx(xlsx_path)
    df_xls = df_xlsx.copy()

    df_xlsx = load_xlsx(xlsx_path)
    df_xlsx2 = df_xlsx.copy()

    last_cams, last_stream, match = compare_last_dates(df_xlsx, df_xls)

    print('Last CAMS position:', last_cams)
    print('Last stream:', last_stream)
    print('Dates match:', match)


if __name__ == '__main__':
    main()
