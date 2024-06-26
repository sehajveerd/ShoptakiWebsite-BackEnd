# Real  Estate Financial Metrics
## Follow These Steps:

1. Data Import: The code reads a CSV file containing real estate information, replacing "Not Available" entries with NaN.

2. Data Cleaning: Rows with missing values (NaN) are removed to ensure data quality.

3. Feature Selection: The script selects specific columns (features) from the dataset, including daysOnZillow, latitude, livingArea, lotAreaValue, price, priceForHDP, and rentZestimate.

4. Financial Metrics Calculation: It calculates important financial metrics such as Annual Return, Capitalization Rate, and Debt Yield based on assumptions for Net Operating Income, Mortgage Payment, Property Value, and Loan Amount.

5. Machine Learning Model: The data is split into features (X) and the target variable (Annual Return). A Random Forest Regressor model is created, trained on the training data, and used to make predictions.

6. Model Evaluation: The Mean Absolute Error (MAE) is computed to assess the model's accuracy in predicting Annual Return.

7. Data Saving: The code saves both the original data and the calculated metrics into a new CSV file named "Processed_house_data.csv."

In summary, this script demonstrates data preprocessing, financial analysis, and machine learning modeling for real estate data, providing insights into property investment potential.


## Financial Metrics Introduction:
1. **Annual Return:**
   - The Annual Return represents the expected annual profit or return on investment (ROI) for a real estate property.
   - Formula: `(Net Operating Income - Mortgage Payment) / Property Value`
   - Explanation:
     - Net Operating Income (NOI): This is the expected annual rental income generated by the property minus any operating expenses (property taxes, insurance, maintenance, etc.). It's essentially the profit generated by the property before accounting for financing costs.
     - Mortgage Payment: This is the annual mortgage payment on the property.
     - Property Value: This is the current market value of the property.

2. **Capitalization Rate (Cap Rate):**
   - The Capitalization Rate is a measure of the property's potential return on investment, expressed as a percentage.
   - Formula: `(Net Operating Income / Property Value) * 100`
   - Explanation:
     - Net Operating Income (NOI): As mentioned above, this is the expected annual rental income minus operating expenses.
     - Property Value: This is the current market value of the property.
   - Cap Rate is often used by real estate investors to quickly assess the potential profitability of a property. A higher Cap Rate suggests a potentially higher return.

3. **Debt Yield:**
   - Debt Yield is a measure of a property's ability to cover its mortgage debt with its NOI.
   - Formula: `(Net Operating Income / Loan Amount) * 100`
   - Explanation:
     - Net Operating Income (NOI): The annual rental income minus operating expenses.
     - Loan Amount: The total amount of the mortgage loan on the property.

