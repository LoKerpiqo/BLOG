libsvm tutorial

[livsvm tutorial](https://www.csie.ntu.edu.tw/~cjlin/libsvm/)
```ruby
model = svmtrain(training_label_vector, training_instance_matrix, [, 'libsvm_options']);
[predicted_label, accuracy, decision_values/prob_estimates] = svmpredict(testing_label_vector, testing_instance_matrix, model,[, 'libsvm_options]);
```

Returned model structure
[Parameters, nr_class, totalSV, rho, Label, ProbA, ProbB, nSV, sv_coef, SVs]
-Parameters: parameters
-nr_class: no of classes
-rho: -b of the decision functions wx+b
-Label: label of each class; empty for regression/one-class SVM
-sv_indices: values in [1,...,num_training_data] to indicate SVs in the training set
-ProbA: pairwise probability information; empty if -b 0 or in one-class SVM
-ProbB: pairwise probability information; empty if -b 0 or in one-class SVM
-nSV: number of SVs for each class; empty for regression/one -class SVM
-sv_coef: coeficients for SVs in decision functions
-SVs: support vectors

If you do not use the option '-b 1', ProbA and ProbB are empty
matrices. If the '-v' option is specified, cross validation is
conducted and the returned model is just a scalar: cross-validation
accuracy for classification and mean-squared error for regression.

The function 'svmpredict' has three outputs. The first one,
predictd_label, is a vector of predicted labels. The second output,
accuracy, is a vector including accuracy (for classification), mean
squared error, and squared correlation coefficient (for regression).
The third is a matrix containing decision values or probability
estimates (if '-b 1' is specified). If k is the number of classes
in training data, for decision values, each row includes results of
predicting k(k-1)/2 binary-class SVMs. For classification, k = 1 is a
special case. Decision value +1 is returned for each testing instance,
instead of an empty vector. For probabilities, each row contains k values
indicating the probability that the testing instance is in each class.
Note that the order of classes here is the same as 'Label' field
in the model structure.


Multi
