def high_na_columns(df, threshold = 0.85):
     
    '''
    This function returns a list of the columns names that have na's percentage above a threshold
    '''
    import pandas as pd

    nulls_percent_df = pandas.DataFrame(df.isna().sum()/len(df)).reset_index()
    
    nulls_percent_df.columns = ['column_name', 'nulls_percentage']
    
    nulls_percent_df[nulls_percent_df['nulls_percentage']!=0]
    
    columns_above_threshold = nulls_percent_df[nulls_percent_df['nulls_percentage']>threshold]
    
    drop_columns_list = list(columns_above_threshold['column_name'])
    
    return drop_columns_list 


def clean_gender(x):
    if x in other:
        return 'other'
    else:
        return x

