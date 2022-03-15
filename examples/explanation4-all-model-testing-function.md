### Explaining the functions in model_testing_function.py

This .py script creates a for-loop of the ``model_val`` function that iterates through all of the locations in our DataFrame. 

``test_all`` is the main function in this script, which iterates through a pandas dataframe ("locations") containing the metadata for each location. It appends the results of the ``model_val`` function (MSE and r2 score) for each location and appends them to arrays for each. These two arrays are then turned into dataframes and concatenated together to create a single two-columned df "results". 

This function specifically works for the ``model_val`` function, but it could be modified to work for the ``predict_test`` function to return a dataframe of predicted values for the test set.

    def test_all(locations):
        '''time-series splits the ALLSKY_KT data into X_train, X_test,
        fits model with X_train and opt hyperparams,
        compares to X_test and returns MSE, r2 for each row in Locations_2.csv'''
        MSEs = []
        r2s = []
        for row in range(len(locations)):
            MSE, r2 = model_val(locations, sample=row)
            MSEs.append(MSE)
            r2s.append(r2)
        MSEs = pd.DataFrame([MSEs]).T
        r2s = pd.DataFrame([r2s]).T
        results = pd.concat([MSEs, r2s], keys=['MSE', 'r2'], axis=1)
        results.columns = results.columns.droplevel(1)
        return(results)

The resulting dataframe can be concatenated to the original metadata dataframe ("locations") so that each location's respective MSE and r2 score for the optimized models are easily accessible.

    def append_results(locations, results):
        '''adds results from test_all function to a
        df with Locations_2.csv information'''
        accuracy = pd.concat([locations, results], axis=1)
        return(accuracy)