import pandas as pd
import numpy as np

def convert_nslkdd_txt_to_csv(input_txt_path, output_csv_path):
    """
    Convert NSL-KDD TXT file to properly formatted CSV
    
    Args:
        input_txt_path: Path to KDDTrain+.txt or KDDTest+.txt
        output_csv_path: Path where CSV will be saved
    """
    
    # Define column names for NSL-KDD dataset (41 features + label + difficulty)
    column_names = [
        'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
        'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
        'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations',
        'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login',
        'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
        'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
        'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
        'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate',
        'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'label', 'difficulty'
    ]
    
    print(f"Reading {input_txt_path}...")
    
    try:
        # Read the TXT file
        df = pd.read_csv(input_txt_path, header=None, names=column_names)
        
        print(f"✓ File read successfully. Shape: {df.shape}")
        print(f"\nFirst few rows:")
        print(df.head())
        
        # Check for any anomalies
        print(f"\nData types:")
        print(df.dtypes)
        
        print(f"\nCategorical column unique values:")
        print(f"protocol_type: {df['protocol_type'].unique()}")
        print(f"service: {df['service'].nunique()} unique values")
        print(f"flag: {df['flag'].unique()}")
        
        print(f"\nLabel distribution:")
        print(df['label'].value_counts())
        
        # Save to CSV
        df.to_csv(output_csv_path, index=False)
        print(f"\n✓ CSV saved successfully to: {output_csv_path}")
        
        return df
        
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return None


def convert_without_difficulty(input_txt_path, output_csv_path):
    """
    Convert NSL-KDD TXT file to CSV without difficulty column
    (Use this if your TXT file doesn't have difficulty column)
    
    Args:
        input_txt_path: Path to KDDTrain+.txt or KDDTest+.txt
        output_csv_path: Path where CSV will be saved
    """
    
    # Define column names for NSL-KDD dataset (41 features + label only)
    column_names = [
        'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
        'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
        'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations',
        'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login',
        'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
        'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
        'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
        'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate',
        'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'label'
    ]
    
    print(f"Reading {input_txt_path}...")
    
    try:
        # Read the TXT file
        df = pd.read_csv(input_txt_path, header=None, names=column_names)
        
        print(f"✓ File read successfully. Shape: {df.shape}")
        print(f"\nFirst few rows:")
        print(df.head())
        
        print(f"\nCategorical column unique values:")
        print(f"protocol_type: {df['protocol_type'].unique()}")
        print(f"service: {df['service'].nunique()} unique values")
        print(f"flag: {df['flag'].unique()}")
        
        print(f"\nLabel distribution:")
        print(df['label'].value_counts())
        
        # Save to CSV
        df.to_csv(output_csv_path, index=False)
        print(f"\n✓ CSV saved successfully to: {output_csv_path}")
        
        return df
        
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return None


if __name__ == "__main__":
    # Since we're running from inside the data folder
    train_input = "KDDTrain+.txt"
    train_output = "KDDTrain_converted.csv"
    
    test_input = "KDDTest+.txt"
    test_output = "KDDTest_converted.csv"
    
    print("="*60)
    print("CONVERTING TRAINING DATA")
    print("="*60)
    convert_nslkdd_txt_to_csv(train_input, train_output)
    
    print("\n" + "="*60)
    print("CONVERTING TEST DATA")
    print("="*60)
    convert_nslkdd_txt_to_csv(test_input, test_output)