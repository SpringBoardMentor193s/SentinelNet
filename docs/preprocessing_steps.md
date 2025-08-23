# 📝 NSL-KDD Preprocessing Steps

- Reviewed dataset composition: Normal vs. Attack traffic

- Grouped attacks into categories: DoS, Probe, R2L, U2R

- Noted class imbalance to plan mitigation strategies

## Data Preprocessing

#### Missing Values
 
Checked for missing values in the dataset

```bash

No missing values found

```

####  Duplicate Rows
 
Counted duplicate rows and removed.

```bash

Duplicated rows removed

```

#### Encode Categorical Features

`````text 
- One-hot encoded categorical features:

    - protocol_type

    - service

    - flag
`````

#### Scale Numerical Features

`````text 
- Numerical features scaled using MinMaxScaler

- Binary features kept as-is:

    -land, logged_in, root_shell, su_attempted, is_host_login, is_guest_login
`````

#### Simple Preprocessing Techniques Applied

- Duplicates removed

- Categorical features one-hot encoded

- Numerical features scaled

- Binary features kept as-is

- Target label (label) unchanged

## Output

Preprocessed dataset ready for machine learning models

Saved schema mapping and preprocessed data for further analysis
